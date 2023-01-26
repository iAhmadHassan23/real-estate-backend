# Generated by Django 4.1.5 on 2023-01-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('star', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('icon', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('profession', models.CharField(blank=True, max_length=225, null=True)),
                ('star', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('comment', models.CharField(blank=True, max_length=225, null=True)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('description', models.CharField(blank=True, max_length=225, null=True)),
                ('icon', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('icon_color', models.CharField(blank=True, max_length=225, null=True)),
                ('icon_color_bg', models.CharField(blank=True, max_length=225, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('description', models.CharField(blank=True, max_length=225, null=True)),
                ('title_direction', models.CharField(blank=True, choices=[('1', 'One'), ('2', 'Two')], max_length=225, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('Blog_image', models.ManyToManyField(blank=True, to='main.blogimage')),
                ('Blog_posts', models.ManyToManyField(blank=True, to='main.blogpost')),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='Experts_blogs',
            field=models.ManyToManyField(blank=True, to='main.homeblog'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='HIW_steps',
            field=models.ManyToManyField(blank=True, to='main.homestep'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='Home_category',
            field=models.ManyToManyField(blank=True, to='main.homecategory'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='Rev_reviews',
            field=models.ManyToManyField(blank=True, to='main.homereview'),
        ),
    ]