# Generated by Django 4.0.4 on 2023-05-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gshop', '0004_promotion_send_now'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Тип автомобиля', 'verbose_name_plural': 'Типы автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Автомобили', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=180, verbose_name='Тип автомобиля'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание автомобиля'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование автомобиля'),
        ),
    ]
