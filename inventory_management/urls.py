"""
inventory_management URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authViews
from inventory import views as inventory_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('reporting/', include('reporting.urls')),
    path('login/', authViews.LoginView.as_view(template_name = 'inventory/login.html'), name = 'login'),
    path('logout/', authViews.LogoutView.as_view(template_name = 'inventory/logout.html'), name = 'logout')
]

urlpatterns += static(settings.STATIC_URL)
