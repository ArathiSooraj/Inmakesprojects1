from.import views
from django.urls import path

urlpatterns=[

    path('',views.calculator,name='calculator'),
    path('add/',views.addition,name='addition'),
]