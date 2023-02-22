import markdown
from django.db import models

from core.models import AbstractModel


class Project(AbstractModel):
    name = models.CharField('Название проекта', max_length=255, unique=True)
    link = models.TextField('Ссылка на проект')
    logo = models.ImageField('Лого проекта')
    description = models.TextField('Описание проекта')
    html_description = models.TextField(editable=False)
    owner = models.ForeignKey('users.User', models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/projects/{self.uuid}'

    def save(self, *args, **kwargs):
        self.html_description = markdown.markdown(self.description)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created']
