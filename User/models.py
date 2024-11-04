from django.db import models

GENDER_CHOICES = [
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ('Khác', 'Khác'),
]

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank = False, default='')
    gender = models.CharField(choices=GENDER_CHOICES, default='Nam', max_length=4)
    age = models.IntegerField(default=0)
    occupation = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']