from django.shortcuts import render, redirect
from django.views import View
import app.models

# Create your views here.
class User(View):
    def get(self, request):
        some_data = {"my_text": "hello world"}
        return render(request, 'main/users.html', some_data)

class Registration(View):
    def get(self, request):
        return render(request, 'main/users.html')

    def post(self, request):
        return render(request, 'main/users.html')


class Home(View):
    def get(self, request):
        return render(request, 'main/home.html')

    def post(self, request):
        user = request.session.get("user", None)

        if(user == None):
            loginuser = app.models.User.objects.filter(username=request.POST["username"])

            if(loginuser.count() == 0):
                return redirect('/registration')

            loginuser = loginuser.first()

            request.session["user"]=loginuser

            return redirect('/users')