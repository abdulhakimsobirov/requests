# Generated by Django 4.0.4 on 2022-09-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_objects_brigadir'),
    ]

    operations = [
        migrations.AddField(
            model_name='objects',
            name='phone',
            field=models.CharField(default=1, max_length=9, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
