# Nutriverse

"Nutriverse" - a Nutrition and Fitness Universe: This is a space created to allow our customers to view different Fitness and Nutrition products, services and classes that are available, as well as our range of accessories and merchandise. It allows the customer to view each product description and reviews before deciding on their purchase.

The Community section allows our customers to add discussion topics for any of the services we offer, where they can share their experiences of these and other users can comment on the topics to answer questions. This area allows customers to support eachother as well as offering tips and advice.

The site also has an integrated administration and store management section. This allows authorised users to easily update and maintain the products and subscriptions available in the store.

## Table of Contents
- [Nutriverse](#nutriverse)
  * [UX](#ux)
  * [Features](#features)
    + [Existing Features](#existing-features)
    + [Features Left to Implement](#features-left-to-implement)
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
|7| Shopper | View individual product details | Identify the description, product rating, product image and available subscriptions or sizes.|
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
- [Nutriverse - Large screen layout wireframes](https://balsamiq.cloud/s11kk48/p31mhpy)


## Features

Nutriverse is an Fitness and Nutrition e-Commerce website to provide users access to the Nutriverse range of Fitness and Nutrition classes and programs, as well as their fitness accessories needed for the classes.
While viewing the products available on the site, the user can also read through the product reviews and ratings given by other site users, as well as being able to add their own reviews for a product.

The site also has a Community area which allows for members to add new discussion topics for the range of products, so that they can provide progress reports or share their experience of how they progressed in the program, as well as being a base to ask questions or share ideas with other community members.
 
### Existing Features
- The site has an option to allow the user to register and login to their profile, which allows them to store and update their delivery details for faster checkouts. As well as being able to view their order history. On completion of the registration process a confirmation email is sent to the user to allow them to complete the account setup process by validating their email address using the validation link provided.
- As part of the user profile configuration, the user has the option to reset their password through the use of a link. This will send an email to the registered email address and provide them with a link to enter a new password.
- The main page in the site provides access to the three main categories: "Fitness Products", "Nutrition Products" and "Community Area". A navbar with additional subcategory options is also available to filter the product selection further, to display similar items from that subcategory.
- The products page will display all of the products by default, a search bar is also provided to allow a keyword search on the product titles and descriptions to allow them to search for a specific item that they are interested in purchasing.
- There is a product sorting option to allow the customer to view and compare similar products by price or rating
- On selecting an individual product, the user can then view further information about the product, including its description, reviews and rating and the subscriptions available for the product.
- The subscriptions options available for a product are listed in a select box, when any of the subscriptions are selected then the fields below it will be populated to show the price and availability for that subscription.
- When an item is added to the basket the total basket price is calculated and displayed in the navbar at the top of the page, which provides a convenient way for users to easily see and keep track of the total cost of their purchases.
- The view basket option allows the customer to review the items that were selected for purchase, it also allows for the quantity selected on individual items to be adjusted, as well as being able to remove the item from the basket completely. 
- The customer can checkout their purchases quickly and easily without the need to input too many details. There is also an option to save the delivery address details which will be automatically populated into the delivery details on any subsequent purchases.
- The Stripe payments API provides a secure and convenient method to process the customer card payment details.
- On confirmation of the order and payment being processed, the order summary page is then displayed. This can also be access through the user's profile where a history of all orders is displayed.
- An order confirmation email is also sent once the order has been successfully completed, for the user to keep for their records.
- The community area allows users to create discussion topics for both Fitness and Nutrition topics. The main community page displays a list of all previous topics. This list can be sorted and is automatically paginated to reduce the number of records being loaded, which is better for speed and uses less data.
- A community member has the option to add new discussion topics for a selected product. This can provide an evaluation of the product / service or class. It can also be used to give a report on their progress through the program, or to ask questions related to the product. The discussion topic can be edited by the author.
- Other community members can add comments to each discussion in order to respond to the topic posted. These comments can also be edited and updated by the comment author.
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
- The community area could be further developed with more options available to allow the user to add fitness challenges / exercise plans, which would include multiple steps or exercises to be entered for each day of the challenge / plan. 
- An example of this would be a 30-day fitness challenge that focuses on a particular fitness area, with instructions to complete a range of different exercises on each day of the challenge.
- The topics and comments in the community area could be enhanced to show more details about the user such as the date they joined the site, and the number of topics they have created on the site. Other details could be added depending on the sites requirements / areas of interests.
- Another section that could be added would be an index to look up details for any exercise with pictures or videos on how to complete the exercise.
- The user profile section could also be updated to include options to add and store multiple delivery addresses for the account. This could then be integrated into the Checkout page where the user could select the delivery address from their list of saved addresses.
- Further customisation of the user profile could also be achieved by allowing the users to add or update a profile picture, and some details about themselves. The profile pictures could be displayed as a small circular image beside each of the user's reviews or community area topics / comments.
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
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- [Business Name Generator](https://businessnamegenerator.com/)

#### CSS
- I initially thought of creating a home page with two images which were split at the top of the screen. I worked with this a little to test it before returning to try the Bootstrap carousel, where I have now implemented three rotating images relating to the three sections of the site.
- [CSS Tricks - Multiple image background-image](https://css-tricks.com/almanac/properties/b/background-image/)
- [Responsive Full Background Image Using CSS - William Craig](https://www.webfx.com/blog/web-design/responsive-background-image/)
- [CSS background-image Property - W3Schools.com](https://www.w3schools.com/cssref/pr_background-image.asp)
- [Bootstrap carousel resizing image - Stackoverflow](https://stackoverflow.com/questions/17357306/bootstrap-carousel-resizing-image)

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
- [Django Documentation - Many-to-many relationships](https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/)
- [Database Relationships | One To Many & Many to Many | Django (3.0) Crash Course Tutorials (pt 6) - Dennis Ivy](https://www.youtube.com/watch?v=wIPHER2UBB4)
- [Database Model Queries | Django (3.0) Crash Course Tutorials (pt 7) - Dennis Ivy](https://www.youtube.com/watch?v=PD3YnPSHC-c)
- [Rendering Data to Templates | Template Tags | Django (3.0) Crash Course Tutorials (pt 8) - Dennis Ivy](https://www.youtube.com/watch?v=7a23TbUXfWE)
- [Dynamic URL Routing & Templates | Django (3.0) Crash Course Tutorials (pt 9) - Dennis Ivy](https://www.youtube.com/watch?v=HhjnQIpXqPc)
- Also on the Product Details page, I wanted to have an update functionality once the Subscription Type select box was changed, that it would automatically display the price and quantity available for the selected subscription. Instead I ended up with "Change" button to submit the form and query the database. I hope to have more time to implement the Javascript to do this without the need for a button in the future. The resources used to implement this are detailed below.
- [How to display value of a field in a *linked* table, in a Django template? - Stack Overflow](https://stackoverflow.com/questions/25232741/how-to-display-value-of-a-field-in-a-linked-table-in-a-django-template)
- [Populating a drop-down from Database in Django - Stack Overflow](https://stackoverflow.com/questions/54171359/populating-a-drop-down-from-database-in-django)
- [Django - Populating data from database in a dropdown select tag - Stack Overflow](https://stackoverflow.com/questions/49731140/django-populating-data-from-database-in-a-dropdown-select-tag)
- [Django dynamic forms - on-the-fly field population? - Stack Overflow](https://stackoverflow.com/questions/8998428/django-dynamic-forms-on-the-fly-field-population)
- [Django/jQuery Cascading Select Boxes? - Stack Overflow](https://stackoverflow.com/questions/3233850/django-jquery-cascading-select-boxes)
- [HTML DOM Events - onchange Event - w3schools.com](https://www.w3schools.com/JSREF/event_onchange.asp)

### Media
- The photos used in this site were obtained from ...
- [Logo] - wix.com
- [Main images x2 - Shutterstock]
- [BodySculpt Beginner by Steve Buissinne - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2465478)
- [BodySculpt Intermediate by Taco Fleur - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2054729)
- [BodySculpt Advanced by Pete Linforth - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1946596)
- [BodyTone by Scott Webb - Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=828726)
- [Senior Workout Beginner - Shutterstock](https://www.shutterstock.com/image-photo/portrait-happy-men-women-on-fitness-259037090)
- [Senior Workout Advanced - Shutterstock](https://www.shutterstock.com/image-photo/senior-couple-exercising-gym-619305275)
- [Children's Fitness Workout - Shutterstock](https://www.shutterstock.com/image-photo/cute-funny-children-dance-studio-569123587)
- [Advanced Children's Workout - Shutterstock](https://www.shutterstock.com/image-photo/laughing-preteen-kids-posing-sport-equipment-1309879342)
- [Online Kettlebells Workout - ]
- [Online HIIT Workout - ]
- [Senior Workout Online - Shutterstock](https://www.shutterstock.com/image-photo/fitness-training-online-senior-woman-home-1672681894)

### Acknowledgments

- I received inspiration for this project from X