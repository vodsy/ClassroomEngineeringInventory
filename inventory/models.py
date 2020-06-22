from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class InventoryData(models.Model):
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

    id = models.AutoField(primary_key=True)
    category = models.CharField(
        max_length = 2,
        choices = category_choices,
        default = 'NA'
        )
    equipment = models.CharField(
        max_length = 2,
        choices = equipment_choices,
        default = 'OT'
        )
    model_brand = models.CharField(max_length = 100, unique = True)
    quantity_deployed = models.PositiveIntegerField(default = 0)
    keep_in_stock = models.PositiveIntegerField(default = 0)
    in_stock = models.PositiveIntegerField(default = 0)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    relevant_link = models.TextField(max_length = 400)

    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('edit-item-view', kwargs = {'pk': self.pk})

    def get_absolute_url(self):
        return reverse('history-detail-view', kwargs = {'pk': self.pk})

    def get_absolute_url(self):
        return reverse('item-detail-view', kwargs = {'pk': self.pk})

    def get_absolute_url(self):
        return reverse('item-delete-view', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.model_brand

    def save(self):
        super().save()


class User(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    email_address = models.EmailField(default = 'N/A')
    first_name = models.CharField(max_length = 100, default = '')
    last_name = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return f'{self.user.username} profile'
