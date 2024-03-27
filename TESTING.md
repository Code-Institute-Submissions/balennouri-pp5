# Testing

## Contents

* [Manual Testing](#manual-testing-for-fastshoes-website)
    * [Test Case: Website Functions](#test-case-for-website-functions)
    * [Test Case: Users Functions](#test-case-for-users-functions)
    * [Test Case: Admin Functions](#test-case-for-admin-functions)
* [Other Tests](#other-tests)
    * [Lighthouse Test](#lighthouse-test)
    * [Wave Test](#wave)
    * [Browsers and Devices](#browsers-and-devices)
* [Validator Test](#validator-testing)
    * [CSS](#css)
    * [HTML](#html)
    * [Python Linter](#python-linter)
    * [JShint](#jshint-for-javascript)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Fixed Bugs](#fixed-bugs)

## Manual Testing for FastShoes Website

### Test Case For Website Functions :

| Test Case | Description                             | Status |
|-----------|-----------------------------------------|--------|
| TC-1-WF   | Verify homepage loads correctly         | Pass   |
| TC-2-WF   | Verify navigation bar functionality     | Pass   |
| TC-3-WF   | Verify product list view                | Pass   |
| TC-4-WF   | Verify product details view             | Pass   |
| TC-5-WF   | Verify adding product to cart           | Pass   |
| TC-6-WF   | Verify viewing shopping cart            | Pass   |
| TC-7-WF   | Verify updating product quantity in cart| Pass   |
| TC-8-WF   | Verify removing product from cart       | Pass   |
| TC-9-WF   | Verify checkout process                 | Pass   |
| TC-10-WF  | Verify search functionality             | Pass   |
| TC-11-WF  | Verify payment processing               | Pass   |
| TC-12-WF  | Verify responsive design on mobile      | Pass   |
| TC-13-WF  | Verify responsive design on tablet      | Pass   |
| TC-14-WF  | Verify filtering products by category   | Pass   |
| TC-15-WF  | Verify all users can use contact form   | Pass   |

### Test Case For Users Functions :

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC-1-UF   | Verify that a new user can successfully create an account with valid credentials. | Pass |
| TC-2-UF   | Verify that the system displays appropriate error messages when invalid credentials are used for account creation. | Pass |
| TC-3-UF   | Verify that the system prevents the creation of duplicate accounts with the same email address. | Pass |
| TC-4-UF   | Verify that a logged-in user can update their profile information successfully. | Pass |
| TC-5-UF   | Verify that the system displays appropriate error messages when invalid data is provided for profile updates. | Pass |
| TC-6-UF   | Verify that a user can successfully delete their account and associated data. | Pass |
| TC-7-UF   | Verify that the system prompts for confirmation before deleting the account. | Pass |
| TC-8-UF   | Verify that a logged-in user can add products to their wishlist. | Pass |
| TC-9-UF   | Verify that a logged-in user can delete products from their wishlist. | Pass |
| TC-10-UF  | Verify that the system handles errors gracefully when adding or deleting products from the wishlist. | Pass |
| TC-11-UF  | Verify that a logged-in user can submit a review for a product. | Pass |
| TC-12-UF  | Verify that a logged-in user can update their existing review for a product. | Pass |
| TC-13-UF  | Verify that a logged-in user can delete their review for a product. | Pass |

### Test Case For Admin Functions :

#### Adding a Product (FRONT-END)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-01 | Verify that the admin can access the "Add Product" page. | Pass   |
| TC-ADM-02 | Verify that all required fields are displayed on the form. | Pass   |
| TC-ADM-03 | Verify that the admin can successfully add a new product. | Pass   |
| TC-ADM-04 | Verify that appropriate error messages are displayed if the form is not filled correctly. | Pass |

#### Updating a Product (FRONT-END)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-05 | Verify that the admin can access the "Update Product" page. | Pass   |
| TC-ADM-06 | Verify that the existing product details are pre-filled in the form. | Pass   |
| TC-ADM-07 | Verify that the admin can successfully update a product. | Pass   |
| TC-ADM-08 | Verify that appropriate error messages are displayed if the form is not filled correctly. | Pass |

#### Deleting a Product (FRONT-END)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-09 | Verify that the admin can delete a product.             | Pass   |
| TC-ADM-10 | Verify that the product is successfully deleted when the delete button is clicked. | Pass |


#### Managing Orders (ADMIN-PANEL)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-12 | Verify that the admin can access the orders section.   | Pass   |
| TC-ADM-13 | Verify that the admin can view all orders.             | Pass   |
| TC-ADM-15 | Verify that the admin can delete an order.             | Pass   |

#### Managing Users (ADMIN-PANEL)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-16 | Verify that the admin can access the users section.    | Pass   |
| TC-ADM-17 | Verify that the admin can view all users.              | Pass   |
| TC-ADM-18 | Verify that the admin can edit user details.           | Pass   |
| TC-ADM-19 | Verify that the admin can delete a user.               | Pass   |

#### Managing Contact Mails (ADMIN-PANEL)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-20 | Verify that the admin can access the contact mails section. | Pass |
| TC-ADM-21 | Verify that the admin can view all contact mails.      | Pass   |
| TC-ADM-23 | Verify that the admin can delete contact mails.        | Pass   |

#### Managing Reviews (ADMIN-PANEL)

| Test Case | Description                                             | Status |
|-----------|---------------------------------------------------------|--------|
| TC-ADM-24 | Verify that the admin can access the reviews section.  | Pass   |
| TC-ADM-25 | Verify that the admin can view all reviews.            | Pass   |
| TC-ADM-26 | Verify that the admin can delete a review.             | Pass   |

## Other Tests

### Lighthouse Test

### WAVE

### Browsers And Devices

Tested on the following browsers:

* Google Chrome
* Safari
* Firefox

Tested on the following devices:

* Ipad Air
* Iphone 12, 13 and 14
* Samsung Galaxy

## Validator Testing

### CSS

### HTML

### Python Linter

### JSHint for Javascript

## Bugs

### Known Bugs

### Fixed Bugs