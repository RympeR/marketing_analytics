# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    login = models.TextField(unique=True)
    password = models.TextField()
    work_stage = models.FloatField(blank=True, null=True)
    salary_preference = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class ClientWork(models.Model):
    client_work_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    work_category = models.ForeignKey('WorkCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_work'


class ClientWorkPreferences(models.Model):
    client_work_preferences_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    work_category = models.ForeignKey('WorkCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_work_preferences'


class Scrapper(models.Model):
    scrapper_id = models.AutoField(primary_key=True)
    address = models.TextField()
    is_deleted = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    name = models.TextField()
    login = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrapper'


class Vacancy(models.Model):
    vacancy_id = models.AutoField(primary_key=True)
    vacancy_name = models.TextField()
    expirience = models.FloatField(blank=True, null=True)
    effectivness = models.FloatField(blank=True, null=True)
    posted_date = models.DateField(blank=True, null=True)
    website_name = models.TextField()
    salary = models.FloatField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacancy'


class WorkCategory(models.Model):
    work_category_id = models.AutoField(primary_key=True)
    category_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'work_category'
