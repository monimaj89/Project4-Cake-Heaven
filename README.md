
# Cake Heaven

![Website mock-up](media/docs/mockup.png)

Cake heaven is a e-commerce website project created for a imaginary bake shop in UK. The main goal of this project was to create the most user-friendly website possible, where you can shop for cakes in an easy and intuitive way. 
The user can browse products, add them to the cart, and make a payment. The user can make a purchase as a registered user or as a guest. Registered users also have the option to view their order history and leave reviews about products.

Project was created using Python, Django, HTML5, CSS3, and JavaScript. The data was stored in a PostgreSQL database using ElephantSql for manipulation. Cake Heaven is my fourth and last milestone project for Code Institute's Level 5 Diploma in Web Application Development.

[View the live site](https://cake-heaven-8414245a4be7.herokuapp.com/)

# UX and Five Planes of Website Design

## Strategy

### User stories

1. As a first time user I want to:
* Immediately understand the main purpose and use of the site
* Be able easily navigate through the page
* Be able search for the products on the page
* Contact the company with any queries 
* Buy prodcts without registration
* See the reviews left by other users
* Be able use the page on any devices and size screens
* Login/ create an user account

2. As a registered user I want to:
* Have access to my profile page
* Be able to leave the products reviews
* See my order history 
* Be able to update and save my personal info
* Make purchase with my delivery info always filled

3. As an admin I want to:
* Be able to add, edit and delete products
* View and manage customer reviews
* Delete customer review if not appropriate
* Have easy acces to admin controls

## Scope

1. When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

| Feature                          | Importance | Difficulty |
|-----------------------------|------------|------------|
| Responsive design                | 5          | 1          |
| Navigation through page              | 5          | 1          |
| Search function              | 4          | 3          |
| Welcome text                   | 4          | 1          |
| Shop Now button               | 4          | 1          |
| Featured products            | 3          | 3          |
| Contact Form            | 4          | 4          |
| Social links              | 2          | 1          |
| Products page           | 5          | 3          |
| Sorting products            | 4          | 4          |
| Products detail card            | 5          | 4          |
| Select quantity                 | 5          | 4          |
| Add to bag function          |5      |3         |
| CRUD Functionality for admin        | 5          | 3          |
| User reviews           | 3          | 4          |
| Review management for admin      | 5          | 2          |
| Checkout page                | 5          | 4          |
| Secure payment system          |5      |5         |
| Order summary on succesful purchase       | 3          | 3          |
| Register/Login functionality          | 5         | 4          |
| User's profile page with order history         | 5          | 3          |
| Update user's info         | 5          | 4          |

2. Future features - There are also a number of features I would like to implement to the page in the future:
* Live chat
* Order Tracking
* Discount vouchers
* User's wishlist

## Structure

The website structure is divided into many separate pages that are displayed depending on the type of user. The details are displayed on flow diagram below build using [Lucidchart](https://www.lucidchart.com/pages/)
 
![Flow Diagram](media/docs/Diagram.png)

## Skeleton

1. Database Schema
During the planning phase, a crucial step involved constructing a well-defined database schema to facilitate the development process. To visually represent the database, I used [DrawSQL](https://drawsql.app/), which proved to be a valuable tool throughout the development journey. The site uses a relational database model using Postgres (Elephant SQL). Several models were adapted from the Boutique Ado walkthrough (User, Email, UserProfile, Category, and Product). Additionally, two original models were introduced, Contact form and Product review.

![Database Schema](media/docs/database.png)

2. Wireframes

The wireframes were created using [Balsamiq](https://balsamiq.com/).

**Desktop**

<details><summary>Home Page</summary>
<img src="media/docs/deshome.png">
</details>
<details><summary>Products Page</summary>
<img src="media/docs/desprod.png">
</details>
<details><summary>Profile Page</summary>
<img src="media/docs/desprofile.png">
</details>
<details><summary>Contact Form</summary>
<img src="media/docs/descontact.png">
</details><br>

**Tablet**

<details><summary>Home Page</summary>
<img src="media/docs/ipadhome.png">
</details>
<details><summary>Profile Page</summary>
<img src="media/docs/ipadprofile.png">
</details>
<details><summary>Contact Form</summary>
<img src="media/docs/ipadcontact.png">
</details><br>

**Mobile**

<details><summary>Home Page</summary>
<img src="media/docs/mobilehome.png">
</details>
<details><summary>Product Page</summary>
<img src="media/docs/mobileprod.png">
</details>
<details><summary>Profile Page</summary>
<img src="media/docs/mobileprofile.png">
</details>
<details><summary>Contact Form</summary>
<img src="media/docs/mobilecontact.png">
</details>


## Surface

[Bootstrap](https://getbootstrap.com/) was used and customised for the front-end development

### Colour
The colors used on my website are simple. I decided on a white background with pink accents to emphasize the sweetness of the page

![Colour Palette](media/docs/palette.png)

Additionally, four colors were used for danger/warning/success/info features

![Secondary colour](media/docs/secolour.png)

### Typography
Fonts was imported from [Google Fonts](https://fonts.google.com/)
* Great Vibes has been used as a welcome header on home page

![Great Vibes](media/docs/fontgreat.png)

* Lato has been used as a main body font

![Lato](media/docs/lato.png)

* Sans serif is set as a backup if any of the fonts fail to load


### Images and icons

All images are fully credited [here](#credits)

* Favicon - borrowed from [Here](https://favicon.io/)

![Favicon](media/docs/favicon.png)

* 404 error page borrowed from rawpixel.com on [Freepik](https://www.freepik.com/)

![404page](media/docs/error.webp)



## Note
* Commit from 8 Nov - Site Deployment - An accidentally committed piece of code that should not had been committed at this stage. The committing concerned only site deployment, and the code from the products/views.py had not been plan to commited yet.
* Credentials exposed - My AWS access and secret keys had been committed and pushed before I manage to hide them. Both keys were generated once again and switched.