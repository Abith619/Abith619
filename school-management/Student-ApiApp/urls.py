"""Pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ..Pro1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', views.SchoolView.as_view(), name='schools'),
    path('school/<int:school_id>/', views.SchoolDetailView.as_view(), name='school-detail'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student')
    path('', views.index, name='index'),
    path('polls/', ('polls.urls')),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-Create"),
]
