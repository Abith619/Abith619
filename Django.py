#                                                                                              Django
from Django.forms import Valueform, fileform, emailform, responsecheckform
from Django_app1.forms import Valueform, fileform, emailform, responsecheckform
from django.core.mail import send_mail, EmailMessage
from django import responses
import responses
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.core.exceptions import ViewDoesNotExist
from Django_app1 import views
from Django_app1.forms import Valueform
from django.http import HttpResponse
from django import forms
import os
from Django.apps import views
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from . import views
from django.urls import path
from django.db import models

# settings.py file stores all the custom configurations such as database connection parameters, server details, global variables
# urls.py file has a list of all the custom URLs, 
# models = Database Tables, put into models.py, 
# SECURITY = csrf (Cross-Site Request Forgery). csrf is a random token that is generated every time we submit form data. This token is validated by the Django server on every Http POST Request it receives. 
#            If some hacker tries to attack, then this token becomes invalid and our application remains secure.
# Template extensions and Tags, 


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
#                                         Create your views here.
def home(request):
    return HttpResponse("Welcome")  # output to the screen
def setting_cookie(request):
    response = HttpResponse("We are setting a cookie")
    response.set_cookie('Learning', 'Django', 5)
    return response
def getting_cookie(request):
    first_test = request.COOKIES['Learning']
    return HttpResponse("Practice: " + first_test)
#                                                                                                          urls.py
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin',admin.site.urls ),
    path('', include('blog.urls')),
    path('', views.home, name='home'),
    path('setc', views.setting_cookie, name='setc'),
    path('getc', views.getting_cookie, name='getc')]
#                                                              URLconf:
from django.urls import path
from . import views
urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    ]
#                                                                Modify Cookie
#                                     view.py
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
    first_test = request.COOKIES['Stay']
    return HttpResponse("Always be: " + first_test)


#                                                         urls.py
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
    response = HttpResponse(
        "We are now finally deleting the cookie which is set")
    response.delete_cookie('Learning')
    return response


#                                urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('setc', views.setting_cookie, name='setc'),
    path('updc', views.updating_cookie, name='updc'),
    path('getc', views.getting_cookie, name='getc'),
    path('delc', views.deleting_cookie, name='delc')
]
#                                                                                                  Views
# Every view is callable and holds the capability to take a request and response
# For Declaring the view in Django we need to have an HTTP request and a response
# python manage.py runserver
def view1(request):
    return HttpResponse("Hello World")
#                                                        Tag the view in urls.py File
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'admin/', admin.site.urls), ]
# Reload the server using python manage.py runserver command and verify the webpage
#                                                                                    Create a Template Folder
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Template_DIR = os.path.join(BASE_DIR, 'Templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Template_DIR, ],
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
Template_DIR = os.path.join(BASE_DIR, 'Templates')
# Place an HTML file inside the Templates Folder = Django App1
#                                                                                                    Rendering
# Render the HTML File in views.py using() Method
# newly created HTML content to The render method combines a template with the context dictionary to return a HttpResponse object
def index(request_iter):
    return render(request_iter, 'design.html')
"""arguments	Description
Request      	This is used to generate a response. This is a mandatory argument.
Template Name	Name of the template used for this view. This is a mandatory argument.
Context	        A context is a variable name and variable value mapping maintained as a dictionary. In default, this is an empty dictionary. So if the key is passed the corresponding value from the dictionary can be retrieved and rendered. This is an optional argument.
content_type	MIME(Multipurpose Internet Mail Extensions) to be used. The default value is ‘text/html’. This is an optional argument.
Status	        The response code to be used. The default response code is 200.
Using	        This argument is used to represent the name of the template engine used for loading the template. This is an optional argument."""
# view Rendered from Template TAG {{ Key1 }}
# Add a context template dictionary in the view and tag the dictionary to the context
def index(request_iter):
    dict_Var = {
        "Key1": "The Template tag value is rendered with reference to key1"}
    return render(request_iter, 'design.html', context=dict_Var)
#                                                                                             Create a Django Form
class Valueform(forms.Form):
    user = forms.CharField(max_length=100)

#                                                Create a View for The Form
def form_view(request_iter):
    form = Valueform()
    return render(request_iter, 'Form_Handeling.html', {"form": form})
# Formulate an HTML file for displaying the form
    {{form.as_p}}
    {} % csrf_token % {}


#                          Tag the view in urls.py file
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'formpage/', views.form_view, name='form'),
    url(r'admin/', admin.site.urls), ]
#                                                                           forms.py
# -*- coding: utf-8 -*-


class Valueform(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.SlugField()
    gender = forms.BooleanField()
    Ip = forms.GenericIPAddressField()
    file = forms.FileField()
    department = forms.ChoiceField(
        choices=(('1', 'CSE'), ('2', 'IT'), ('3', 'ECE'), ('4', 'EEE')))


#                                                           All Form Fields Available in Django Forms
Boolean = forms.BooleanField(), forms.widgets.CheckboxInput()
Boolean = forms.NullBooleanField(), forms.widgets.NullBooleanSelect()
Text = forms.CharField(), forms.widgets.TextInput()
Text = forms.EmailField(), forms.widgets.EmailInput()
Text = forms.GenericIPAddressField(), forms.widgets.TextInput()
Text = forms.RegexField(regex="regular_expression"), forms.widgets.TextInput()
Text = forms.SlugField(), forms.widgets.TextInput()
Text = forms.URLField(), forms.widgets.URLInput()
Text = forms.UUIDField(), forms.widgets.TextInput()
Text = forms.ComboField(
    fields=[field_type1, field_type2]), forms.widgets.TextInput()
Text = forms.MultiValueField(fields=[field_type1, field_type1])
TextFiles = forms.FilePathField(path="directory"), forms.widgets.Select()
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


def form_view(request_iter):
    form = Valueform()
    if request_iter.method == "POST":
        value = Valueform(request_iter.POST)
    if value.is_valid():
        print("First Name: ", value.cleaned_data['first_name'])
        print("First Name: ", value.cleaned_data['last_name'])
        return render(request_iter, 'Form_Handeling.html', {"form": form})


#                                                                                              Response
# HttpResponse attribute	Reason
HttpResponse.content  # This attribute is used to denote the content of the message
# A string value representing the character encoding of the response.
HttpResponse.charset
HttpResponse.status_code  # This represents the response status code
HttpResponse.reason_phrase  # This represents the reason phrase of the response
# Mentions whether it is a streamed communication or not.
HttpResponse.streaming
# When the formulated response is closed then this value is assigned as true
HttpResponse.closed
#                                                                         Response Framework Methods
# Httpresponse attribute	                        Description
# The content page and content type is associated to the response object
HttpResponse.__init__(content=”, content_type=None, status=200, reason=None, charset=None)
# The value is associated with the header name
HttpResponse.__setitem__(header, value)
HttpResponse.__delitem__(header)  # Deletes a specific header
# Returns a value for the specific header name
HttpResponse.__getitem__(header)
# It returns either True or False based on a case-insensitive check for a header with the provided name.
HttpResponse.has_header(header)
# Allows to formulate a default header value
HttpResponse.setdefault(header, value)
# The response for a file-like object is created using this.
HttpResponse.write(content)
HttpResponse.flush()  # Allows the response object to get flushed
HttpResponse.tell()  # A file-like object will be created in the response
HttpResponse.getvalue()  # It is used to get the value of HttpResponse.content.
HttpResponse.readable()  # A stream-like object will be created in the response
HttpResponse.seekable()  # Makes the response object reachable

#                               choiceField() in the forms.py


def email_sending(response):
    email = emailform()
    if response.method == 'POST':
        email_id = response.POST['email']
        email_subject = response.POST['email_subject']
        email_message = response.POST['email_message']
        mail = send_mail(email_subject, email_message,
                         'testmysmtpconnection@gmail.com', [email_id], fail_silently=False)
        response = HttpResponse(mail)
        print("Content of the resposne: ", response.content)
        print("Charecterset of the response: ", response.charset)
        print("Status code of the response: ", response.status_code)
        print("Reason phrase of the response: ", response.reason_phrase)
        print("Reason close status: ", response.closed)
        return response
        return render(response, 'emailpage.html', {"email": email})


# response values from a file upload page is been verified


def file_upload(response):
    file = fileform()
    print(" File Values in File Dictionary:", response.FILES)
    if response.method == 'POST' and response.FILES['Uploaded_File']:
        uploaded_file = response.FILES['Uploaded_File'] fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_File_Size = 'Size of Uploaded file: ' + \
            str(uploaded_file.size)
        content_type_of_uploaded_file = 'Content type of uploaded file: ' + \
            str(uploaded_file.content_type)
        uploaded_file_name = 'Name of Uploaded file: ' + \
            str(uploaded_file.name)
        uploaded_file_url = fs.url(filename)
        print("uploaded file url", uploaded_file_url)
        messages.success(response, '!!! File upload successful !!!')
        messages.success(response, uploaded_File_Size)
        messages.success(response, uploaded_file_name)
        messages.success(response, content_type_of_uploaded_file)
        response = HttpResponse(filename)
        print("Content of the resposne: ", response.content)
        print("Charecterset of the response: ", response.charset)
        print("Status code of the response: ", response.status_code)
        print("Reason phrase of the response: ", response.reason_phrase)
        print("Reason close status: ", response.closed)
        return render(response, 'filehandeling.html', {"file": file})
        return render(response, 'filehandeling.html', {"file": file})


# Here the response values generated form a form page is been captured and verified


def formView(response_iter):
    form = Valueform()
    if response_iter.method == "POST":
        value = Valueform(response_iter.POST)
    if value.is_valid():
        first_name = value.cleaned_data['first_name']
        response = HttpResponse(first_name)
        print("Content of the resposne: ", response.content)
        print("Charecterset of the response: ", response.charset)
        print("Status code of the response: ", response.status_code)
        print("Reason phrase of the response: ", response.reason_phrase)
        print("Reason close status: ", response.closed)
    if response_iter.session.has_key(first_name):
        print(response_iter.session.items())
        return render(response_iter, 'Session.html')
    else:
        response_iter.session[first_name] = first_name
        return render(response_iter, 'Form_Handeling.html', {"form": form})


#                                                                            Methods to Catch Session Data
# Store Sessions onto the connected middleware database
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Django_app1',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#                                                          Store Sessions onto a cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Django_app1',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
#                                                                  Creating a Session in Django
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
CACHES = {
'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
    }
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Django_app1',
    ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
#                           Create a forms.py file in the application
from django import forms
class Valueform(forms.Form):
    user = forms.CharField(max_length = 100)
    last_name = forms.SlugField()
#                                              Create a view for the form
from django.shortcuts import render
from django.http import  HttpResponse
from Django_app1.forms import Valueform
def formView(request_iter):
    form = Valueform()
    if request_iter.method == "POST":
        value = Valueform(request_iter.POST)
    if value.is_valid():
        first_name = value.cleaned_data['first_name'] if request_iter.session.has_key(first_name):
        print(request_iter.session.items())
        return render(request_iter, 'Session.html' )
    else:
        request_iter.session[first_name] = first_name
        return render(request_iter, 'Form_Handeling.html', {"form":form})
        return render(request_iter, 'Form_Handeling.html', {"form":form})
#                                                         Formulate a HTML file for displaying the form
{{ form.as_p }} #Here “as_p” is used for better designing of the form elements.
{}% csrf_token %{}} # line is used for attesting the internal security verification
#                                                        Tag the view in urls.py file
from django.contrib import admin
from django.conf.urls import url
from Django_app1 import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'formpage/',views.form_view,name='form'),
    url(r'admin/', admin.site.urls),
    ]
#                                                                                        Ensure django.contrib.staticfiles
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'Django_app1'
    ]
STATIC_URL = '/static/'  # Ensure static url
#                                                       Ensure STATICFILES_DIRS or STATIC_ROOT
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # SETTINGS.py
#                                                                                                     EMAIL HANDELING 
"""EMAIL_HOST − SMTP server.
EMAIL_HOST_USER − SMTP server login credentials.
EMAIL_HOST_PASSWORD − SMTP server password credentials
EMAIL_PORT − port of SMTP server.
EMAIL_USE_TLS or _SSL − True if secure connection."""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testmysmtpconnection@gmail.com'
EMAIL_HOST_PASSWORD =  '*********'
EMAIL_USE_TLS = True
"""send_mail()
send_mass_mail()
mail_admins()
mail_managers()"""
send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None,connection=None, html_message=None)
send_mass_mail(datatuple, fail_silently=False, auth_user=None, auth_password=None, connection=None)
mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
mail_managers(subject, message, fail_silently=False, connection=None, html_message=None)
send_mail(
    'Subject',
    'Message.',
    'from_email@example.com',
    ['end_email1@example.com', 'end-email2@example.com'],
    )
# Creating a                                                     temporary smptp server within the system for debugging purpose
python -m smtpd -n -c DebuggingServer 127.0.0.1:8001
# email is captured in the temporary smtp server, the server is set up to hear at port 8001.
# Also the django server localhost id (127.0.0.1) is set as host name here, Make the email configurations in SETTINGS.py file
#                                                                                                           views.py
def email_sending(request):
    email = emailform()
    if request.method == 'POST':
        email_id =  request.POST['email']
        email_subject =  request.POST['email_subject']
        email_message =  request.POST['email_message']
        res = send_mail(email_subject,email_message,'testmysmtpconnection@gmail.com',[email_id],fail_silently = False)
        return HttpResponse('%s'%res)
        return render(request, 'emailpage.html',{"email":email})
#                                                                                                          Forms.py
from django import forms
class emailform(forms.Form):
    email = forms.EmailField()
    email_subject =  forms.CharField()
    email_message =  forms.CharField(max_length = 2000)
# the email is triggered using a valid mail account
#---------- EMAIL HANDELING ----------# Settigs.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testmysmtpconnection@gmail.com'
EMAIL_HOST_PASSWORD =  '*********'
EMAIL_USE_TLS = True
#                                                                                                      Form Validations
# CharField, EmailField, BooleanField, DateField, DecimalField, ChoiceField
#                                                                                 forms.py
class MyForm(forms.Form):
    Name=forms.CharField()
    email=forms.EmailField(label='Email')
    Gender=forms.ChoiceField(choices=[(' ','Choose'),('M','Male'),('F','Female')])
    Description=forms.CharField(widget=forms.Textarea,required=False)
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper=FormHelper
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
        'Name','email','Gender','Description',
        Submit('submit','Submit',css_class='btn-success')
        )
#                                                                              views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import MyForm
# Create your views here.
def first_form(request):
    if request.method=='POST':
        form=MyForm(request.POST)
    if form.is_valid():
        Name=form.cleaned_data['name']
        Email=form.cleaned_data['email']
        Gender=form.cleaned_data['gender']
        Description=form.cleaned_data['description']
        print(Name,Gender)
        form=MyForm()
        return render(request,'form.html',{'form':form})
#                                                                              Urls.py
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('first_form',views.first_form,name='first_form'),
    ]
# Urls.py: Project level
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('',include('Third.urls')),
    path('admin/', admin.site.urls),
    ]
#                                                                            Settings.py 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Third',
    'crispy_forms'
    ]
#                                                                                                     Django Static Files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
body {
    font-family: "Comic Sans MS", cursive, sans-serif;
    font-size: 36px;
    letter-spacing: 2px;
    word-spacing: 1.8px;
    color: #02071C;
    font-weight: 700;
    text-decoration: none;
    font-style: normal;
    font-variant: normal;
    text-transform: capitalize;
    }
h1 {
    font-family: "Comic Sans MS", cursive, sans-serif;
    font-size: 34px;
    letter-spacing: 2px;
    word-spacing: 1.8px;
    color: #02071C;
    font-weight: 650;
    text-decoration: none;
    font-style: normal;
    font-variant: normal;
    text-transform: capitalize;
    }
h2 {
    font-family: "Comic Sans MS", cursive, sans-serif;
    font-size: 32px;
    letter-spacing: 1px;
    word-spacing: 2.0px;
    color: #02071C;
    font-weight: 600;
    text-decoration: none;
    font-style: normal;
    font-variant: normal;
    text-transform: capitalize;
    }
h3 {
    font-family: "Comic Sans MS", cursive, sans-serif;
    font-size: 30px;
    letter-spacing: 1px;
    word-spacing: 2.1px;
    color: #02071C;
    font-weight: 400;
    text-decoration: none;
    font-style: normal;
    font-variant: normal;
    text-transform: capitalize;
    }
#                                                                             css file:
@import url(fonts.css);
body {
    margin: 0;
    padding: 0;
    font-size: 45px;
    font-family: "Roboto","Lucida Grande","DejaVu Sans","Bitstream Vera Sans",Verdana,Arial,sans-serif;
    color: grey;
    background: #fff;
    }
a:link, a:visited {
    color: #447e9b;
    text-decoration: none;
    }
a:focus, a:hover {
    color: #036;
    }
a:focus {
    text-decoration: underline;
    }
a img {
    border: none;
    }
a.section:link, a.section:visited {
    color: #fff;
    text-decoration: none;
    }
a.section:focus, a.section:hover {
    text-decoration: underline;
    }
/* GLOBAL DEFAULTS */
p, ol, ul, dl {
    margin:.2em 0.8em 0;
    }
p {
    padding: 0;
    line-height: 140%;
    }
h1,h2,h3,h4,h5 {
    font-weight: bold;
    }
h1 {
    margin: 0 0 20px;
    font-weight: 300;
    font-size: 20px;
    color: #666;
    }
h2 {
    font-size: 16px;
    margin: 1em 0.5em 0;
    }
h2.subhead {
    font-weight: normal;
    margin-top: 0;
    }
h3 {
    font-size: 14px;
    margin:.8em 0.3em 0;
    color: #666;
    font-weight: bold;
    }
h4 {
    font-size: 12px;
    margin: 1em 0.8em 0;
    padding-bottom: 3px;
    }
h5 {
    font-size: 10px;
    margin: 1.5em 0.5em 0;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
    }
ul li {
    list-style-type: square;
    padding: 1px 0;
    }
li ul {
    margin-bottom: 0;
    }
li, dt, dd {
    font-size: 13px;
    line-height: 20px;
    }
dt {
    font-weight: bold;
    margin-top: 4px;
    }
dd {
    margin-left: 0;
    }
form {
    margin: 0;
    padding: 0;
    }
fieldset {
    margin: 0;
    padding: 0;
    border: none;
    border-top: 1px solid #eee;
    }
blockquote {
    font-size: 11px;
    color: #777;
    margin-left: 2px;
    padding-left: 10px;
    border-left: 5px solid #ddd;
    }
code, pre {
    font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
    color: #666;
    font-size: 12px;
    }
pre.literal-block {
    margin: 10px;
    background: #eee;
    padding: 6px 8px;
    }
code strong {
    color: #930;
    }