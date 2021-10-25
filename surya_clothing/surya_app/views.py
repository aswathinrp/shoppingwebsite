from django.shortcuts import render
from . models import dress
# Create your views here.
def fun(request):

   return render(request,"index.html")

def contact(request):
   if request.method == 'POST':
      Your_Name = request.POST['Your Name ']
      Your_Email = request.POST['Your Email']
      Subject = request.POST['Subject']
      Message = request.POST['Message']

      return render(request, "contact.html",{Your_Name:'Your_Name'})

   else:
      return render(request,"contact.html")

def product_detail(request):

   return render(request,"product-detail.html")

def wishlist(request):

   return render(request,"wishlist.html")

def cart(request):
    return render(request,"cart.html")

def myaccount(request):
   return render(request,'my-account.html')

def productlist(request):
   return render(request,'product-list.html')

def login(request):
   return render(request,'login.html')

def checkout(request):
   return render(request,'checkout.html')