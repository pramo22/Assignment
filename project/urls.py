from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create_data/',views.create_data, name="create"),
    path('view/<int:pk>/', views.view_data,name="view"),
    path('update/<int:pk>/',views.update_data, name="update"),
    path('delete_data/<int:pk>/',views.delete_data,name="delete")
]
