from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=200, default='www')
    is_mvp = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
