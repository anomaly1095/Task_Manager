from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseBadRequest
from .hash import hash_password, verify_password
from typing import List
from .models import *

"""Summary

"""
def signup(request):
    """This function like signup will be used by 2 forms searches for task in all database
    
        * if Test == True the user signed up and uses the form for redirection to home page
        
        * else the user is soming from the form in index.html and gonna sign up
    """
    if request.method == 'POST' and request.POST.get("Test") != "True":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Custom_User.objects.filter(username=username).exists():
            message = "Username already exists. Please choose a different one."
            render(request=request, template_name= 'signup.html', context= {'message': message})
        else:
            salt, hashed_pwd = hash_password(password=password)
            user = Custom_User()
            user.username = username
            user.password = hashed_pwd
            user.salt = salt
            user.save()
            return render(request=request, template_name= 'index.html', context= {'user': user})
    return render(request=request, template_name= 'signup.html', context= {})


def login(request):
    if request.method == 'POST':
        if request.POST.get("username") != None and request.POST.get("password") != None:
            username = request.POST.get("username")
            password = request.POST.get("password")
            users = Custom_User.objects.all()
            for user in  users:
                if verify_password(password, user.salt, user.password) == 1:
                    return render(request=request, template_name="index.html", context= {'user': user})
        else:
            return render(request=request, template_name="login.html", context= {})
    return render(request=request, template_name= 'login.html', context= {})
    

def home(request):              # add a method to track time left for each task
    if request.method != 'POST':
        return redirect(to=login)
    else:
        return render(request=request, template_name="index.html", context= {})
    

def delete_task(request): #searches for task in all database
    if request.method != 'POST':
        return redirect(to=login)
    else:
        try:
            task = get_object_or_404(Task, id = int(request.POST.get("id")))
        except Http404:
            return redirect(to= home)
        else:
            task.delete()
            return  
        
    
def modify_task(request):    
    """This function like signup will be used by 2 forms searches for task in all database
    
        * if Test == False the user just used the form in index.html
        
        * else the user updated he values and confirmed the changes
    """
    if request.method != 'POST':
        return redirect(to=login)
    else:
        if request.POST.get("Test") == 'False':

            try:
                task = get_object_or_404(Task, id = int(request.POST.get("id")))
            except Http404:
                return Http404
            else:
                return render(request= request, template_name= "modify_task.html", context={"task": task})
        else:
            #apply modifications made to the task and save
            try:
                task = get_object_or_404(Task, id = int(request.POST.get("id")))
            except Http404:
                return Http404
            else:
                task.title = request.POST.get("title")
                task.description = request.POST.get("description")
                task.location = request.POST.get("location")
                task.subject = request.POST.get("subject")
                task.save()
                return redirect(to= home)
        
def search(request):        #searchs for task in user's tasks
    if request.method == 'POST':
        try:
            user = get_object_or_404(Custom_User, id = int(request.POST.get("id")))
        except Http404:
            return redirect(to= home)
        else:
            tasks = user.tasks.all()
            value = request.POST.get("value")
            for task in tasks:
                if value in task.title:
                     tasks.append(task)
            return render(request= request, template_name= "search.html", context={"tasks": tasks})
    else:
        return redirect(to= login)