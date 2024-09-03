from django.shortcuts import render
from .models import ItemInfo
from .forms import ItemInfoForms 

# Create your views here.
def home(request):
    form = ItemInfoForms()
    if request.method=="POST":
        form = ItemInfoForms(request.POST,request.FIlES)
        if form.is_valid():
            form.save()

    data = ItemInfo.object.all()
    return render(request,'home.html',{'form':form,'data':data})
