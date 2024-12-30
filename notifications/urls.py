from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_list, name='notifications'),
    path('mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark_notification_as_read'),
    path('mark-all-as-read/', views.mark_all_as_read, name='mark_all_notifications_as_read'),
    path('count/', views.get_notification_count, name='notification_count'),
]