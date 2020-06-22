import django_tables2 as tables
from .models import InventoryData

class MinimalInventoryTable(tables.Table):
    class Meta:
        model = InventoryData
        template_name = "django_tables2/bootstrap4.html"
        fields = ["category", "equipment", "model_brand", "keep_in_stock", "in_stock"]
        attrs = {"class": "minimalTable"}

class FullInventoryTable(tables.Table):
    class Meta:
        model = InventoryData
        template_name = "django_tables2/bootstrap4.html"
        fields = ["id", "category", "equipment", "model_brand", "keep_in_stock", "in_stock", "price", "url"]
        attrs = {"class": "fullTable"}
