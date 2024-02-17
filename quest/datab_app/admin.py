from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import c_employee


class c_employee_admin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'hired', 'salary', 'photo_preview')
    readonly_fields = ('photo_preview',)
    fields= ('full_name', 'position', 'hired', 'salary', 'photo_preview', 'photo')


    @admin.display(description="Фото сотрудника", ordering='content')
    def photo_preview(self,Employee: c_employee):
        if(Employee.photo):
            return mark_safe(f"<img src='{Employee.photo.url}' width=50")
        else:
            return "Нет фото"
admin.site.register(c_employee, c_employee_admin)