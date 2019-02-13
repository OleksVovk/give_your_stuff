from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return str(self.name), str(self.description)


class Present(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return str(self.name), str(self.description)
