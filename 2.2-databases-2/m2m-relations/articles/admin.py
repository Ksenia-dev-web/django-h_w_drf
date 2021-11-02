from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleMainTag, ArticleTag

from .models import Article

class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_marked = 0
        for form in self.forms:
            if is_marked > 1:
                raise ValidationError('Please mark only one main tag')
            if form.cleaned_data.get('is_main'):
                is_marked += 1
        if is_marked == 0:
            raise ValidationError('Need to mark main tag')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleMainTagInline(admin.TabularInline):
    model = ArticleMainTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleMainTagInline]


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass

