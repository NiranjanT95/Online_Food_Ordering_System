#to seed use 'python django shell'
#then 'from apps.restaurants import seed'
from .models import *
import random

cuisines = [f'cuisine {i}' for i in range(10)]
data = [
    {'restaurant_name':f'Hotel {i}','address':f'address {i}', 'veg_only':random.choice([0,1]), 'cost':random.choice(['low','medium','high']),'cuisine_types':[random.choice(cuisines) for j in range(random.randint(2,10))]} for i in range(20)
]

for d in data:
    restaurant = Restaurant.objects.create(**d)
    restaurant.save()
