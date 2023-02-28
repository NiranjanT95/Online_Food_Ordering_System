from django.contrib import admin
from .models import *
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_id','restaurant_name','veg_only','cost']


admin.site.register(Restaurant, RestaurantAdmin)