from django.db import models


class Location(models.Model):
    id = models.IntegerField()
    listing_url = models.URLField()
    name = models.CharField(max_length=100)
    host_url = models.URLField
    host_name = models.CharField(max_length=100)
    precinct = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    price = models.FloatField
    review_scores_rating = models.IntegerField
    price_as_dp = models.FloatField
    rating_as_int = models.IntegerField
    precint = models.CharField(max_length=100)
    crime_count = models.IntegerField
    precint_crime_rating = models.FloatField
    goal_function = models.FloatField