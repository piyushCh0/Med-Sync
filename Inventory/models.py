from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
1


class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity_in_stock = models.IntegerField()
    last_updated = models.DateField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
