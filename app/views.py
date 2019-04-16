from django.shortcuts import render
from django.views import View

# Create your views here.
class User(View):
    def get(self, request):
        some_data = {"my_text": "hello world"}
        return render(request, 'main/users.html', some_data)