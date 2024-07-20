from django.shortcuts import render,get_object_or_404
from .models import Items

def details(request,pk):
      item=get_object_or_404(Items,pk=pk)
      return render(request,'item/detail.html',{
            'item':item
      })
