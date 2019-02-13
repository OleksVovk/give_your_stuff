from django.db import models

# Create your models here.

# jeden do wielu Organization --> Present


class Organization(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name), str(self.description)


class Present(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.name), str(self.description)
