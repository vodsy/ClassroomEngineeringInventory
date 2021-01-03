from django import forms
from django.contrib.auth.models import User
from .models import ReportingData

class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportingData
        user = User
        fields = [
            'category',
            'equipment',
            'model_brand',
            'reason',
            'comments'
            ]

    """
    FIXME: FIGURE OUT HOW TO CLEAN INPUT BETTER
    """

    def __clean__(self):

        model_brand = self.model_brand
        model_brand.strip().lower()

        return model_brand
