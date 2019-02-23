from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

# jeden do wielu Organization --> Present
# jeden do jeden Adresses --> Organization/Present


class Organization(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    address = models.CharField(max_length=64, default=False, editable=True)

    def __str__(self):
        return str(self.name), str(self.description)


class Present(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField(blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.name), str(self.description)




