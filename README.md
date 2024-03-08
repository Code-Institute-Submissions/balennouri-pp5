# FastShoes

The live site can be viewed [here](https://fastshoes-be1fd2fa0203.herokuapp.com/)

![Am I responsive screenshot]()

## Contents

* [Project Goals](#project-goals)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Epics](#epics)
    * [Site Structure](#site-structure)
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
            * [Admin/Staff](#adminstaff-product-management)
            * [Home Page](#home-page)
            * [Info Page](#info-page)
            * [Category Page](#category-page)
            * [Account Pages](#account-pages)
            * [Cart Page](#cart-page)
            * [Checkout Page](#checkout-page)
            * [Comment Page](#comment-page)
        * [The Footer](#the-footer)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
   * [Languages](#languages)
   * [Frameworks](#frameworks)
   * [Database](#database)
   * [Tools](#tools)
   * [Supporting Libraries and Packages](#supporting-libraries-and-packages)
* [Testing](#testing)
   * [Manual Testing](#manual-testing-for-fastball-website)
   * [Summary Table of Manual Testings](#summary-table-of-manual-testings-for-fastball-website)
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

[Back to top](#contents)

## User Experience

### User Stories

#### Epics 

During the planning for the project, I started and created 4 epics and then broke them down into 38 user stories.

The user stories that were broken down from the epics, I labeled them with different labels and I used the MoSCoW (must have, should have, could have and won't have) to develop them. I labeled them, so I could put energy on the important ones before I started with the non-important ones. You can se all of them on the project board [here.]() On the project board you will be able to see the future features as well.

Below here is the completed user stories for this version of this project listed by epics:

##### Epic: Initial Django Setup

##### Epic: User Authentication and Account Management

##### Epic: Product Management and Cart/Checkout

##### Epic: The Webiste and Content:


[Back to top](#contents)

### Site Structure

#### Wireframes

I used Balsamiq to create my wireframes. I decided to make wireframes for larger screens and for mobile phones. I think wireframes are a good thing to do before starting with the project, so I can put my ideas on what I want the website to look like. Some pages are a little different from the wireframes, but it small details differ from page to page. The reason is because, during development, to make a website with good functionality.

##### Home page in wireframe

![wireframe home page]()

##### Info page in wireframe

![wireframe Info page]()

##### Category page in wireframe

![wireframe category page]()

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

For this project, I utilized the built-in Django User Model for user accounts and created one model in the store app. In the store model, I built a customer model, order model, product model and category model.

The database schema seen below was created using [Drawsql.app.](https://drawsql.app/) All the fields are not labeled correctly because of limitations in the "drawsql" app. One are the email field and the cloudinary field. However, the diagram still shows the general layout of the models in the store app.

If you want to see the true field choices, head over to the models.py in the store app.

The Database schema:

![Database schema]()

[Back to top](#contents)

### Design Choices

#### Typography

#### Colour Palette

![colour pallete]()

The color palette image was generated from [coolers.](https://coolors.co/)

[Back to top](#contents)

### Project Management

I used agile methodology throughout the development of this project utilizing GitHub projects and issues. You can read more about this in the AGILE.md file [here.](https://github.com/balennouri/pp5/blob/main/AGILE.md)

[Back to top](#contents)

## Features

### Existing Features

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
* [Cloudinary](https://cloudinary.com/)
   * Cloudinary was used to save my media. It's a cloud-based platform for saving and storing images.
* [Start Bootstrap](https://startbootstrap.com/)
   * Start bootstrap was used for the project's theme. Start boostrap creates open source themes, templates and snippets.

### Database
 [ElephantSQL](https://www.elephantsql.com/)
   * ElphantSQL is used as a database for the FastBall project. ElphantSQL is a PostgresSQL database that saves and stores databases.

### Tools
* [Gitpod](https://www.gitpod.io/#get-started)
   * An online integrated development environment (IDE) used for developing and testing the FastBall project. 
* [GitHub](https://github.com/)
   * A web-based hosting service for version control repositories, used for storing and managing the project's source code.
* [Balsamiq](https://balsamiq.com/wireframes/)
   * A wireframing tool used for creating mockups and prototypes of the FastBall website.
* [Heroku](https://dashboard.heroku.com/)
   * Used for deploying the page and publish it. Heroku is a cloud platform that enables deployment and hosting of web applications.

### Supporting Libraries and Packages


[Back to top](#contents)

## Testing

### Manual Testing for FastBall Website

#### Test Schedule Plan:

### Summary Table of Manual Testings for FastBall Website

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
    * For this project, the unique name is "FastBall" and the region selected is Europe.
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