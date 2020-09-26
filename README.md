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
These are available to view on [Balsamiq - Mobile Layout Wireframes](https://balsamiq.cloud/s11kk48/py0t2ol)
[Balsamiq - Large screen layout wireframes](https://balsamiq.cloud/s11kk48/p31mhpy)


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
- When adding a new product, there are a number of selection boxes to choose options from, this makes it easier for product entry. There is also a list of subscriptions that can be added to any product. These are available in a multi-select list box so that a number of subscriptions can be selected and assigned to any product. There are also convenient links access the add or edit subscriptions sections from the add or edit product pages.
- On adding a new subscription the user can select the subscription type as well as the price, quantity available and delivery charge (Y/N) - this is used to calculate delivery costs when the user is checking out. As some products are available as online programs or classes - there would be no need to charge for delivery of such subscriptions.
- The lists of Products or Subscriptions will be displayed to show the user all existing items. These lists can be sorted by each column heading and there is also a search option available to find a particular product or subscription through a keyword search of the name or description.
 

### Features Left to Implement
- The community area could be further developed with more options available to allow the user to add fitness challenges / exercise plans, which would include multiple steps or exercises to be entered for each day of the challenge / plan. 
- An example of this would be a 30-day fitness challenge that focuses on a particular fitness area, with instructions to complete a range of different exercises on each day of the challenge.
- Another section that could be added would be an index to look up details for any exercise with pictures or videos on how to complete the exercise.
- The user profile section could also be updated to include options to add and store multiple delivery addresses for the account. This could then be integrated into the Checkout page where the user could select the delivery address from their list of saved addresses.

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




## Testing

-- See Testing.md (link)

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- [Business Name Generator](https://businessnamegenerator.com/)

####CSS
- I initially thought of creating a home page with two images which were split at the top of the screen. I worked with this a little to test it before returning to try the Bootstrap carousel, where I have now implemented three rotating images relating to the three sections of the site.
- [CSS Tricks - Multiple image background-image](https://css-tricks.com/almanac/properties/b/background-image/)
- [Responsive Full Background Image Using CSS - William Craig](https://www.webfx.com/blog/web-design/responsive-background-image/)
- [CSS background-image Property - W3Schools.com](https://www.w3schools.com/cssref/pr_background-image.asp)
- [Bootstrap carousel resizing image - Stackoverflow](https://stackoverflow.com/questions/17357306/bootstrap-carousel-resizing-image)

####Django
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