from django.urls import path
from reg import views

urlpatterns=[
    path("",views.index,name='index'),
    path('forms',views.forming,name="form"),
    path('posted',views.posted,name='posted'),
]