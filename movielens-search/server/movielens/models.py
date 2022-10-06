from django.db import models

# Create your models here.

class Links(models.Model):
    movieid = models.IntegerField(primary_key=True)
    imdbid = models.IntegerField(db_column='imdbId')  # Field name made lowercase.
    tmdbid = models.IntegerField(db_column='tmdbId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'links'


class Movies(models.Model):
    movieid = models.IntegerField(db_column='movieId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=-1)
    genres = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class Ratings(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieId')  # Field name made lowercase.
    rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    timestamp = models.AutoField()

    class Meta:
        managed = False
        db_table = 'ratings'


class Tags(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(max_length=-1, blank=True, null=True)
    timestamp = models.AutoField()

    class Meta:
        managed = False
        db_table = 'tags'
