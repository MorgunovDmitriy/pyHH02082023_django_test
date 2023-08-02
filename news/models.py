from django.db import models
from django.contrib.auth.models import User

class ArticleNew(models.Model):
    author = models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name = 'article_new_object'
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(default='Нет описания', verbose_name='текст новости')
    created_at = models.DateTimeField(verbose_name='дата создания новости')
    updated_at = models.DateTimeField(null=True,blank=True,verbose_name='дата изменеия новости')
    views_count = models.IntegerField(default=0, verbose_name='число просмотров')
    likes_users = models.ManyToManyField(
        to=User,
        blank=True,
        null=True,
        verbose_name='лайки'

    )
    def __str__(self):
        return self.title