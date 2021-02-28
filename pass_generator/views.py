from django.shortcuts import render
import random
import string


# Create your views here.

def func(request):
    return render(request, 'pass_generator/index.html')


def pass_generator():
    random_pass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8)])
    return random_pass
