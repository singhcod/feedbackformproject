from django.db import models

class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    date = models.DateField(max_length=30)
    feedback = models.CharField(max_length=100)

