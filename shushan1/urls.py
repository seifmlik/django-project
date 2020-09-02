from django.urls import path

from shushan1.views import index
from .views import getbarile,get,get2,prel,prelback,rabbocco

urlpatterns = [
    path('',index),
    path('page/<str:nome>',getbarile,name='getbarile'),
    path('page1/<str:nome>',get,name='get'),
    path('p/<str:nome>',get2,name='get2'),
    path('page2/<str:nome>',prel,name='prel'),
    path('pr/<str:nome>',prelback,name='prelback'),
    path('pa/<str:nome>',rabbocco,name='rabbocco'),
]
