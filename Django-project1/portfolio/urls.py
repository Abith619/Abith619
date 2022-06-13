from django.urls import path
from portfolio import views

app_name="portfolio"
urlpatterns = [
    path('home/',views.home,name="home"),
    path('show/',views.show,name="show"),
    path('edit/<int:pk>', views.edit,name="edit"),
    path('delete/<int:pk>',views.destroy,name="delete"),
    path('form/',views.normalform,name="form")
]