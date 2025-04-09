from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_food_items, name='fooditem_list'),
    path('food/<int:pk>/', views.food_item_detail, name='fooditem_detail'),
    path('create/', views.food_item_create, name='fooditem_create'),
    path('update/<int:pk>/', views.food_item_update, name='fooditem_update'),
    path('delete/<int:pk>/', views.food_item_delete, name='fooditem_delete'),
]