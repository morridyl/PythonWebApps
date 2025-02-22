from django.db import models


class Superhero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.description}'
