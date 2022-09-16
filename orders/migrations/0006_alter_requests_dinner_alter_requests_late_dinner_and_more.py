# Generated by Django 4.1.1 on 2022-09-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_requests_dinner_alter_requests_late_dinner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='dinner',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Ужин'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='late_dinner',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Поздный ужин'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='lunch',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Обед'),
        ),
    ]