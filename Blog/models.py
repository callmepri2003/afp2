from django.db import models

# Create your models here.

class blog_post(models.Model):
    title = models.CharField(max_length= 50)
    subtitle = models.CharField(max_length= 50)
    datetime = models.DateTimeField()
    content = models.CharField(max_length= 2000)

    def __str__(self):
        return self.title + " : " + str(self.datetime.date())
    
    def weekday(self):
        return str(self.datetime.weekday())
