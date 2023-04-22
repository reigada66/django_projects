
from django.shortcuts import render
from django.contrib import messages


def inicio(request):
    return render(request, 'principal/index.html')

