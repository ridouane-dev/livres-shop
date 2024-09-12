from django.urls import path
from shop.views import index, checkout , confirmation

urlpatterns = [
    path('', index , name='home'),
    path('checkout' , checkout, name="checkout"),
    path('confirmation' , confirmation ,name="confirmation"),
]