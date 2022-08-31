# Table of Contents

***

# Introduction

***

# Database Schema - Entity Relationship Diagram

***

# Testing
(link to separate tests.md file)
Implement manual testing and document the procedures and results. 

***

# Bugs

## Fixed

- When attempting to access the Profile edit page in the admin panel, I encountered the following error: "In order to use cloudinary storage, you need to provide CLOUDINARY_STORAGE dictionary with CLOUD_NAME, API_SECRET and API_KEY in the settings or set CLOUDINARY_URL variable (or CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET variables)".
This error was showing because the env.py file was not saved in the top directory of the project. Upon moving the file to the top directory, this error was rectified. 

- When attempting to render the Comment List views for Gallery and Walk posts I encountered the following error: " 'Meta.fields' must not contain non-model fieldnames". This error was showing as I had given the filterset_fields lists in each comment model the wrong value. I corrected the values to 'walk_post' and 'gallery_post', where they had previously been 'post' and 'gallery'. 

   


## Unfixed

***

# Technologies Used

## Modules

## Languages
- Python - The base language of the Django REST Framework

## Libraries
- Django Cloudinary Storage
- Pillow (image processing capabilities)

## Frameworks
- Django REST Framework

## Platforms

## Services 

## Resources

***

# Deployment
(process for API)

## Project Setup

1. Create a new repository from the Code Institute template repository.
2. Run terminal command **pip3 install 'django<4'** to install Django.
3. Run terminal command **django-admin startproject pp5_drf_api .** (pp5-drf-ap is the name of my api - make to include the dot at the end to initialize project in it's current directory).
4. Run terminal command **pip install django-cloudinary-storage** to install Django Cloudinary Storage.
5. Run terminal command **pip install Pillow** to install Pillow image processing capabilities (note the uppercase 'P').
6. Add the newly installed apps 'cloudinary_storage' and 'cloudinary' to INSTALLED_APPS in settings.py as shown below:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', 
    'django.contrib.staticfiles',
    'cloudinary',
]
```
7. Create env.py in the top directory, import os and add the CLOUDINARY_URL as shown below: 
```
import os
os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
```
8. Back in settings.py, load environment variable with Cloudinary credentials, set a CLOUDINARY_STORAGE variable, define the MEDIA_URL folder and set a DEFAULT_FILE_STORAGE variable as follows: 
```
import os

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
***

# References

***

# Credits


