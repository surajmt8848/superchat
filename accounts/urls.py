
from django.contrib import admin
from django.urls import path, include

from accounts.views import (
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('register', register_view, name="register"),
    path('login', logout_view, name="login"),
    path('logout', logout_view, name="logout")


]
