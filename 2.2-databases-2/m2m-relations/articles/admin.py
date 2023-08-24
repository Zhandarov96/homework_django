from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if dictionary.get('is_main'):
                i += 1
            else:
                continue
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()
    # def clean(self):
    #     count = 0
    #     # for form in self.forms:
    #     #     if 'is_main' in form.cleaned_data:
    #     #         if form.cleaned_data['is_main']:
    #     #             count += 1
    #     #     if count == 0:
    #     #         raise ValidationError('Какая-то ошибка')
    #     #     else:
    #     #         pass

    #     for self.deleted_forms in self._should_delete_form(form):
    #         continue
    #     elif self.form.cleaned_data.get(‘is_main’):
    #         count += 1
    #     if count > 1:
    #         raise ValidationError(‘Is_main should be only one tag’)
    #     elif count == 0:
    #         raise ValidationError(‘Assign is_main’)

    #     return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    pass