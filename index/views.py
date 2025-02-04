from django.shortcuts   import render, redirect
from django.db          import IntegrityError
from django.shortcuts   import render
from django.http import HttpResponse

def hello(request):
    return render(request, "index.html")