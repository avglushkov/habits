# Generated by Django 4.2 on 2024-09-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit_action',
            field=models.CharField(blank=True,
                                   max_length=255,
                                   null=True,
                                   verbose_name='Действие'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_pleasant',
            field=models.BooleanField(default=False,
                                      verbose_name='Приятная привычка'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=True,
                                      verbose_name='Публичная привычка'),
        ),
    ]
