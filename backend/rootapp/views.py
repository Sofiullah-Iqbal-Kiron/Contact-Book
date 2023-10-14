from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'rootapp/index.html')


class SignUp(View):
    def get(self, request):
        return render(request, 'rootapp/sign_up.html')

    def post(self, request):
        post_data = request.POST
        username = post_data['username']
        password = post_data['password']
        User.objects.create(username=username, password=password)
        return HttpResponse("User Created Successfuly.")


class SignIn(View):
    def get(self, request):
        return render(request, 'rootapp/sign_in.html')

    def post(self, request):
        pass


class SignOut(View):
    def get(self, request):
        logout(request)
