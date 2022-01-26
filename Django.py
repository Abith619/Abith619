#                                                                                              Django
from django.db import models

#                                          mapping the views.py in urls.py file
#                                          Django Template Language
# {{variable_name}}, {% if condition %}
#                                                render function = 3 Parameters
"""Request
Mentioning the path of template in settings.py
Parameters that contain all variables and can create as many as possible"""
#                                         set Cookie Using Django
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome") # output to the screen 
def setting_cookie(request):
    response = HttpResponse("We are setting a cookie")
    response.set_cookie('Learning', 'Django',5)
    return response
def getting_cookie(request):
    first_test  = request.COOKIES['Learning']
    return HttpResponse("Practice: "+  first_test);
#                                                           urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('setc', views.setting_cookie, name='setc'),
    path('getc', views.getting_cookie, name='getc')
    ]
#                                                                Modify Cookie
#                                     view.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome")
def setting_cookie(request):
    response = HttpResponse("We are setting cookie")
    response.set_cookie('Learning', 'Django')
    return response
def updating_cookie(request):
    response = HttpResponse("We are updating  the cookie which is set before")
    response.set_cookie(Learning, 'Happy')
    return response
def getting_cookie(request):
    first_test  = request.COOKIES['Stay']
    return HttpResponse("Always be: "+  first_test);
#                                                         urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('setc', views.setting_cookie, name='setc'),
    path('updc', views.updating_cookie, name='updc'),
    path('getc', views.getting_cookie, name='getc')
    ]
#                                                          Update Cookies
#                               view.py
def updating_cookie1(request):
    response = redirect(home)
    response.set_cookie('Learning', 'Practising')
    return response
#                                                          Delete Cookie
#                                view.py
def deleting_cookie(request):
    response = HttpResponse("We are now finally deleting the cookie which is set")
    response.delete_cookie('Learning')
    return response
#                                urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('setc', views.setting_cookie, name='setc'),
    path('updc', views.updating_cookie, name='updc'),
    path('getc', views.getting_cookie, name='getc'),
    path('delc', views.deleting_cookie, name='delc')
    ]
#                                                                                                  Views
from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    return HttpResponse ("Hello World")
#                                                        Tag the view in urls.py File
from django.contrib import admin
from django.conf.urls import url
from Django.apps import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'admin/', admin.site.urls), ]
# Reload the server using python manage.py runserver command and verify the webpage
# Create a Template Folder
#
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Template_DIR = os.path.join(BASE_DIR,'Templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Template_DIR,],
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
Template_DIR = os.path.join(BASE_DIR,'Templates')
# Place an HTML file inside the Templates Folder = Django App1
#                                                                   Render
# Render the HTML File in views.py using() Method
from django.shortcuts import render
from django.http import HttpResponse
def index(request_iter):
    return render(request_iter,'design.html')
"""arguments	Description
Request      	This is used to generate a response. This is a mandatory argument.
Template Name	Name of the template used for this view. This is a mandatory argument.
Context	        A context is a variable name and variable value mapping maintained as a dictionary. In default, this is an empty dictionary. So if the key is passed the corresponding value from the dictionary can be retrieved and rendered. This is an optional argument.
content_type	MIME(Multipurpose Internet Mail Extensions) to be used. The default value is ‘text/html’. This is an optional argument.
Status	        The response code to be used. The default response code is 200.
Using	        This argument is used to represent the name of the template engine used for loading the template. This is an optional argument."""
# view Rendered from Template TAG {{ Key1 }}
# Add a context template dictionary in the view and tag the dictionary to the context
from django.shortcuts import render
from django.http import HttpResponse
def index(request_iter):
    dict_Var = {"Key1" : "The Template tag value is rendered with reference to key1"}
    return render(request_iter,'design.html',context=dict_Var)
#                                                                                             Create a Django Form
from django import forms
class Valueform(forms.Form):
    user = forms.CharField(max_length = 100)
#                                                Create a View for The Form
from django.shortcuts import render
from django.http import  HttpResponse
from Django_app1.forms import Valueform
def form_view(request_iter):
    form = Valueform()
    return  render(request_iter,'Form_Handeling.html', {"form": form})
# Formulate an HTML file for displaying the form
    {{ form.as_p}}
    {}% csrf_token %{}
#                          Tag the view in urls.py file
from django.contrib import admin
from django.conf.urls import url
from Django_app1 import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'formpage/',views.form_view,name='form'),
    url(r'admin/', admin.site.urls), ]
#                                                                           forms.py
#-*- coding: utf-8 -*-
from django import forms
class Valueform(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.SlugField()
    gender =  forms.BooleanField()
    Ip = forms.GenericIPAddressField()
    file =  forms.FileField()
    department = forms.ChoiceField(choices = (('1','CSE'),('2','IT'),('3','ECE'),('4','EEE')))
#                                                           All Form Fields Available in Django Forms
Boolean = forms.BooleanField(), forms.widgets.CheckboxInput()
Boolean = forms.NullBooleanField(), forms.widgets.NullBooleanSelect()
Text = forms.CharField(), forms.widgets.TextInput()
Text = forms.EmailField(), forms.widgets.EmailInput()
Text = forms.GenericIPAddressField(), forms.widgets.TextInput()
Text = forms.RegexField( regex="regular_expression"), forms.widgets.TextInput()
Text = forms.SlugField(), forms.widgets.TextInput()
Text = forms.URLField(), forms.widgets.URLInput()
Text = forms.UUIDField(), forms.widgets.TextInput()
Text = forms.ComboField(fields=[field_type1,field_type2]), forms.widgets.TextInput()
Text = forms.MultiValueField(fields=[field_type1, field_type1])
TextFiles = forms.FilePathField( path="directory"), forms.widgets.Select()
Files = forms.FileField(), forms.widgets.ClearableFileInput()
Files = forms.ImageField(), forms.widgets.ClearableFileInput()
DateTime = forms.DateField(), forms.widgets.DateInput()
Datetime = forms.TimeField(), forms.widgets.TextInput()
Datetime = forms.DateTimeField(), forms.widgets.DateTimeInput()
Datetime = forms.DurationField(), forms.widgets.TextInput()
Number = forms.IntegerField(), forms.widgets.NumberInput()
Number = forms.DecimalField(), forms.widgets.NumberInput()
Number = forms.FloatField(), forms.widgets.NumberInput()
#                                                        Processing Form Fields in View
from django.shortcuts import render
from django.http import  HttpResponse
from Django_app1.forms import Valueform
def form_view(request_iter):
    form = Valueform()
    if request_iter.method == "POST":
        value = Valueform(request_iter.POST)
    if value.is_valid():
        print("First Name: ",value.cleaned_data['first_name'])
        print("First Name: ",value.cleaned_data['last_name'])
        return  render(request_iter,'Form_Handeling.html', {"form": form})