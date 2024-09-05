from django.shortcuts import render
from .models import *
from .forms import ItemInfoForms 

# Create your views here.
def home(request):
    form = ItemInfoForms()
    if request.method=="POST":
        form = ItemInfoForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    data = ItemInfo.objects.all()
    return render(request,'home.html',{'form':form,'data':data})

def showdata(request):
    data = ItemInfo.objects.all()
    return render(request,'dashbord.html',{'data':data})
