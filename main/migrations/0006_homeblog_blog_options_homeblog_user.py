# Generated by Django 4.1.5 on 2023-01-26 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_remove_blogimage_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeblog',
            name='blog_options',
            field=models.CharField(blank=True, choices=[('1', 'Simple Blog'), ('2', 'Blog with product cards')], max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
