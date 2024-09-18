from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    age = models.IntegerField()
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title