from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="pics")
    desc=models.TextField()
    def __str__(self):
        return self.name

class place1(models.Model):
    name2 = models.CharField(max_length=250)
    image2 = models.ImageField(upload_to="pics")
    desc2 = models.TextField()
    cust = models.TextField()
    def __str__(self):
        return self.name2

