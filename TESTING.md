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

<details><summary>Add Product</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page only visible for and admin user, display warning for non admin user | Pass |
| Site Management - admin | Display Add product page with form | Pass |
| Category | Choose available category from the list | Pass |
| Fill the form | Fill all required fields  | Pass |
| Select image (non required) | Select image through the button, for product without the image, the default image will display | Pass |
| Add product button | Clicked, directs to added product detail page with a success message | Pass |
| Cancel button | Clicked, directs to all products page | Pass |
</details>

<details><summary>Edit/Delete Product</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Links only visible for and admin user, display warning for non admin user | Pass |
| Edit/Delete links | Available on products, and product detail pages | Pass |
| Edit product | Clicked link leads to edit product form page with alert message | Pass |
| Edit the form | Edit all fields that need editing  | Pass |
| Remove the image | Check the remove image box just for removing the image | Pass |
| Select image | Select new image, no need to remove the old one | Pass |
| Update product button | Clicked, directs to  the edited product detail page with succes message | Pass |
| Delete product | Clicked, displays modal message confirming deleting the product, clicked 'Delete' deletes the product and directs to all products page with a success message, clicked 'No' directs back to product detail page | Pass |
</details>

<details><summary>Bag</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
| Empty Bag | Clicked on empty bag icon, directs to the bag with 'empy bag' message, and button to kepp shopping | Pass |
| Keep shopping button | Clicked, directs to all product page | Pass |
| Full bag icon | When product in the bag, the bag icon changes | Pass |
| Bag page | Display summary of item added to the bag | Pass |
| Quantity input | Change the quantity of ordered item and update | Pass |
| Remove item | Remove link removes item from the bag and update the bag content with a success message| Pass |
| Bag total | Calculate the total amount of ordered items | Pass |
| Delivery charge | Calculate the 10% of the total amount | Pass |
| Grand total | Bag total + delivery cost | Pass |
| Free delivery threshold | “Spend £— more” message appears when total is under free delivery threshold | Pass |
| Keep shopping button | Directs to all product page | Pass |
| Secure Checkout button | Directs to the checkout page | Pass |
</details>

<details><summary>Checkout</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
| User details form | Form for user's details, filled for logged in users | Pass |
| Links to register/login | For guest users links leads to sign in/up pages | Pass |
| Save info checkbox | Checkbox to save details for logged in users  | Pass |
| Contact Form | Link leads to contact form page | Pass |
| Payment field | Secure payment function | Pass |
| Valid form submission | Form is disabled while page is processing order & loading icon appears | Pass |
| Valid form submission - order created | Successful form submission creates an order in the database | Pass |
| Valid form submission - 3D Authentication | Successful form submission using the Stripe Authenticate card number brings up the Stripe authentication popup | Pass |
| Valid form submission - 3D Authentication | Clicking ‘complete’ on authentication popup puts the order and payment through successfully | Pass |
| Valid form submission - 3D Authentication | Clicking cancel or fail on authentication returns user to form with details filled in and an error message. Order is not created | Pass |
| Order created in webhook backup | Any failure to create order during valid submission will result in order being created by the web hook. Only 1 order is created | Pass |
| Invalid form submission - user details | Logged in user cannot submit form with invalid information | Pass |
| Invalid form submission - payment info | Errors in card info are reflected in text below the payment form | Pass |
| Invalid form submission - order not created | Any submission with errors in form or incomplete information doesn’t create an order in the database | Pass |
| Confirmation email | Email is sent to email address provided by user on successful checkout submission | Pass |
| Orded confirmation page | User is directed to the order confirmation page with order summary and a success message | Pass |
| Keep shopping button | Directs to all products page | Pass |
| Order added to profile page | For registered users order is add to his order summary on profile page | Pass |
</details>

<details><summary>Profile</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible only for registered users | Pass |
| Welcome Header | Welcome header display name of the user| Pass |
| Delivery form | Form with saved delivery info | Pass |
| Update information button | Clicked, updates user informations | Pass |
| Order history | Display all user's orders | Pass |
| Order number | Clicked, directs to the this order summary page with an alert message | Pass |
| Order history | Available only for user who placed this order | Pass |
| Back to profile button | Clicked, leads back to the profile page | Pass |
</details>

<details><summary>Contact</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
| Form | All fields are required | Pass |
| Cancel button | Clicked, redirect to the all products page | Pass |
| Send button | Clicked, send a message to the company email, and redirects to the Thank you page | Pass |
| Thank you page | Display confirmation of sending the message with two links | Pass |
| Contact page link | Go back to the contact oage for another inquiry | Pass |
| Keep shoppin link | Leads to the all products page | Pass |
</details>

<details><summary>Admin page</summary>
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Page Content | Accessible by typing /admin to the url address | Pass |
| Authentication Tests | Page is visible only for user with admin password | Pass |
| Review | Display list of products which contain a review | Pass |
| Display review | Clicked on product's name display the review  | Pass |
| Review content | Name of reviewed product, rating, review text and created by | Pass |
| Edit review | Admin is able to edit any part of the review | Pass |
| Delete review | Admin is able to delete any review | Pass |
</details>

<details><summary>Authentication</summary>

| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Sign In Page | Contains user form, 'Remember me' checkbox, 'Home' and 'Sign in' buttons and 'Forgot Password' link. All features are clickable and leads to appropriate pages| Pass |
| Sign In | Only logged out users can access page. Already logged in user is directed to the home page | Pass |
| Sign in - unverified user | Unverified user is directed to the Verify email page, and can not log in | Pass |
| Sign in - user form | All fields required | Pass |
| Sign in - user form | Incorrect username/email address or password results in error message, and user cannot log in | Pass |
| Sign up page | Only logged out users can access page. Already logged in user is directed to the home page | Pass |
| Sign up page | Contains 'Sign in' link for already registered user, an user form, and 'Sign up' button which redirect to 'Verify email' page | Pass |
| Sign up - user form | All fields required | Pass |
| Sign up Page - Success | Successful form submission creates a new user on the database - user email is unverified | Pass |
| Sign up Page - Success | Successful form submission sends an email to the user to verifyhis address | Pass |
| Verify email | Email confirmation link redirects user to page to verify email address | Pass |
| Verify email | Clicking on ‘confirm’ on confirm email address page confirms the user’s email | Pass |
| Register Page - Success | Once registered user can now sign in to site with new credentials | Pass |
| Sign Out | Only logged in users can access page. For logged out users page reloads | Pass |
| To sign out | Click on sign out directs user to confirmation page. Clicking on ‘sign out’ button signs user out and clears current bag. Display a success message | Pass |
| Manage Email | Only for logged in users, accessible through profile page, allows user to manage his email address | Pass |
| Change Password | Only for logged in users, accessible through profile page, allows user to change his password | Pass |
</details>

<details><summary>Error page</summary>

| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| Responsiveness | Page content appears and is fully responsive | Pass |
| Authentication Tests | Page is visible for all users, guests, registered and admin | Pass |
| Go Home button | Clicked redirects back to home page | Pass |
</details>