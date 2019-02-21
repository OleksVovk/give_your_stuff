from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import View, CreateView, FormView
from django.contrib.auth.models import User

# Create your views here.


from django.views import View


class MainPage(View):

    def get(self, request):
        return render(request, 'rzeczy/index.html')


class LoginPage(View):

    def get(self, request):
        return render(request, 'rzeczy/login.html')

    def post(self, request):
        pass


class RegisterPage(View):

    def get(self, request):
        return render(request, 'rzeczy/register.html')

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main_page')
        else:
            form = UserCreationForm()
        return render(request, 'rzeczy/register.html', {'form': form})






