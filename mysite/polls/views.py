from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # processing - database, cache, rendering HTML template, etc.
    return HttpResponse("Hello, world. You're at the polls index!!!!!!")