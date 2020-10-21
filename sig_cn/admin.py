from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Enterprise
from .models import News


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'available')
    search_fields = ('name',)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'available', 'index')
    search_fields = ('name', 'owner')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'available')
    search_fields = ('title',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(News, NewsAdmin)
