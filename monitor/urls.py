from django.urls import path 
from .views import HomePageView, CrudeOilWtiView, commodity_price_table

urlpatterns = [
    path('monitor/wti/', CrudeOilWtiView.as_view(), name='monitor_wti'),
    # path('monitor/wti/commodity_price_table/', commodity_price_table, name='commodity_price_table'),
    path('', HomePageView.as_view(), name='home'),
    path('commodity_price_table/', commodity_price_table, name='commodity_price_table'),
]
