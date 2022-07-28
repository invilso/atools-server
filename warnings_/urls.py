from django.urls import path
from . import views

app_name = 'warnings_'

urlpatterns = [
    path('longpoll/', views.LPView.as_view(), name='longpoll'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('get/', views.GetView.as_view(), name='get'),
    path('send-to-all/', views.SendAll.as_view(), name='get'),
    # path('single/', views.CreateView.as_view(), name='single')
]