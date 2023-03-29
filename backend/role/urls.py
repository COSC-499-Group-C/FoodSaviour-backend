from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_alt_view),
    path('<int:pk>/', views.role_alt_view),
    path('<int:pk>/update/', views.role_update_view),
    path('<int:pk>/destroy/', views.role_delete_view),
    path('group/', views.role_group_list_create_view),
    path('group/<int:pk>/', views.role_group_detail_view),
    path('group/<int:pk>/update/', views.role_group_update_view),
    path('group/<int:pk>/destroy/', views.role_group_delete_view),
]
