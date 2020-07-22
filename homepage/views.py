from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
	p = Project.objects.all()
	return render(request,'homepage/index.html',{'projects':p})
