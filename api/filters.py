from django_filters import rest_framework as filters


class WorkerFilter(filters.FilterSet):
    level = filters.NumberFilter(field_name="level")

    fields = ['first_name', 'middle_name', 'last_name',
              'position', 'work_date', 'salary',
              'boss_id', 'company_level', 'salary_paid']