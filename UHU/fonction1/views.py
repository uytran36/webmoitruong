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
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Tree"]
    data = mycol.find({})
    
    list_item = []
    for item in data:
        temp = request.POST.get(item['name'], 'false')
        if temp == 'on':
            list_item.append(item)
    
  
    list_bed = []
    for item in list_item:
        bed = []
        bed.append(item)

        def check(tree1, tree2):
            flag_soil = False
            flag_water = False
            flag_height = True

            if(tree1['soil_type'] == tree2['soil_type'] and tree1['name'] != tree2['name']):
                flag_soil = True

            temp = tree1['water'].split(' ')
            tree1_water = temp[0]

            temp2 = tree2['water'].split(' ')
            tree2_water = temp2[0]
            
            if(abs(float(tree1_water) - float(tree2_water)) < 200):
                flag_water = True
            
            if(abs(float(tree1['height'][:-1]) - float(tree2['height'][:-1])) < 5):
                flag_height = False
            
            if(flag_height == True and flag_soil == True and flag_water == True):
                return True
            else:
                return False

        for item2 in list_item:
            if(check(item, item2)):
                bed.append(item2)

        if len(bed) == 1:
            list_bed.append([item])
        else: 
            list_bed.append(bed)
    
    list_id = []
    for item in list_bed:
        _id = []
        for j in range(len(item)):
            _id.append(int(item[j]['_id']))
        _id.sort()
        list_id.append(_id)

    for i in range(len(list_id) - 1):
        for j in range(i + 1, len(list_id)):
            if(list_id[i] == list_id[j]):
                del list_id[j]
                del list_bed[j]
                break
    return render(request, 'pages/result.html', {'list_bed':list_bed})

# def plus(request):
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     mydb = myclient["UHU"]
#     mycol = mydb["Tree"]
#     data = mycol.find({})
    
#     list_item = []
#     for item in data:
#         temp = request.POST()
        
#     area = float(request.POST['area']) * 10000

#     return render(request, 'pages/result1.html', {'list_item':list_item, 'list_tree':list_tree, 'cost':cost})