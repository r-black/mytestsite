from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Tree(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
     blank=True, verbose_name='Родитель', related_name='children', db_index=True)
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name