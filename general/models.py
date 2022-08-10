from django.core.checks import messages
from django.db import models

# Create your models here.
class Testimony(models.Model):
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=20)
    author_title = models.CharField(max_length=60)

    def __str__(self):
        return self.author

class Enquiry(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ": " + self.subject

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Website(models.Model):
    title = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)
    abbreviation = models.CharField(max_length=5, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    client = models.CharField(max_length=100, null = True)
    project_date = models.DateField(null = True)
    project_url = models.URLField(null = True)
    # images
    desktop_view = models.URLField()
    mobile_view = models.URLField()
    screenshot = models.URLField()
    cool_aspect = models.URLField()

    def __str__(self):
        return self.title

