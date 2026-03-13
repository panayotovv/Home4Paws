from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

import User
from Dog.views import login_view, signup_view
from User.views import ProfileView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signin/', login_view, name='signin'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("index")),
        name="logout",
    ),
    path("create-payment-intent/", User.views.create_payment_intent, name="create_payment_intent"),
]