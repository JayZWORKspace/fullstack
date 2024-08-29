from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response


from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world! This is the index page.")