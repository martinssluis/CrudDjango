from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_modelform, name='form_modelform'), #* this path is used to show the route to the HTML page where the page content is located
    path('clients/', views.client_list, name='client_list'),
    path('clients/edit/<int:id>/', views.editar_cliente, name='editar_cliente'),  
    path('clients/delete/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
]
