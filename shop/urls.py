from urllib import request
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('contact', views.contact,name="contact"),
   
    path('Checkout', views.checkout,name="checkout"),
    path('track', views.track,name="track"),
    path('about1/<int:id>', views.about1,name="about1",),
    path('about', views.about,name="about",),
    path('search', views.search,name="search"),
    path('track/', views.track,name="track"),
 
    path('products/<int:pid>', views.productview,name="productview"),
]
