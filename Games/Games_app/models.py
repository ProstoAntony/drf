from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length = 60)
    developers_company = models.CharField(max_length = 60)
    description = models.CharField(max_length = 60)
    mark = models.IntegerField()
    price_usd = models.IntegerField()


    def __str__(self):
        return f"{self.name} | {self.developers_company} | {self.description} | {self.mark}  | {self.price_usd}$,"


class Todo(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
    ]

    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        db_table = 'GameProjects.todo_list'  # Имя таблицы в PostgreSQL



