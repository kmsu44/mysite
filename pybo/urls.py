from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Post_id>/', views.detail, name='detail'),
    
    path('create/', views.create, name="create"),
    path('cart/', views.cart, name="cart"),
]

