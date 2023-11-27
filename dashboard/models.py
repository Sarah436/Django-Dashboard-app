# dashboard/models.py

from django.db import models

class Insight(models.Model):
    # Define your model fields based on your JSON data structure
    end_year = models.CharField(max_length=4, blank=True, null=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=255)
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    impact = models.CharField(max_length=255, blank=True, null=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Insights"
