
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

* Favicon - borrowed from [Favicon page](https://favicon.io/)

![Favicon](media/docs/favicon.png)

* 404 error page borrowed from rawpixel.com on [Freepik](https://www.freepik.com/)

![404page](media/docs/error.webp)


# Features

## Home Page

![Home Page](media/docs/homepage.png)

  * Animated banner - located at the top of the page, an animated banner informs the user about free delivery and the deadline for ordering next day delivery

  ![Order By](media/docs/orderby.png)

  ![Free delivery](media/docs/freedel.png)

  * Logo, Search Bar, account icon and shopping Bag - Logo is a simple company name, using search bar user can search for his favoutire flavours. Through 'My Account' user can register or login, already logged in user can also go to his profile page, for admin there is also management page. Shopping bag change the icon when full

  ![Logo Navbar](media/docs/logonav.png)
  ![Full Bag icon](media/docs/fullbag.png)

  * Main navbar - User can choose his favourite cakes using dropdown menu with categories

  ![Main Navbar](media/docs/mainnav.png)

  * Welcome Banner - Main banner with welcome text, an image and Shop now button, which directs to all products page

  ![Main Banner](media/docs/mainbanner.png)

  * Featured cakes - a gallery with our featured cakes

  ![Featured cakes](media/docs/featured.png)

  * Footer - contains general info about our bakery, contact us form, bakery address and social links. On the bottom there is a copyright info

  ![Footer](media/docs/footer.png)

## Products Page 
Contains all products within all categories. On the top user can sort and filter according to name, category, price and rating

![Product Page](media/docs/product.png)

  * Product detail - a separate card with all product's details as a name, price, rating, description with ingredients and quantity

  ![Detail Card](media/docs/proddetail.png)

  * Reviews - Below the detail card user can see all the review from other users, and logged in user can add his own review

  ![Reviews](media/docs/review.png)

  * Go Back/Add to Bag Buttons - Buttons to go back to products page, or to add product to the bag

  ![Buttons](media/docs/prodbutton.png)

## Shopping Bag

  * Empty Bag - if the bag remains empty, user can only see a button to keep shopping which directs to products page

  ![Empty Bag](media/docs/emptybag.png)

  * Bag with product - contains summary of order with update quantity function and delete products function. Below summary there is a total of all products with info how much more user can spend for free delivery

  ![Full Bag](media/docs/fullshopbag.png)

  * Buttons - Keep shopping button to go back to product page and Secure Checkout button for checkout

  ![Bag Buttons](media/docs/checkoutbutt.png)

## Checkout 
Guest user can fill his details in the form provided, which can be already saved for logged in users. Checkout page also contains order summary with all product details

![Checkout](media/docs/Checkout.png)

  * Contact form link - Directs to contac form page, where user can send all inquiries

  * Card detail box - a simple payment form using Stripe for secure and easy purchase

  * Buttons - Go back to bag button, to see user's bag, and Place order, with warning info about the amount being charged

  ![Payment Box with Buttons](media/docs/stripepaym.png)

  * Checkout Process - after order being placed user see a loading spin page, and then the stripe window to confirm payment

  ![Loading spin](media/docs/load.jpeg)

  * Success Page - after order being placed and payment confirmed user is directed to the success checkout page with order and details summary. User gets a confirmation email on his address

## Profile Page 
Any logged in user has access to his profile page which contains:

  * Personal info details - phone number and address which can be updated
  * Order history with order number which directs to order summary page

![Profil Page](media/docs/profile.png)

## Management Site 
Form created for admin to easy add product to the page

![Add Product form](media/docs/addprod.png)

## Contact Form 
A form connected with company email address for user to easy and fast contact

![Contact Form](media/docs/contactform.png)

  * Thank you page - after sending the inquiry user is directed into Thank you page saying that company will contact back as soon as possible

  ![Thank you page](media/docs/thankyou.png)

## Authentication

The project uses AllAuth to implement User login and authentication functionality. AllAuth comes with a whole load of backend functionality and front end templates that make the user, registration, sign in/out and user management easy and quick to create

Main templates provided by AllAuth:

  * Register - function provided straight from an account navbar, allows for new user to register on a page, contains a 'sign-in' link for already registered users. Successfully registered user receives a confirmation email with verification code
  * Sign In - For already registered users, accessible from an account navbar, contains a 'register' link for new users. User can sign in using Username or email, and tick the box to remember him. Page also contains a "Forgot password" link if user can not log in
  * Sign Out - Accessible from an account navbar, redirects to page where user can confirm if ready to log out. After signing out the bag contect is removed from the session.
  * Forgot password - Available for already registered user on 'sign in' page, required an email address existing in database. Send an email with password reset link, where user is able to reset his password and login again.

## Error Page 
A 404 error page created for a positive user experiance when lost on non-existent page, with button to quick get back to home page

![404 Page](media/docs/error.png)  

# Technologies Used

## Language
* HTML - Used for the main structure of the page
* CSS - Used for styling, combined with Bootstrap
* JavaScript - Used for fronend interactive features
  * Stripe Payment Functionality
  * CountryField on address form
  * Modal window 
  * Products' quantity input
  * Update quantity/Remove item
  * Products' sort/filter box
  * Product form image field
  * Scroll to top button
* Python - Used for the core of the page backend
  * Python Modules Used:
    * asgiref==3.7.2
    * boto3==1.28.80
    * botocore==1.31.80
    * dj-database-url==0.5.0
    * Django==3.2.22
    * django-allauth==0.41.0
    * django-countries==7.2.1
    * django-crispy-forms==1.14.0
    * django-ses==3.5.0
    * django-storages==1.14.2
    * gunicorn==21.2.0
    * jmespath==1.0.1
    * oauthlib==3.2.2
    * Pillow==10.1.0
    * psycopg2==2.9.9
    * python3-openid==3.2.0
    * pytz==2023.3.post1
    * requests-oauthlib==1.3.1
    * s3transfer==0.7.0
    * sqlparse==0.4.4
    * stripe==7.6.0
    * urllib3==1.26.18
* Tools
  * [GitHub](https://github.com/) - used to host the site
  * [Gitpod](https://gitpod.io/workspaces) - used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub
  * [Heroku](https://dashboard.heroku.com/) - used to deploy the site
  * [Balsamiq](https://balsamiq.com/wireframes/) - used to create a wireframes for this project
  * [LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart
  * [DrawSQL](https://drawsql.app/) - to design the database schema
  * [Favicon.io](https://favicon.io/) - used for a browser tab icon
  * [TinyPNG](https://tinypng.com/) - for compressing the images
  * [Font Awesome](https://fontawesome.com/) - used for icons across the site
  * [Bootstrap5](https://getbootstrap.com/) - used for the styling as well as the responsivness of the site
  * [Google Fonts](https://fonts.google.com/) - used to select and import font for the project
  * [JsHint](https://jshint.com/) - used for validating the javascript code
  * [CI Phython Linter](https://pep8ci.herokuapp.com/) - used for validating the python code
  * [HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML
  * [CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS
  * [Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - used for debugging and testing with Lighthouse
  * [W.A.V.E.](https://wave.webaim.org/) - for testing accessibility
  * [AWS](https://aws.amazon.com/) - for storing media and static data
  * [AWS SES](https://us-east-1.console.aws.amazon.com/ses/home?region=us-east-1#/homepage) - to handle sending contact form 
  * [ElephantSql](https://www.elephantsql.com/) - for hosting the PostgresSql database migrated from Heroku
  * LightHouse - for testing performance
  * Gmail - for sending emails using the SMTP server

## All testing undertaken for this project can be found in the [Testing documentation](/TESTING.md)


# Deployment

## Project creation
I used the [CI GitPod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) to create this project and used GitPod as my IDE.

From the CI GitPod template above the steps to create this project were:
1. Click on 'Use this template' and select 'Create a new repository'
2. Enter your chosen repo name
3. Click 'Create Repository'
4. Click on the green GitPod button
5. Choose New workspace picking first one from the list
6. Click 'Continue'

## Deploy the App
### Set Up the database
1. Go to [ElephantSQL](https://www.elephantsql.com/) and click on 'get a managed database'
2. Select 'Tiny Turtle'
3. Sign in using your GitHub account & authorise ElephantSQL to access your GitHub account
4. Set up a team and go through the login credential process or log in if you already have an account
5. Once you are logged in name your plan (usually the project name)
6. Select your nearest region
7. If you're happy click on 'create instance'
8. Go to your dashboard (click on the ElephantSQL logo) and click on the instance name
9. Copy the database URL for later use

### Set up Heroku
1. Go to [Heroku](https://www.heroku.com/) and log in/register
2. Click on the 'New' button then 'create new app'
3. Name your app and select your nearest region
4. With your app set up go to the app's settings tab and under config variable click on 'reveal config variables' and add a new variable with the Key of `DATABASE_URL` and the value as the database URL that you copied from ElephantSQL
5. Back in GitPod go to settings.py and paste the following in to your DATABASE section to tell it to connect to the new database. **Warning - do not push your code to GitHub whilst this value is in your settings.py, it is a secret value that must not be shared, we will remove it later**

```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('your elephanySQL database url here'))
    }
```

6. In you GitPod terminal type `python3 manage.py showmigrations` to check you are connected to the new database, if you are you will see a list of migrations with no ticks next to them
7. Run the following command `python3 manage.py migrate` to migrate the database structure from your project to the new database
8. Any data that you have added to your SQLite database will not transfer to the new one. You will need to populate the site on the deployed app once it is up and running or using Fixtures (JSON files with all your database content) if you have them. 
9. Create a superuser for your deployed site and new database (this will allow you to check if the database is working and access the site admin on the deployed site) using the following command in the terminal: `python3 manage.py createsuperuser` and set up login details for them following the instructions.
10. Go to the ElephanySQL site, click on your database, go to the browser tab and click on 'table queries' and select 'auth_user (public)' and click on execute, you should see your newly created user.
11. You now need to remove your new database settings from settings.py and set it up to know which version of the site you are on (development or live) to know which database to use. Go back to your GitPod dashboard, click on your avatar to go your your GitPod user settings and select 'variables'
12. Add a key of DEVELOPMENT and a value of True
13. Got to your settings.py file to the DATABASES section and replace what's there with the following code:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

14. Push your code. Your deployed database is set up and GitPod knows which one to use for which version of the site.

### Deploying to Heroku

1. Create a Procfile in your app in the root directory with the following content 'web: gunicorn cake_heaven.wsgi:application'
2. Log in to Heroku using the GitPod terminal using the command 'Heroku login' and enter your Heroku email and password
  - if you have 2 factor authentication set up you will need to use 'Heroku login -i' followed by your email and your Heroku API key as the password.
3. Temporarily disable Heroku from collecting static files during deployment using the command 'heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name'
4. Commit and push your changes to GitHub
5. Then to deploy your site to Heroku use the command 'git push Heroku main'
6. Your site will now be deployed without any of the static files
7. Back in GitPod go to settings.py and add your deployed site's URL to the ALLOWED_HOSTS list
8. Git add, commit and push again and then 'git push Heroku main' to push your changes
11. Once the site has finished deploying you should be able to navigate to the deployed site's URL and see your site
12. Replace the Django secret key in your settings.py (if you included it there) with an environment variable to keep it safe. You can use a Django secret key generator online e.g. [djecrety](https://djecrety.ir/), copy the key it provides.
13. Go to your Heroku app's dashboard, open settings and reveal config variables and add a new variable with a key of SECRET_KEY and a value of what you just copied.
14. In GitPod, if you have used your secret key in settings.py, go back to your GitPod dashboard, click on your avatar to go your your GitPod user settings and select 'variables'
15. Add a key of SECRET_KEY and a Django secret key
16. In settings.py change the SECRET_KEY to 'SECRET_KEY = os.environ.get('SECRET_KEY', '')'
17. Below it change the value of DEBUG to the following 'DEBUG = 'DEVELOPMENT' in os.environ` to dynamically change whether the app is in DEBUG mode depending on whether it is the development or deployed site
18. Commit ang push changes again and then 'git push Heroku main' to push your changes
19. To enable automatic deployment, on Heroku account, go to 'Deploy' tab, scroll down and click on 'Enable Automatic Deploys'


### Set Up AWS to store static and media files

1. Sign up to AWS [here](https://aws.amazon.com/).
2. Created an account and logged in, under the All Services>Storage menu, click the link that says S3.
3. On the S3 page create a new bucket. Click the orange button that says 'Create Bucket'
4. Name the bucket and select the closest region to you
5. Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred 
6. Uncheck the 'Block all public access' checkbox and check the warning box to acknowledge that the bucket will be made public, then click create bucket 
7. Once created, click the bucket's name and navigate to the properties tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'
8. Now navigate to the permissions tab, scroll down to the Cross-origin resource sharing (CORS) section, click edit and paste in the following code:  
    ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
9. Then scroll back up to the 'Bucket Policy' section. Click 'edit' and then 'Policy generator'. This should open the AWS policy generator page
10. Under the 'select type of policy' dropdown menu, select 'S3 Bucket Policy', and inside 'Principle' allow all principals by typing a '*'
11. From the 'Actions dropdown menu select 'Get object'. Then head back to the previous tab and locate the Bucket ARN number. Copy that, return to the policy generator and paste it in the field labelled Amazon Resource Name (ARN)
12. Once that's completed click 'Add statement', then 'Generate Policy'. Copy the policy that's been generated and paste it into the bucket policy editor
13. Before you click save, add a '/*' at the end of your resource key. This is to allow access to all resources in this bucket
14. Once those changes are saved, scroll down to the Access control list (ACL) section and click 'edit'
15. Next to 'Everyone (public access)', check the 'list' checkbox. This will pop up a warning box that you will also have to check. Once that's done click 'save'

### IAM
When your bucket is ready you need to create a user to access it.

1. In the top of the window search for IAM and select it.
2. Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'
3. Name the group 'manage-*your-project-name*' and click 'Create group' at the bottom of the page
4. From the sidebar click 'Policies', then 'Create policy'
5. Go to the JSON tab and click 'import managed policy'. Search for 'S3' and select 'AmazonS3FullAccess' and click import
6. Once this is imported you need to make small changes. Go back to your bucket and copy your ARN number. Head back to this policy and update the Resource key to include your ARN, and another line with your ARN followed by a /*. It should look like this: 
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "YOUR-ARN-NO-HERE",
                    "YOUR-ARN-NO-HERE/*"
                ]
            }
        ]
    }
    ```
7. Click 'Next: Tags', 'Next: Review', and on this page give the policy a name, and description, and click 'Create policy'
8. This will take you back to the policy page where you should be able to see your newly created policy. Now you need to attach it to the group you created before 
9. Click 'User groups', and click the your group. Go to the permissions tab and click 'Add permission' and from the dropdown click 'Attach policies'
10. Find the policy you just created, select it and click 'Add permissions'.
11. Finally you need to create a user to put in the group. Select users from the sidebar and click 'Add user' 
12. Give your user a user name, check 'Programmatic Access', then click 'Next: Permissions'
13. Select your group that has the policy attached and click 'Next: Tags', 'Next: Review', then 'Create user'
14. On the next page, download the CSV file. This contains the user's access key and secret access key for later use

### Connect AWS to django

After creating a S3 bucket you need to connect it to django

1. Install two packages, Boto3 and Django storages, by running these commands:  
    ```
    pip3 install boto3
    pip3 install django-storages
    ```
    And remember to freeze the requirements with:  
    ```
    pip3 freeze > requirements.txt
    ```
2. Add 'storages' to your installed apps section inside your settings.py file
3. Next, in your setting.py file on the bottom, add an if statement to check if there is an environment variable called USE_AWS. This variable does not exist yet but we will add it later. Inside the if statement, write the following settings so it looks like this:  
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
        AWS_S3_REGION_NAME = 'insert-your-region-here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```
4. Next, go back to heroku and in the settings tab, under config vars, add keys with values that were downloaded earlier in the CSV file.
5. Add the key USE_AWS, and set the value to True.
6. Remove now the DISABLE_COLLECTSTAIC variable, since django should now collect static files automatically and upload them to S3.
7. Now head back to the settings.py file in your django project to the if statement you wrote earlier and inside the statement add this line setting:  
    ```
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
    This will tell django where your static files will be coming from in production.
8. Next in the root directory of your project create a file called 'custom_storages.py'. Inside this file import your settings as well as the s3boto3 storage class. Insert this code at the top of the file:  
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    ```
9. Then underneath the imports insert these two classes:  
    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
    Now define the STATICFILES_LOCATION and MEDIAFILES_LOCATION
10. Back in the settings.py file, underneath the bucket config settings but still inside the if statement, add these lines:  
    ```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    ```
11. Next to override and explicitly set the URLs for static and media files using your custom domain and new locations. To do this add these two lines inside the same if statement:  
    ```
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
12. Save, add, commit and push your changes, you should see that your S3 bucket now has a static folder with all your static files inside 
13. Add this piece of code to let the browser know that its ok to cache static files for a long time:    
    ```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    ```
14. Back in S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'. 
15. Inside the new media folder you just created, click 'Upload', 'Add files', and then select all the images that you are using on your site.
16. Then under 'Permissions' select the option 'Grant public-read access' and click upload. Check the warning checkbox
17. And that is it. All your static files and media files should be automatically linked from django to your S3 bucket

### Set up Stripe Payments

1. Log in to Stripe, click on the developers tab and API keys copy the API key and set them in Heroku as config variables in the following:

- STRIPE_PUBLIC_KEY: Stripe publishable key goes here
- STRIPE_SECRET_KEY: Stripe secret key goes here

2. Back in Stripe set up a new webhook for your deployed site by clicking on webhooks, click on 'add endpoint' and paste in your deployed site's URL followed by /checkout/wh/ and set it to listen for all events.
3. Click on your newly set up webhook and click on 'Signing Secret' at the top to reveal the secret value. Copy it and set it as a new config variable in Heroku:
- STRIPE_WH_SECRET: Signing secret from new webhook.

## Run locally
Note: The project will not run locally with database connections unless the user sets up an env.py file configuring IP, PORT, DATABASE_URL, CLOUDAINRY_API and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository for security purposes.

To Run Locally:
1. Navigate to the [GitHub Repository](https://github.com/monimaj89/Project4-Cake-Heaven)
2. Click on 'Code' & select 'Download Zip' to download the files locally and open with an IDE or Copy the URL from the top box
3. If copying the code open your development editor & in the terminal use the 'Git Clone' command followed by the above URL to create a clone of the project locally.

To Fork Project:
1. Navigate to the [GitHub Repository](https://github.com/monimaj89/Project4-Cake-Heaven)
2. Click on the 'Fork' button at the top right of the page
3. Give the fork the name and click "Create Fork"
4. Once in your IDE you can install the project requirements from the requirements.txt file using the command pip3 install -r requirements.txt


# Credits

## Code
* I've looked through a lot of ideas and website to find a concept for this project, and my main inspiration was my local bakery page [Cutter and Squidge](https://cutterandsquidge.com/pages/swansea-cake-delivery).<br>
* As it was my first ever project created with Django I relied a lot on Google, [StackOverflow](https://stackoverflow.com/) and Slack community.
* Building the e-commerce project in Django was a huge and sometimes really overwhelmig challenge. The majority of the code was based on Code Institute's 'Boutique Ado' walkthrough project.

## Images
* Home image has been borrowed from Almendra López Varela from (Pexel)[https://www.pexels.com/]
* All cakes images were borrowed from (Pexel)[https://www.pexels.com/]


## Note
* Commit from 8 Nov - Site Deployment - An accidentally committed piece of code that should not had been committed at this stage. The committing concerned only site deployment, and the code from the products/views.py had not been plan to commited yet.
* Credentials exposed - My AWS access and secret keys had been committed and pushed before I manage to hide them. Both keys were generated once again and switched.

[Go to Top](#cake-heaven)