from django.conf.urls import url
from Student import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^student$',views.StudentApi),
    url(r'^student/([0-9]+)$',views.StudentApi),

    url(r'^student/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)