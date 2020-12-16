from django.shortcuts import render
import pymongo

# Create your views here.
def fonction2(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Tree"]
    data = mycol.find({})
    
    return render(request, 'pages/fonction2.html', {'data':data})

def result1(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Tree"]
    data = mycol.find({})
    
    list_item = []
    for item in data:
        temp = request.POST.get(item['name'], 'false')
        if temp == 'on':
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
    return render(request, 'pages/result1.html', {'list_item':list_item, 'list_tree':list_tree, 'cost':cost})
