from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    resim = models.CharField(max_length=150)
    anasayfa = models.BooleanField(default=False)

    #class Meta:
    #    db_table = 'MoviesTable'
    #    verbose_name = 'Movie'
    #    verbose_name_plural = 'Movies'    