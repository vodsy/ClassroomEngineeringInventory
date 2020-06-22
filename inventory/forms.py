from django import forms
from django.contrib.auth.models import User
from .models import InventoryData

class InventoryUpdateForm(forms.ModelForm):
    category_choices = [
        ('EX', 'Extron'),
        ('LE', 'Lectern'),
        ('AM', 'Amplifier'),
        ('SP', 'Speaker'),
        ('MO', 'PC Monitor'),
        ('CA', 'Cable'),
        ('NA', 'None')
        ]

    equipment_choices = [
        ('OT', 'Other'),
        ('CO', 'Controller'),
        ('TO', 'Touchscreen'),
        ('SW', 'Switcher'),
        ('DE', 'Audio De-embedder'),
        ('TX', 'HDMI Transmitter'),
        ('RX', 'HDMI Receiver'),
        ('DA', 'HDMI DA'),
        ('AM', 'Amplifier'),
        ('TP', 'Twisted Pair'),
        ('PS', 'Power Supply'),
        ('PI', 'Power Injector'),
        ('IN', 'Infrastructure'),
        ('BD', 'Blu-Ray Drive'),
        ('BC', 'Blu-Ray Case'),
        ('VP', 'VoIP Box'),
        ('PH', 'Phone Handset'),
        ('PR', 'Phone Ringer'),
        ('KS', 'Key Switch'),
        ('PW', 'Power Strip'),
        ('DC', 'Doc Cam'),
        ('DM', 'Doc Cam Mount'),
        ('IE', 'IEC'),
        ('BF', 'Blu-Ray Fan'),
        ('SS', 'Small Speaker'),
        ('SM', 'Medium Speaker'),
        ('SL', 'Large Speaker'),
        ('SC', 'Ceiling Speaker'),
        ('MO', 'Monitor'),
        ('HD', 'HDMI'),
        ('VG', 'VGA'),
        ('AU', 'Audio'),
        ('US', 'USB')
        ]

    category = forms.ChoiceField(
        choices = category_choices
        )
    equipment = forms.ChoiceField(
        choices = equipment_choices
        )
    model_brand = forms.CharField(max_length = 100)
    quantity_deployed = forms.IntegerField()
    in_stock = forms.IntegerField()
    keep_in_stock = forms.IntegerField()
    price = forms.DecimalField()
    relevant_link = forms.URLField()

    class Meta:
        model = InventoryData
        user = User
        fields = [
            'category',
            'equipment',
            'model_brand',
            'in_stock',
            'keep_in_stock',
            'price',
            'relevant_link'
            ]

class AddInventoryItemForm(forms.ModelForm):
    category_choices = [
        ('EX', 'Extron'),
        ('LE', 'Lectern'),
        ('AM', 'Amplifier'),
        ('SP', 'Speaker'),
        ('MO', 'PC Monitor'),
        ('CA', 'Cable'),
        ('NA', 'None')
        ]

    equipment_choices = [
        ('OT', 'Other'),
        ('CO', 'Controller'),
        ('TO', 'Touchscreen'),
        ('SW', 'Switcher'),
        ('DE', 'Audio De-embedder'),
        ('TX', 'HDMI Transmitter'),
        ('RX', 'HDMI Receiver'),
        ('DA', 'HDMI DA'),
        ('AM', 'Amplifier'),
        ('TP', 'Twisted Pair'),
        ('PS', 'Power Supply'),
        ('PI', 'Power Injector'),
        ('IN', 'Infrastructure'),
        ('BD', 'Blu-Ray Drive'),
        ('BC', 'Blu-Ray Case'),
        ('VP', 'VoIP Box'),
        ('PH', 'Phone Handset'),
        ('PR', 'Phone Ringer'),
        ('KS', 'Key Switch'),
        ('PW', 'Power Strip'),
        ('DC', 'Doc Cam'),
        ('DM', 'Doc Cam Mount'),
        ('IE', 'IEC'),
        ('BF', 'Blu-Ray Fan'),
        ('SS', 'Small Speaker'),
        ('SM', 'Medium Speaker'),
        ('SL', 'Large Speaker'),
        ('SC', 'Ceiling Speaker'),
        ('MO', 'Monitor'),
        ('HD', 'HDMI'),
        ('VG', 'VGA'),
        ('AU', 'Audio'),
        ('US', 'USB')
        ]

    category = forms.ChoiceField(
        choices = category_choices
        )
    equipment = forms.ChoiceField(
        choices = equipment_choices
        )
    model_brand = forms.CharField(max_length = 100)
    quantity_deployed = forms.IntegerField()
    in_stock = forms.IntegerField()
    keep_in_stock = forms.IntegerField()
    price = forms.DecimalField()
    relevant_link = forms.URLField()

    class Meta:
        model = InventoryData
        user = User
        fields = [
            'category',
            'equipment',
            'model_brand',
            'in_stock',
            'keep_in_stock',
            'price',
            'relevant_link'
            ]
