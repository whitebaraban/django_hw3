from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    def __str__(self):
        return self.name