# Deployment and Development

## Contents

* [Deployment and Development](#deployment-and-development)
    * [Setup and Deployment](#setup-and-deployment)
    * [The ElephantSQL Database](#the-elephantsql-database)
    * [Amazon Web Services ( AWS )](#amazon-web-services--aws)
    * [Project Settings Adjustments](#project-settings-adjustments)
    * [Deployment Heroku](#deployment-heroku)
    * [Forking the Repository](#forking-the-repository)
    * [Cloning The Repository](#cloning-the-repository)

* The project was developed using [Gitpod](https://www.gitpod.io/#get-started) to create the code and overall file structure.

* The repository for this project is hosted on [GitHub](https://github.com/).

## Setup and Deployment

### Creating the Workspace Project repository ###

1. This project has been created by using the full Code Institute provided template which you can find here : [Gitpod Full Template - Code Institute.](https://github.com/Code-Institute-Org/gitpod-full-template)

2. Click : Create New repository - using that template.

3. Name : Name the repository/project.

4. Launch : Launch the creation of the repository as it can take a few minutes to complete.

### Initial Workspace Installations

Here are the steps to install the necessary frameworks/packages : 

1. Installation of Django : 
    
        pip3 install django

2. Installation of Gunicorn : 
    
         pip3 install gunicorn

3. Installation of Libraries :

         pip3 install dj_database_url
        
         pip3 install psycopg2-binary

4. Create the requirements file with the installed libraries/packages :

* (Note: You must rerun this command if you install any additional dependencies!)
    
        pip3 freeze local > requirements.txt

5. Now you create your project : 

* You do this by running the command :
    
        django-admin startproject (PROJECT_NAME) . 
        
    * (Make sure to include the full stop at the end)

6. Next you create your app :

* You do this by running the command :
    
         python3 manage.py startapp (APP_NAME)
    
    * As soon as you created your app make sure to add the app into your settings.py under the section of INSTALLED_APPS. This is important.

7. Here you run your migrations again :

* Make your migartions by :
    
         python3 manage.py makemigrations

    * also a good idea to run : python3 manage.py makemigrations --dry-run to have a pre-flight check before you make any changes.


* Migrate your changes to the database : 

        python3 manage.py migrate

* You can test your website then locally by running : python3 manage.py runserver
    * This is good to make sure everything is set up and working correctly. If everything is correct you will see the Django Default Page.

8. Create your env.py file in the root directory.

[Back to top](#contents)

## The ElephantSQL Database

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

[Back to top](#contents)

## Amazon Web Services ( AWS )

To configure media/static storage for our project, we utilized [AWS]((https://aws.amazon.com/)). Follow these steps to set it up:

### Create an AWS Account :
     
* Head to the AWS website and sign up for an account if you haven't already.

### Set Up AWS S3 Bucket :

To set up your S3 bucket for static website hosting, follow these steps :

1. In the AWS Management Console, use the search bar to find and select "S3".
2. Create a new bucket with a name preferably matching your Heroku project name, and choose your desired region.

3. Uncheck the "Block all public access" option to allow public access to your bucket.

4. Enable ACLs under "Object Ownership" and select "Bucket owner preferred" for enhanced control over object ownership.

5. In the "Properties" tab of your bucket, activate static website hosting. Enter "index.html" for both the Index document and Error document fields.

6. Under the "Permissions" tab, navigate to the CORS configuration and paste the following configuration:

 * ```  [
     {
         "AllowedHeaders": ["Authorization"],
         "AllowedMethods": ["GET"],
         "AllowedOrigins": ["*"],
         "ExposeHeaders": []
     }
   ]

### Configure Bucket Permissions :

* Go to the "Bucket Policy" tab in your S3 bucket settings and select "Policy Generator".

Configure the Policy Generator as follows :

1. Set the "Policy Type" as "S3 Bucket Policy".

2. Set the "Effect" as "Allow".

3. Set the "Principal" as "*".

4. Set the "Actions" as "GetObject".

5. Paste your ARN (Amazon Resource Name) into the "Amazon Resource Name (ARN)" field.

6. Generate the policy, copy it, and paste it into the Bucket Policy Editor

 * ``` {
     "Id": "Policy1234567890",
     "Version": "2012-10-17",
     "Statement": [
         {
             "Sid": "Stmt1234567890",
             "Action": ["s3:GetObject"],
             "Effect": "Allow",
             "Resource": "arn:aws:s3:::your-bucket-name/*",
             "Principal": "*"
         }
     ]
   }

7. After pasting the policy into the Bucket Policy Editor, append "/*" to the end of the "Resource" key before saving.

8. In the ACL (Access Control List) section, enable "List" for Everyone to grant access to list objects in the bucket.

### Create user and User Group in IAM :

1. Navigate to the IAM (Identity and Access Management) service.

2. Create a new user group, naming it something like "group-your-app-name".

3. Select the created group, go to the "Permissions" tab, click "Add Permissions", then "Attach Policies".

4. Switch to the JSON tab, and click on the "Import Managed Policy" link. Search for "S3" and select the "AmazonS3FullAccess" policy, then click "Import". Finally, paste your ARN from the S3 Bucket into the "Resources" key.

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::your-bucket-name",
                    "arn:aws:s3:::your-bucket-name/*"
                ]
                }
            ]
        }

5. Review the policy and proceed to create it.

6. Attach this policy to your group.

7. When adding a new user to the group, select "Programmatic Access" as the AWS Access Type. Afterward, download the .csv file containing the user's Access Key ID and Secret Access Key.

### Create Media Folder

1. Navigate to your S3 bucket and create a new folder called "media" where your image files will be stored.

2. Upload all the necessary files for your project into this "media" folder.

3. Ensure that the "Manage Public Permissions" setting is configured to "Grant Public Read Access to this object(s)" for the files in the "media" folder.

### Integrate AWS S3 with Django :

1. Install the boto3 and django-storages packages in your Django project.

2. Add 'storages' to the INSTALLED_APPS in your project's settings.py file.

3. Add your AWS secret variables to the env.py file.

By following these steps, you'll be able to set up AWS for media/static storage in your project.

[Back to top](#contents)

## Project Settings Adjustments

Here, I'll outline all the settings that were added or adjusted in the settings.py file of the project folder. 

1. Initial settings and imports at the top of the file include :

        import os
        from pathlib import Path
        import dj_database_url

        if os.path.isfile("env.py"):
            import env

2. Secret key settings, always keep these secret with caution, include :

        SECRET_KEY = os.environ.get("SECRET_KEY")

        DEBUG = "DEVELOPMENT" in os.environ 

3. Database settings will include the secret URL that you have set in the Env.py file :
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }

4. Media and Static files : 

        STATIC_URL = '/static/'
        STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

5. Add the following imports into your URLS.py in your project folder.

        from django.conf import settings
        from django.conf.urls.static import static

        followed by the following command at the end of the urlpatterns: 

        urlpatterns = [
            path(your paths),
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

6. Template DIRS setting : 

        TEMPLATES = [
            {
                'DIRS': [
                    os.path.join(BASE_DIR, 'templates'),  *// ADD THIS // *
                ]
            } 
        ] 

7. AWS Setup :

        if 'USE_AWS' in os.environ:

            # Cache control
            AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=94608000',
            }

            # Bucket Config
            AWS_STORAGE_BUCKET_NAME = 'your-storage-bucket-s3-name' // Your S3 name
            AWS_S3_REGION_NAME = 'your-region-1' // Your Region
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

8. Create custom_storages.py file in root directory :

        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

9. Create Procfile in the root directory :

        Once you created the procfile add this command inside : 
        web: gunicorn your_app_name.wsgi:application

        * This file is essential for Heroku Deployment.*

10. Change your allowed hosts at the top to the following : 

        ALLOWED_HOSTS = [
        "project_name.herokuapp.com", 
        "localhost", "local_gitpod_workspace_url"]

   * To run the app on the development side, once you run python3 manage.py runserver, you will need to copy your workspace URL and add it to your ALLOWED_HOSTS setting in the settings.py file. This usually looks like: https://8000.projectname.... depending on the port assigned
        

* At this stage you are ready to make your commit and push changes into your GitHub repository.
With the following commands : 

       1. git add .
       2. git commit -m "Commit Message"
       3. git push

[Back to top](#contents)

## Deployment Heroku

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

[Back to top](#contents)

## Forking the Repository

To create a copy of the repository for viewing and editing without affecting the original repository you can fork the repository through the following steps:

1. In the "FastShoes" repository, click on the "fork" tab in the top right corner.

2. Click on "create fork" to fork the repository in your own GitHub account.

[Back to top](#contents)

## Cloning The Repository

To clone the repository through GitHub, follow these steps:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.

2. Select "HTTPS" in the dropdown menu.

3. Copy the URL under HTTPS.

4. Open Git Bash in your IDE of choice.

5. Change the working directory to the location where you want the cloned directory to be created.

6. Type "git clone" and paste the URL that was copied from the repository.

7. Press the "enter" key to create the clone

[Back to top](#contents)