from django.urls import path

from . import views

urlpatterns = [
    path('', views.organization_alt_view),  # api/organization/
    path('<int:pk>/', views.organization_alt_view),  # api/organization/#
    path('<int:pk>/update/', views.organization_update_view),  # api/organization/#/update/
    path('<int:pk>/destroy/', views.organization_delete_view),  # api/organization/#/destroy/
    path('group/', views.org_group_list_create_view),  # api/organization/group
    path('group/<int:pk>/', views.org_group_detail_view),  # api/organization/group/#
    path('group/<int:pk>/update/', views.org_group_update_view),  # api/organization/group/#/update
    path('group/<int:pk>/destroy/', views.org_group_delete_view),  # api/organization/group/#/destroy
]
