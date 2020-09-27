## Testing

I carried out extensive testing on all elements of the site at each stage of development in order to ensure that the functionality being built was working in the expected way, and that no errors were being reported while completing the process. If any issues were found while testing, they could be reviewed and corrected. The testing would then be completed again to ensure it was now working correctly.

Other testing was also performed in order to check the layout on different browsers and different screen sizes. I tested the site on Google Chrome, Mozilla Firefox, Avast Secure Browser and Microsoft Edge. I also completed a full site test on an Android phone (Galaxy S10), as well as testing all screen sizes through the responsive settings in the browser.

The scenarios used for testing each of the sites components are detailed below:

1. Site Registration and User Profile:
	1. Registration Form:
		1. Select Register from the My Account menu on the nav bar
		2. Enter required details in the registration form with email address, username and password then click Sign Up
		3. Tested with an invalid username format - error was displayed to inform me of the format it should be in.
		4. Corrected the username and tested again, but the passwords were not matching. Another error was displayed to say that passwords should match.
		5. Tested with an invalid email address, the error was displayed below the email address input box to inform me to enter a valid email address.
		6. With all the inputs correctly completed, I clicked Sign up again.
		7. Page is displayed confirming registration and asking the user to verify their email address using the link provided in the confirmation email.
		8. Checked that the confirmation email was sent, clicked the link in the email and the Confirm email address page is displayed.
		9. Checked that the email address displayed was correct, then clicked the Confirm button. The sign in page is then displayed.
	2. Sign In Form:
		1. Checked that error messages were displayed in all of the following scenarios:
			- [x] Invalid username - Error displayed
			- [x] No username - Error displayed and input box border shown in red
			- [x] Valid username and invalid password - Error displayed
			- [x] Valid username and no password - Error displayed and password input border shown in red
			- [x] No username or password entered - Error displayed and both input boxes borders are shown in red
		2. Clicked the forgot password link and opened the password reset page.
		3. Entered an invalid password and clicked the Reset my password button. Error was displayed to inform that the email address was not assigned to any user account.
		4. Entered a valid email address of a registered user, clicked Reset my password button again. Got confirmation page to inform that an email had been sent with a link to reset the password.
		5. Opened link in the reset password email and entered the details to test the field validation:
			- [x] Tried with a password that was too short in length - Error was displayed informing of the problem and details of minimum length of 8 characters
			- [x] Tried with a longer password, but repeated password was not the same value - Error displayed to inform that passwords must match
			- [x] Entered matching password with correct length requirements and clicked the reset password button - Confirmation page was displayed to inform that the password had been changed, and success message was also displayed.
		6. Clicked the sign up link to test that it loaded the registration page correctly
		7. Entered the correct username and password, then clicked sign in button, got success message displayed informing that the user was logged in.
		8. Checked the Profile option under My Account to verify that the correct user details were displayed
		9. Tested the Log out option under My Account, clicked sign out and got message to show that the user was signed out.
		10. Confirmed the user was signed out by selecting the My Account menu and checking the the option to Log in was now available.		
	3. User Profile:
		1. Testing on the user profile was completed after a purchase had been made where a delivery address had been selected to save to the profile.
		- [x] Check that the delivery address entered during checkout is saved to the user profile
		- [x] Update the First Name Last Name and email address fields and test that these are correct on returning to the page
		- [x] Update the delivery details address to ensure it can be updated without error
		- [x] View Order History list for all purchases made by the user
		- [x] Click the order number link to view the full order details as well as delivery address and billing details

2. Navigation, Sorting and Searching:
	1. Tested the products catalog using the following filters and searches:
		- [x] Display full catalog for all products
		- [ ] Selected the Products sorting by Price - but got an error, this was because the price field had been removed from the Products model onto the Product Subscriptions model as prices are now linked to individual subscriptions. An update is required to the view to change the filter / sort query for the price field. Testing will redone when the updates have been completed.
		- [ ] Selected the Products sorting by Rating - also got an error for this as the average rating is now calculated through a function called "get_avg_rating" in the Product model, which calculates the average rating from the Reviews model user_rating field for ratings on each individual product. An update is also required for this filter / sort query in order to user the calculated average rating for sorting the products list. Re-testing will be required on this element again, once completed.
		- [x] Selected sort by Category for all products - the Products Catalog was displayed successfully, and the categories tag displayed in each product card was sorted alphabetically (A-Z).
		- [x] Used the Sort option to change the sort direction from (Z-A) - Product list was correctly displayed with categories in reverse alphabetical order.
		- [x] Used the sort option to sort products by Name, both ascending and descending - both worked correctly sorting by the product name.
		- [x] Tested that the number of products found was correctly displayed
		- [x] Used the search bar to enter search text "nothing" that was not contained in the product titles or descriptions - correctly displayed message with: 0 products found for "nothing"
		- [x] Used the search bar to search for the text "children" which is contained in the product title - correctly displays the 2 products containing the search text.
		- [x] Used the search bar to search for the text "circuit" which is contained in the product descriptions - correctly displayed 3 products containing this search text.
	2. Tested the Fitness Plans menu options from the nav bar:
		- [x] All Fitness Plans - displayed all of the products under the Fitness category, also displayed the badges with links for each of the Subcategories that were found
		- [x] Clicked on each of the subcategory badges to filter the products for each of these - correctly displayed all products for any subcategory selected
		- [x] Filtered by Subcategory "Beginners" from the Fitness Plans menu - Displayed 8 products under the subcategory Beginners
		- [x] Filtered by Subcategory "Online Classes" from the Fitness Plans menu - Displayed 6 products under this subcategory for Online Classes
	3. Tested the Nutrition Plans menu options from the nav bar:
		- [x] All Nutrition Plans - displayed all of the products under the Nutrition category, badges were also displayed for each of the subcategories that were found
		- [x] Clicked on each of the subcategory badges to filter the products for each of these - correctly displayed all products for any subcategory selected
		- [x] Filtered by Subcategory "General Nutrition Plans" from the Nutrition Plans menu - Displayed 3 products under this subcategory
		- [x] Filtered by Subcategory "Personalised Plans" from the Nutrition Plans menu - Displayed 1 product under the Personalised Plans subcategory
	4. Tested the Accessories menu options from the nav bar:
		- [x] All Accessories - shows all the products available under the Accessories category
		- [x] Clicked on each of the subcategory badges to filter the products for each of these - correctly displayed all products for any subcategory selected
		- [x] Filtered by Subcategory "Clothing" from the Accessories menu - Displayed 3 products under the Clothing subcategory
		- [x] Filtered by Subcategory "Weights" from the Accessories menu - Displayed 7 product under this subcategory
	5. Tested the Community menu options from the nav bar:
		- [x] All Community - shows all the discussion topics that have been entered in the Community Area
		- [ ] Filtered by "Fitness Plan Discussions" from the Community menu - 
		- [ ] Filtered by "Nutrition Plan Discussions" from the Community menu - 
		
3. Products selection, Purchase and Checkout:
	1. Products were selected from the product catalog to open the product detail page, the following settings were tested:
		- [x] The product picture and name are displayed
		- [x] The subscription or size list box is displayed - tested this for both types of products (with Subscriptions or with Sizes) and the correct list box is displayed for both types.
		- [x] Check that the Subscription/Size, Price, Available Stock, and Colour placeholders are visible.
		- [x] That the quantity input box and +/- buttons are available and that they work to increase / decrease the quantity
		- [x] That the subcategory and rating are displayed
		- [x] Check that the product description and reviews tabs can be viewed, and that the correct reviews are displayed for each product
		- [x] Click the Keep Shopping button to return to the Products Catalog
	2. When the Add to Basket button is clicked it will trigger a JavaScript function which checks that a subscription or size (if applicable) has been selected before allowing the product to be added to the basket
		- [x] Click the Add to Basket button - correctly displayed an error below the subscription select box to indicate that a subscription needs to be selected before adding a product to the basket
		- [x] Select a subscription and test the Add to Basket button again - Product and quantity selected is the successfully added to the basket
		- [ ] Add to basket on mobile layout causes the basket icon in the nav bar to disappear - Error to be reviewed and fixed before re-testing.
	3. Selecting the subscription or size for a product has gone through a number of iterations and improvements were made as to how this would work best for the user experience and convenience. The different methods that I tried before getting to the final solution are detail below:
		1. A "Change Subscription" button was originally implemented to allow the user to select an available subscription and then click the button to display the subscription details for Price, Available stock, and colour. When this button was clicked it gave errors because it was missing the name attribute on the hidden field - which was there to hold the selected subscription value. JavaScript was used on the change event of the select box to write the selected subscription value for the form submission.
		2. Tried to implement a second view to "refresh_subscription" after the Change subscription button was clicked. This caused conflicts, although sometimes appeared to work, but then stopped working.
		3. I then realised that I could pass the values from the form using hidden fields through to the original product_detail view, using these I filtered the product subscription with the selected subscription value and passed this to the context. Then the page was reloaded and displayed the subscription.
		4. When adding to the basket this option didn't work as I had intended, but a 2nd hidden field was added to store the subscription ID for the actual purchase and this was used to add the subscription to the basket.
		5. Finally the Change Subscription button was replaced by using a function called "updateSubscription" on the onchange event of the subscription list to put the subscription ID value in a hidden field and call the form submit event which will reload the form with the selected subscription details from the view, as described above.
	4. Check that only the available subscriptions or sizes for that product are displayed in the list
		- [x] Tested with different fitness and nutrition products to see that the subscription list updated
		- [x] Tested with a clothing item which had sizes to ensure the correct sizes were displayed in the list
		- [x] Tested with a product that does not have a subscription or a size, like the "Exercise Mat" - the subscription / size list is not displayed for this product, and all the details relating to price, available stock and colour are automatically displayed.
	5. Selecting a subscription / size should trigger the JavaScript to update the subscription details placeholders by submitting the form and reloading the view with the selected subscription details. 
		- [x] Check that the subscription type is displayed together with the Price, Available Stock and Colour for that subscription and are correctly displayed
		- [x] Change the subscription and check that the name, price and other items have been updated
		- [x] Check the selected size displays the correct price, stock and colour
		- [x] Change the size and check that these fields have been updated
	6. Updating the quantity using the + and - buttons on the form should trigger a JavaScript function which checks the value is within the range of 1-99 and disables these buttons if it is outside of this range. The function also checks against the available stock for the product / subscription and also disables these buttons if the quantity reaches the stock limit.
		- [x] After selecting a product subscription / size, check the available stock for this product, and then try and increase the purchase quantity above this number. The plus button is then disabled to prevent a higher quantity being purchased than is available
	7. When products are added to the basket they can be viewed by clicking on the basket icon in the main nav bar. The basket functionality was tested as follows:
		- [x] Check that all of the selected products have been displayed in the basket
		- [x] Check that the quantity, subscription / size and colour have been displayed correctly
		- [x] Change the quantity and click on update to ensure that the basket updates, and the total cost is adjusted
		- [x] Check that other items are not affected by this update
		- [x] Test removing an item from the basket, and that the total price is correctly adjusted
		- [x] Test that the delivery costs are correctly calculated and only for items which have delivery charge selected in the subscription table. 
		- [x] Check subscriptions that have no delivery charges (such as Online Content or Live Online Classes) should not be included in the total for delivery costs
		- [x] Select the Keep Shopping button to return the main Products page
		- [x] Use the Checkout button to proceed to the checkout and payments page
	8. On the checkout page, testing was carried out to check that all required fields should be completed and that a valid payments method was provided before the form could be submitted. The following items were checked during these extensive tests
		- [x] Check the order summary to ensure that the correct products, subscription / size and quantity are displayed
		- [x] Click the confirm payment option without having the all of the required fields completed - Required field are display with a red border when they have not been completed.
		- [x] Untick the option to save delivery details to the profile - then check the user profile after the purchase has been completed to see that there is no delivery information saved
		- [x] Complete another purchase and tick the save delivery details box this time. When the user profile is checked these details have now been updated to the default delivery details fields
		- [x] The default delivery details are displayed on the checkout screen for subsequent purchases, but can also be updated and saved to the profile each time
		- [x] Enter an invalid payment card number  - The error is displayed immediately to inform the user of an invalid card number 
		- [x] Complete the order and check that the Stripe payment is processed correctly by checking the webhook attempts for the Endpoint being used (for example the Heroku deployment site was configured as an endpoint to receive payment intentions from). 
		- [x] Webhook details for a successful payment in Stripe: "Webhook received: payment_intent.succeeded | SUCCESS: Verified order already in database"
		- [x] When the payment has been processed and a successful status has been received back from Stripe then the Order Confirmation page will be displayed with the Order details, delivery address and billing details. A message is also displayed to confirm that an email has been sent to the registered email address for the user.
		- [x] Check that the order confirmation email has been received which shows the correct order details and delivery information
    9. Adding a product review - an authenticated user has the option to add a review under the Product Details page. The following tests were performed to test that the reviews could be added and viewed on the product details page	
		- [x] Select the reviews tab on a product while logged out, the Add Review button is not available
		- [x] Login and select a product, click on Review tab again and check that the Add Review button is now available
		- [x] Leave the review title and comment fields blank and try to submit the form - Error displayed and required field borders are shown in red
		- [x] Try to enter a decimal number for the rating - Error displayed asking to round the number to the nearest value
		- [x] Enter the title, comment and rating value, then click Add Review - Form submitted and redirected back to the Product Details page, success message is also displayed
		- [x] Check that the review is displayed under this product details and that all fields from the review and user are correctly displayed
		- [x] Check that the star rating value is displayed correctly with the star icons in the review
		- [x] Check that the product rating has been updated with the average rating and is correctly displayed with the star icons

4. Community and Discussions:
	1. When the Community area is loaded a list of existing topics will be displayed, the following tests were performed to check the functionality of this list as follows:
		- [x] Check that the list can be sorted by each of its column headings in both ascending and descending order
		- [x] Test the page links to move forward and backwards between the different pages, and change the value in the show number of entries box to increase and decrease the number of records returned per page.
		- [x] Use the keyword search to ensure the table results are filtered by the value in the search input box
		- [x] Select the topic title link to open the topic to view / edit / add comments
		- [x] Select the New Topic button to access the Add Topic form
	2. When adding or editing a topic, the product will be selected from the list of products. The user must enter details in both the title and description fields before being able to save the topic.
		- [x] Try to save a topic without the required fileds being completed - The field border is displayed in red when the required field has not been completed
		- [x] Enter details in all the fields and click Add Topic - the topic is saved and then displayed in the list of topics on the main Community page
		- [x] Select the topic that was just added and ensure the edit link is available
		- [x] Select a topic created by another user to check that it cannot be edited by the current user - the Edit link is not available in this case
		- [x] When editing a topic, update the title and the description - the topic is saved and the updated details are shown in the list of topics.
		- [x] Select a topic from the list and ensure that the correct details are shown when viewing the topic
	3. Comments can be added to the topic by any user, including the author. The following tests were carried out on the topic comments:
		- [x] View the topic and click on the Add comment button - the Add Comment form is loaded and the topic / discussion title is displayed
		- [x] The comment field is required before allowing the comment to be added - this shows an error and a message to inform the user it is a required field
		- [x] Enter the comment for the topic and click the Add Comment button - when the comment has been saved, it returns to the view topic page and the newly added comment is displayed in the list with the other comments.
		- [x] Check that the Edit link for the newly added comment is available for the user
		- [x] Click the link to edit the comment, update it and save it. - The updated comment is visible in the list of comments for that topic
		- [x] Check that there is no edit link available for other users comments

5. Product Management / Administration:
	1. On loading the main product management page a list of options are available for both products and subscriptions. These options include Add new product / subscription, and View the list of existing products or subscriptions. All of these buttons were tested to ensure that the correct page for each was loaded.
	2. Add new product - the following testing was performed on the Add Product form:
		- [x] Submit the form without completing any required fields - the fields with errors are displayed with red borders
		- [x] Complete all required fields, excluding the product subscription selection and try to submit the form - Get an error to indicate that this is required
		- [x] Select a subscription and submit the form - the product is saved and the product details is displayed showing the new product
		- [x] Check subscription list to ensure the subscriptions that were selected are available to choose in the list
	3. On viewing the products list all of the existing products will be displayed, the functionality of this list was tested as follows:
		- [x] Check that the list can be sorted by each of its column headings in both ascending and descending order
		- [x] Test the page links to move forward and backwards between the different pages, and change the value in the show number of entries box to increase and decrease the number of records returned per page.
		- [x] Use the keyword search to ensure the table results are filtered by the value in the search input box
		- [x] Select the product name link to view / edit the product
		- [x] Select the Product Mgt. button to return to the main product management page
	4. The Edit product form can be accessed from the list of products in the product management section, and also from the product details page. Both options require an authenticated superuser account to access these sections. The tests carried out for editing a product are detailed below:
		- [x] Select the product to edit and check that all the fields have been correctly populated
		- [x] Check that the subscription(s) that were previously selected are correctly displayed
		- [x] Edit and update some of the fields and then save the product - check the details again under view product to see that the updates have been displayed
	5. Delete Product - the product deletion options have the same availability as the edit options and can be accessed either through the product management list view of products, or on the product details page. When the correct product is selected click on the delete link and the product will immediately be deleted. A message is displayed to inform the user if the deletion was successful.
	6. When viewing the products subscriptions list, the subscriptions available for all of the products will be displayed, testing was performed on the following areas:
		- [x] Check that the list can be sorted by each of its column headings in both ascending and descending order
		- [x] Test the page links to move forward and backwards between the different pages, and change the value in the show number of entries box to increase and decrease the number of records returned per page.
		- [x] Use the keyword search to ensure the table results are filtered by the value in the search input box
		- [x] Select the subscription name link to view / edit the product subscription
		- [x] Select the Product Mgt. button to return to the main product management page
	7. Add new subscriptions - the list below details the tests that were performed for adding new subscriptions to the list of product subscriptions:
		- [x] Subscription name is the only required field on this form - cannot submit the form without this value, on error the border is displayed in red
		- [x] When the name has been entered and all the other field are completed as necessary, then submit the form and the subscription list is returned which now includes the newly added subscription.
		- [x] The new subscription is now availability in the list of product subscriptions on the Add or Edit Product forms.
	8. Edit subscription - this option can be accessed from the Product Management section, and can also be accessed when on the Add or Edit Product form by using the add or edit links. The following steps were completed in order to test the subscriptions edit option:
		- [x] Select a product from the list and ensure that the correct details are shown in each of the fields
		- [x] Update some of the fields and click the Update Product Subscription button - the form is submitted and the updated subscription can be viewed in the subscriptions list view.
		- [x] The updated subscription is available in the product subscriptions list on the Add or Edit Product forms
	9. Delete Subscription - this option can only be accessed through the product subscriptions list view. When the correct product subscription has been found, then click on the delete icon for that subscription row. The product subscription will be deleted immediately and a message is displayed confirming to the user of its successful deletion.