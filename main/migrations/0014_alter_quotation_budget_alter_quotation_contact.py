# Generated by Django 4.1.5 on 2023-02-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_quotation_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='budget',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='contact',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=15),
        ),
    ]