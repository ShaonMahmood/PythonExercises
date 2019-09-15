from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=200,
    )

class Game(models.Model):
    name = models.CharField(
        max_length=200,
    )
    image = models.ImageField(
        upload_to='games/%Y/%m/%d/'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name='game_list'
    )
