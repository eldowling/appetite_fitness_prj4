<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome eldowling,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- [Business Name Generator](https://businessnamegenerator.com/)

**CSS**
- I initially thought of creating a home page with two images which were split at the top of the screen. I worked with this a little to test it before returning to try the Bootstrap carousel, where I have now implemented three rotating images relating to the three sections of the site.
- [CSS Tricks - Multiple image background-image](https://css-tricks.com/almanac/properties/b/background-image/)
- [Responsive Full Background Image Using CSS - William Craig](https://www.webfx.com/blog/web-design/responsive-background-image/)
- [CSS background-image Property - W3Schools.com](https://www.w3schools.com/cssref/pr_background-image.asp)
- [Bootstrap carousel resizing image - Stackoverflow](https://stackoverflow.com/questions/17357306/bootstrap-carousel-resizing-image)

**Django**
- When it came to implementing my Product Details page, I needed to find out how to create the Model for the table structure where a Product has multiple Subscription Types and each Subscription Type had a Price and a Quantity Available. I also needed to understand the method used to extract the related data and display it on the Product Details page. For this I looked up some pages related to getting data from multiple tables. This in turn lead me to investigating the Django Select_Related and Prefetch_Related functions further to try and implement these with my project. I found that this was not the right solution and instead tried to find tutorials relating to Many to Many field relationships. I then found a few parts in the set of tutorials by Dennis Ivy to be very useful in what I was trying to implement, and I took these as the basis to write my own views and updated the models accordingly. The following links were used in order to research and implement the Many to Many related tables needed to build the Product Details page.
- [Fetching data from multiple tables in Django - Stack Overflow](https://stackoverflow.com/questions/48596388/fetching-data-from-multiple-tables-in-django)
- [Django Documentation - QuerySet API Reference](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)
- [Django select_related and prefetch_related - by Goutom Roy | Better Programming(https://medium.com/better-programming/django-select-related-and-prefetch-related-f23043fd635d)
- [Daily Django - #09 - select_related() e prefetch_related()](https://www.youtube.com/watch?v=JU7scCwEAI0)
- [Querying One-To-Many Relationships in Django - PrettyPrinted](https://www.youtube.com/results?search_query=django+select_related+and+prefetch_related)
- [How to Get Data Out of a Django Model and in to the HTML Template (Django Tutorial) | Part 48 - Max Goodridge](https://www.youtube.com/watch?v=VxOsCKMStuw&t=322s)
- [Django - Filter the prefetch_related queryset - Stack Overflow](https://stackoverflow.com/questions/52757040/django-filter-the-prefetch-related-queryset)
- [Django select_related Examples |Django select_related and prefetch_related |Django n+1 Query Problem - Code Band](https://www.youtube.com/watch?v=mO-pfdJpnBA)
- [How to Use a Many to Many Field in a Django Model (Django Tutorial) | Part 55- Max Goodridge](https://www.youtube.com/watch?v=nwpLCa79DUw&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=54)
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

