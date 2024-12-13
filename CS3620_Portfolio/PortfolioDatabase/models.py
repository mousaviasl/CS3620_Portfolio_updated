from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hobbies/', blank=True, null=True)  # New field for images

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)  # New field for images

    def __str__(self):
        return self.name
