from django.db import models

# Create your models here.


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
