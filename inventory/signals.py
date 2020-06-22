"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InventoryData


#Try using history to identify id of changed item
#use conditional only on that item to save time
#if less than 25% of keep in stock value, display notification
#and send email
@receiver(post_save, sender = InventoryData)
def inventory_check(sender, **kwargs):
    for item in InventoryData:
        if (item.in_stock <= (item.keep_in_stock * .25)):

"""
