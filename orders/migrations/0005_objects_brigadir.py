# Generated by Django 4.0.4 on 2022-09-22 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_brigadir_is_active_alter_brigadir_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='objects',
            name='brigadir',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.brigadir', verbose_name='Ф.И.О. Бригадира'),
            preserve_default=False,
        ),
    ]
