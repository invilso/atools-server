from django.urls import path
from . import views

app_name = 'admins'

urlpatterns = [
    path('update/<str:field>', views.UpdateView.as_view(), name='update'),
    path('get/', views.GetView.as_view(), name='get'),
]