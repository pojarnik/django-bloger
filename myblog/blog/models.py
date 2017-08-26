from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.TextField()
    surname = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name