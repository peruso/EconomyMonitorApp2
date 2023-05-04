from djongo import models
from decimal import Decimal

class ExchangeRate(models.Model):
    timestamp = models.DateTimeField()
    currency_pair = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_rate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()


class StockPrice(models.Model):
    timestamp = models.DateTimeField()
    index_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_rate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()


class CommodityPrice(models.Model):
    timestamp = models.DateTimeField()
    commodity_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_rate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()

class BondRate(models.Model):
    timestamp = models.DateTimeField()
    bond_name = models.CharField(max_length=255)
    annual_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    change_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    change_interest_rateByRate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()


class FedRate(models.Model):
    timestamp = models.DateTimeField()
    fed_name = models.CharField(max_length=255)
    fedRate = models.DecimalField(max_digits=10, decimal_places=2)
    change_fedRate = models.DecimalField(max_digits=10, decimal_places=2)
    change_fedRateByRate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()


class ShippingIndex(models.Model):
    timestamp = models.DateTimeField()
    index_name = models.CharField(max_length=255)
    index_value = models.DecimalField(max_digits=10, decimal_places=2)
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_rate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()


class GdpData(models.Model):
    timestamp = models.DateTimeField()
    country_name = models.CharField(max_length=255)
    gdp = models.DecimalField(max_digits=10, decimal_places=2)
    change_gdp = models.DecimalField(max_digits=10, decimal_places=2)
    change_rate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()


class News(models.Model):
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField()
