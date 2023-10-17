from django.db import models


class Contact(models.Model):
    Firstname = models.CharField(max_length=122, null=True, blank=True)
    Lastname = models.CharField(max_length=122, null=True, blank=True)
    Email = models.CharField(max_length=122, null=True, blank=True)
    Mobile = models.CharField(max_length=12, null=True, blank=True)
    Desc = models.TextField(max_length=122, null=True, blank=True)
    Date = models.DateField()

    def __str__(self):
        return self.Firstname+" "+self.Lastname


# Create your models here.
