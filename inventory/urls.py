from django.urls import path, include
from .views import (
    MainPageView,
    InventoryDetailView,
    UpdateHistoryDetailView,
    EditItemView,
    AddItemView,
    ItemDetailView,
    NotificationDetailView,
    ItemDeleteView
)
from . import views
from reporting import views as reporting_views

urlpatterns = [
    path('', MainPageView.as_view(), name = 'home'),
    path('detail/', InventoryDetailView.as_view(), name = 'detail-view'),
    path('detail/<int:pk>/update/', EditItemView.as_view(), name = 'edit-item-view'),
    path('detail/<int:pk>/delete/', ItemDeleteView.as_view(), name = 'item-delete-view'),
    path('detail/<int:pk>/view/', ItemDetailView.as_view(), name = 'item-detail-view'),
    path('detail/add_new_item/', AddItemView.as_view(), name = 'add-item-view'),
    path('history_detail/', UpdateHistoryDetailView.as_view(), name = 'history-detail-view'),
    path('notifications/', NotificationDetailView.as_view(), name = 'notification-detail-view'),
    path('reporting', include('reporting.urls'))
]
