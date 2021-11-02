from django.db import models


class ArticleTag(models.Model):
    topic = models.CharField(max_length=256, verbose_name='Тема статьи')

    class Meta:
        ordering = ['topic']
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статьи'

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    article_tag = models.ManyToManyField(ArticleTag, through='ArticleMainTag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleMainTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_tag = models.ForeignKey(ArticleTag, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Главный раздел')

    class Meta:
        ordering = ['-is_main']
