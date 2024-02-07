from django.urls import path
from stuapp import views

urlpatterns = [
    path('addstu', views.addstu),               #Create
    path('dashboard', views.dashboard),         #Read
    path('update/<stuid>', views.updatestu),    #Update
    path('delete/<stuid>', views.deletestu),    #Delete
]