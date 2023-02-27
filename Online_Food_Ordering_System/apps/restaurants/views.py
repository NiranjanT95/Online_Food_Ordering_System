from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import *
from .serializers import *

class Retaurants(View):
    """
            Code documentation 
                blank input(empty string) in postman/get request means don't consider attribute for search
    """
    def get(self, request):
        data = {}
        try:
            required_keys = ['veg_only', 'costs', 'cuisine_types','cuisine_op']
            for key in required_keys:
                if key not in request.GET:
                    raise Exception("Required Key "+key+" not present in the request")
            veg_only,costs,cuisine_types, cuisine_op = request.GET['veg_only'], request.GET['costs'], request.GET['cuisine_types'],request.GET['cuisine_op']
            filters = {}
            if veg_only != '':
                filters['veg_only'] = bool(int(veg_only))
            if costs != '':
                filters['cost__in'] = costs.split(',')
            if cuisine_types != '':
                if cuisine_op == 'and':
                    filters['cuisine_types__contained_by'] = cuisine_types.split(',')
                elif cuisine_op == 'or':
                    filters['cuisine_types__contains'] = cuisine_types.split(',')
            restaurants =[]
            for restaurant in Restaurant.objects.filter(**filters):
                restaurants.append(RestaurantSerializer(restaurant).data)
            data = {'restaurants':restaurants, 'status':'success'}
            status_code = 200
        except Exception as e:
            data={'status': 'Error','message': str(e)}
            status_code = 400
        return JsonResponse(data, status=status_code)