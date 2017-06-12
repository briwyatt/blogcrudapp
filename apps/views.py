from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django CRUD BLOG</h1>
    <a href="/blog/">This is my Blog!!!!</a><br>
    """
    return HttpResponse(html)