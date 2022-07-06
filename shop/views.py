from email.mime import image
from email.policy import default
import json
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from django.utils.html import strip_tags

from django.conf import settings
from turtle import update
from unicodedata import category, name
from urllib import response
from datetime import datetime
from django.shortcuts import redirect, render
import functools


from django.http import Http404, HttpResponse
from .models import Product,Contact,Orders,OrderUpdate,promocode
# Create your views here.



def index(request):
    products=Product.objects.all()
    revpr=reversed(list(products))
    
    params={'no':len(products),'products':products,'revpr':revpr}
    return render(request,'index.html',params)

def searchmatch(query,item):
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
       
        return True
    else :
        
        return False

def catmatch(query,item):
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
       
        return True
    else :
        
        return False


def search(request):
    query=request.GET.get("search")
    query=query.lower()
    
    products=Product.objects.all()
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchmatch(query,item)]
       
       
        if len(prod)!=0:
            s=0
            for j in prod:
                allprods.append(prod[s])
                s=s+1
        


    params={'no':len(allprods),'products':allprods,'query':query,'all':products,}
    return render(request,'search.html',params)


def productview(request,pid):
    
    product=Product.objects.filter(id=pid)
    # print(product)
    return render(request,'productview.html',{'product':product[0]})

def checkout(request):
    promos=promocode.objects.all()
    promoc={'promos':promos,'no':8}


    if request.method=="POST":
        fname=request.POST.get('fname',"")
        phone=request.POST.get('phone',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        state=request.POST.get('state',"")
        zipc=request.POST.get('zipc',"")
        lname=request.POST.get('lname',"")
        item_Json=request.POST.get('itemJson',"")
        amount=request.POST.get('amount',"")
        
        
        # print(name,phone,email,query)
        Order=Orders(fname=fname,lname=lname,phone=phone,email=email,state=state,zipc=zipc,address=address,item_Json=item_Json,amount=amount)
        Order.save()
        id=Order.order_id
        oid=int(id)
        update= OrderUpdate(order_id= Order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        
        
        az=[]
        az.append(email)
        
        # send_mail("Order Details",f"Thanks for Shopping. Your order id is {id}.Use it to track and get details of your order.", settings.DEFAULT_FROM_EMAIL,az)

        html_content=render_to_string("image.html",{'title':'testing','content':id})
        textc=strip_tags(html_content)

        emai=EmailMultiAlternatives('Order dertails',textc, settings.DEFAULT_FROM_EMAIL,az)
        emai.attach_alternative(html_content,'text/html')
        emai.send()
        
        return redirect(f'/about1/{id}')
        # return render(request,'checkout.html',{'thank':thank,'id':id})
        # return render(request,'ck.html',{'thank':thank,'id':id})
    
    return render(request,'ck.html',promoc)


def about1(request,id):
    thank=True
    
    return render(request,'checkout.html',{'thank':thank,'id':id})
    
def about(request):
    return render(request,'checkout.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name',"")
        phone=request.POST.get('phone',"")
        email=request.POST.get('email',"")
        query=request.POST.get('query',"")
        # print(name,phone,email,query)
        contact=Contact(name=name,phone=phone,email=email,query=query)
        contact.save()
        mission=True
        return render(request,'contact.html',{'mission':mission})

    return render(request,'contact.html',)


def track(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        # print(orderId,email)
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
           
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                
                for item in update:
                    
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].item_Json], default=str)
                    
                return HttpResponse(response)
            else:
                return HttpResponse('{}'
                )
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'track.html')


    
