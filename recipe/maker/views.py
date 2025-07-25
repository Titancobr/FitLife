from django.shortcuts import render,redirect
from .models import *


def lister(request):
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter (receipe_name__icontains = request.GET.get('search'))
    queryset = Recipe.objects.all()
    context ={'receipe': queryset}
    return render(request,'mern.html',context)




def receipe(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_name')
        receipe_dis = data.get('receipe_dis')

        Recipe.objects.create(
            receipe_img= receipe_img,  
            receipe_name= receipe_name, 
            receipe_dis= receipe_dis,
         )
        return redirect('/home/')
    queryset = Recipe.objects.all()
    context ={'receipe': queryset}
    return render(request,'main.html',context)

def update_receipe(request,id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST" :
            data = request.POST
            
            receipe_img = request.FILES.get('receipe_img')
            receipe_name = data.get('receipe_name')
            receipe_dis = data.get('receipe_dis')

            queryset.receipe_name = receipe_name
            queryset.receipe_dis = receipe_dis
            if receipe_img:
                queryset.receipe_img = receipe_img
            queryset.save ( )
            return redirect('/home/')



    context ={'receipe': queryset}
    return render(request,'update.html',context)

def delete_receipe (request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/home/')

def home(request):
    return render(request,'home.html')
    