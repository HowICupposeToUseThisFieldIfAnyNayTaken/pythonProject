import datetime
from django.utils.timezone import now
from django.db import models
from django.utils.html import mark_safe

class c_employee(models.Model):
    full_name = models.CharField('ФИО',default='Ткачев Михаил Сергеевич')
    position = models.CharField('Должность',default='Инженер')
    hired = models.DateTimeField('Дата трудоустройства', default=now)
    salary = models.DecimalField('Зарплата,р', max_digits=10, decimal_places=0,default=80000)
    photo = models.ImageField('Фотография', upload_to="photos/%Y%m%d", default=None,blank=True, null=True )

    # Create your models here.
    def __str__(self):
        return self.full_name
