# Create your models here.

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    depatment_choices = (('Investment partner', 'Investment partner'),
                         ('Investment manager', 'Investment manager'),
                         ('Global management', 'Global management'),
                         ('Investment adviser', 'Investment adviser'),
                         ('Post-investment', 'Post-investment'),
                         ('Legal', 'Legal'),
                         ('Operation', 'Operation'),
                         )
    department = models.CharField(max_length=30, null=True, blank=True, choices=depatment_choices)
    introduction = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='employee', null=True)
    available = models.BooleanField(null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.TextField()
    date = models.DateField()
    summary = models.TextField()
    introduction = models.TextField()
    available = models.BooleanField(null=True)

    class Meta:
        ordering = ["title"]
        verbose_name = 'New'

    def __str__(self):
        return self.title


class Enterprise(models.Model):
    name = models.CharField(max_length=30)
    site = models.URLField(null=True, blank=True)
    owner = models.CharField(max_length=30)
    introduction = models.TextField()
    picture_owner = models.ImageField(upload_to='owner', null=True, blank=True)
    trademark = models.ImageField(upload_to='trademark', null=True)
    available = models.BooleanField(null=True)
    index = models.BooleanField(null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
