from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import JsonResponse
from .models import CommodityPrice

class HomePageView(TemplateView): 
  template_name = 'home.html'

class CrudeOilWtiView(TemplateView):
  template_name = 'crude_oil_wti.html'


def commodity_price_table(request):#Receive http request
  commodity_prices = CommodityPrice.objects.all() #get objects from mongodb
  # print(commodity_prices)
  data = []
  for commodity in commodity_prices:
    data.append({
      'timestamp': commodity.timestamp.strftime('%Y-%m-%d'),
      'price':str(commodity.price),
      'change_price': str(commodity.change_price),
      'change_rate': str(commodity.change_rate)
    })
  # print(data)
  return JsonResponse(data, safe=False)#client responseを返す