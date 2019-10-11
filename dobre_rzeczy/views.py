from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')



class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class AddFormView(View):
    def get(self, request):
        return render(request, 'form.html')