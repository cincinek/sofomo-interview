from django.db import models


class Location(models.Model):
    url = models.CharField(max_length=100, null=True)
    ip = models.CharField(max_length=16, unique=True)
    ip_type = models.CharField(max_length=4)
    continent_code = models.CharField(max_length=3)
    continent_name = models.CharField(max_length=20)
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=3)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=7)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    #LOCATION fields
    geoname_id = models.IntegerField()
    capital = models.CharField(max_length=50)
    country_flag = models.URLField()
    calling_code = models.CharField(max_length=10)
    is_eu = models.BooleanField()
