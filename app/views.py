from django.shortcuts import render
from django.views import View


class User(View):
    def get(self, request):
        some_data = {"my_text": "hello world"}
        return render(request, 'main/users.html', some_data)


class Registration(View):
    def get(self, request):
        a = User()
        return render(request, 'main/users.html')

    def post(self, request):
        a = User()
        a.username = str(request.POST["uName"])
        a.password = str(request.POST["pWord"])
        a.save()
        return render(request, 'main/users.html')
