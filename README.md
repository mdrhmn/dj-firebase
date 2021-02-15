# Django + Firebase Cloud Storage

This is a sample project to test Firebase storage integration with Django using Pyrebase package.

## Getting Started

### 1. Set up your Django project

If you are **cloning this repo**, run the following command preferably inside your virtual environment and **skip to step 5**:

- Using **pipenv**:
    ```Shell
    $ pipenv install -r requirements.txt # (Python 2)
    $ pipenv3 install -r requirements.txt # (Python 3)
    ``` 
- Using **venv**:
    ```Shell
    $ pip install -r requirements.txt # (Python 2)
    $ pip3 install -r requirements.txt # (Python 3)
    ``` 

Else, to **create your Django project** from scratch (make sure to have Django installed):

```Shell
$ django-admin startproject project_name
``` 

Next, **navigate** into the newly created project folder. Then, **start a new Django app**. We will also **run migrations** and **start up the server**:

```Shell
$ cd project_name
$ python manage.py startapp app_name
$ python manage.py migrate
$ python manage.py runserver
``` 

If everything works well, we should see an instance of a Django application running on this address — http://localhost:8000

![alt text](https://scotch-res.cloudinary.com/image/upload/v1542486456/ia8jlkozut4uxwatnqwp.png)

### 2. Configure project settings

1. Add app inside INSTALLED_APPS (`settings.py`)

    Once you’ve created the app, you need to install it in your project. In `project_name/settings.py`, add the following line of code under `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app_name',
    ]
    ```

    That line of code means that your project now knows that the app you just created exists.

2. Add templates folder directory in TEMPLATES  (`project_name/settings.py`)

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates/'], # HERE
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

2. Add static and media folder directory in STATIC_ROOT  (`project_name/settings.py`)

    ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

3. Add desired URL for the app (`project_name/urls.py`)

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('(INSERT_URL)', include('APP_NAME.urls')),
    ]
    ```

4. Create new `urls.py` for the app (`app_name/urls.py`)

### 3. Configure app settings

1. **Create new template (**`app_name/templates/`**)**
    - You need to create the HTML template to display to the user after creating a view function.
    - Create a directory named **templates a**nd subsequently a file named `app_name.html` inside it:

        ```python
        # Create directory (if haven't)
        mkdir app_name/templates/

        # Create HTML template
        touch app_name/templates/app_name.html
        ```

2. **Create view function (FBV/CBV) in app's `views.py`**
    - Views in Django are a **collection of functions or classes** inside the `views.py` file in your app directory.
    - Each function or class handles the logic that gets processed each time a different URL is visited.

        ```python
        from django.shortcuts import render

        def view_name(request):
            return render(request, 'template_name.html', {})
        ```

    - The function defined is called a **view function**. When this function is called, it will render an HTML file called `app_name.html`.

3. **Add URL to app's `urls.py`**
    - The final step is to hook up your URLs so that you can visit the page you’ve just created.
    - Your project has a module called `urls.py` in which you need to include a URL configuration for the app. Inside `app_name/urls.py`, add the following:

        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('', views.view_name, name="view_name"),
        ]
        ```

        - This looks for a module called `urls.py` inside the hello_world application and registers any URLs defined there.
        - Whenever you visit the root path of your URL (localhost:8000), the application’s URLs will be registered.

### 4. Install Pyrebase package

[Pyrebase](https://github.com/thisbejim/Pyrebase) is a simple python wrapper for the Firebase API.

To install Pyrebase:

```Shell
$ pip install pyrebase
``` 

### 5. Create a new Firebase project

In order to use Firebase, you need to be logged into your Google account. Go to [Firebase](https://firebase.google.com) and click Get started. You will be redirected to [Firebase Console](https://console.firebase.google.com).

Next, click **Add project** and fill up the necessary fields.

![Imgur Image](https://miro.medium.com/max/640/1*R0Oh8L0E0D254hX6j2jaDg.gif)


### 6. Create Firebase app

Once the project has been successfully created, click the **'</>'** button to create a new Firebase web app. 

![Imgur Image](https://imgur.com/GfpeLS.png)

Go through the **'Add Firebase to your web app'** creation process as shown below.

![Imgur Image](https://imgur.com/uybKwI2.png)

When you reach the 'Add Firebase SDK' part, **copy the web app's Firebase configuration** as highlighted in the image below. You will need this for your Pyrebase config inside Django later.

![Imgur Image](https://imgur.com/qzxkKDj.png)

### 7. Set up Django app views

The next step is to initialise our Firebase connection in Python (Django) by first **importing the pyrebase package** and **creating a dictionary** called `config` based on the Firebase configuration that you copied previously. You will need to amend the codes a bit by encapsulating the keys as strings.

You also need to add another key-value pair inside the dictionary called `databaseURL`. This is because in order to connect with Firebase, you need to declare the `databaseURL` environment variable (which in this guide is not configured since we will be focusing more on Firebase Cloud Storage).

```python
# app_name/views.py
import pyrebase
import os

config = {
    "apiKey": "KEY",
    "authDomain": "project_name-id.firebaseapp.com",
    "projectId": "project_name-id",
    "storageBucket": "project_name-id.appspot.com",
    "messagingSenderId": "msg_sender_id",
    "appId": "1:app_id",
    "measurementId": "G-measurement_id",
    "databaseURL": ""
}
```

Then, to **initialise the Firebase connection and storage**, write the following codes:

```python
# app_name/views.py

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
```

### 8. Create new Firebase Cloud Storage

To create a Cloud Storage, click **'Storage'** on the **left sidebar** and then **click 'Get Started' button**. 

![Imgur Image](https://imgur.com/uXcja84.png)

Follow the two steps prompted. Keep in mind that the Cloud Storage location should be in your region (in our case, southeastasia2).

![Imgur Image](https://imgur.com/mEhTmFT.png)

Once the Cloud Storage has been successfully created, **go to the Rules tab** and **edit the rules** to the following (**IMPORTANT: only for development purposes!**)

![Imgur Image](https://imgur.com/hnLyMCq.png)

```
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write
    }
  }
}
```

### 9. Configure file upload to Firebase Cloud Storage

Going back to `app_name/views.py`, to upload files inside the Firebase Cloud Storage, we need to use the `storage.child()` and `storage.put()` functions as follows:

```python
# app_name/views.py

storage = firebase.storage()
storage.child(PATH/DIRECTORY_ON_CLOUD).put(PATH_TO_LOCAL_IMAGE  )

# Example (same directory, same file name)
storage.child("images/example.jpg").put("example.jpg")

# Example (different directory, different file name)
storage.child("images/renamed_img.jpg").put("media/original_img.jpg")
```

The `child()` method is used to build paths to your data with the Storage service. You can specify the file directory and even the uploaded file name (renaming). The `put()` method on the other hand takes the path to the local file that you want to upload on Cloud Storage.

### 10. Implement file upload logic (optional)

This is an additional and optional step on my part, where I created a simple file upload logic from the template form:

```python
# app_name/views.py

from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os

config = {
    # REDACTED
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("files/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        messages.success(request, "File upload in Firebase Storage successful")
        return redirect('main')
    else:
        return render(request, 'main.html')

```

What this essentially does is that the **user is able to upload any file** via the form created using TailwindCSS. The function-based view will then **retrieve the uploaded file**, **save it locally** (MEDIA_ROOT directory as specified in `settings.py` and using Django's `default_storage` library), **upload the file in Firebase Cloud Storage** and then **delete the local file** (since I only cared about uploading in cloud instead of local). 

## References

1. https://www.youtube.com/watch?v=I1eskLk0exg&feature=youtu.be
2. https://github.com/thisbejim/Pyrebase
3. https://stackoverflow.com/questions/65873454/python-pyrebase-config/65873526#65873526
4. https://www.geeksforgeeks.org/how-to-create-a-new-project-in-django-using-firebase-database/
