from django.shortcuts import render, redirect
from django import forms
from django.core import serializers
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from inventory.models import InventoryData
from .models import ReportingData
from .stats import (
    Model_Brand_Frequency_Bar,
    Reason_Pie_Chart,
    Equipment_Stats
    )

class ReportingMainView(CreateView):
    model = ReportingData
    template_name = 'reporting/reportingdata_form.html'
    fields = [
            'category',
            'equipment',
            'model_brand',
            'reason',
            'comments'
            ]
    success_url = '/reporting/'

    def get_context_data(self, **kwargs):
        context = super(ReportingMainView, self).get_context_data(**kwargs)
        context['reportingTable'] = ReportingData.history.all().order_by('history_date').reverse()
        return context

class ReportingDetailView(ListView):
    model = ReportingData
    template_name = 'reporting/reportingdata_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ReportingDetailView, self).get_context_data(**kwargs)
        context['reportingTable'] = ReportingData.history.all().order_by('history_date').reverse()
        return context

class ReportingStatsView(TemplateView):
    model = ReportingData
    template_name = 'reporting/stats_view.html'

    def get_queryset(self):
        return ReportingData.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ReportingStatsView, self).get_context_data(**kwargs)
        context['equipment'] = [
        'Other',
        'Controller',
        'Touchscreen',
        'Switcher',
        'Audio De-embedder',
        'HDMI Transmitter',
        'HDMI Receiver',
        'HDMI DA',
        'Amplifier',
        'Twisted Pair',
        'Power Supply',
        'Power Injector',
        'Infrastructure',
        'Blu-Ray Drive',
        'Blu-Ray Case',
        'VoIP Box',
        'Phone Handset',
        'Phone Ringer',
        'Key Switch',
        'Power Strip',
        'Doc Cam',
        'Doc Cam Mount',
        'IEC',
        'Blu-Ray Fan',
        'Small Speaker',
        'Medium Speaker',
        'Large Speaker',
        'Ceiling Speaker',
        'Monitor',
        'HDMI',
        'VGA',
        'Audio',
        'USB'
        ]
        context['Model_Brand_Frequency_Bar_x_data'] = Model_Brand_Frequency_Bar.get_x_data(self)
        context['Model_Brand_Frequency_Bar_y_data'] = Model_Brand_Frequency_Bar.get_y_data(self)
        context['Model_Brand_Frequency_Bar_x_labels'] = Model_Brand_Frequency_Bar.get_x_labels(self)
        context['Reason_Pie_Chart_x_data'] = Reason_Pie_Chart.get_x_data(self)
        context['Reason_Pie_Chart_y_data'] = Reason_Pie_Chart.get_y_data(self)
        context['Reason_Pie_Chart_x_labels'] = Reason_Pie_Chart.get_x_labels(self)
        context['Reason_Pie_Chart_y_labels'] = Reason_Pie_Chart.get_y_labels(self)
        return context



class TestView(ListView):
    model = ReportingData
    template_name = 'reporting/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['master_dict'] = Equipment_Stats.get_data(self)
        context['x_data'] = Equipment_Stats.get_x_data(self)
        context['x_labels'] = Equipment_Stats.get_x_labels(self)
        context['y_data'] = Equipment_Stats.get_y_data(self)
        return context


