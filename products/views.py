from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm

import ast


def all_products(request):
    """
    A view to show all cakes
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        # Handles product sorting based on sortkey & direction
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handles product filtering by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handles product search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't"
                               "enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


# View for product details
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # Display list of ingredients
    ingredients = (
        product.ingredients
        .replace('[', "")
        .replace(']', "")
        .replace("'", "")
        .split(',')
    )
    # Review functionality
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(
                created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect(reverse('product_detail', args=[product.id]))

    context = {
        'product': product,
        'ingredients': ingredients,
    }

    return render(request, 'products/product_detail.html', context)


#  Add a product
@login_required
def add_product(request):
    """ Add a product to the store """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit the product
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Delete the product
@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    #  Checks if the product is added to the bag
    bag = request.session.get('bag', {})
    if str(product.id) in bag:
        #  Delete product from the bag
        bag.pop(str(product.id))

        # Updates bag in session
        request.session['bag'] = bag

    # Delete product from the page
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
