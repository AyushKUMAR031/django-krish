from django.shortcuts import render, redirect
from django.http import HttpResponse

def Me(request):
    return render(request, 'land.html')