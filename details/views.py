from django.shortcuts import render
from details.models import menu
# Create your views here.
def func(request):
    obj=menu.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        no=request.POST.get('no')
        res=menu(name=name,number=no)
        res.save()
        obj=menu.objects.all()
        return render(request,"index.html",{'res':res})
    return render(request,"index.html",{'res':obj})
def func2(request):
    result=menu.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        num=request.POST.get('no')
        obj=request.POST.get(name=name)
        obj.number=num
        obj.save()
        return render(request,"form.html",{'res':obj})
    return render(request,"form.html",{'res':result})
def func3(request):
    result=menu.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        num=request.POST.get('no')
        obj=request.POST.get(name=name)
        obj.number=num
        obj.save()
        obj.delete()
        return render(request,"form.html",{'res':obj})
    return render(request,"form.html",{'res':result})
