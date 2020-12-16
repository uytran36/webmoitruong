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

def plus(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Tree"]
    data = mycol.find({})
    
    list_item = []
    for item in data:
        temp = request.POST.get(item['name'])
        if(temp != None):
            list_item.append(item)

    area = float(request.POST['area']) * 10000
    
    list_tree = {}
    cost = 0

    sum_area = 0
    for item in list_item:
        list_tree[item['name']] = 0
        item_area = float(item['size'][:-1])
        sum_area += item_area

    if(len(list_tree) != 1):
        number_set = int(area//sum_area)
        remain1_area = area - sum_area*number_set + 0.0001
        
        list_double = {}

        for i in range(len(list_item) - 1):
            for j in range(i + 1, len(list_item)):
                temp = float(list_item[i]['size'][:-1]) + float(list_item[j]['size'][:-1])
                temp_key = (list_item[i]['name'], list_item[j]['name'])
                list_double[temp_key] = temp    

        list_double = {k: v for k, v in sorted(list_double.items(), key=lambda item: item[1])}
        sum_area2 = list(list_double.values())
        number_set2 = int(remain1_area//sum_area2[0])

        remain2_area = remain1_area - number_set2*sum_area2[0]

        temp = list(list_double.keys())
        for key in list_tree:
            number_last_tree = 0
            list_tree[key] += number_set
            for item in temp[0]:
                if(key == item):
                    list_tree[key] += number_set2
            
            for item in list_item:
                if(key == item['name']):
                    number_last_tree = int(remain2_area//float(item['size'][:-1]))
            list_tree[key] += number_last_tree

        for item in list_item:
            for key in list_tree:
                if(item['name'] == key):
                    temp = item['price'].split(' ')
                    price = int(temp[0])
                    cost += price * list_tree[key]
    else:
        for item in list_item:
            item_area = float(item['size'][:-1])
            number_tree = int(area//item_area)
            list_tree[item['name']] = number_tree
        
            temp = item['price'].split(' ')
            price = int(temp[0])
            cost += price * number_tree

    cost = '{:,.0f}'.format(cost)
    return render(request, 'pages/plus.html', {'list_item':list_item, 'list_tree':list_tree, 'cost':cost})