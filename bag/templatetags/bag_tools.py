from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates the subtotal for a product in the bag """
    return price * quantity