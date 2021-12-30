from django.contrib import admin
from .models import Worker, Big_Boss, Position, CompanyLevels

from django_admin_relation_links import AdminChangeLinksMixin


def delete_total_paid(modeladmin, request, queryset):
    new = 0
    for worker in queryset:
        worker.total_salary_paid = new
        worker.save()


delete_total_paid.short_description = "Delete chosen salaries"


@admin.register(Big_Boss)
class Big_BossAdmin(AdminChangeLinksMixin, admin.ModelAdmin):

    list_display = ['boss_id']

    changelist_links = ['empl_boss_id']


@admin.register(Worker)
class WorkerAdmin(AdminChangeLinksMixin, admin.ModelAdmin):

    list_display = ('first_name', 'middle_name', 'last_name',
                    'position', 'big_boss_id_link', 'salary', 'salary_paid')
    list_filter = ('position', 'company_level')
    change_links = ['big_boss_id']
    actions = [delete_total_paid]


admin.site.register(Position)
admin.site.register(CompanyLevels)