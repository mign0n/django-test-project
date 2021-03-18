from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h3>Functionality is coming soon.</h3>')
