from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import Donation, Institution, User, Category


def bags_counter():
    return Donation.objects.filter().count()


def supported_org_counter():
    return Institution.objects.filter().count()


class IndexView(View):
    def get(self, request):
        fundations = Institution.objects.filter(type="fundacja")
        nonGovOrg = Institution.objects.filter(type="organizacja pozarządowa")
        localCollect = Institution.objects.filter(type="zbiórka lokalna")

        ctx = {"fundations": fundations, "nonGovOrg": nonGovOrg, "localCollect": localCollect, "bags_counter": bags_counter(), "supported_org_counter": supported_org_counter()}
        return render(request, "index.html", ctx)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        mail = request.POST.get("email")
        if mail in User.objects.values_list('username', flat=True):
            return HttpResponse("Konto z podanym adresem email już isnieje! " + "<meta http-equiv=\"refresh\" content=\"2\" />")
        else:
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            passwordvalue1 = request.POST.get("password")
            passwordvalue2 = request.POST.get("password2")
            if passwordvalue1 != passwordvalue2:
                return HttpResponse("Hasła się nie zgadzają! " + "<meta http-equiv=\"refresh\" content=\"2\" />")
            else:
                u = User()
                u.username = mail
                u.first_name = name
                u.last_name = surname
                u.set_password(passwordvalue1)
                u.save()
                http = "Dziękujemy! Proces rejestracji został pomyślnie zakończony. " + "<meta http-equiv=\"refresh\" content=\"3\;url=index.html/\" />"
                user = authenticate(username=mail, password=passwordvalue1)
                login(request, user)
                return redirect(http)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AddFormView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/login")
        else:
            categories = Category.objects.all()
            institusions = Institution.objects.all()
            return render(request, 'form.html', {"categories": categories, "institutions": institusions})
