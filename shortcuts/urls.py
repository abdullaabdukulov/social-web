from django.urls import path
from . import views

app_name = 'shortcuts'

urlpatterns = [
    path('create/', views.short_create, name='create'),
]
