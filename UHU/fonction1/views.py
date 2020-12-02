from django.shortcuts import render
from .models import Tree
# import pymongo
# from pymongo import MongoClient
# from .models import Post
# # Create your views here.
# def classification(request):
#    Data = {'Posts': Post.objects.all().order_by('-date')}
#    return render(request, 'blog/blog.html', Data)

#mongbodb
import pymongo

def fonction1(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Tree"]
    data = mycol.find({})
    return render(request, 'pages/fonction1.html', {'data':data})

def result(request):
    return render(request, 'pages/result.html')





#clear button
