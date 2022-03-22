from django.contrib import admin
from django.urls import path, include
from wasapp import views

urlpatterns = [
    path('', views.course, name='course'),
    path('admin/', admin.site.urls),
]
