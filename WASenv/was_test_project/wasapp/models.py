from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)
    date = models.CharField(max_length=128, unique=True)
    desc = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __list__(self):
        return [self.title, self.date, self.desc]
