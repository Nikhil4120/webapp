from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Category,SubCategory,Product


# Create your views here.
def productDetails(request,pid):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    product=Product.objects.filter(product_id = pid).get()
    product.quantity = [0] * product.quantity
    context = {'category': category, 'subcategory': subcategory, 'product':product}
    return render(request,"product-detail.html",context)

def productlist(request,cid,sid):
    category= Category.objects.all()
    subcategory = SubCategory.objects.all()
    product = Product.objects.filter(category_id=cid ,subcategory_id=sid)
    categoryName= Category.objects.filter(category_id=cid).get().category_name
    subcategoryName = SubCategory.objects.filter(subcategory_id=sid).get().subcategory_name
    context = {'category': category, 'subcategory': subcategory, 'product': product, 'categoryName':categoryName, 'subcategoryName':subcategoryName}
    return render(request, "product.html", context)