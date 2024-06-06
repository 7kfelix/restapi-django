from django.urls import path
from .views import ItemCreate, ItemUpDestroy

urlpatterns = [
    path('items/', ItemCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>', ItemUpDestroy.as_view(), name='item-retrieve-update-destroy'),
]