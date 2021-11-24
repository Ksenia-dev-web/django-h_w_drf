from django.contrib import admin
from django.core.exceptions import ValidationError  # Проверка форм и полей формы
from django.forms import BaseInlineFormSet  # вложенные формы
from .models import Article, Scope, ArticleScope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        selected_themes = 0
        for form in self.forms:

            if form.cleaned_data and form.cleaned_data['is_main']:
                selected_themes += 1

        if selected_themes == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if selected_themes > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

