# FastShoes

Welcome to FastShoes, your premier online destination for high-quality football footwear designed for athletes. Our modern e-commerce platform features a curated selection of top-notch football shoes, meticulously chosen to enhance your performance on the field.

In addition to our diverse range of shoes available for purchase, we offer convenient features such as the ability to create an account on our website. By creating an account, you can easily add products to your wishlist and write reviews for items you love.

This business idea has always been close to my heart. As a former professional football player, I understand the importance of quality footwear in enhancing performance on the field. FastShoes is my passion project, allowing me to combine my love for football with my desire to learn more about Django and Python.

The live site can be viewed [here](https://fastshoes-be1fd2fa0203.herokuapp.com/)

![Am I responsive screenshot](docs/readme/ami.responsive.png)

## Contents

* [Project Goals](#project-goals)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Epics](#epics)
    * [Skeleton](#skeleton)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
    * [Design Choices](#design-choices)
        * [Typography](#typography)
        * [Colour Palette](#colour-palette)
* [Project Management](#project-management)
* [Features](#features)
    * [Existing Features](#existing-features)
        * [All The Pages](#all-the-pages)
        * [The Navigation Bar](#the-navigation-bar)
        * [The Main Content](#the-main-content)
        * [The Footer](#the-footer)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
   * [Languages](#languages)
   * [Frameworks](#frameworks)
   * [Database](#database)
   * [Tools](#tools)
   * [Supporting Libraries and Packages](#supporting-libraries-and-packages)
* [Marketing](#marketing)
* [Testing](#testing)
   * [Manual Testing](#manual-testing-for-fastshoes-website)
   * [Summary Table of Manual Testings](#summary-table-of-manual-testings-for-fastshoes-website)
   * [Other Tests](#other-tests)
   * [Validator Testing](#validator-testing)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Fixed Bugs](#fixed-bugs)
* [Deployment and Development](#deployment-and-development)
    * [Deploying the Site](#deployment)
    * [Forking the Repository](#forking-the-repository)
    * [Cloning the Repository](#cloning-the-repository)
    * [The ElephantSQL Database](#the-elephantsql-database)
    * [The Cloudinary API](#the-cloudinary-api)
* [Credits](#credits)
* [Acknoledgements](#acknowledgements)

## Project Goals

- I aimed to develop a website equipped with an admin panel for effortless product management and user account handling, seamlessly integrated with a database.

- The objective was to empower admin/staff members to efficiently add, remove, and update products directly from the website while logged in.

- Additionally, I sought to provide admin/staff with the capability to set products on sale to facilitate the clearance of older inventory.

- Users were to be afforded the opportunity to create accounts and manage their account details at their convenience.

- Enhancing user experience, I aimed to implement robust categorization, search, and filtering functionalities to assist users in locating their desired brands with ease.

- To enrich user engagement, I aimed to enable users to curate their own wishlist by adding or removing products, provided they are logged in.

- Furthermore, I aimed to foster user interaction by enabling them to leave reviews for products, enhancing the community aspect of the platform.

- Lastly, I endeavored to provide users with a means to reach out to the FastShoes team through the contact page for any inquiries or assistance needed.

[Back to top](#contents)

## User Experience

### User Stories

The aim of the project was to develop a user-centric website, prioritizing key user stories:

* Store Owner Objectives:
   
   * Craft an engaging design to captivate users
   * Establish a user-friendly front end for intuitive navigation
   * Enable user account management and product management
   * Enable order management

* User Objectives:

   * Enable users to create accounts and retain control over their personal information
   * Deliver a responsive and intuitive design that operates seamlessly across all devices
   * Provide functionality for adding, editing, removing, and updating products in the shopping cart
   * Implement features allowing users to add and remove products from their wishlist, contingent upon user authentication
   * Implement functionality that allows logged-in users to write reviews for products

The objective of e-commerce is to prompt users to explore a variety of products and make purchases. The design is sleek and enables users to categorize and sort products according to their preferences.

Every interaction on the site is meticulously crafted to elicit a positive emotional response from the user. This is achieved through thoughtfully designed information flow, color usage, clear navigation structures, and responsive user action feedback. The absence of intrusive automatic pop-ups ensures a seamless user experience. Users maintain full control over their actions, aided by progress indicators and feedback provided during financial transactions.

### Scope 

Once the structure was established, the focus shifted to the scope phase. This involved defining website requirements aligned with the goals outlined in the strategy phase. These requirements were categorized into two main groups: content and functionality.

Content:

* Privacy Policy has been instituted
* An assortment of purchasable products
* Rating and price of the products
* Information text about each product
* Links to FastShoes social media accounts

Functionality:

* Browse products on the website
* Register and delete accounts as needed
* Easily manage shopping cart items by adding, updating, or removing products
* Save desired products to a personal wishlist for future reference
* Share feedback by leaving reviews for products
* Securely complete orders using Stripe, a trusted payment solution
* Reach out to the store via the contact page for inquiries or assistance
* Stay up-to-date with the latest news, releases, and promotions by subscribing to FastShoes!

### Structure

Navigation:

* Ensure responsive navigation is consistent across all pages for seamless browsing.
* Integrate cart functionality to display the total amount and quantity of products added.
* Implement a search feature enabling customers to easily find products by name, category, or keywords.

Registration and User Profiles:

* Enable user registration and login capabilities for customers to establish and oversee their accounts.
* Implement user authentication and access control mechanisms to guarantee secure and tailored interactions.
* Provide users with the ability to modify their information through the user profile page.
* Allow users to access and monitor their order history via the user profile page.

Products and Sorting:

* Showcase an extensive list of available products.
* Enable users to filter products by category for easier navigation.
* Present comprehensive product details, such as price, images, and ratings.
* Enable users to select their preferred shoe size for the products they desire.

Shopping Cart, Checkout, and Payment Process:

* Users can conveniently add products to their cart and adjust quantities or remove items as needed.
* Ensure a secure checkout process, collecting address and payment details for smooth transactions.
* Integrate a reliable payment gateway, such as Stripe, to facilitate secure online payments.

Admin Panel:

* Develop an intuitive admin panel granting site administrators control over products, categories, wishlists, reviews, contact forms, orders, and user accounts.

Responsive Design:

* Craft a responsive website interface optimized for seamless user experiences across various devices and screen sizes.
* Prioritize intuitive navigation and legible content presentation across desktops, tablets, and mobile devices

Contact Us:

* Integrate a user-friendly contact form or feature to facilitate communication between users and the business.

SEO, Marketing, and Legal:

* Implement a Privacy Policy to ensure compliance with legal regulations.
* Configure robots.txt and sitemap.xml files to facilitate search engine indexing.
* Enhance search engine visibility by optimizing meta descriptions and keywords.
* Establish a Facebook page to promote the business and engage with customers.

### Epics 

In the project planning phase, I started with six main epics and then broke them down into individual user stories. These user stories were labeled and prioritized using the MoSCoW technique (Must have, Should have, Could have, Won't have) to guide their development. This approach helped me concentrate on implementing the most essential features first, ensuring a focused development process. You can view all the user stories on the project board, the link to which is provided below. Additionally, the project board offers a glimpse into upcoming features and developments.

[Project Board For FastShoes](https://github.com/users/balennouri/projects/7)

Below, you'll find the completed user stories for this version of the project, organized by epics:

#### Epic: Initial Django Setup

- As a developer I want to set up Django and install the initial supporting libraries needed so that I can begin development of the site.
- As a developer I want to set up the environment to secure secret configuration variables so that I can ensure sensitive data is kept private.
- As a developer I want to deploy the site to Heroku so that I can ensure the site works in a production environment and share the completed site publicly.

#### Epic: The Website Features

- As a user, I will have it easy to navigate on the page.

- As a user, I will be able to categorize the brand of the products

- As a user, I can filter and search on the website.

- As a user, I can make a wishlist on the website.

- As a user, I want the site to be accessible and user-friendly on mobile devices.

- As a user, I want a seamless experience across different screen sizes.

- As a user, I can write reviews for products.

- As a user, I can contact the store through the contact page

#### Epic: User Authentication and Account Management

- As a first time user, I can create an account

- As a user I can delete my account.

- As a returning user I can login/logout of my account.

- As returning user I can update my profile information.

- As site user I can forget my password and get my account back if so.

- As a user i can add/remove product to the wishlist

- As site owner I can see all the detail information for the users in the admin panel.

#### Epic: Order Management

- As a customer, I want to view my order history.

- As an admin, I want to process and manage customer orders.

#### Epic: Security and Privacy

- As a user, I want my personal and payment information to be secure.

#### Epic: Store Management, Cart and Checkout

- As a admin I can add/delete/update products on the admin panel and on the website.

- As a admin I can add new categories on the admin panel.

- As a user I can rate the product from 0 to 5 in the reviews

- As a user I can add products to the cart.

- As user I can pay directly on the website with my credit card.

- As a user I can update the quantity of the product in the cart and delete the product from the cart.

- As user I can place an order and checkout.

- When a user place a order the cart becomes empty.

[Back to top](#contents)

### Skeleton

#### Wireframes

I utilized Balsamiq to design my wireframes, creating versions tailored for both larger screens and mobile devices. Wireframing was a crucial step for me to visualize and organize my ideas before diving into the project development. While some pages may deviate slightly from the wireframes, these differences are minor and were made to ensure optimal functionality and user experience during the development process.

##### Home page in wireframe

![wireframe home page]()

##### Your Profile page in wireframe

![wireframe update profile page]()

##### Sign Up page in wireframe

![wireframe sign up page]()

##### Login page in wireframe

![wireframe Login page]()

##### Product Management page in wireframe

![wireframe product management page]()

##### Add Product page in wireframe

![wireframe add product page]()

##### Update Product page in wireframe

![wireframe update product page]()

##### Shopping cart page in wireframe

![wireframe shopping cart page]()

[Back to top](#contents)

#### Database Schema

Below, you'll find the models used in this project. In the database schema displayed below, models with the same color belong to the same app.
The database schema shown here was generated using [FigJam.](https://www.figma.com/)

Colours for each apps:

Green: products App
Yellow: checkout App
Red: profiles App 

The Database schema:

![Database schema](docs/readme/datebase.png)

[Back to top](#contents)

### Design Choices

#### Typography

For the website fonts, I opted to use Kode Mono for the header in the navigation section. For the remaining content, I utilized the Lato font. Additionally, I included a secondary font fallback as Sans-serif to ensure compatibility in case the user's browser does not support the primary fonts. 

#### Colour Palette

![colour pallete](docs/readme/colours.png)

For this website, I opted for darker colors with white used for the content sections. The darker colors complement the colorful nature of football shoes, as most of them feature vibrant colors. This choice ensures that the products stand out effectively when users view them on the website.

The color palette image was generated from [coolers.](https://coolors.co/)

[Back to top](#contents)

### Project Management

I employed agile methodology throughout the project development, utilizing GitHub projects and issues for streamlined management. More detailed information about this approach can be found in the AGILE.md file.

[AGILE.md](https://github.com/balennouri/pp5/blob/main/AGILE.md)

[Back to top](#contents)

## Features

### Existing Features

#### CRUD

The authenticated Store Owner can manage all major product-related functions directly from the front-end of FastShoes. This includes adding new products, editing existing product details, and deleting products entirely, all accessible from either the Products page or the individual Product detail page.

Authenticated users on FastShoes have control over several key functionalities directly from the front-end. They can add or remove products from their wishlist, manage their account by updating or deleting it, and write reviews for all products available on the platform.

#### All The Pages

##### The Navigation Bar

##### The Main Content

###### Admin/Staff: Product Management

###### Home page

###### View Product page

###### Info page

###### Category page

###### Account pages

###### Cart page

###### Checkout page

##### The Footer

[Back to top](#contents)

### Future Features

Below, you can find my future plans for the website:

* As a user, i can read about the store (About Page)
* As a user i can comment on products

## Technologies Used

### Languages
* [HTML5](https://html.spec.whatwg.org/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [JavaScript](https://www.javascript.com/)

### Frameworks

* [Django](https://www.djangoproject.com/)
   * Django was used as the python framework in the project.
* [Bootstrap](https://getbootstrap.com/)
   * The CSS framework that was used for styling the website, saved me a lot of time when I learned to use it.
* [AWS.Amazon](https://us-east-1.console.aws.amazon.com/)
   * I utilized AWS to store both my media and static files for the project.

### Database
 [ElephantSQL](https://www.elephantsql.com/)
   * ElephantSQL serves as the database for the FastShoes project. It is a PostgresSQL database solution that efficiently manages and stores databases.

### Tools
* [Gitpod](https://www.gitpod.io/#get-started)
   * An online integrated development environment (IDE) used for developing and testing the FastShoes project. 
* [GitHub](https://github.com/)
   * A web-based hosting service for version control repositories, used for storing and managing the project's source code.
* [Balsamiq](https://balsamiq.com/wireframes/)
   * A wireframing tool used for creating mockups and prototypes of the FastShoes website.
* [Heroku](https://dashboard.heroku.com/)
   * Used for deploying the page and publish it. Heroku is a cloud platform that enables deployment and hosting of web applications.
* [Stripe](https://stripe.com/).
   * Stripe is a widely used payment processing platform that allows businesses to accept online payments securely.

### Supporting Libraries and Packages

[Back to top](#contents)

## Marketing

### Marketing Strategies

Subscribing:

* Allow users to subscribe to Fastshoes to receive notifications about new deals and product arrivals, ensuring they stay up-to-date with the latest offerings in the store. By subscribing, users gain exclusive access to promotions and updates, enhancing their shopping experience.

Social Media Marketing - Facebook business page:

* Given Facebook's extensive user base and diverse demographic reach, I've established a Facebook Business Page to leverage its marketing potential. Utilizing this platform, I can launch targeted ad campaigns tailored to specific geographic locations, cities, or age groups, maximizing the effectiveness of my marketing efforts. With its widespread popularity and robust advertising features, Facebook presents an ideal platform for promoting my business.

## Testing

### Manual Testing for FastShoes Website

#### Test Schedule Plan:

### Summary Table of Manual Testings for FastShoes Website

### Other Tests

#### Lighthouse Test

#### WAVE

#### Browsers And Devices

Tested on the following browsers:

* Google Chrome
* Safari
* Firefox

Tested on the following devices:

* Ipad Air
* Iphone 12, 13 and 14
* Samsung Galaxy

### Validator Testing

#### CSS

#### HTML

#### Python Linter

#### JSHint for Javascript

## Bugs

### Known Bugs


### Fixed Bugs


## Deployment and Development

* The project was developed using [Gitpod](https://www.gitpod.io/#get-started) to create the code and overall file structure.
* The repository for this project is hosted on [GitHub](https://github.com/).

### Deployment

The project was deployed using [Heroku](https://id.heroku.com/login).

INFO - to ensure a successful deployment of the project in Heroku, you need to ensure that you create a Procfile and a requirements.txt file.

* In the Procfile insert the following:
  * ``` web: gunicorn PROJECT_NAME.wsgi ```

Once you are certain that everything is ready to deploy the repo, you can do so through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
    * For this project, the unique name is "FastShoes" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and click "Reveal config vars".
6. Add the config vars necessary for the project.
7. Navigate to the "Deploy" section by clicking the "Deploy" tab in the navbar.
8. Select "GitHub" as the deployment method and click "Connect to GitHub".
9. Search for the GitHub repository that you wish to deploy.
10. Click on "connect" to link the repository to Heroku.
11. Scroll down and click on "Deploy Branch" to manually deploy.
12. Once the app has deployed successfully, Heroku will notify you and provide a button to view the app.

INFO - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys" in Heroku.

### Forking the Repository

To create a copy of the repository for viewing and editing without affecting the original repository you can fork the repository through the following steps:

1. In the "FastShoes" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository in your own GitHub account.

### Cloning The Repository

To clone the repository through GitHub, follow these steps:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Select "HTTPS" in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### The ElephantSQL Database

The [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database was used for this project.

To set up a database, follow these steps:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance (this is usually the name of the project.)
4. Select "Tiny Turtle (Free)" free plan.
5. The "Tags" field can be left blank.
6. Click "Select Region".
7. Select a data center near you.
8. Click "Review".
9. Ensure that all details are correct and then click "Create instance".
10. Once created, you can return to the dashboard and click on the instance created to view relevant details such as the database URL and password.

### The Cloudinary API
[Cloudinary](https://cloudinary.com/) is used in this project to store media assets. This is done due to the fact that Heroku does not store media files reliably.

[Back to top](#contents)

## Credits

To style the page and the content to Read me:

- The screenshot at the top of the ReadMe was built from [Ami Responsive.](https://ui.dev/amiresponsive)
- The database schema for the ReadMe was built from [drawSQL.](https://drawsql.app/)
- The color palette image was generated from [coolers.](https://coolors.co/)

To write the code for this project:

- [Code institute LMS](https://learn.codeinstitute.net/dashboard)
- [W3Schools](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [Coding 4 You](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)
- [Docs.Djangoproject](https://docs.djangoproject.com/en/5.0/topics/forms/)
- [Docs.Djangoproject](https://docs.djangoproject.com/en/5.0/topics/auth/default/)

Youtube videos that helped me alot:

- [Django Ecommerce Website](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)
- [E-commerce FullStack Website using Django](https://www.youtube.com/playlist?list=PL_KegS2ON4s53FNSqgXFdictTzUbGjoO-)
- [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

## Acknowledgements

This site was developed as my Fifth portfolio project for the Code Institute course in Full Stack Software Development. I would like to thank my mentor David Bowers, the slack community and the Code Institute team.

[Back to top](#contents)