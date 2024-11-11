from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('criar/', views.criar_post, name='criar_post'),

]