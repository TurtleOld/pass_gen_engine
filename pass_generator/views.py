from django.shortcuts import render, redirect


# Create your views here.

def func(request):
    return render(request, 'pass_generator/index.html')