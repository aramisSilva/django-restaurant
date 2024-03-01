from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_detail),
    #path('<str:last_name>/', views.employee_detail_with_filter)
]