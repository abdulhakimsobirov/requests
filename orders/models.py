from django.db import models

class Objects(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Объект")
        verbose_name_plural = ("Объекты")

    def __str__(self):
        return self.name

class Brigadir(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=9)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Бригадир")
        verbose_name_plural = ("Бригадиры")

    def __str__(self):
        return self.name


class Requests(models.Model):
    TYPES = (
        ('1', 'Обед'),
        ('2', 'ужин'),
        ('3', 'Позд ужин'),
    )
    date = models.DateField(auto_now_add=True)
    brigadir = models.ForeignKey(Brigadir, on_delete=models.CASCADE)
    object = models.ForeignKey(Objects, on_delete=models.CASCADE)
    lunch = models.IntegerField(default=0, blank=True, null=True,  verbose_name='Обед')
    dinner = models.IntegerField(default=0, blank=True, null=True,verbose_name='Ужин')
    late_dinner = models.IntegerField(default=0, blank=True, null=True,verbose_name='Поздный ужин')
    is_active = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = ("Заявка")
        verbose_name_plural = ("Заявки")


    # def __str__(self):
    #     return self.o


