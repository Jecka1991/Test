from django.db import models

from django.contrib.auth.models import User


class MaxLimitException(BaseException):
    pass


class CompanyLevels(models.Model):
    level = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        max_count = CompanyLevels.objects.count()
        if max_count >= 5:
            raise MaxLimitException({"message": "Can be only 5 levels "})
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name_plural = "CompanyLevels"


class Big_Boss(models.Model):
    boss_id = models.PositiveIntegerField(unique=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.boss_id)

    class Meta:
        verbose_name_plural = "Big_Bosses"


class Position(models.Model):
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.position


class Worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="empl_position")
    work_date = models.DateField()
    salary = models.PositiveIntegerField(blank=True)
    salary_paid = models.PositiveIntegerField(null=True)
    boss_id = models.ForeignKey(Big_Boss, on_delete=models.CASCADE, related_name='empl_boss_id')
    company_level = models.ForeignKey(CompanyLevels, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.last_name
