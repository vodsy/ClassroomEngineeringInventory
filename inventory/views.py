from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from .models import InventoryData
from .forms import InventoryUpdateForm
from django import forms
from reporting.models import ReportingData

class MainPageView(ListView):
    model = InventoryData
    template_name = 'inventory/mainPage_view.html'

    def get_queryset(self):
        return InventoryData.objects.all().order_by('category')

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['minimalTable'] = InventoryData.objects.all().order_by('category')
        context['history'] = InventoryData.history.all().order_by('history_date').reverse()
        context['reporting'] = ReportingData.history.all().order_by('history_date').reverse()
        return context



class InventoryDetailView(ListView):
    model = InventoryData
    context_object_name = 'fullTable'
    template_name = 'inventory/detailView_view.html'

class EditItemView(UpdateView):
    model = InventoryData
    context_object_name = 'item'
    fields = [
        'category',
        'equipment',
        'model_brand',
        'keep_in_stock',
        'in_stock',
        'price',
        'relevant_link'
        ]
    success_url = '/detail/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ItemDetailView(DetailView):
    model = InventoryData
    context_object_name = 'detail'
    template_name = 'inventory/inventorydata_detail.html'

class NotificationDetailView(ListView):
    model = InventoryData
    context_object_name = 'minimalTable'
    template_name = 'inventory/notifications_detail.html'

class AddItemView(CreateView):
    template_name = 'inventory/addinventoryitem_form.html'
    model = InventoryData
    fields = [
        'category',
        'equipment',
        'model_brand',
        'keep_in_stock',
        'in_stock',
        'price',
        'relevant_link'
        ]
    success_url = '/detail/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateHistoryDetailView(ListView):
    model = InventoryData
    template_name = 'inventory/inventoryhistory_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateHistoryDetailView, self).get_context_data(**kwargs)
        context['minimalTable'] = InventoryData.objects.all().order_by('category')
        context['history'] = InventoryData.history.all().order_by('history_date').reverse()
        return context

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory/inventorydata_confirm_delete.html'
    model = InventoryData
    context_object_name = 'item'
    success_url = '/detail/'
