from django.urls import include, path
from . import views
from django.contrib import admin



admin.site.site_header = "Avid hive Smarthomes & Security Solutions " 


urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('services',views.services, name='services'),
    path('signup', views.signup, name='signup'),
    path('products',views.products, name='products'),
    path('account',views.account,name='account'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('cart',views.cart,name='cart'),
    path('shipping',views.shipping,name='shipping'),
    path('successpage',views.successpage,name='successpage'),
    path('ordersuccesspage',views.ordersuccesspage,name='ordersuccesspage'),
    path('accsuccesspage',views.accsuccesspage,name='accsuccesspage'),
    path('accfailpage',views.accfailpage,name='accfailpage'),
    


]    
    
