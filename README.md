# Nutriverse

"Nutriverse" - a Nutrition and Fitness Universe: This is a space created to allow our customers to view different Fitness and Nutrition products, services and classes that are available, as well as our range of accessories and merchandise. It allows the customer to view each product description and reviews before deciding on their purchase.

The Community section allows our customers to add discussion topics for any of the services we offer, where they can share their experiences of these and other users can comment on the topics to answer questions. This area allows customers to support eachother as well as offering tips and advice.

The site also has an integrated administration and store management section. This allows authorised users to easily update and maintain the products and subscriptions available in the store.

## Table of Contents
- [Nutriverse](#nutriverse)
  * [UX](#ux)
  * [Features](#features)
    + [Existing Features](#existing-features)
    + [Future Enhancements](#future-enhancements)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

 
## UX
The overall specification for the project was to create an e-commerce website for a Fitness and Nutrition company in order to sell their products and to provide an area for members to get involved in discussions related to the company's products and services.

The user stories below detail all of the requirements for the website from each of the different types of users that would be using the site.
These will be used as a starting point in order to help build a draft of what the system would eventually look like.

| No.| As a / an: | I want to:                   | So that I can :                |
|----|:----------:|------------------------------|--------------------------------|
| ||<em><strong>-- Site Registration and User Profile --</strong></em>|
|1| Site User | Create a new account | Have a user account to save my delivery details and view my profile|
|2| Site User | Login or logout easily | Access my personal profile details|
|3| Site User | Easily recover forgotten password | Recover access to my account|
|4| Site User | Receive an email confirmation after registering | Verify that my account registration was successful|
|5| Site User | Have a personalised user profile | View my personal order history and order confirmations, and save my payment details|
| ||<em><strong>-- Viewing and Navigation --</strong></em>|
|6| Shopper | View a list of products | Select some to purchase|
|7| Shopper | View individual product details | Identify the description, product rating and reviews, product image and available subscriptions or sizes.|
|8| Shopper | View subscriptions available for a product | View available subscription options for a product, as well as the price for each and other options available.|
|8| Shopper | View the total price of the items I have selected for purchase easily | Keep track of the overall total and avoid spending too much|
| ||<em><strong>-- Sorting and Searching --</strong></em>|
|9 | Shopper | Sort the list of available products | Easily review and compare other similar products, their price or their rating|
|10 | Shopper | Filter by a specific category of product | Find all relevant products in a specific category, and sort the products in that category by name|
|11 | Shopper | Sort multiple categories of products simultaneously | Review products in the general categories such as "Fitness" or "Nutrition" or even by "Class" or a level of fitness that suits my requirements|
|12 | Shopper | Search for a product by name or description | Find a specific product I'm interested in|
|13 | Shopper | View the number of results matched for the search text entered | Allow me see if the product I am interested in is available|
| ||<em><strong>-- Purchase and Checkout --</strong></em>|
|14 | Shopper | Easily select the subscription or size and quantity of a product when purchasing it | Review the options available before selecting for purchase|
|15 | Shopper | View selected items in the basket | Review the items I have selected for and purchase and the total cost before checking out|
|16 | Shopper | Adjust the quantity selected for any individual item in my basket | Allow changes to be made, or items removed before checkout|
|17 | Shopper | Easily enter payment and delivery details | Checkout quickly and easily without too much input|
|18 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the required details to complete my purchase|
|19 | Shopper | View an order confirmation after checkout | Review the order and check that all items are correct|
|20 | Shopper | Receive an email confirmation after checking out | Have a confirmation of what I purchased for my own records|
| ||<em><strong>-- Community and Discussions --</strong></em>|
|21 | Community Member | Search for discussion topics by specific category groups such as "Fitness" or "Nutrition" | Find a list of previous discussions about a particular product|
|22 | Community Member | View individual discussions | Find out more details about the product or plan and read other peoples experiences|
|23 | Community Member | Comment on existing discussions | To add some details to the discussion or answer questions on the topic|
|24 | Community Member | Add a discussion topic for a selected product | Add my own experience of the product or plan that I have used|
| ||<em><strong>-- Product Management / Admin --</strong></em>|
|25 | Store Owner | Add a product | Add new items to my store|
|26 | Store Owner | Edit / update a product | Change product descriptions, images and other product criteria|
|27 | Store Owner | Delete a product | Remove items that are no longer for sale|
|28 | Store Owner | Add a subscription | Add new subscription types for the products|
|29 | Store Owner | Edit / update a subscription | Change product subscription price, delivery charge and stock|
|30 | Store Owner | Delete a subscription | Remove subscriptions that are no longer used|

After reviewing all of the user stories, some wireframes / mockups of the pages for the site were created, 
These are wireframes available to view on Balsamiq:
- [Nutriverse - Mobile layout wireframes](https://balsamiq.cloud/s11kk48/py0t2ol)
- [Nutriverse - Large screen layout wireframes](https://balsamiq.cloud/s11kk48/p8tfm35)


## Features

Nutriverse is an Fitness and Nutrition e-Commerce website to provide users access to the Nutriverse range of Fitness and Nutrition classes and programs, as well as their fitness accessories needed for the classes.
While viewing the products available on the site, the user can also read through the product reviews and ratings given by other site users, as well as being able to add their own reviews for a product.

The site also has a Community area which allows for members to add new discussion topics for the range of products, so that they can provide progress reports or share their experience of how they progressed in the program, as well as being a base to ask questions or share ideas with other community members.
 
### Existing Features
- Site Registration and Profile
	- The site has an option to allow the user to register and login to their profile, which allows them to store and update their delivery details for faster checkouts. As well as being able to view their order history. On completion of the registration process a confirmation email is sent to the user to allow them to complete the account setup process by validating their email address using the validation link provided.
	- As part of the user profile configuration, the user has the option to reset their password through the use of a link. This will send an email to the registered email address and provide them with a link to enter a new password.
- Viewing and Navigation
	- The main page in the site provides access to the three main categories: "Fitness Products", "Nutrition Products" and "Community Area". A navbar with additional subcategory options is also available to filter the product selection further, to display similar items from that subcategory.
	- The products page will display all of the products by default, a search bar is also provided to allow a keyword search on the product titles and descriptions to allow them to search for a specific item that they are interested in purchasing.
	- There is a product sorting option to allow the customer to view and compare similar products by price or rating
- Purchase and Checkout
	- On selecting an individual product, the user can then view further information about the product, including its description, reviews and rating and the subscriptions available for the product.
	- The subscriptions options available for a product are listed in a select box, when any of the subscriptions are selected then the fields below it will be populated to show the price and availability for that subscription.
	- When the subscription is selected, there is some JavaScript to check the quantity being selected against the quantity available for that product or subscription. The + button is disable when it reaches the stock available level to prevent the user adding more items to their basket than is available.
	- Some further validations are completed at two stages when the Quantity is changed and when the Add to Basket button is clicked:
		- When the quantity is updated a function is run to check that the value is within the range 1 to 99 and disables either the + or - button when it reaches these values
		- The function also checks the quantity against the stock available for the product / subscription. If the quantity is greater than the stock available it will display a warning to the user.
		- When the form is being submitted there is another function to check that the item has a subscription or size selected has been selected. Otherwise it will prompt the user to select one.
		- The quantity ordered is checked against the quantity available to ensure that there is enough stock at the time of adding to the basket.
		- The stock should be checked again before processing the order.
	- When an item is added to the basket the total basket price is calculated and displayed in the navbar at the top of the page, which provides a convenient way for users to easily see and keep track of the total cost of their purchases.
	- The view basket option allows the customer to review the items that were selected for purchase, it also allows for the quantity selected on individual items to be adjusted, as well as being able to remove the item from the basket completely. 
	- The customer can checkout their purchases quickly and easily without the need to input too many details. There is also an option to save the delivery address details which will be automatically populated into the delivery details on any subsequent purchases.
	- The Stripe payments API provides a secure and convenient method to process the customer card payment details.
	- The order will be added to the database during this process, and the stock for the products purchased will be reduced by the quantity purchased. 
	- There are some limitations with this as there might be less stock when the customer is checking out, as another customer might have also selected to purchase this item in that time. Some additional work is required to complete a solution to this, but due to time limitations I have not been able to complete it. This is documented further in the Future Enhancements section.
	- On confirmation of the order and payment being processed, the order summary page is then displayed. This can also be access through the user's profile where a history of all orders is displayed.
	- An order confirmation email is also sent once the order has been successfully completed, for the user to keep for their records.
- Product Rating and Reviews
	- The site users can also add product reviews, these reviews are visible on the Product Details page on the Reviews tab near the end of the page. 
	- The Add Review button is available to the site users and allows them to add a review with a title and details about the product as well as giving them the option to rate the product. 
	- When the review is saved it will display a star rating using star icons to depict rating with the number of stars out of a possible five stars. 
	- The same star rating is displayed on the product, which is calculated from an average star rating taken from all the reviews for that product.
- Community and Discussions
	- The community area allows users to create discussion topics for both Fitness and Nutrition topics. The main community page displays a list of all previous topics. This list can be sorted and is automatically paginated to reduce the number of records being loaded, which is better for speed and uses less data.
	- Issues encountered with filtering the discussions list view by Fitness / Nutrition type topics:
		- Although I made a few attempts at trying to add a filter to the list view, I ran into a lot of issues with getting it to work. I also asked for the Tutors advise on how to use a filter on it, but I was advised that class based views were not recommended, but did provide me with some links to have a look at if I wished. 
		- As I had already used one to display all discussions without a filter, I then decided to try out a few different suggestions from the links. I still ended up with errors after implementing these.
		- As a workaround, I decided to reverse these changes, and instead added an if statement to the template so that I could display the discussion topics in two separate groups and put a heading for each group in the table at the start of each of the groups.
		- I also removed the two category filter options from the nav bar
		- In a future iteration of this page, I would create a view to display the objects in the same way as other pages were built. I used this as I thought it was a good method to display a list of the discussions easily. However I've learnt a lot from being able to try and work through some of these issues.
	- A community member has the option to add new discussion topics for a selected product. This can provide an evaluation of the product / service or class. It can also be used to give a report on their progress through the program, or to ask questions related to the product. The discussion topic can be edited by the author.
	- Other community members can add comments to each discussion in order to respond to the topic posted. These comments can also be edited and updated by the comment author.
- Product Management / Admin
	- The site has a Product Management section to allow store administrators to add, edit or delete products and subscriptions to the store. The main page in the Product Management section displays some buttons for quick and simple access to the different options available. These include Add Product, View a list of products - which allows individual products to be selected to edit or delete. The same options are available for product subscriptions.
	- The store has many Products which are linked to many Product Subscriptions, this many-to-many relationship is managed using a "through" table called Subscriptions.
	- When adding a new product, there are a number of selection boxes to choose options from, this makes it easier for product entry. There is also a list of subscriptions that can be added to any product. These are available in a multi-select list box so that a number of subscriptions can be selected and assigned to any product. There are also convenient links access the add or edit subscriptions sections from the add or edit product pages.
	- There are some fields in the Products model that are used to provide selection functionality when loading the templates, or excluding items when calculating delivery charges, a summary of these fields and their uses are detailed below:
		- Product.Subscription - This boolean field is used to show the Product Subscription list on the Product Details page. It was used because as the models evolved and I grew to understand how the many-to-many relationship worked, then all products ended up with a product subscription which has the price and stock available fields.
		- Product.Has_Sizes - Also a boolean field to determine if the Product has sizes, and used to display the Sizes list instead of the subscription list on the Product Details page.
		- There can be 3 types of Products: Those with a subscription, those with a size, and those with neither as they are just an item such as a sports bag or exercise mat and don't need a selection from either list. They do however have to be associated with a product subscription which is where the price and stock available is taken from.
		- Product.product_sub - This is the ManyToManyField from the Product_Subscription model. All products must have one product subscription, but if the value in Product.Subscription is False - then the subscription list will not be displayed, and the price and quantity will be displayed directly on the product details page. Similarly if the Product.Has_Sizes is True then the sizes list will be displayed instead of the subscription list on the product details page.
		- Some helper texts were added to the Add Product form to assist with the values used in these fields.
	- On adding a new subscription the user can select the subscription type as well as the price, quantity available and delivery charge (Y/N) - this is used to calculate delivery costs when the user is checking out. As some products are available as online programs or classes - there would be no need to charge for delivery of such subscriptions.
	- The lists of Products or Subscriptions will be displayed to show the user all existing items. These lists can be sorted by each column heading and there is also a search option available to find a particular product or subscription through a keyword search of the name or description.
 

### Future Enhancements
- Stock Management & Order Processing
	- When the product is being purchased there is currently a check in place to ensure that there is enough stock for the quantity being ordered. This happens when the product is being added to the basket.
	- During the checkout process when the order is being saved to the database, the stock for the selected product is also reduced
	- This solution is not ideal, as other customers could have ordered that product during the time between where the first customer had added it to the basket, and when they went to check out. This means that the stock might not be available.
	- Some more development is needed in order to check for the stock before the order has been created, and if there is not sufficient stock available the user should then be prompted to reduce the quantity they wish to purchase, or to cancel the purchase of this product. 
	- When the user has made their selection they should check out again.
	- Due to time limitations I have not completed this section, but would be done in the next iteration.
- Community and Discussions
	- The community area could be further developed with more options available to allow the user to add fitness challenges / exercise plans, which would include multiple steps or exercises to be entered for each day of the challenge / plan. 
	- An example of this would be a 30-day fitness challenge that focuses on a particular fitness area, with instructions to complete a range of different exercises on each day of the challenge.
	- The topics and comments in the community area could be enhanced to show more details about the user such as the date they joined the site, and the number of topics they have created on the site. Other details could be added depending on the sites requirements / areas of interests.
	- Another section that could be added would be an index to look up details for any exercise with pictures or videos on how to complete the exercise.
- User Profile
	- The user profile section could also be updated to include options to add and store multiple delivery addresses for the account. This could then be integrated into the Checkout page where the user could select the delivery address from their list of saved addresses.
	- Further customisation of the user profile could also be achieved by allowing the users to add or update a profile picture, and some details about themselves. The profile pictures could be displayed as a small circular image beside each of the user's reviews or community area topics / comments.
- Product Management
	- Some updates could be made to the Product Administration section in particular for the product deletion option where currently no warning is given to the user for them to confirm if the product should be deleted. An extra step could be added to this process to prevent user error in selecting the wrong product for deletion. This would ask the user to confirm the product being deleted, and give an option to cancel or continue with deleting the selected item.

## Technologies Used

Some of the technologies that I used to implement the features and functionality of this e-Commerce site are detailed below:

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - **HTML5** is the markup language used to structure and present the content of the website. It provides features allowing for use of forms and tables in the website.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - A **CSS Stylesheet** was used to define the style of the page such as images, headings and tables. Some Media Queries are also used in order to apply different settings depending on the screen size being used to view the site.
- [FontAwesome](https://fontawesome.com/)
    - **Font Awesome** is used to add icons to the navbar and on buttons, and throughout the project.
- [Bootstrap 4](https://getbootstrap.com/)
	- **Bootstrap** is a CSS framework that contains  CSS and JavaScript based design templates to help in development of responsive, mobile-first websites.
	- It has been used on all pages for the site in order to assist with the layout by making uses of the Grid, Table and Card templates.
	- Bootstrap also has helper texts that allow the use of simple classes to format the layout further without having to re-write more CSS. For example the bottom margin can be set by just specifying the "mb-5" class / helper text in an element, and the Bootstrap CSS will then be used to apply it, which saves time in development as well as allowing consistency across each template.
- [Bootswatch - Flatly Theme](https://bootswatch.com/flatly/)
	- **Bootswatch** is a free and customisable theme that is used with Bootstrap.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
	- **JavaScript** is one of three core technologies alongside HTML and CSS which are used to create web pages. It is a scripting language that is used to make the web page dynamic  by adding interactivity to it. This means with JavaScript code can be added for mouse click or mouse over, and other events on the web page. 
	- A combination of functions were used in both JavaScript and JQuery in order to add functionality throughout the site.
	- On the Product Details page a JavaScript function was used to check they quantity value and disable the quantity +/- buttons if the value was outside of 1-99 range.
	- It was also used to provide additional validation against the product's quantity available, and would also disable these buttons if it reached the product's stock limit.
	- Also on the Product Details page, a JavaScript function was used to get the selected product subscription value and send it to the form submission. The page was then reloaded with the details for this subscription available.
	- On the Checkout form it handles real-time validation errors on the card element, checks for card errors and if there is an error on the page it will be displayed. 
	- It also handles the Checkout form submission and sends the billing and shipping details as a Stripe payment intent, as well as handling the toggle for the loading logo to be displayed by CSS while the payment intent is being sent and returns a success status.
- [JQuery](https://jquery.com)
    - **JQuery** is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation. It is used for many different functions to improve the user interactivity on the website.
	- A back to top button is implemented on some pages where there could be a lot of scrolling through product lists, the function simply returns the user to the top of the page. Another simple function is used on some pages to set the sorting value and direction of a table or on the main Products page.
	- On the shopping basket page JQuery is used on both the update quantity and remove item links to submit the form updating the quantity for the selected item, or to remove the subscription / size for a product from the basket.
	- While JavaScript is used on the Product Details page to validate the quantity values, JQuery is also used  to enable or disable the +/- buttons for the quantity depending on the value in the quantity input box. It is also used to increment or decrement the quantity value when these buttons are clicked.
	- A validation is performed on the Product Detail page also so that a form submission is prevented if the user has not selected a product subscription or size. Otherwise an error will be displayed asking them to select an option before trying to add the product to the basket.
	- In the Product Management section for both adding or editing a product, JQuery will check if an image file has been selected, and show the file name / location for the new image.
- [Python](https://www.python.org/)
	- **Python** is a high-level programming language that can be used for developing desktop and web applications.
	- It was used throughout the project in order to build views and functions that can get the required data for each template.
	- Views and Functions were used to search for and filter data from the Database, and also to add / update or delete records in the various models used for the application.
	- Python was also used to create a model function which calculates the average rating for an individual product, based on the user rating value from each product review.
- [Django](https://www.djangoproject.com/)
	- **Django** is a high-level Python web framework, that encourages rapid development and clean pragmatic design, through the use of the model-template-views architectural pattern.
	- It was used in the project in order to create the database models, which structured the format in which the data was stored.
	- Views and Templates were also then used to select and filter data and perform various functions before adding these variables to the template which is then displayed as a page in the web application.
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
	- **django-allauth** is an integrated set of applications for user account management that provides authentication, registration, account management, as well as social account authentication.
	- It was used to provide a simplistic account registration and authentication process, along with account management functionality for password resets.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/)
	- **django-crispy-forms** allow for creation of a customised form template that will let you control the rendering behavior of the sites Django forms. 
	- It allows for these customisations to be done while still allowing for the standard interaction with Django on the form template.
- [django-countries](https://pypi.org/project/django-countries/)
	- **django-countries** is an application that provides country choices for use with forms, flag icons static files, and a country field for models.
	- It was used on the Checkout form in order to provide a list of Countries to select for the postal / billing address, which would be sent to Stripe as a valid country code when making the payment.
- [Stripe](https://stripe.com/docs/api)
	- **Stripe** is an American financial services and software as a service company headquartered in San Francisco, USA.
	- The Stripe API is organized around REST. The API uses predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
	- The Stripe API was used in the project to build the payment form on the Checkout page, and to send secure payment intents to Stripe to process the payments.
	- A response was received from Stripe to indicate if the payment intent was successful or not, and could provide warnings to the user if not.
- [Amazon S3](https://aws.amazon.com/s3/)
	- **Amazon S3 - Simple Storage Service** is a service offered by Amazon Web Services that provides object storage through a web service interface.
	- A storage bucket was set up and configured on Amazon S3 to allow for storage of the media and static files that would be used on the website. 
	- Through the use of the django-storages and boto3 APIs, it allows the store administrators to upload new product images which will be stored in the S3 bucket.
- [django-storages, boto3 and s3transfer for Amazon S3](https://django-storages.readthedocs.io/en/1.1.6/backends/amazon-S3.html)
	- **django-storages** is a collection of custom storage backends for Django, it is used in the project to provide the connection to Amazon S3
	- Two backend API's are need to interact with Amazon S3. Storages is the s3 backend, which is simple and based on the Amazon S3 Python library. 
	- The second backend is **boto3**; it is the only supported backend for interacting with Amazon’s S3, S3Boto3Storage, based on the boto3 library. It allows you to upload media files by setting the Default file storage and the Static file storage.
	- **S3transfer** is a Python library for managing Amazon S3 transfers which is used by boto3 to pass configuration settings for file upload
- [Pillow](https://pypi.org/project/Pillow/2.2.1/)
	- **Pillow** is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images
- [Gunicorn](https://gunicorn.org/)
	- **Gunicorn** is a Python Web Server Gateway Interface (WSGI) HTTP server. It takes care of everything which happens in-between the web server and the web application. 
	- It handles a number of functions through the WSGI Interface, such as: Communicating with multiple web servers; Reacting to lots of web requests at once and distributing the load; Keeping multiple processes of the web application running
- [dj-database-url](https://pypi.org/project/dj-database-url/)
	- **dj-database-url** is simple Django utility allows you to configure the a Database URL and has a method to return a Django database connection dictionary 
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
	- **psycopg2-binary** is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.
- [sqlparse](https://sqlparse.readthedocs.io/)
	- **sqlparse** sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
- [SQLite](https://www.sqlite.org/)
	- **SQLite** is a relational database management system contained in a C library. It is embedded into the end program rather than being a client-server database engine like most other database management systems.
	- It was used as the development database while creating the project, providing fast and reliable data services to the application. SQLite works great as the database engine for most low to medium traffic websites
- [Heroku Postgres](https://www.heroku.com/postgres)
	- **Heroku Postgres** is a managed SQL database service provided directly by Heroku. You can access a Heroku Postgres database from any language with a PostgreSQL driver, including all languages officially supported by Heroku.
	- When deploying the website to Heroku, the Heroku Postgres database was selected to use in the production environment because SQLite runs in memory, and backs up its data store in files on disk. This is not suitable for use with the Heroku ephemeral filesystem where the contents will be cleared periodically. If the SQLite database was used on Heroku, the entire database at least once every 24 hours.	
- [Heroku](https://www.heroku.com)
	- **Heroku** is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. 
	- It is used to deploy, manage, and scale modern apps. The platform is elegant, flexible, and easy to use, and offers the simplest path for getting apps to market.
	- Heroku manages app deployments with Git or GitHub, which are popular version control systems
	- The web application has been deployed to and run from the Heroku platform. All updates are managed automatically with a connection to the GitHub software repository.
- [GitHub](https://github.com/)
	- **GitHub** provides hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features.
	- It can be used as a command line tool, but a Web-based graphical interface is also available to use which provides access control and several collaboration features, such as a wikis and basic task management tools for every project.
	- As the project was being developed it was pushed to a GitHub software repository which acted as a backup and version control, meaning that a previous version could be rolled back to using GitHub command line functions or the web-based interface.
- [GitPod](https://gitpod.io/)
	- Development of the application was completed in **GitPod** which is an online IDE which can be launched from any GitHub page and provides a fully working development environment, including a VS Code-powered IDE and a cloud-based Linux container configured specifically for the project at hand.
	- It contains the entire development workflow in a browser tab, and has convenient tools for sharing and collaborating.
- [coverage](https://pypi.org/project/django-coverage/)
	- **coverage** is a reporting tool to use on your tests which shows how much of your code is exercised with your tests.
	- It was used in this project to generate a report of the coverage of tests created for a particular app


## Testing

- The tests carried out for the completion of this site are detailed in the [Testing Documentation](./Testing.md)

## Deployment

In order to deploy the project to the Heroku hosting platform a number of configuration settings had to be completed. The Production environment also uses a Postgres database, and the database models as well as the data from the SQLite development database had to be recreated in the new Postgres database.
Details of the updates and configuration completed to deploy to the production environment are detailed below

- Database Setup and Configuration	
	- I used the dumpdata command to take a backup of individual tables in the SQLite database
	- The Heroku Postgres database was created and configured
	- After this 2 new applications were installed **dj-database-url** and ***psycopg2-binary** - these were used to connect to the Heroku Postgres database
	- Updates were required in Settings.py in order to set the DATABASES configuration settings to use the dj-database-url
	- Added the DATABASE_URL to the Heroku config vars
	- After this the migrations needed to be run to transfer all of the models to the new Postgres database.
	- Once this was completed, the loaddata commands were run, I choose to run the command for each model individually with the backed up data from the SQLite database. This helped in saving some time rather than having to reconfigure a lot of settings that had been manually done in the Django admin.
	- A superuser was created and validated for access to the admin
- Heroku Configuration Settings
	- Gunicorn was installed then to act as a web server
	- Created the Procfile - this tells Heroku to create a webdino that runs Gunicorn to server the Django application
	- Temporarily disabled Collect Static to stop Heroku trying to collect static when deployed "DISABLE_COLLECTSTATIC = 1 --app nutriverse"
	- Add Heroku application name to the ALLOWED_HOSTS in settings.py
	- I linked the GitHub repository in Heroku and allowed automatic deploys from the GitHub master after doing an initial push to the Heroku master
	- A new secret key was generated and the a key for SECRET_KEY was added to the config vars in Heroku, as well as updating the settings.py to get this value from the environment variables.
	- Added a key in the GitPod Environment Variables for DEVELOPMENT = True, and updated the settings.py to remove the secret key allow it to switch between the development and production environments easily.
- Amazon S3	Setup and Configuration
	- Created an Amazon AWS account and signed into the AWS Management console
	- Found the Amazon S3 service and created a new bucket in it to match the Heroku app name
	- Select Europe West 1 region (nearest my location), and unticked the box to block all public access.
	- Accepted the acknowledgment that the bucket will be public, then created the bucket
	- Click on the properties tab and turn on static website hosting, enter the defaults for index.html & error.html and click save. 
	- On the permissions tab the CORS configuration had to be pasted into the text box - to set up the required access between Heroku app and the S3 bucket
	- On the policy tab click the policy generator and select S3 bucket policy.
	- Allow all priciples by using a * 
	- Select Get Object in the Action list
	- Go to the Bucket Policy Editor on the Permissions tab and copy the ARN, and paste it into the ARN box at the end of the policy generator
	- Click Add Statement, then Generate Policy
	- Now copy the policy into the Bucket Policy Editor, modify the resource key to include slash star at the end of the Resourse line, which allows access to all resouces in the bucket. Then click Save
	- Go to the Access Control List option under the Permissions tab
	- Select Everyone under Public Access, and tick the List objects box, then click Save
- Creating IAM users and Access Groups
	- Go to the services menu in AWS and click on IAM (Identity and Access Management)
	- 3 steps to be completed in this section: Create a Group, Access Policy to give the group access to the bucket, assing a user to the group
	- **Group Creation**
		- Click Groups, select New Groups and enter a name for your group according to its function such as "manage-nutriverse"
		- Click next step twice, the click Create Group
	- **Create Policy**
		- Click Policies, and Create Policy, then select the JSON tab
		- Select import managed policy and search fro S3 and import "S3 full access policy"
		- Change the Resource on the JSON tab from having [star] which would have access to everything, and instead paste in the ARN which can be copied from the S3 Bucket Policy page.  
		- This will allow full access to the bucket and everything in the bucket only.
		- Click Save and then review policy and give it a name and description
		- Name "eldowling-nutriverse-policy"
		- Description "Access to S3 bucket for Nutriverse static files"
		- Then click Create Policy
	- **Attaching Groups**
		- Select Groups, then select the group that was created (manage-nutriverse group)
		- Click attach policy in permissions
		- Search for the policy name that was created (eldowling-nutriverse-policy) and select it
		- Click attach policy
	- **Adding User to the Group**
		- Select Users and click Add user
		- Enter a name: "Nutriverse-staticfiles-user"
		- Tick progrmmatic acces and click Next
		- Add user to the Group, select the group name "manage-nutriverse" and click Next
		- Click Next again and then Create user
		- **Download and Save** the csv file - important to save this as it will be used to configure the in Heroku
- Configuring Application to connect to the S3 bucket
	- Install **boto3** and **django-storages** in the Django project - these are needed to connect to the S3 storages
	- In settings.py add 'storages' to the INSTALLED_APPS
	- Also in settings.py add the AWS connection settings which are detailed below, use if USE_AWS key is True from the Heroku environment variables so that these settings are only applied in the production environment
	- **Config vars for settings.py**:
		- AWS_STORAGE_BUCKET_NAME = 'nutriverse-edowling'
		- AWS_S3_REGION_NAME = 'eu-west-1'
		- AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
		- AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
	- **Add new variables to Heroku config vars**
		- AWS_SECRET_ACCESS_KEY - use settings from the csv file that was downloaded and saved 
		- AWS_ACCESS_KEY_ID - use settings from the csv file that was downloaded and saved 
		- USE_AWS = True
		- Delete the DISABLE_COLLECTSTATIC variable - Django will collect static files automatically and upload them to Heroku the next time the project is deployed.
	- In settings.py add another variable below the other AWS vars
	- AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' 
	- This tells Django where the static files are coming from in production.
	- Created 2 custom classes: **StaticStorage** and **MediaStorage** to set the location of static files and media files, these are saved in custom_storages.py
	- The settings to use these file locations are created in settings.py add the following variables to it which is also done just below the "if USE_AWS" condition:
		- STATICFILES_STORAGE = 'custom_storages.StaticStorage'
		- STATICFILES_LOCATION = 'static'
		- DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
		- MEDIAFILES_LOCATION = 'media'
		- STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
		- MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
	- Commit these settings and push to Heroku
- Copy Media files to the S3 bucket
	- Open S3 and create a new folder called "Media" in the bucket
	- Inside the new folder click on Upload, the Add Files and select all of the product images
	- Click Next and select "Grant public read access to these objects" under Manage Public Permissions
	- Click Next through to the end, then click Upload
- Add Stripe Keys to Heroku Config Vars
	- A new webhook needs to be created in Stripe for the url to the Heroku app: "https://nutriverse.herokuapp.com/checkout/wh/"
	- A signing secret can then be copied from this webhook to the Heroku Config vars as well as the Strip secret key:
		- STRIPE_SECRET_KEY - get the settings from the Stripe account
		- STRIPE_WH_SECRET - get this from the new webhook created
	- Send a test webhook from Stripe to the Heroku app, check that it returns a successful message at the bottom of the page.
- Email Configuration
	- In your email account (Gmail used for this project) open settings
	- Select Accounts & Import, then other Gmail account settings
	- Click the security tab, and turn on 2 step verification
	- Click Get started and enter password
	- Select verification method
	- In settings, signing in under Google
	- Add App Passwords
	- Select Mail
	- Choose "Other" and type "Django" then click Generate
	- Copy the password and set up the following 2 variables in Heroku config vars:
		- EMAIL_HOST_PASS - copied from Gmail app password just created
		- EMAIL_HOST_USER - type your own email address for the account you used to configure the app password.
	- Commit this and push it to GitHub / Heroku
	- Test by creating a new account in the application and checking that the verification email is sent.


## Credits

### Content
- [Business Name Generator](https://businessnamegenerator.com/)

#### CSS
- I initially thought of creating a home page with two images which were split at the top of the screen. I worked with this a little to test it before returning to try the Bootstrap carousel, where I have now implemented three rotating images relating to the three sections of the site.
- [CSS Tricks - Multiple image background-image](https://css-tricks.com/almanac/properties/b/background-image/)
- [Responsive Full Background Image Using CSS - William Craig](https://www.webfx.com/blog/web-design/responsive-background-image/)
- [CSS background-image Property - W3Schools.com](https://www.w3schools.com/cssref/pr_background-image.asp)
- [Bootstrap carousel resizing image - Stackoverflow](https://stackoverflow.com/questions/17357306/bootstrap-carousel-resizing-image)
- [Bootstrap 4 Responsive tables won't take up 100-width](https://stackoverflow.com/questions/41747667/bootstrap-4-responsive-tables-wont-take-up-100-width) - this forum question was used to try and fix an issue I had with trying to implement a responsive Bootstrap table, by moving the table-responsive class from the table tag to the div it resolved the issue.
- [DataTables.net Bootstrap Tables]() A CSS script was used to apply the styling on the Data Tables used for the Discussion List View and Products / Product Subscriptions List views - more details about this is provided in the JavaScript / JQuery section below as the tables also use some JavaScript functions and libraries.
	- The css library file "https://cdn.datatables.net/1.10.22/css/dataTables.bootstrap.min.css" was also used together with the Bootstrap CDN
- For the Product Ratings and Review I wanted to implement a star rating which would use an icon and the number of coloured stars would indicate the average rating for the product. For example a 4 out of 5 rating would display 4 coloured stars and 1 empty star. I looked up a few tutorials on this to try and find some JavaScript / CSS that could do this. These included the following tutorials / videos:
	- [Star Ratings With JavaScript & Font Awesome - Traversy Media](https://www.youtube.com/watch?v=u3rylF3y3og)
	- [Star Ratings Codepen - Brad Traversy](https://codepen.io/bradtraversy/pen/GQLRZv)
	- [Pure CSS Star Rating Widget - How To Create a Simple Star Rating with Html and CSS - No Javascipt - by Online Tutorials](https://www.youtube.com/watch?v=Ep78KjstQuw)
	- [Rating Systems in HTML, CSS and JS - Steve Griffith](https://www.youtube.com/watch?v=dPCj6Qkq13Y&t=48s)
	- [#9. Django Ratings - Programming Knowledge .360](https://www.youtube.com/watch?v=uRJuONWrlEw&t=149s)
	- [Convert ratings in stars in Django template - Stack Overflow](https://stackoverflow.com/questions/55448221/convert-ratings-in-stars-in-django-template)
	- I successfully installed and implemented this Django application in order to generate the Product Star ratings and user review ratings. However when I began testing the star-ratings within the site I realised that it wasn't working exactly how I wanted it to and that the star ratings could be selected and un-selected too. There was also problems with other customisations I wanted to make, and although there is some documentation available for various settings used to customise the app, the documentation was limited and I couldn't find solutions to what I wanted to do. I then decided to uninstall the app and find an alternative solution. The link for the django-star-ratings app is below
	- [django-star-ratings app](https://pypi.org/project/django-star-ratings/)
	- [Please Add documentation for 'how to use' django-star-ratings with needed screenshots #140 - GitHub](https://github.com/wildfish/django-star-ratings/issues/140)	
	- [Django Rated Reviews - Quick start guide](https://django-rated-reviews.readthedocs.io/en/latest/quickstart.html)
	- [Five Methods for Five-Star Ratings - Alfred Genkin](https://css-tricks.com/five-methods-for-five-star-ratings/) After reading this I decided to try and implement "Method 4: Using CSS to draw the shape" in my solution and it is currently displaying star ratings for both products average rating and the user review ratings.


### JavaScript / JQuery
- I tried to implement some custom JavaScript functions that would allow the site to be more interactive for the user. Some of the pages I used as a reference to implement these functions are listed below
- [HTML DOM Events - onchange Event - w3schools.com](https://www.w3schools.com/JSREF/event_onchange.asp) the onchange event was used in the Product Details page when a subscription or size was selected from the list, then a Javascript function "updateSubscription" will get the subscription ID and populate it to a hidden field. It can then submit the form which will get the subscription selected and pass the details back to the template using the view.
- [JavaScript Events - w3schools.com](https://www.w3schools.com/js/js_events.asp)
- [How can I use the JavaScript onchange event to submit a form? - Stack Overflow](https://stackoverflow.com/questions/23861674/how-can-i-use-the-javascript-onchange-event-to-submit-a-form/23861697#23861697)
- [jQuery Traversing - Ancestors - w3schools.com](https://www.w3schools.com/jquery/jquery_traversing_ancestors.asp)
- [Jquery remove parent or parents until a specific class name - Stack Overflow](https://stackoverflow.com/questions/43952269/jquery-remove-parent-or-parents-until-a-specific-class-name)
- [Form Validation with JavaScript - Check for an Empty Text Field - Ralph Phillips](https://www.youtube.com/watch?v=Pc2e2YpKArg&t=342s)
- I looked into using the following table functionality which was documented on the MDBootstrap website, I thought at firsth that it only needed the JQuery functions to support it, however it on reading further I seen that this was a downloadable product that needed to be purchased and so I didn't continue to try and use it.
	- [MDBootstrap Responsive Tables](https://mdbootstrap.com/docs/jquery/tables/responsive/)
	- [MDBootstrap Pagination and Advanced Table Options](https://mdbootstrap.com/docs/jquery/tables/pagination/)
- I continued to research other options to apply advanced table styles to display the discussion topic list views in the Community Area as well as the Products and Product Subscriptions list views in the Product Management section. I was able to find something suitable on the DataTables.net site:
- [DataTables.net Bootstrap Tables](https://datatables.net/examples/styling/bootstrap) These tables can be easily integrated with Bootstrap tables and using Bootstrap styling options. There was some additional CSS libraries installed (see CSS section above). The following JavaScript libraries were also used to complete the table functionality
	- https://code.jquery.com/jquery-3.5.1.js
	- https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js
	- https://cdn.datatables.net/1.10.22/js/dataTables.bootstrap.min.js


#### Django
- When it came to implementing my Product Details page, I needed to find out how to create the Model for the table structure where a Product has multiple Subscription Types and each Subscription Type had a Price and a Quantity Available. I also needed to understand the method used to extract the related data and display it on the Product Details page. For this I looked up some pages related to getting data from multiple tables. This in turn lead me to investigating the Django Select_Related and Prefetch_Related functions further to try and implement these with my project. I found that this was not the right solution and instead tried to find tutorials relating to Many to Many field relationships. I then found a few parts in the set of tutorials by Dennis Ivy to be very useful in what I was trying to implement, and I took these as the basis to write my own views and updated the models accordingly. The following links were used in order to research and implement the Many to Many related tables needed to build the Product Details page.
	- [Fetching data from multiple tables in Django - Stack Overflow](https://stackoverflow.com/questions/48596388/fetching-data-from-multiple-tables-in-django)
	- [Django get data from multiple tables](https://stackoverflow.com/questions/36569457/django-get-data-from-multiple-tables)
	- [Django Documentation - QuerySet API Reference](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)
	- [Django select_related and prefetch_related - by Goutom Roy | Better Programming(https://medium.com/better-programming/django-select-related-and-prefetch-related-f23043fd635d)
	- [Daily Django - #09 - select_related() e prefetch_related()](https://www.youtube.com/watch?v=JU7scCwEAI0)
	- [Querying One-To-Many Relationships in Django - PrettyPrinted](https://www.youtube.com/results?search_query=django+select_related+and+prefetch_related)
	- [How to Get Data Out of a Django Model and in to the HTML Template (Django Tutorial) | Part 48 - Max Goodridge](https://www.youtube.com/watch?v=VxOsCKMStuw&t=322s)
	- [Django - Filter the prefetch_related queryset - Stack Overflow](https://stackoverflow.com/questions/52757040/django-filter-the-prefetch-related-queryset)
	- [Django select_related Examples |Django select_related and prefetch_related |Django n+1 Query Problem - Code Band](https://www.youtube.com/watch?v=mO-pfdJpnBA)
	- [How to Use a Many to Many Field in a Django Model (Django Tutorial) | Part 55- Max Goodridge](https://www.youtube.com/watch?v=nwpLCa79DUw&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=54)
	- [How to Create Useful Many to Many Relationships in Django (Django Tutorial) | Part 56 - Max Goodridge](https://www.youtube.com/watch?v=bFhuOULgKDs)
	- [Django Documentation - Many-to-many relationships](https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/)
	- [Database Relationships | One To Many & Many to Many | Django (3.0) Crash Course Tutorials (pt 6) - Dennis Ivy](https://www.youtube.com/watch?v=wIPHER2UBB4)
	- [Database Model Queries | Django (3.0) Crash Course Tutorials (pt 7) - Dennis Ivy](https://www.youtube.com/watch?v=PD3YnPSHC-c)
	- [Tips for Using Django's ManyToManyField - Lacey Williams Henschel](https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/)
	- [Django Documentation - Many-to-many through](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField.through)
	- [Django Many To Many Insert Ordering - Stack Overflow](https://stackoverflow.com/questions/1880530/django-many-to-many-insert-ordering)
	- [Rendering Data to Templates | Template Tags | Django (3.0) Crash Course Tutorials (pt 8) - Dennis Ivy](https://www.youtube.com/watch?v=7a23TbUXfWE)
	- [Dynamic URL Routing & Templates | Django (3.0) Crash Course Tutorials (pt 9) - Dennis Ivy](https://www.youtube.com/watch?v=HhjnQIpXqPc)
	- [Django Documentation - Built-in template tags and filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)
- Defining a Unique Constraint for a field in a Model
	- [Django Models - Constraints reference](https://docs.djangoproject.com/en/3.0/ref/models/constraints/#django.db.models.UniqueConstraint.fields)
	- [Django Models - Fields reference](https://docs.djangoproject.com/en/3.0/ref/models/fields/)
	- [Django UniqueConstraint - Stack Overflow](https://stackoverflow.com/q/56024059)
	- [How to define two Django fields unique in certain conditions - Stack Overflow](https://stackoverflow.com/questions/62863568/how-to-define-two-django-fields-unique-in-certain-conditions?noredirect=1&lq=1)
- Also on the Product Details page, I wanted to have an update functionality once the Subscription Type select box was changed, that it would automatically display the price and quantity available for the selected subscription. Instead I ended up with "Change" button to submit the form and query the database. This method was initially implemented using the change button beside the select box, as I progressed through the project I was able to create the JavaScript function that allowed for the form to be submitted - This is detailed in the JavaScript section above. The resources used to implement this are detailed below.
	- [How to display value of a field in a *linked* table, in a Django template? - Stack Overflow](https://stackoverflow.com/questions/25232741/how-to-display-value-of-a-field-in-a-linked-table-in-a-django-template)
	- [Populating a drop-down from Database in Django - Stack Overflow](https://stackoverflow.com/questions/54171359/populating-a-drop-down-from-database-in-django)
	- [Django - Populating data from database in a dropdown select tag - Stack Overflow](https://stackoverflow.com/questions/49731140/django-populating-data-from-database-in-a-dropdown-select-tag)
	- [Django dynamic forms - on-the-fly field population? - Stack Overflow](https://stackoverflow.com/questions/8998428/django-dynamic-forms-on-the-fly-field-population)
	- [Django/jQuery Cascading Select Boxes? - Stack Overflow](https://stackoverflow.com/questions/3233850/django-jquery-cascading-select-boxes)
	- [Django - Built-in template tags and filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#id2)
	- [How to pass csrf_token to javascript file in django? - Stack Overflow](https://stackoverflow.com/questions/23349883/how-to-pass-csrf-token-to-javascript-file-in-django)
- The JavaScript function detailed above was also modified to check the stock available against the quantity being purchased. The link below was used to help with creating the function, I combined this with the other checks that were being done and returned a status from the new function called "checkStockAvailable()". If the status returned = "OK" then it could proceed with submitting the form. Otherwise an error was displayed to the user.
	- [JavaScript Quantity Validation - Stack Overflow](https://stackoverflow.com/a/16931755)
- For the Product Rating on the Product Details page, I needed to create a function to get the average rating which would be calculated from the Reviews.user_rating field. I looked at many options including doing it in the view using a filter query, and then update the Products table with the average rating value, but couldn't find a solution that worked well. I also looked at creating a function and returning the value to a view. I also asked for help with this on Slack and Malia Havlicek (Lead) was able to give me some some links to look at. By looking at these resources and some further help, I was able to build a function in the Product Model and reference the function from the template using "{{ product.get_avg_rating }}"
	- [Django - Function inside a model. How to call it from a view?](https://stackoverflow.com/questions/21093591/django-function-inside-a-model-how-to-call-it-from-a-view)
	- [Django Documentation - Generating aggregates over a QuerySet](https://docs.djangoproject.com/en/3.1/topics/db/aggregation/#generating-aggregates-over-a-queryset)
- For the Checkout page I needed to find some tutorials on adding items to the basket/cart, as I was trying to add items that had subscriptions / foreign key fields and was having issues with getting the subscription details to add to the basket. I used the following tutorials to help with my understanding of the process and then could try to implement a solution
	- [Django Ecommerce Website | Add to Cart Functionality | Part 3 - Dennis Ivy](https://www.youtube.com/watch?v=woORrr3QNh8&t=1426s)
	- [Django tutorial for beginners - 26 Cart Item - Coding Point](https://www.youtube.com/watch?v=N3VWvPqWnwc&t=64s)
- In the checkout view the Order and Order Items will be written to the database, I needed to also update the stock and reduce it by the quantity being purchased. I looked at the link below which gave me an idea of how I was going to approach it. I also had some suggestions made by my mentor Dick Vlaanderen to help simplify the method to update it slightly, as I had already a variable that stored the filtered the selected product subscription object, so I could just use this variable to select the field that I wanted to update.
	- [Django: How to edit value and store back in database - Stack Overflow](https://stackoverflow.com/a/54535126)
- On the checkout page I wanted to use an animated icon for the loading page while the payment was being processed - these are some of the examples I found
	- [https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons](https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons)
- I needed to find solutions the error "Reverse for '' Not Found"
	- [Django - Reverse for '' not found. '' is not a valid view function or pattern name - Stack Overflow](https://stackoverflow.com/questions/45724006/django-reverse-for-not-found-is-not-a-valid-view-function-or-pattern-na)
	- [What is a NoReverseMatch error, and how do I fix it? - Stack Overflow](https://stackoverflow.com/a/38390178)
- I wanted to create a list of all items in certain tables such as the Community Discussion Topics and the Products or Product Subscriptions in the Product Management section. I looked at various tutorials related to List views in order to be able to implement them.
	- [Try DJANGO Tutorial - 36 - Class Based Views - ListView - CodingEntrepreneurs](https://www.youtube.com/watch?v=Xeh9r0CXBmU&t=59s)
	- [Try DJANGO Tutorial - 37 - Class Based Views - DetailView - CodingEntrepreneurs](https://www.youtube.com/watch?v=TrJtYmfTWiA)
	- [The Basics of Django ListView - Pretty Printed](https://www.youtube.com/watch?v=J74OTEhmLU0)
	- [Django Filtering System with django-filter - Filter Queryset - The Dumbfounds](https://www.youtube.com/watch?v=nle3u6Ww6Xk&t=59s)
	- [Best way to filter ListView with drop down form in Django - Stack Overflow](https://stackoverflow.com/questions/46491786/best-way-to-filter-listview-with-drop-down-form-in-django)
	- [Django Documentation - Built-in class-based generic views](https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/)
	- [Django Tutorial Part 6: Generic list and detail views - MDN Web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
	- [Django no reverse match with filtered ListView - Stack Overflow](https://stackoverflow.com/questions/57803351/django-no-reverse-match-with-filtered-listview)
	- [Django Documentation - Retrieving specific objects with filters](https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-specific-objects-with-filters)
	- [How do I do an OR filter in a Django query? - Stack Overflow](https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query)
	- [Django ListView - Form to filter and sort - Stack Overflow](https://stackoverflow.com/questions/33350362/django-listview-form-to-filter-and-sort)
- For the Community Area I wanted to try and implement a filter on the products that would allow the user to only add a discussion for products that they had previously purchased. In doing this I came across some errors - one of these was when I tried to put a filter on the order line items by using the orders which was itself a filter of the selected users' Orders. The error I got on loading that view was "The QuerySet value for an exact lookup must be limited to one result using slicing". Using the following topics I was able to finish the filter that I wished to build and I was able to populate the users' ordered products to a select box on the form.
	- [The QuerySet value for an exact lookup must be limited to one result using slicing. Filter error - Stack Overflow](https://stackoverflow.com/questions/55994907/the-queryset-value-for-an-exact-lookup-must-be-limited-to-one-result-using-slici)
	- [Django - display all products created by a user](https://stackoverflow.com/questions/47027356/django-display-all-products-created-by-a-user)
	- [MultipleObjectsReturned Django - Stack Overflow](https://stackoverflow.com/questions/52155601/multipleobjectsreturned-django)
	- [get_list_or_404 with multiple filters in django - Stack Overflow](https://stackoverflow.com/questions/12950250/get-list-or-404-with-multiple-filters-in-django)
	- [Python django.shortcuts.get_list_or_404() Examples - Programcreek.com](https://www.programcreek.com/python/example/50062/django.shortcuts.get_list_or_404)
	- [Getting only the models related to a Django queryset - Stack Overflow](https://stackoverflow.com/questions/15162177/getting-only-the-models-related-to-a-django-queryset)
	- [Django excluding one queryset from another - Stack Overflow](https://stackoverflow.com/questions/22266734/django-excluding-one-queryset-from-another)
- Also relating to the filtered products on the Add Discussion form, I had an error when it came to submitting the form, it seemed to be related to the product I was trying to set from the selected value on the form. "MultiValueDictKeyError  ... 'product' ". To resolve this issue I had some help from the Tutor Support, who advised me to look at a link for a similar issue. On reading over this a few times and trying it out, I found / fixed the issue.
	- [django MultiValueDictKeyError error, how do I deal with it](https://stackoverflow.com/a/5895670)
- On the Community Discussions page when a topic was selected to view, I wanted to display a number in the list to show the comment number beside each comment I did this by displaying the {{forloop.counter}} but needed to add 1 to it to start from 1
	- [Django Template: How to modify the value in the for-loop tag?](https://stackoverflow.com/questions/30120196/django-template-how-to-modify-the-value-in-the-for-loop-tag)
- Also on the community discussions I wanted to show the created date for the discussion topic as well as the comments field, I wanted to learn how to format the date in a different format to how it was displayed by default
	- [Django Documentation - Date Format in template](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#date)
	- [How to format datetime objects in the view and template in Django - Ourcodeworld.com](https://ourcodeworld.com/articles/read/555/how-to-format-datetime-objects-in-the-view-and-template-in-django)
- To add line breaks on a form TextField
	- [newline in models.TextField() not rendered in template](https://stackoverflow.com/a/50630089)
- In the add product form of products management I wanted to add a link to Add / View Product Subscriptions above the Product Subscription select box, I researched some topics on this to find how to customise the form widgets in such a way. I also wanted to add some helper text below the input fields
	- [How to add a custom button or link beside a form field - Stack Overflow](https://stackoverflow.com/questions/45648692/how-to-add-a-custom-button-or-link-beside-a-form-field)
	- [How can I change the modelform label and give it a custom name - Stack Overflow](https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name/36905090)
	- [Django Documentation - Overriding default fields](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields)
	- [Django: how do I include a url link in a form label - Stack Overflow](https://stackoverflow.com/questions/6490408/django-how-do-i-include-a-url-link-in-a-form-label)
	- [Adding links to full change forms for inline items in django admin? - Stack Overflow](https://stackoverflow.com/questions/2857001/adding-links-to-full-change-forms-for-inline-items-in-django-admin/2925462)
	- [Display some free text in between Django Form fields - Stack Overflow](https://stackoverflow.com/questions/727917/display-some-free-text-in-between-django-form-fields)
- When it came to backing up and restoring the data in the SQLite database so that it could be restored to the new Postgres Database in Heroku, I needed to find more details on how to use the dumpdata and loaddata commands
	- [Django dumpdata and loaddata - by itseranga](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)
	

### Media
- The photos used for the products and main images were obtained from the following sources
- [Logo] - wix.com
- [Main image - Fitness by  Andrea Piacquadio](https://www.pexels.com/photo/selective-focus-photography-of-woman-in-white-sports-brassiere-standing-near-woman-sitting-on-pink-yoga-mat-864939/)
- [Main image - Nutrition by  Ella Olsson](https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Main image - Community by  Helena Lopes](https://images.pexels.com/photos/708440/pexels-photo-708440.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [BodySculpt Beginner by Steve Buissinne - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2465478)
- [BodySculpt Intermediate by Taco Fleur - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2054729)
- [BodySculpt Advanced by Pete Linforth - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1946596)
- [BodyTone by Scott Webb - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=828726)
- [Senior Workout Beginner - Shutterstock](https://www.shutterstock.com/image-photo/portrait-happy-men-women-on-fitness-259037090)
- [Senior Workout Advanced - Shutterstock](https://www.shutterstock.com/image-photo/senior-couple-exercising-gym-619305275)
- [Children's Fitness Workout by Lucas](https://images.pexels.com/photos/296301/pexels-photo-296301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Advanced Children's Workout by Luis Quintero](https://images.pexels.com/photos/1671217/pexels-photo-1671217.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Online Kettlebells Workout by Purple Smith from Pexels](https://images.pexels.com/photos/4527389/pexels-photo-4527389.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Online HIIT Workout by Karolina Grabowska from Pexels](https://images.pexels.com/photos/1671217/pexels-photo-1671217.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Senior Workout Online - Shutterstock](https://www.shutterstock.com/image-photo/fitness-training-online-senior-woman-home-1672681894)
- [Medicine Ball 3kg - Amazon.com](https://m.media-amazon.com/images/I/81n+-q4G47L._AC_UL480_FMwebp_QL65_.jpg)
- [Medicine Ball 5kg - Amazon.com](https://m.media-amazon.com/images/I/91Vmngw-z5L._AC_UL480_FMwebp_QL65_.jpg)
- [Medicine Ball 10kg - Amazon.com](https://m.media-amazon.com/images/I/51fO3yD359L._AC_UL480_FMwebp_QL65_.jpg)
- [Resistance bands set of 3 - Amazon.com](https://m.media-amazon.com/images/I/81LlSQGGwLL._AC_UL480_FMwebp_QL65_.jpg)
- [Resistance Bands 21 piece set - Amazon.com](https://m.media-amazon.com/images/I/71yPK88pcPL._AC_UL480_FMwebp_QL65_.jpg)

### Acknowledgments

- I would like to thank everyone who supported me through the completion of this project, in particular to my mentor Dick Vlaanderen, who guided and advised me throughout the course.
- I'd also like to thank the Tutors and Leads in Code Institute and fellow students on Slack, all of whom played a part in helping me to find different solutions when 