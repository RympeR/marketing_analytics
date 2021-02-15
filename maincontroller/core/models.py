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
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.login


class ClientWork(models.Model):
    client_work_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    work_category = models.ForeignKey('WorkCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_work'
        verbose_name = 'Клиент - работа'
        verbose_name_plural = 'Клиенты - работы'

    def __str__(self):
        return self.client + ' -- ' + self.work_category


class ClientWorkPreferences(models.Model):
    client_work_preferences_id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    work_category = models.ForeignKey('WorkCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client_work_preferences'
        verbose_name = 'Избранные категории клиента'
        verbose_name_plural = 'Избранные категории клиентов'

    def __str__(self):
        return self.client + ' -- ' + self.work_category


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
        verbose_name = 'Парсер'
        verbose_name_plural = 'Парсеры'

    def __str__(self):
        return self.address + ' -- ' + self.login


class Vacancy(models.Model):
    vacancy_id = models.AutoField(
        verbose_name='Айди вакансии', primary_key=True)
    vacancy_name = models.TextField(verbose_name='Название вакансии',)
    expirience = models.FloatField(
        verbose_name='Опыт рабооты', blank=True, null=True)
    effectivness = models.FloatField(
        verbose_name='Перспективность вакансии', blank=True, null=True)
    posted_date = models.DateField(
        verbose_name='Дата публикации вакансии', blank=True, null=True)
    website_name = models.TextField(verbose_name='Названгие вебсайта',)
    salary = models.FloatField(verbose_name='Зарплата', blank=True, null=True)
    city = models.TextField(verbose_name='Город', blank=True, null=True)
    country = models.TextField(verbose_name='Страна', blank=True, null=True)
    company = models.TextField(verbose_name='Компания', blank=True, null=True)
    work_category = models.ForeignKey(
        'WorkCategory', models.DO_NOTHING, blank=True, null=True, verbose_name='Категория вакансии')

    class Meta:
        managed = False
        db_table = 'vacancy'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.vacancy_name


class WorkCategory(models.Model):
    work_category_id = models.AutoField(primary_key=True)
    category_name = models.TextField()
    category_parent = models.ForeignKey(
        'WorkCategory', verbose_name='Родительская категория', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'work_category'

    def __str__(self):
        return self.category_name


class City(models.Model):
    city_id = models.AutoField(verbose_name='Айди города', primary_key=True)
    city_name = models.TextField(verbose_name='Город')
