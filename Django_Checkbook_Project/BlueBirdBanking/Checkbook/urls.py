from django.urls import path
from . import views

urlpatterns = [
    #sets the url path to home page index.html
    path('', views.home, name='index'),

    #sets the url path to create new account page createnewaccount.html
    path('create/', views.create_account, name='create'),

    #sets the url path tobalance sheet page balancehsheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),

    #sets url path to add new trancsation page add new transcation.html
    path('transaction/', views.transaction, name='transaction')
]