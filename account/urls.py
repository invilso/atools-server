from django.urls import path
from account.views import UserView, UsersView, RegistrUserView, LoginUserView, UpdateOnline, UpdateSpectate, OnlineUsersView, UserActivateView, LPView, UserBlockView
# from .views import PaginatorView, StatsView

app_name = "account"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('api/users', UsersView.as_view()),
    path('api/users/online/', OnlineUsersView.as_view()),
    path('api/users/<str:username>', UserView.as_view()),
    path('api/activate-user', UserActivateView.as_view()),
    path('api/block-user', UserBlockView.as_view()),
    path('edit/<str:username>', UserView.as_view()),
    path('registration/', RegistrUserView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('update/spectate', UpdateSpectate.as_view(), name='upd_spectate'),
    path('update/online', UpdateOnline.as_view(), name='upd_online'),
    path('longpoll/unactivated', LPView.as_view(), name='lp_unactivated')
]