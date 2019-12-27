from django.contrib import admin
from django.urls import path
from oooo import views
from oooo.views import aaa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.aaa,name='aaa'),
]