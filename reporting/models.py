from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from inventory.models import InventoryData




class ReportingData(models.Model):
    #Create drop-down menu choices for damage report submission form
    category_choices = [
        ('EX', 'Extron'),
        ('LE', 'Lectern'),
        ('AM', 'Amplifier'),
        ('SP', 'Speaker'),
        ('MO', 'PC Monitor'),
        ('CA', 'Cable'),
        ('NA', 'None')
        ]
    reason_choices = [
        ('DA', 'Damaged'),
        ('OB', 'Obsolete'),
        ('OT', 'Other')
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
        ('US', 'USB'),
        ('NA', 'None')
        ]

    """
    NEED TO TAKE INPUT FOR MODEL_BRAND AND JUST CLEAN IT
    """

    category = models.CharField(
        max_length = 2,
        choices = category_choices,
        default = 'NA'
        )
    equipment = models.CharField(
        max_length = 2,
        choices = equipment_choices,
        null = False
        )
    model_brand = models.TextField(
        max_length = 100
        )
    reason = models.CharField(
        max_length = 2,
        choices = reason_choices,
        null = False
        )
    comments = models.TextField(
        max_length = 400
        )

    history = HistoricalRecords()

    def __str__(self):
        return self.get_reason_display()

    def save(self):
        super().save()
