# Generated by Django 4.1.5 on 2023-02-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='budget',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
    ]