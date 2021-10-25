from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('contact.html',views.contact,name='contact'),
    path('product-detail.html',views.product_detail,name='product-detail'),
    path('wishlist.html',views.wishlist,name='wishlist'),
    path('cart.html',views.cart,name='cart'),
    path('my-account.html',views.myaccount,name='myaccount'),
    path('product-list.html',views.productlist,name='productlist'),
    path('login.html',views.login,name='login'),
    path('checkout.html',views.checkout,name='checkout'),
]