from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
import uuid

class Restaurant(models.Model):

    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    restaurant_name = models.CharField(max_length=256, blank=False)
    address = models.CharField(max_length=512)
    veg_only = models.BooleanField(default=True)
    cost = models.CharField(max_length=8)
    cuisine_types = ArrayField(
        models.CharField(max_length=16, blank=False)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_open = models.BooleanField(default=False)



