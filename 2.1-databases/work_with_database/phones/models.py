from django.db import models


class Phone1(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=50)
    image = models.ImageField()
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return self.slug

