# Generated by Django 4.2.2 on 2023-06-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0002_alter_garden_cultivation_pattern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='area',
            field=models.PositiveIntegerField(),
        ),
    ]
