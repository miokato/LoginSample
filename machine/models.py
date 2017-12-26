from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
