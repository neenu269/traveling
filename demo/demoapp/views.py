from django.shortcuts import render
from .models import place
from .models import place1
from django.http import HttpResponse
# Create your views here.
def demo(request):
    obj=place.objects.all()
    chart=place1.objects.all()

    return render(request,"index.html",{"replace":obj,"chart":chart})
# def about(request):
#     return render(request,"about.html")
# def details(request):
#     return HttpResponse("details")
# def content(request):
#     return HttpResponse("content")
# def credit(request):
#     return HttpResponse("credit")