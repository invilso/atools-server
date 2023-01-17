from django.urls import path
from account.views import UserView, UsersView, RegistrUserView
# from .views import PaginatorView, StatsView

app_name = "account"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('api/commands', UsersView.as_view()),
    path('api/commands/<str:username>', UserView.as_view()),
    path('api/last', UserView.as_view()),
]