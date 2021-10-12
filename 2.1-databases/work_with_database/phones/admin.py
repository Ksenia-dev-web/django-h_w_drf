from django.contrib import admin
from phones.models import Phone


# # ТУТ Я НИЧЕГО НЕ ПОНИМАЮ!!!!
# @admin.register(Phone)
# class PhoneAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'release_date', 'lte_exists')
#     list_display_links = ('name',)
#     ordering = ['-release_date']

class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
