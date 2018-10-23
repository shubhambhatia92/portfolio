from django.db import models


# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    date=models.DateTimeField()
    def summary(self):
        return self.body[:100]
    def date_pretty(self):
        return self.date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
        
