# Generated by Django 4.1.5 on 2023-01-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mainsite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeblog',
            name='title_direction',
            field=models.CharField(blank=True, choices=[('1', 'Left'), ('2', 'Right')], max_length=225, null=True),
        ),
    ]