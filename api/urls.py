from django.urls import path
from . import views

urlpatterns = [
    path('api', views.InfoViews.as_view(), name='info-view'),

]