
<a name="top-of-page"><img src="/readme/readme-assets/logo/lawn-genie-nav-logo-v4-resized-546-x-150px.png" width="300"></a>

# LawnGenie - Testing Document :microscope: #  

<br>

## Table of Contents ##
1. [Test User Accounts](#test-user-accounts)
1. [User & Client Stories Testing](#user-client-stories-testing)
1. [Code Validation](#code-validation)
1. [Manual Testing](#manual-testing)
1. [Browser Testing](#browser-testing)
1. [Bugs Discovered](#bugs-discovered)

<br>

## 1. <a name="test-user-accounts">Test User Accounts</a> ##

All of the LawnGenie website features and functionality can be tested using one or other of the below User Accounts.

* SuperUser - Website Admin and Django Admin Account
  * UN: johndeere
  * PW: husqvarna

* Registed Customer Account
  * UN: larrylawn
  * PW: greenfingers
  
<br>

## 2. <a name="user-client-stories-testing">User & Client Stories Testing</a> ##

I tested each of the Client and User stories which were used to determine the design, features, functions and styling of the Lawn Genie website. See the results of these tests here; 

#### Client Stories ####
> - [x] "The business owners want to; "Create a specialist e-commerce store which sells products relating to the care and maintenance of Lawns."
* TEST RESULT: The store has a catalogue of Lawn care products which can be purchased by users.
> - [x] "The store must provide the business owners with an easy to use interface to enable to addition, editing, and deletion of products and their content. This content must include a product name, SKU, category, description, price, a product image, and rating. The interface should also allow for the addition of other attributes which may be unique to certain products, for example, a 'size' attribute for boots."
* TEST RESULT: The store SuperUser has the ability to add, edit, and delete products and product content. All required content attributes have been included.
> - [x] "The store must use the Stripe payment processing platform to ensure an elegant and secure payment process for users."
* TEST RESULT: The Stripe billing system has been integrated into the store.
> - [x] "The store design must allow users to navigate easily and intuitively through the product offering, regardless of what device they are using."
* TEST RESULT: The store is responsive. The Navigation bar, footer, and buttons on pages offer an intuitive and easy navigation flow for users.
> - [x] "For ease of use, the store must allow users of the site to register and login so that they can store their personal delivery/account information and. This is to facilitate quick purchaing transactions. They should also be able to view their past order history."
* TEST RESULT: Registered User have access to a My Profile page where they can add or edit their delivery information, and where they can view their past orders.
> - [x] “The store must give users the option to subscribe to an email mailing list. Marketing/promotional emails can then be sent to users based on topics such as; tips and tricks from gardening professionals and lawn care specialists, new product infromation, and special offers."
* TEST RESULT: Users can sign-up to be added to a Newsletter subsciber list on a dedicated sign-up page.
> - [x]  “The store must have a blog section where users can read articles and get information about lawn care and maintenance etc. A secure interface to add, update, and delete blog posts must be provided to the business owners."
* TEST RESULT: Users can view a Blog page and individual Blog articles. The store SuperUser has access to and Add Blog Post page and an Edit Post page. They can also delete posts from the Blog Post pages.

> - [x] “The store must contain a number of product categories of products which should be easily accessible and identifiable to a user." These categories are;
* TEST RESULT: All Categories listed below are available on the store and products have been added to them.
* Category 1 - Mowers:  
   * Robot Mowers
   * Self-propelled
   * Push Mowers
   * Tractor Mowers 
* Category 2 - Tools:
   * Rakes
   * Edging Tools
   * Aerators
   * Watering
   * Hand Tools
   * Sprayers
* Category 3 - Improvers:
   * Lawn Feed
   * Weeding
   * Seeds
* Category 4 - Clothng:
   * Jackets
   * Trousers
   * Boots
   * Gloves


#### User Stories ####
> - [x] “I want to learn to immediately understand the overall concept of what the website offers when I land on the homepage, i.e. the online sale of lawn care equipment and associated products.”
* TEST RESULT: A user can immediately see that the website's prime function is to sell lawn care products. This is obvious from a combination of the logo, navigation bar, and the 'Hero' image at the the top of the homepage.
> - [x] “I want to be able to access all product categories from every page.”
* TEST RESULT: The main navigation bar and category links is available at the top of every page.
> - [x] “I want to be able to view a list of all products in a category.”
* TEST RESULT: The store offers a view of all products in both a main category (e.g. Mowers) and subcategories (e.g. Robot Mowers)
> - [x] “I want to be able to easily search for products from every page."
* TEST RESULT: The top navigation bar offers a search box which will search the product names and descriptions on the store for a search term and display a list of the products which produce a hit for the term.
> - [x] “I want to be able to easily sort product listings by price, name, category, and rating."
* TEST RESULT: The store offers the ability to sort product listings by price, name, category, and rating.
> - [x] “I want to be able to add products to a shopping cart and easily view all the products in my shopping cart."
* TEST RESULT: The store does offer 'add to cart' functionality. The cart can be accessed directly from the navigation bar at any time.
> - [x] “I want to be able to easily change the quantities of the products in my shopping cart."
* TEST RESULT: A User can easily update the quantitiy of a product in their shopping cart.
> - [x] “I want to be able to be able to see the total cost of my current shopping basket from every page.”
* TEST RESULT: A User can easily update the quantitiy of a product in their shopping cart.
> - [x] “I want to be able to view a product detail page showing me all relevant information about a product.”
* TEST RESULT: Every product has a product detail page showing all attributes/data about a product.
> - [x] “I want to be able to easily register on the site and store my personal delivery information for automatic retrieval at the checkout when making purchases."
* TEST RESULT: A User can register for a My Profile Account. They can record their delivery address themselves on their My Profile page. Or, if they make a purchase they can also opt to have their delivery info added to their My Profile page for future purchases. If they then buy another product, their delivery information will be pre-populated in the checkout form.
> - [x] “I want to get an email confirmation/verification email after I register for an account."
* TEST RESULT: A User will be sent a verification email upon registration. The must click on a reistration link in order to be able to sign-in on the store.
> - [x] “I want to be able to easily login or logout of my account from every page."
* TEST RESULT: A My Profile link is displayed in the top navigation bar on every page. When a user clicks on the icon/link a dropdown offers them a login/logout link depending on whether they are logged in or out at the time.
> - [x] “I want to be able to view a Blog page and relvant informative Blog post articles."
* TEST RESULT: The store does offer a Blog page showing a list of all available posts. A user can click on a post item to view the full article.
> - [x] “I want to be able to sign up to receive a newsletter in order to get information about new products, promotions, and lawn care advice/articles."
* TEST RESULT: Users can subscribe to receive Newsletters. They can also easily unsubscribe if they wish too.


#### [Back To Top ^ ](#top-of-page) ####

<br>

## 3. <a name="code-validation">Code Validation</a> ##

I ran the website through the W3C validators for [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/). I also ran my JavaScript & jQuery code through the [JSHint.com](https://jshint.com/) code checker, and used the PEP8 checker at [PEP8online.com](http://pep8online.com/) to check my Python code for PEP8 compliance.  

#### HTML ####

The W3C CSS Validation Service. The validator highlighted the following warning for index.html. No other errors or warnings were found.

* "Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections." - I decide not to 'fix' the issue this warning relates to. It relates to the title of the introduction section which is a h1 title. I decide to leave it as a h1 as it looks better like this when underneath the 'hero' carousel.

#### CSS ####

The W3C CSS Validation Service. The validator found the following errors. No other warnings or erros were found.

* The validator highlighted 246 Warnings relating to the bootstrap.min.css style sheet. I queried this with Tutor Support and was advised that these were acceptable issues as I have no control over the CDN-delivered Bootstrap style sheet.
* ERROR: ".navbar-toggler:focus	rgb(243, 8, 8, 0.1) is not a box-shadow value : rgb(243, 8, 8, 0.1)" - I updated the value to a HEX value and this fixed the error.

#### JavaScript & jQuery ####

I ran the below JavaScript files and code blocks through the JSHint validator and foucn the following Warnings. No errors were found.
countryfield.js
stripe_elements.js


#### Python ####

I ran the following files through the PEP8online.com Python validator and found some errors relating to some lines of code being too long, some whitespace on blank lines, and some files had no blank line at the end of the page. I fixed all errors.

* Blog App - admin.py, apps.py, forms.py, models.py, urls.py, views.py, widgets.py
* Cart App - cart_tools.py, apps.py, contexts.py, urls.py, views.py
* Checkout App - admin.py, apps.py, forms.py, models.py, signals.py, urls.py, views.py, webhook_handler.py, webhooks.py
* Home App - apps.py, urls.py, views.py
* LawnGenie App - asgi.py, settings.py, urls.py, wsgi.py
* Newsletter App - admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py
* Products App - admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py, widgets.py
* Profiles App - admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py
* custom_storages.py
* manage.py


#### [Back To Top ^ ](#top-of-page) ####

<br>

## 4. <a name="manual-testing">Manual Testing</a> ##

I manually tested the LawnGenie site elements and functionality under the below headings. Where appropriate I tested each item on a large screen device and a mobile device.

I also tested these while logged in as the SuperUser to ensure all features/functions were visible.

## Homepage ##

#### Navbar (Common to all pages) ####
* Tested Logo/Home Link. -> Result: Worked as expected.
* Tested Search link. -> Result: Worked as expected.
* Tested Search functionality. -> Result: Worked as expected.
* Tested My Account dropdown link. -> Result: Worked as expected.
* Tested My Account links:
 * Tested My Account Add a Product link -> Result: Worked as expected.
 * Tested My Account Create Blog Post link -> Result: Worked as expected.
 * Tested My Account Send a Newsletter link -> Result: Worked as expected.
 * Tested My Account My Profile link -> Result: Worked as expected.
 * Tested My Account Logout link -> Result: Worked as expected.
 * Tested My Account Register link -> Result: Worked as expected.
 * Tested My Account Login link -> Result: Worked as expected.
* Tested Cart link. -> Result: Worked as expected.
* Tested Cart Total functionality. -> Result: Worked as expected.
* Tested Category Dropdown links in main navbar -> Result: Worked as expected.
* Tested 25 subcategory links -> Result: Worked as expected.
* Tested Our Blog link -> Result: Worked as expected.
* Tested Mobile Nav Toggler link/dropdown  -> Result: Worked as expected.

#### Footer Section (Common to all pages) ####
* Tested Logo link. -> Result: Worked as expected.
* Tested Copyright link. -> Result: Worked as expected.
* Tested Email link. -> Result: Worked as expected.
* Tested Social Media links. -> Result: Worked as expected.
* Tested Top Category buttons. -> Result: Worked as expected.
* Tested Links buttons. -> Result: Worked as expected.

#### Homepage Body ####
* Tested Hero div 'SHOP NOW' button. -> Result: Worked as expected.
* Tested Husqvarna Promo Banner 1. -> Result: Worked as expected.
* Tested John Deere Promo Banner 2. -> Result: Worked as expected.
* Tested Supersoil Promo Banner 3. -> Result: Worked as expected.
* Tested Best Sellers Image and Button links. -> Result: Worked as expected.
* Tested New Arrivals Image and Button links. -> Result: Worked as expected.
* Tested Blog section button link. -> Result: Worked as expected.
* Tested Newsletter section button link. -> Result: Worked as expected.

## Product List/Results Page ##

#### Sorting and Back To Top button (common to all category listing/results pages) ####
* Tested All Sort options in sorting dropdown. -> Result: Worked as expected.
* Tested Product number count. Result: -> Result: Worked as expected.
* Tested Back To Top button. Result: -> Result: Worked as expected.

#### Product links (common to all category listing/results pages) ####
* Tested Product image link. -> Result: Worked as expected.
* Tested Product More Info button. -> Result: Worked as expected.
* Tested Product Category button. -> Result: Worked as expected.
* Tested Product Edit button. -> Result: Worked as expected.
* Tested Product Delete button. -> Result: Worked as expected.

## Product Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.
* Tested Category link. -> Result: Worked as expected.
* Tested Category link. -> Result: Worked as expected.
* Tested Product Edit button. -> Result: Worked as expected.
* Tested Product Delete button. -> Result: Worked as expected.
* Tested Add To Cart button. -> Result: Worked as expected.

#### Inputs ####
* Tested Quantity increment/decrement icons. -> Result: Worked as expected.
* Tested Quantity increment/decrement icons and Add To Cart to check correct quantity in cart. -> Result: Worked as expected.
* Tested Size selector. -> Result: Worked as expected.
* Tested Size selector and Add To Cart to check correct size in cart. -> Result: Worked as expected.
* Tested Size selector for same product of different size and Add To Cart to check additional line item with new size in cart. -> Result: Worked as expected.



## Cart Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Checkout Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Checkout Success Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Blog and Blog Post Pages ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.




## Profile Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Newsletter Subscribe and unsubscribe pages ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Add a Product Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Create a Blog Post Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.

## Send a Newsletter Page ##
 
#### Links ####
* Tested Image link. -> Result: Worked as expected.





## Django Template pages ##

#### Registration Page  ####
* Tested Logo Link. -> Result: Worked as expected.

#### Login Page ####
* Tested Logo Link. -> Result: Worked as expected.

#### Log Out Page ####
* Tested Logo Link. -> Result: Worked as expected.

#### Email Confirmation Page ####
* Tested Logo Link. -> Result: Worked as expected.

#### Email Validation Page ####
* Tested Logo Link. -> Result: Worked as expected.





#### [Back To Top ^ ](#top-of-page) ####

<br>

## 5. <a name="browser-testing">Browser Testing</a> ##

I completed the above manual testing of the CPC site on the following browsers. Please see results below.

### Chrome ###
* All tests ran OK.

### Firefox ###
* All tests ran OK. 

### Safari ###
* Issue discovered with the fact that Safari doesn't support Form DatePicker by default. Pleasee see Bugs Discovered section for more detail.
* All other tests ran OK. 

#### [Back To Top ^ ](#top-of-page) ####


## 6. <a name="bugs-discovered">Bugs Discovered / Remedies</a> ##

While developing and testing the site I discovered the below bugs/issues. If I found a remedy to a bug I have listed this below.

#### Bugs Discovered / Remedies ####

1. Floating Footer - When I initally created my base.html and index.html templates and added a navbar and footer, the footbar did not behave itself. It was 'floating' up from the bottom of the page and hugging the bottom of the last container on the page. I did some research and found that I could fix it by applying some CSS to it. I added the 'Margin-Top: auto' property and value and it fixed the issue.


#### [Back To Top ^ ](#top-of-page) ####
