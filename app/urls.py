from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('adddata/', adddata, name='adddata'),
    path('showdata/', showdata, name='showdata'),

]