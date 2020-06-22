from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authViews
from inventory import views as inventory_views
from .views import ReportingMainView, ReportingDetailView, ReportingStatsView, TestView

urlpatterns = [
    path('', ReportingMainView.as_view(), name = 'reporting-main'),
    path('detail/', ReportingDetailView.as_view(), name = 'reporting-detail'),
    path('stats/', ReportingStatsView.as_view(), name = 'reporting-stats'),
    path('test/', TestView.as_view(), name = 'test-page')
    ]
