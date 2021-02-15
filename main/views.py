from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os

config = {
    "apiKey": "AIzaSyA-99K3f5TK26Z7n5szV4wLq_fl6Gf9kcs",
    "authDomain": "dj-firebase-6f10d.firebaseapp.com",
    "projectId": "dj-firebase-6f10d",
    "storageBucket": "dj-firebase-6f10d.appspot.com",
    "messagingSenderId": "719069501836",
    "appId": "1:719069501836:web:822c7843a3d428d32f9ea9",
    "measurementId": "G-VLZXVGDCZF",
    "databaseURL": ""
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
