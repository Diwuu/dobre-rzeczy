from django.shortcuts import render
from django.views import View
from .models import Donation, Institution


def bags_counter():
    return Donation.objects.filter().count()


def supported_org_counter():
    return Institution.objects.filter().count()

class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {"bags_counter": bags_counter(), "supported_org_counter": supported_org_counter()})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class AddFormView(View):
    def get(self, request):
        return render(request, 'form.html')