# Cake Heaven - Testing

![MockUp](media/docs/mockup.png)

This is the testing documentation for my web application Cake Heaven. Full README available [here](/README.md)

See the live site [here](https://cake-heaven-8414245a4be7.herokuapp.com/)


# Table of content

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Linting](#javascript-linting)
    * [Python Linting](#python-linting)
    * [Lighthouse Testing](#lighthouse-testing)
    * [Wave Testing](#wave-testing)
* [Responsiveness](#responsiveness)
* [Manual Testing](#manual-testing)
* [User Stories Testing](#user-stories-testing)
* [Bugs, Issues and Solutions](#bugs-issues-and-solutions)

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


# Responsiveness
Responsive design testing has been carried out on different devices and screen sizes using [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

### Mobile devices used for testing
* Iphone SE
* Iphone 12 pro
* Samsung Galaxy S8+
* Pixel 5

<details><summary>Home Page</summary>
<img src="media/docs/responsive/mobhome.png">
</details>
<details><summary>Product Page</summary>
<img src="media/docs/responsive/mobprod.png">
</details>
<details><summary>Product Detail Page</summary>
<img src="media/docs/responsive/detailmob.png">
</details>
<details><summary>Bag Page</summary>
<img src="media/docs/responsive/mobbag.png">
</details>

### Tablets used for testing
* Ipad Pro
* Ipad Air
* Surface Pro 7
* Nest Hub

<details><summary>Home Page</summary>
<img src="media/docs/responsive/tabhome.png">
</details>
<details><summary>Product Page</summary>
<img src="media/docs/responsive/tabprod.png">
</details>
<details><summary>Profile</summary>
<img src="media/docs/responsive/tabprofile.png">
</details>
<details><summary>Bag Page</summary>
<img src="media/docs/responsive/tabbag.png">
</details>
<details><summary>Checkout</summary>
<img src="media/docs/responsive/tabcheck.png">
</details>


### Browser used for testing
* Google Chrome was the main browser I've been using during creation of the project, and I've notice Chrome has some issues with showing boldness of the text, basicly Chrome does not display bold text appropriate, so after test my page on different browser I've decided to change some text styling and leave it without bold feature
* Safari
* Mozilla Firefox

[Go to Top](#cake-heaven---testing)

# Manual Testing
I conducted comprehensive manual testing on my page, ensuring all functions, links and button functioned correctly. I verified the layout and design, checked the responsiveness on different devices, and reviewed the content for accuracy. The page successfully passed the thorough testing, ensuring its functionality and user-friendliness.

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
| Rating view | Update rating score according to user review | Pass |
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

| **Test** | **Goal** | **Result** |
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

| **Test** | **Goal** | **Result** |
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


# User Stories Testing
I thoroughly tested various user stories to ensure the functionality and usability of my page. I verified that users could access all pages, order products, and use all page functionality. I also confirmed that the page displayed the relevant information accurately and maintained a seamless user experience throughout the testing process.

| **#**| **User Type** | **User Story** | **Achieved** |
| :--- | :--- | :--- | :---|
| 1.1 | First time user | Immediately understand the main purpose and use of the site | The home page is the first page that the user encounters when entering the website, in the foreground there is a welcome text with a large Shop Now button and an image of delicious macaroons. Below, the user can see the section of featured cakes,  which clearly represent the purpose of the website |
| 1.2 | First time user | Be able easily navigate through the page | All pages have the same unchanged navbar with the search option and logo, which always directs user to the main page, user account, shopping cart and cake categories available on the website. At the bottom of each page there is also a footer with a form and contact details |
| 1.3 | First time user | Be able search for the products on the page | Search bar is available through whole site and on all devices. On product page user can also use sorting features to see products according to category or price |
| 1.4 | First time user | Contact the company with any queries | A contact form available in the footer on each page allows the user to quickly and easily contact the bakery |
| 1.5 | First time user | Buy prodcts without registration | Every user, even not registered one is able to order cakes, and will receive order confirmation with order number to his email address |
| 1.6 | First time user | See the reviews left by other users | Every user is able to see product's review left by other users in the product detail page |
| 1.7 | First time user | Be able use the page on any devices and size screens | The entire website was designed and built to be fully responsive and work on any device. All features have been thoroughly tested and work regardless of device and size |
| 1.8 | First time user | Login/ create an user account | User account is available on main navbar through whole site, dropdown menu lets user to register or log in if user is already registered. For new users, veryfication email is send to confirm his email address, and to be able to login to his account |
| 2.1 | Registered user | Have access to my profile page | All registered users has access to their profile page through dropdown Account menu on navbar |
| 2.2 | Registered user | Be able to leave the reviews for purchased products | Logged in user is able to use review form, which is invisible for quest users, to leave his review on product detail page, also user can navigate to the product card from his order history so he do not have to search on a page for the product he bought |
| 2.3 | Registered user | See my order history | Every user can see his order history on his profile page and use the order number to see summary of this order |
| 2.4 | Registered user | Be able to update and save my personal info | Personal details on profile page can be saved and updated if necessary |
| 2.5 | Registered user | Manage my email or change the password | Below personal details form, user have access to links to manage his email address or to change his password |
| 2.6 | Registered user | Make purchase with my delivery info always filled | Logged in user has the opportunity to save his delivery details by checking the box below checkout form |
| 3.1 | Admin user | Be able to add, edit and delete products | Admin can add a new product through his Management site on dropdown menu, or by admin site, typing /admin to the site address url. Editing or deleting product is also available on admin site, or by links provided on product cards. Deleting product is protected by pop up window, where admin has to confirm deleting the product |
| 3.2 | Admin user | View and manage customer reviews | Admin is able to view, edit users' reviews on the admin site, typing /admin to the site address url and login into the admin panel |
| 3.3 | Admin user | Delete customer review if not appropriate | Every inappropriate review can be deleted by admin using the admin panel, typing /admin to the site address url |
| 3.4 | Admin user | Have easy access to admin controls | Admin has easy and quick access to management panel typing /admin to the site address url and login into the admin page |


# Bugs, Issues and Solutions
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | Countryfield.js file did not work in the profile static file | Move it to the root static js file, probably some issue with the file path |
| 2 | Update quantity in the bag did not work | I'ce created separate js file for update and remove item from a bag, and for some reason update quaintity did not work, while removing worked properly. Moved it back to the HTML file as a script tag, and both worked perfectly  |
| 3 | Search bar dropdown on smaller screens overflowed and looked out of styling | I've reduce the width of the bar, and used a combination of my own and bootstrap styling and as it could looked better I am generally pleased with the outcome  |
| 4 | Veryfication emails didn't work | During creating the project, I've implemented contact form functionality using AWS SES, which worked, but it was sending emails only from verified addresses on AWS, so then when I've added Register function, it wasn't sending verification emails to an user's email because it wasnt verified on AWS. The problem was fixed when I set up sending real emails with gmail. |
| 5 | Sorting according to rating | As I've implemented my own rating functionality, and sorting funtionality has been adapted from Boutique Ado walkthrough, sorting due to rating returns 500 error page. As I had very limited time I've decided to delete option to sort according to rating, instead of fixing it, but this is something worth thinking about in the future |
| 6 | No emails displayed in manage email page | When a user wants to manage their email, no email assigned to the user is displayed on the email management page. Email management page is an AllAuth template and I did not change there anything within the code. The email address seems to be there because using button to make it primary or delete it worked as they should, just not displaying email on the page. Although in the Chrome Dev Tools the email is visible in the code. |
| 7 | Security Issue - Checkout Success page accessible to any user | During testing I've noticed that any user would technically be able to navigate to the checkout success page for any order if they had the order number and entered the relevant URL. Since a purchase can also be made by an unregistered user, it was difficult to apply restrictions to display this page. With the limited time I did not find solution for it, but it would be worth thinking about it in the future because it may cause significant threats in real e-commerce websites |
| 8 | Add Review only after making the purchase | For now, adding reviews to the product is limited only to registered users and every logged in user, even without making a purchase, can write whatever they want. Due to limited time, I could not make any corrections to it, but in the future I would like to introduce review function only for users who have purchased this product |
| 9 | Commit from 8 Nov - Site Deployment | An accidentally committed piece of code that should not had been committed at this stage. The committing concerned only site deployment, and the code from the products/views.py had not been plan to commited yet |
| 10 | Credentials exposed | My AWS access and secret keys had been committed and pushed before I manage to hide them. Both keys were generated once again and switched |

[Go to Top](#cake-heaven---testing)
