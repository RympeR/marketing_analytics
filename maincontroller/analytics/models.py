from django.db import models

# Create your models here.


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
    work_category_id = models.AutoField(
        verbose_name='Айди категории', primary_key=True)
    category_name = models.TextField(verbose_name='Название категории')
    category_parent = models.ForeignKey(
        'WorkCategory', verbose_name='Родительская категория', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'work_category'
        verbose_name = 'Категория работы'
        verbose_name_plural = 'Категории работы'

    def __str__(self):
        return self.category_name
