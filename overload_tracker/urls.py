from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('logout/', views.test_logout),
    path('select-split-dropdown/', views.select_split_from_dropdown, name = 'select_split_from_dropdown'),

]

