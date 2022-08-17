from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=200 , null=True)
    problem = models.TextField(max_length=500, null=True)
    def __str__(self):
        return self.name
