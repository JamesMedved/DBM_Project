# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Streaming(models.Model):
    title_id = models.AutoField(db_column='Title_ID', primary_key=True)  # Field name made lowercase.
    provider = models.CharField(db_column='Provider', max_length=20)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=512, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.CharField(db_column='DateAdded', max_length=45, blank=True, null=True)  # Field name made lowercase.
    listedin = models.CharField(db_column='ListedIn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=250, blank=True, null=True)



class Titles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    cast = models.CharField(max_length=2048, blank=True, null=True)
    director = models.CharField(max_length=1024, blank=True, null=True)