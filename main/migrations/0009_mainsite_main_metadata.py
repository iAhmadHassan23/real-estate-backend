# Generated by Django 4.1.5 on 2023-01-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_metadata_remove_homestep_icon_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsite',
            name='Main_metadata',
            field=models.ManyToManyField(blank=True, default='', to='main.metadata'),
        ),
    ]