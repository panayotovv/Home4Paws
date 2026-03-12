from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

import User
from Dog.views import IndexView
from User.views import ProfileView

urlpatterns = [
    path('signup/', IndexView.as_view(), name='signup'),
    path('signin/', IndexView.as_view(), name='signin'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("index")),
        name="logout",
    ),
    path("create-payment-intent/", User.views.create_payment_intent, name="create_payment_intent"),
]