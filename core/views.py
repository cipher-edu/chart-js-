from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    post = Company.objects.all()
    context = {
        'post':post
    }
    return render(request, 'index.html',context)