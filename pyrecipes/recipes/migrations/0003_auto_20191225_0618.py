# Generated by Django 3.0 on 2019-12-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20191218_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient_text',
            field=models.TextField(default='', max_length=2000, verbose_name='ingredients'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='process',
            field=models.TextField(max_length=9000, verbose_name='step-by-Step process'),
        ),
    ]
