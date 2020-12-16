from django.shortcuts import render
import pymongo

# Create your views here.
def fonction3(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Donator"]
    data = mycol.find({})

    list_donators = []
    sum_tree = 0
    for item in data:
        item['number_tree'] = int(item['number_tree'])
        list_donators.append(item)
        sum_tree += item['number_tree']
    
    list_donators = sorted(list_donators, key = lambda i: i['number_tree'], reverse=True)
    
    sum_tree = '{:,.0f}'.format(sum_tree)
    return render(request, 'pages/fonction3.html', {'list_donators':list_donators, 'sum_tree': sum_tree})

def thanks(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UHU"]
    mycol = mydb["Donator"]

    donator = {}
    
    number_tree = request.POST['number-tree']
    donator['number_tree'] = number_tree

    name = request.POST['name']
    donator['name'] = name

    email = request.POST['email']
    donator['email'] = email

    phone = request.POST['mobile-phone']
    donator['mobile_phone'] = phone

    message = request.POST['message']
    donator['message'] = message

    expiration_date = request.POST['expiration-date']
    donator['expiration_date'] = expiration_date

    security_code = request.POST['security-code']
    donator['security_code'] = security_code

    postal_code = request.POST['postal-code']
    donator['postal_code'] = postal_code

    country = request.POST['country']
    donator['country'] = country

    temp = mycol.insert_one(donator)
    
    return render(request, 'pages/thanks.html')
