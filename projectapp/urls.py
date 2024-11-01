from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('main', views.main, name='main'),
    path('signin/', views.signin, name='signin' ),
    path('signup/', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('single-post', views.single_post, name='single-post'),
    path('signout', views.signout, name='signout'),
    path('dashboard', views.dashboard, name='dashboard'),



]