from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio (request):
    return render(request, r'Paginas\inicio.html')
