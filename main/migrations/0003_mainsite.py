# Generated by Django 4.1.5 on 2023-01-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogimage_blogpost_homecategory_homereview_homestep_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('favicon', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('head_logo', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('foot_logo', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('facebook_link', models.CharField(blank=True, max_length=225, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=225, null=True)),
                ('twitter_link', models.CharField(blank=True, max_length=225, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=225, null=True)),
                ('linkin_link', models.CharField(blank=True, max_length=225, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]