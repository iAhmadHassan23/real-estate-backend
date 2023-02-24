# Generated by Django 4.1.6 on 2023-02-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_quotation_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=225)),
                ('place', models.CharField(blank=True, default='', max_length=225)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShortDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=225)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='homeblogarticle',
            old_name='description',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='homeblog',
            name='blog_options',
        ),
        migrations.RemoveField(
            model_name='homeblog',
            name='title_direction',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Experts_tagline',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Experts_title',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='HIW_tagline',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Home_bgimg',
        ),
        migrations.AddField(
            model_name='blogimage',
            name='deal',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AddField(
            model_name='blogimage',
            name='special_tag',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='special_tag',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AddField(
            model_name='homeblogarticle',
            name='meta',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AddField(
            model_name='homeblogarticle',
            name='meta_description',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AddField(
            model_name='homeblogarticle',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AddField(
            model_name='mainsite',
            name='tiktok_link',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.RemoveField(
            model_name='homeblog',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='homestep',
            name='icon',
            field=models.FileField(blank=True, default='/placeholder.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='homepage',
            name='Home_img_slider',
            field=models.ManyToManyField(blank=True, default='', to='main.homeimageslider'),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='short_description',
            field=models.ManyToManyField(blank=True, to='main.shortdescription'),
        ),
    ]
