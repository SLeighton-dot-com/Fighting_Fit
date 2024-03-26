## Testing
[Testing.md](TESTING.md)


## Technologies Used
### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML) used as the markup language
- [CSS](https://en.wikipedia.org/wiki/CSS) used to style the HTML
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) used mostly for DOM manipulation
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used to run the backend application

### Frameworks and Libraries
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) provided the base CSS framework
- [Font Awesome 6.5.1](https://fontawesome.com/icons) is used for the icons throughout the app
- [Google Fonts](https://fonts.google.com/) serves the fonts used in the app
- [jQuery 3.7.1](https://jquery.com/) is used for example DOM manipulation and event handling
- [Django v3.2.24](https://docs.djangoproject.com/en/3.2/) is the Python framework in thi project. Various Python packages have been used and they are listed below.
<details>
	<summary>Installed Python Libraries - click to view</summary>

Package|Version|Description
---|---|---
asgiref|3.7.2|Essential components for building web applications, especially with Django
boto3|1.34.54|The AWS SDK for Python, used to connect to S3 buckets
botocore|1.34.54|Provides necessary API requests to AWS services
certifi|2024.2.2|Provides Mozilla's CA Bundle for validating SSL certificates
cffi|1.16.0|Provides a means for calling C code from Python using a simple API
charset-normalizer|3.3.2|Aims to replace the chardet library within the requests toolkit
cryptography|42.0.5|A package designed to expose cryptographic primitives and recipes to Python developers
defusedxml|0.7.1|Mitigates XML-related security issues by wrapping standard Python XML parsers with safer implementations
dj-database-url|0.5.0|Parses the DATABASE_URL environment variable to configure Django databases using a single format
Django|3.2.24|The Django framework itself
django-allauth|0.61.1|Provides authentication mechanisms, including social login
django-countries|7.2.1|Offers a country field for Django models and forms
django-crispy-forms|1.14.0|Controls the rendering behaviour of Django forms
django-storages|1.14.2|A collection of custom storage backends for Django, used for Amazon S3 in this project
gunicorn|21.2.0|A Python WSGI HTTP Server for UNIX
idna|3.6|Implements the Internationalized Domain Names in Applications (IDNA) protocol
jmespath|1.0.1|A query language for JSON
oauthlib|3.2.2|A generic implementation of the OAuth request-signing logic
packaging|23.2|Provides core utilities for Python packages
pillow|10.2.0|The friendly PIL fork (Python Imaging Library)
psycopg2|2.9.9|PostgreSQL database adapter
pycparser|2.21|A complete parser of the C language
PyJWT|2.8.0|A Python library for encoding and decoding JSON Web Tokens (JWTs)
python-dateutil|2.9.0.post0|Provides powerful extensions to the standard datetime module
python-dotenv|1.0.1|Reads key-value pairs from a .env file and sets them as environment variables
python3-openid|3.2.0|A set of Python packages to support the use of OpenID
pytz|2024.1|Enables Python programs to work with the Olson timezone database
requests|2.31.0|Simplifies HTTP requests
requests-oauthlib|1.3.1|Provides an easy-to-use interface for making OAuth authenticated requests
s3transfer|0.10.0|A Python library for managing Amazon S3 transfers
setuptools|69.1.1|A stable library designed to facilitate packaging Python projects
six|1.16.0|A Python 2 and 3 compatibility library
sqlparse|0.4.4|A non-validating SQL parser module for Python
stripe|8.4.0|Library for Stripe’s API
typing_extensions|4.10.0|Backports and experimental features for the typing module in Python
tzdata|2024.1|The tzdata package contains data files with rules for various time zones
urllib3|1.25.4|A powerful HTTP client for Python
whitenoise|6.6.0|Simplified static file serving for WSGI applications
</details>

### Tools
-  [Visual Studio Code](https://code.visualstudio.com/) - The IDE used during development
- [AWS S3 Buckets](https://aws.amazon.com/s3/) - Used to host static files and media files
- [Stripe](https://stripe.com/) - For accepting payments when checking out
- [Microsoft Paint](https://en.wikipedia.org/wiki/Microsoft_Paint) & [Photos (Windows)](https://en.wikipedia.org/wiki/Photos_(Windows)) - Image editing and manipulation
- [Git](https://git-scm.com/) - For version control
- [GitHub](https://github.com/) - Repository storage and sharing of code
- [Unsplash](https://unsplash.com/) - Image sourcing
- [miramuse ai](https://miramuseai.net/) - Formerly called midjourney ai for product image creation
- [Favicon](https://favicon.io/) - Used for Favicon generation

### Databases
- [SQLite3](https://www.sqlite.org/index.html) - The local database used during development
- [Elephant SQL](https://www.elephantsql.com/) - PostgreSQL database used in production

### Hosting
- [Heroku](https://www.heroku.com/) - Used to host the deployed version of this project

## Deployment
### Deploying To Heroku
The following instructions are based on the user running VSCode on Windows 10. The process remains the same ff you are using a different IDE or OS, but your commands maybe slightly different.

You will need [Python](https://www.python.org/downloads/) (ideally the latest version) installed on your machine. You will also need [PIP](https://pypi.org/project/pip/) which comes with Python versions 3.4 and later. Having [Git](https://git-scm.com/) is also highly recommended.


- Save a copy of the repo on your local machine or use ``git clone https://github.com/SLeighton-dot-com/Fighting_Fit``.

Please make sure that before you follow these steps that:
- The app has been deployed locally and then pushed to your own GitHub account.
- You have created and configured an [AWS S3 Bucket](https://aws.amazon.com/s3/) for serving the media files and static
- You have a [Stripe](https://stripe.com) account for taking payments

If you have the above in place follow the these steps:
- In your `settings.py` file add the following code
```
import os(<Ensure this is at the head of the file>)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

ALLOWED_HOSTS = [<This will be the URL that Heroku assigned to your deployed site>]

# Email
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = '<fightingfit@example.com>'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'(<The Outgoing Mail Server for your email, for example `smtp.gmail.com`>)
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

#Stripe
load_dotenv()
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
```

- Go to [heroku.com](https://heroku.com) and log in or create an account.
- Click `New` to add a new app, give it a name, choose a region and click `Create app`.
- On the `Setttings`  tab add the config var 'DATABASE_URL' and then copy in your `postgres//....` database url.
- From your local IDE, in your `settings.py` file, under `DATABASES` section add the following code 
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
- Also in `settings.py` add the following code for AWS
```
if 'USE_AWS' in os.environ:
    
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'fighting-fit'
    AWS_S3_REGION_NAME = 'eu-west-2' (Or what server is closest to you)
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
```
- In your terminal run `python3 manage.py showmigrations`, you should see a list of the migrations and none of them should be checked off showing that your local deployment is now connected to the remote Postgres db, so you can run:
- `python manage.py migrate` to set up the database
- `python manage.py loaddata categories` to load the categories
- `python manage.py loaddata products` to load the products
- `python manage.py createsuperuser` to set up your admin account.
- Go to your Postgress DB (I used Elephant SQL) and navigate to `Browser` click `Table queries` and the `auth_user`, click `Execute` and you should see your superuser details displayed.
- Go back to the Dashboard, and from the `Setttings` tab, click the `Reveal Config Vars` button and add the following key / value pairs
	- `EMAIL_HOST_USER` - The email address you want the app to send emails from
	- `EMAIL_HOST_PASS` - The password for above email address
	- `SECRET_KEY` - Use a Django Secret Key Gen, for example [this one](https://miniwebtool.com/django-secret-key-generator/).
	- `STRIPE_PUBLIC_KEY` - Your Stripe API `Public key`
	- `STRIPE_SECRET_KEY` - Your Stripe API `Secret key`
	- `STRIPE_WH_SECRET` - This is your Webhook link for STRIPE
	- `AWS_ACCESS_KEY_ID` - Your AWS Access Key
	- `AWS_SECRET_ACCESS_KEY` - Your AWS Secret Access Key
	- `USE_AWS` - Set this to `TRUE`
- Back in the Heroku Dashboard, click the `Deploy` tab and scroll down to `Deployment Method`. Select `GitHub` and link your account and repository.
- Scroll down further to `Automatic deploys` for Heroku to update your deployed site after you commit changes to Github. 
- Scroll down to `Manual Deploy`, choose the branch you wish to deploy and click `Deploy Branch`
- Wait for the app to build, and once complete, click `view` to launch your app in the browser.
- Log in with the superuser details you created and navigate to the admin panel at `your-deployment-url/admin`

## Credits

### media

- Hero Image
home_background_image_cropped.jpg by https://unsplash.com/photos/people-sitting-on-floor-in-front-of-white-wall-DT3bb-KDAus

- Workout images
leg_workout.jpg https://unsplash.com/photos/woman-in-black-shirt-and-blue-denim-jeans-sitting-on-black-exercise-equipment-Z4Q9KHw9ofE
chest_workouts.jpg https://unsplash.com/photos/man-in-black-crew-neck-t-shirt-and-gray-pants-sitting-on-black-and-red-bench-NXMZxygMw8o
cardio_workout.jpg https://unsplash.com/photos/woman-holding-brown-ropes-U5kQvbQWoG0
whole_body_workouts.jpg https://unsplash.com/photos/person-weightlifting-painting-vqDAUejnwKw
arm_workouts.jpg https://unsplash.com/photos/topless-man-in-black-shorts-carrying-black-dumbbell-7kEpUPB8vNk

- Stretching images
yoga_stretches.jpg https://unsplash.com/photos/woman-in-blue-denim-jeans-lying-on-black-floor-GEjCwneU-YY
leg_stretches.jpg https://unsplash.com/photos/woman-in-black-tank-top-and-black-pants-sitting-on-black-wooden-table-k1KCiRaDQhs
core_stretches.jpg https://unsplash.com/photos/woman-doing-yoga-on-stability-ball-f4RBYsY2hxA
all_body_stretches.jpg https://unsplash.com/photos/man-in-green-shorts-raising-his-both-hands-Ug9ZVq24CIk

All other images on my project were genereated using Midjourney AI which changed name part way through my project to [Muse AI](https://miramuseai.net/)


## Acknowledgements

* My Mentor Rory Patrick for helpful feedback and advice during mentor sessions throughout this project.

* The Tutor support team at Code Institute and Amy Richardson for their support and guidance.
