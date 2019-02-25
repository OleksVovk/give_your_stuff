from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.


from django.views import View

from .forms import LoginForm, RegisterForm


class MainPage(View):

    def get(self, request):
        return render(request, 'rzeczy/index.html')


class LoginPage(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'rzeczy/login.html', {'form': form})

    def post(self, request):
        form = LoginForm()
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if user.is_staff:
                    return redirect('/admin/')
                return render(request, 'rzeczy/form.html')

        return render(request, 'rzeczy/login.html')

    # def get(self, request):
    #     return render(request, 'rzeczy/login.html')
    #
    # def post(self, request):
    #     pass


class RegisterPage(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'rzeczy/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm()
        if form.is_valid():
            form.save()


        pass










