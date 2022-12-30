from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', prod_list, name='prod_list'),
]