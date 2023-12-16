# Cake Heaven - Testing

![MockUp](media/docs/mockup.png)

This is the testing documentation for my web application Cake heaven. Full [README available here](/README.md)

See the live site [here](https://cake-heaven-8414245a4be7.herokuapp.com/)

# Validation 
## HTML Validation
The initial test of the page validated by URL using [W3C HTML Validator](https://validator.w3.org/#validate_by_uri) showed couple of errors:
| **Feature**| **Result** | **Pass/Fail** |
| :--- | :--- | :--- |
| HOME | Double ID attributes on Account dropdown menu - as there is a seperate dropdown menu for desktop and mobile devices, I've change the name of id for mobile devices  | Pass |
| PRODUCT DETAILS | 'li' element as a 'div' child - In ingredients list, changed the 'div' element for an 'ul' element | Pass
| ADD PRODUCT | 1. Delete 'type="text/javascript' from the 'script' tag as it isn't neccessary. 2. Delete 'strong' element from around 'p' element as paragrapf can't be a direct child of a 'strong' element. 3. Double 'id' attribute for image selection in the custom_clearable_file_input - changed JavaScript 'id' for a 'class' and remove 'class' from forms.py to avoid double class error.  | Pass |
| EDIT PRODUCT | Add an 'alt' attribute to an image in custom_clearable_file_input | Pass |
| CHECKOUT | Empty heading tag - a loading spinner was inside 'h1' tags for a bigger font, but instead I've changed the 'h1' to a 'div' element and add the class with font size | Pass |

I have attached only one screenshot of the test results because they all look identical on every page

<details><summary>Final result</summary>
<img src="media/docs/htmlval.png">
</details>

## CSS Validation
I run the CSS code through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and showed one error and couple of warnings

### Error

* Error regards styling on focus effect of Close cross button on modal window, and I've decided to delete the focus styling entirely as it was not necessary at the first place

<details><summary>Css Error</summary>
<img src="media/docs/csserror.png">
</details>

### Warnings

* Imported style sheets - This refers to Google's font import, and aa it is a standard way to import fonts directly in to the CSS, I've decided to ignore thatw arning
* Vendor extension error - there is nothing to do about this since those extensions help support browser compatibility efforts 
* Same colour for background-color and border-color - necessary action to override Bootstrap styling

<details><summary>Css Warnings</summary>
<img src="media/docs/csswarning.png">
</details>

## JavaScript Linting
I ran the JavaScript code through [JSHint](https://jshint.com/), which only showed one missing colon, which was easy to fix, and undeclared variable on stripe_payment.js, which is declared somewhere else

### Results presented below

<details><summary>stripe_element.js</summary>
<img src="media/docs/stripejs.png">
</details>
<details><summary>country_field.js</summary>
<img src="media/docs/countryfield.png">
</details>
<details><summary>quantity_input.js (Bag, Product page)</summary>
<img src="media/docs/quantityjs.png">
</details>
<details><summary>scroll_top.js</summary>
<img src="media/docs/scrolltopjs.png">
</details>
<details><summary>sort_box.js</summary>
<img src="media/docs/sortbox.png">
</details>
<details><summary>Add image input</summary>
<img src="media/docs/addimage.png">
</details>
<details><summary>Update/Remove (Bag)</summary>
<img src="media/docs/updaterem.png">
</details>

## Python Linting
I ran the code through [CI Python Liner](https://pep8ci.herokuapp.com/), which shows a multiple errors mostly regarding blank lines, missing whitespaces and too long lines, which all were fixed.

### Details of every checked code below

| **App** | **File** | **Result** |
|---|---|---|
| cake_heaven | settings | PASS |
| cake_heaven | urls | PASS |
| bag | urls | PASS |
| bag | views | PASS |
| bag | contexts |  PASS |
| bag | test_views |  PASS |
| checkout | admin |  PASS |
| checkout | forms |  PASS |
| checkout | models | PASS |
| checkout | signals |  PASS |
| checkout | urls |  PASS |
| checkout | views |  PASS |
| checkout | webhook_handler |  PASS |
| checkout | webhooks |  PASS |
| home | test_views | PASS |
| contact | admin |  PASS |
| contact | forms |  PASS |
| contact | models |  PASS |
| contact | urls |  PASS |
| contact | views |  PASS |
| products | admin |  PASS |
| products | forms | PASS |
| products | models |  PASS |
| products | urls |  PASS |
| products | views |  PASS |
| products | widgets |  PASS |
| profiles | admin |  PASS |
| profiles | forms |  PASS |
| profiles | models |  PASS |
| profiles | urls |  PASS |
| profiles | views |  PASS |

## Lighthouse Testing
The site was run through Google Chrome Dev Tools Lighthouse on desktop and mobile devices. While on desktop the results are satisfactory, unfortunatelly on mobile devices the performance results are mostly around 70%. The main reasons for the low result were:
* Render-blocking resources - scripts, stylesheets, and HTML imports that block or delay the browser from rendering page content to the screen, which I wasn't able to improve
* Unused JavaScript - refers to Bootstrap and Stripe scripts
* Images in .jpg format - All products images are already in jpg format

For full results see dropdown below

### Desktop

<details><summary>Home Page</summary>
<img src="media/docs/homedes.png">
</details>
<details><summary>Product Page</summary>
<img src="media/docs/proddes.png">
</details>
<details><summary>Product Detail Page</summary>
<img src="media/docs/detaildes.png">
</details>
<details><summary>Bag Page</summary>
<img src="media/docs/bagdes.png">
</details>
<details><summary>Checkout Page</summary>
<img src="media/docs/checkoutdes.png">
</details>
<details><summary>Success Checkout Page</summary>
<img src="media/docs/succesdes.png">
</details>
<details><summary>Profile Page</summary>
<img src="media/docs/profilesdes.png">
</details>
<details><summary>Management Site</summary>
<img src="media/docs/managemdes.png">
</details>
<details><summary>Contact Form</summary>
<img src="media/docs/contactdes.png">
</details>
<details><summary>Edit Products</summary>
<img src="media/docs/editdes.png">
</details>
<details><summary>Login Page</summary>
<img src="media/docs/logindes.png">
</details>
<details><summary>Register Page</summary>
<img src="media/docs/registerdes.png">
</details>
<details><summary>Manage Email</summary>
<img src="media/docs/managedes".png>
</details>
<details><summary>Change Password</summary>
<img src="media/docs/changepassdes.png">
</details>


### Mobile

<details><summary>Home Page</summary>
<img src="media/docs/homemob.png">
</details>
<details><summary>Product Page</summary>
<img src="media/docs/prodmob.png">
</details>
<details><summary>Product Detail Page</summary>
<img src="media/docs/detailmob.png">
</details>
<details><summary>Bag Page</summary>
<img src="media/docs/bagmob.png">
</details>
<details><summary>Checkout Page</summary>
<img src="media/docs/checkoutmob.png">
</details>
<details><summary>Success Checkout Page</summary>
<img src="media/docs/successmob.png">
</details>
<details><summary>Profile Page</summary>
<img src="media/docs/profilesmob.png">
</details>
<details><summary>Management Site</summary>
<img src="media/docs/managemob.png">
</details>
<details><summary>Contact Form</summary>
<img src="media/docs/contactmob.png">
</details>
<details><summary>Edit Products</summary>
<img src="media/docs/editmob.png">
</details>
<details><summary>Login Page</summary>
<img src="media/docs/loginmob.png">
</details>
<details><summary>Register Page</summary>
<img src="media/docs/registermob.png">
</details>
<details><summary>Manage Email</summary>
<img src="media/docs/manageemailmob.png">
</details>
<details><summary>Change Password</summary>
<img src="media/docs/changepassmob.png">
</details>

# Manual Testing

<details><summary>All Pages</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Animated banner  | Display animation on all page sizes and devices  | Pass |
| Clickable logo | Clickable text logo redirects to the home page | Pass |
| Mobile home page button | Home page button on mobile devices redirects to the home page | Pass |
| Search box - empty | Redirects to the all products page with error message to enter search criteria | Pass |
| Search box - filled | Display searched product, or returns "0 Product found" if searched product does not exist | Pass |
| Mobile search box dropdown | On mobile devices clicked search icon triggers dropdown search box | Pass |
| Account dropdown | Clickable icon dropdowns nav links, which lead to correct pages  | Pass |
| Bag icon | Clickable bag icon leads to a bag page | Pass |
| Full bag icon | Icon changes for a full shopping bag | Pass |
| Category Navbar | Navlinks lead to correct pages and not hiding a 500 internal server error | Pass |
| Mobile hamburger menu | Mobile hamburger dropdown icon display all categories and leads to correct pages | Pass |
| Footer | Footer presents across all pages | Pass |
| Footer - Hover effect | Fading hover effect on links | Pass |
| Footer - Contact us link | Clicked link works properly and leads to correct page | Pass |
| Footer - Contact details | Telephone link provides call functionality. Email link opens email client with supplied address. | Pass |
| Footer - Social Links | Links clickable and open correct pages in separate tab | Pass |
| Scroll-up button | Appears after scrolling the page down, and when clicked scrolls page back up  | Pass |
</details>

<details><summary>Home</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Shop now button | Clicked leads to all products page | Pass |
| Featured Cakes | List of only featured products clicked directs to the product details page | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
</details>

<details><summary>Product page</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
| Page links | All links are correct and leads to appriopriate pages | Pass |
| Products counter | Product count matches number of products on the page | Pass |
| Sorting | Sorting box sorts correct according to choosen option | Pass |
| Products card - Category links | Category links under the product image lead to correct category | Pass |
| Products Card - Rating view | Display rating according to the user's review rating | Pass |
| Products Card - Edit/Delete links | Only for admin user - Edit link leads to edit product page. Delete function display warning if admin is sure to delete the product, and then delete it | Pass |
| Product Card | Clicked directs to product detail page | Pass |
</details>

<details><summary>Product detail</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
| Category links | Category links under the product image lead to correct category | Pass |
| Rating view | Display rating according to the user's review rating | Pass |
| Edit/Delete links | Only for admin user - Edit link leads to edit product page. Delete function display warning if admin is sure to delete the product, and then delete it | Pass |
| Product description | Display products description with list of ingredients | Pass |
| Quantity input | Buttons are disabled when lower/upper limit is reached | Pass |
| Go back button | Leads to all products page | Pass |
| Add to bag button | Adds products to the bag, display success messgae with bag content summary and 'Chceckout' button| Pass |
| Checkout button | Leads to checkout page | Pass |
| Reviews box | Logged in user can rate the product and add one review per product. Attempting to add a second review will edit the first review | Pass |
| Reviews display | If the product contains any review, it will be displayed below a review box  | Pass |
</details>