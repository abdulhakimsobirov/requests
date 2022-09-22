from django.db import models


IS_ACTIVE = (
    (1, 'Активный'),
    # (2, 'Неактивный'),
    (3, 'Удаленный'),
)




class Brigadir(models.Model):
    name = models.CharField(max_length=150, verbose_name='Ф.И.О. Бригадира')
    phone = models.CharField(max_length=9, verbose_name='Номер телефона')
    is_active = models.IntegerField(choices=IS_ACTIVE, default='1', verbose_name='Активность')

    class Meta:
        verbose_name = ("Бригадир")
        verbose_name_plural = ("Бригадиры")

    def __str__(self):
        return self.name


class Objects(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название объекта')
    brigadir = models.CharField(max_length=255, verbose_name='Ф.И.О. Бригадира')
    phone = models.CharField(max_length=9, verbose_name='Номер телефона')
    is_active = models.IntegerField(choices=IS_ACTIVE, default='1', verbose_name='Активность')


    class Meta:
        verbose_name = ("Объект")
        verbose_name_plural = ("Объекты")

    def __str__(self):
        return self.name


class Requests(models.Model):

    date = models.DateField(auto_now_add=True)
   
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, verbose_name='Объект')
    lunch = models.IntegerField(default=0, blank=True, null=True,  verbose_name='Обед')
    dinner = models.IntegerField(default=0, blank=True, null=True,verbose_name='Ужин')
    late_dinner = models.IntegerField(default=0, blank=True, null=True,verbose_name='Поздный ужин')
    is_active = models.IntegerField(choices=IS_ACTIVE, default='1', verbose_name='Активность')
    

    class Meta:
        verbose_name = ("Заявка")
        verbose_name_plural = ("Заявки")


    # def __str__(self):
    #     return self.o


