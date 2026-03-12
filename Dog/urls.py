from django.urls import path
from Dog.views import DogDetailView

urlpatterns = [
    path('<str:name>/', DogDetailView.as_view(), name='detail'),
]