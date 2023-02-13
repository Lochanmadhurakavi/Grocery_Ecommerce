from django.urls import path
from . import views

app_name='item'

urlpatterns = [
    path('', views.index, name='category'),
    path('<int:pk>/', views.item_list, name='item_list'),
    path('add-item/', views.add_item, name='add_item'),
    path('category/add-category/', views.add_category, name='add_category'),
]