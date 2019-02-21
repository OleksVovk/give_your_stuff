from django.contrib import admin
from django.urls import path

from rzeczy.views import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main_page'),
]
