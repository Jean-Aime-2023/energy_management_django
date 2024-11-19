from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),  # Correct function name
    path('add-consumption/', views.add_consumption, name='add_consumption'),
    path('consumption/', views.consumption_list, name='consumption'),
    path('update-consumption/<int:pk>/', views.update_consumption, name='update_consumption'),
    path('delete-consumption/<int:pk>/', views.delete_consumption, name='delete_consumption'),
    path('add-saving/', views.add_saving, name='add_saving'),
    path('saving/', views.savings_list, name='saving'),
    path('update-saving/<int:pk>/', views.update_saving, name='update_saving'),
    path('delete-saving/<int:pk>/', views.delete_saving, name='delete_saving'),
]
