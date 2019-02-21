from django.contrib import admin
from django.urls import path

from rzeczy.views import MainPage, LoginPage, RegisterPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main_page'),
    path('login/', LoginPage.as_view(), name='login_page'),
    path('register/', RegisterPage.as_view(), name='register_page'),

]
