from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=2000, blank=True, null=True)
    address = models.CharField(max_length=2000)

    def __str__(self):
        return self.name 

        
