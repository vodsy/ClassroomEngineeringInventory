from django.contrib import admin
from .models import InventoryData, User

#register model
admin.site.register(InventoryData)
admin.site.register(User)

