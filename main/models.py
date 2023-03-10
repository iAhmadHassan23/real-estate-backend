from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MainSite(models.Model):
    title = models.CharField(max_length=225,blank=True, default='')
    favicon = models.ImageField(blank=True, default='/placeholder.png')
    head_logo = models.ImageField(blank=True, default='/placeholder.png')
    foot_logo = models.ImageField(blank=True, default='/placeholder.png')
    foot_copyright = models.CharField(max_length=225,blank=True, default='')
    facebook_link = models.CharField(max_length=225,blank=True, default='')
    instagram_link = models.CharField(max_length=225,blank=True, default='')
    twitter_link = models.CharField(max_length=225,blank=True, default='')
    tiktok_link = models.CharField(max_length=225,blank=True, default='')
    youtube_link = models.CharField(max_length=225,blank=True, default='')
    linkin_link = models.CharField(max_length=225,blank=True, default='')
    Main_metadata = models.ManyToManyField('MetaData', blank=True, default='')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Homepage(models.Model):
    Home_title = models.CharField(max_length=225,blank=True, default='')
    Home_tagline = models.CharField(max_length=225,blank=True, default='')
    Home_button = models.CharField(max_length=225,blank=True, default='')
    Home_button_link = models.CharField(max_length=225,blank=True, default='')
    Home_img_slider = models.ManyToManyField('HomeImageSlider', blank=True, default='')
    Home_category = models.ManyToManyField('HomeCategory', blank=True, default='')

    HIW_title = models.CharField(max_length=225,blank=True, default='')
    HIW_steps = models.ManyToManyField('HomeStep', blank=True)

    Experts_blogs = models.ManyToManyField('HomeBlog', blank=True)

    Blog_articles = models.ManyToManyField('HomeBlogArticle', blank=True)

    Rev_title = models.CharField(max_length=225,blank=True, default='')
    Rev_tagline = models.CharField(max_length=225,blank=True, default='')
    Rev_reviews = models.ManyToManyField('HomeReview', blank=True, default='')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Home_title


class HomeCategory(models.Model):
    title = models.CharField(max_length=225,blank=True, default='')
    icon = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class HomeImageSlider(models.Model):
    title = models.CharField(max_length=225,blank=True, default='')
    place = models.CharField(max_length=225,blank=True, default='')
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class HomeStep(models.Model):
    title = models.CharField(max_length=225,blank=True, default='')
    description = models.CharField(max_length=225,blank=True, default='')
    icon = models.FileField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class HomeBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=225,blank=True, default='')
    description = models.CharField(max_length=225,blank=True, default='')
    short_description = models.ManyToManyField('ShortDescription', blank=True)
    Blog_image = models.ManyToManyField('BlogImage', blank=True)
    Blog_posts = models.ManyToManyField('BlogPost', blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class ShortDescription(models.Model):
    title = models.CharField(max_length=225,blank=True, default='')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=225,blank=True, default='')
    special_tag = models.CharField(max_length=225,blank=True, default='')
    price = models.DecimalField(max_digits=9, decimal_places=0,blank=True, default=0)
    star = models.DecimalField(max_digits=9, decimal_places=0,blank=True, default=0)
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class BlogImage(models.Model):
    special_tag = models.CharField(max_length=225,blank=True, default='')
    deal = models.CharField(max_length=225,blank=True, default='')
    image = models.ImageField(blank=True, default='/placeholder.png')


class HomeBlogArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=225,blank=True, default='')
    meta = models.CharField(max_length=225,blank=True, default='')
    meta_description = models.CharField(max_length=225,blank=True, default='')
    details = models.CharField(max_length=225,blank=True, default='')
    slug = models.CharField(max_length=225,blank=True, default='')
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



class HomeReview(models.Model):
    name = models.CharField(max_length=225,blank=True, default='')
    profession = models.CharField(max_length=225,blank=True, default='')
    star = models.DecimalField(max_digits=9, decimal_places=0,blank=True, default=0)
    comment = models.CharField(max_length=225,blank=True, default='')
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class MetaData(models.Model):
    name = models.CharField(max_length=225,blank=True, default='')
    content = models.CharField(max_length=225,blank=True, default='')
    
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Quotation(models.Model):
    size = models.CharField(max_length=225,blank=True, default='')
    budget = models.CharField(max_length=225,blank=True, default='')
    time = models.CharField(max_length=225,blank=True, default='')
    name = models.CharField(max_length=225,blank=True, default='')
    email = models.CharField(max_length=225,blank=True, default='')
    contact = models.DecimalField(max_digits=15, decimal_places=0, blank=True, default=0)
    comment = models.CharField(max_length=500,blank=True, default='')
    
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=225,blank=True, default='')
    email = models.CharField(max_length=225,blank=True, default='')
    contact = models.DecimalField(max_digits=15, decimal_places=0, blank=True, default=0)
    message = models.CharField(max_length=500,blank=True, default='')
    
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name