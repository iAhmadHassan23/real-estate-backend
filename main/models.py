from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MainSite(models.Model):
    title = models.CharField(max_length=225,blank=True)
    favicon = models.ImageField(blank=True, default='/placeholder.png')
    head_logo = models.ImageField(blank=True, default='/placeholder.png')
    foot_logo = models.ImageField(blank=True, default='/placeholder.png')
    foot_copyright = models.CharField(max_length=225,blank=True)
    facebook_link = models.CharField(max_length=225,blank=True)
    instagram_link = models.CharField(max_length=225,blank=True)
    twitter_link = models.CharField(max_length=225,blank=True)
    youtube_link = models.CharField(max_length=225,blank=True)
    linkin_link = models.CharField(max_length=225,blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Homepage(models.Model):
    Home_title = models.CharField(max_length=225,blank=True)
    Home_tagline = models.CharField(max_length=225,blank=True)
    Home_button = models.CharField(max_length=225,blank=True)
    Home_button_link = models.CharField(max_length=225,blank=True)
    Home_bgimg = models.ImageField(blank=True, default='/placeholder.png')
    Home_category = models.ManyToManyField('HomeCategory', blank=True)

    HIW_title = models.CharField(max_length=225,blank=True)
    HIW_tagline = models.CharField(max_length=225,blank=True)
    HIW_steps = models.ManyToManyField('HomeStep', blank=True)

    Experts_title = models.CharField(max_length=225,blank=True)
    Experts_tagline = models.CharField(max_length=225,blank=True)
    Experts_blogs = models.ManyToManyField('HomeBlog', blank=True)

    Blog_articles = models.ManyToManyField('HomeBlogArticle', blank=True)

    Rev_title = models.CharField(max_length=225,blank=True)
    Rev_tagline = models.CharField(max_length=225,blank=True)
    Rev_reviews = models.ManyToManyField('HomeReview', blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Home_title


class HomeCategory(models.Model):
    title = models.CharField(max_length=225,blank=True,)
    icon = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class HomeStep(models.Model):
    title = models.CharField(max_length=225,blank=True)
    description = models.CharField(max_length=225,blank=True)
    icon = models.ImageField(blank=True, default='/placeholder.png')
    icon_color = models.CharField(max_length=225,blank=True)
    icon_color_bg = models.CharField(max_length=225,blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

DIRECTION_CHOICES =(
    ("1", "Left"),
    ("2", "Right"),
)

BLOG_CHOICES =(
    ("1", "Simple Blog"),
    ("2", "Blog with product cards"),
)

class HomeBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=225,blank=True)
    description = models.CharField(max_length=225,blank=True)
    title_direction = models.CharField(choices = DIRECTION_CHOICES, max_length=225,blank=True)
    blog_options = models.CharField(choices = BLOG_CHOICES, max_length=225,blank=True)
    Blog_image = models.ManyToManyField('BlogImage', blank=True)
    Blog_posts = models.ManyToManyField('BlogPost', blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=225,blank=True,)
    price = models.DecimalField(max_digits=9, decimal_places=0,blank=True)
    star = models.DecimalField(max_digits=9, decimal_places=0,blank=True)
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(blank=True, default='/placeholder.png')


class HomeBlogArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=225,blank=True)
    description = models.CharField(max_length=225,blank=True)
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



class HomeReview(models.Model):
    name = models.CharField(max_length=225,blank=True)
    profession = models.CharField(max_length=225,blank=True)
    star = models.DecimalField(max_digits=9, decimal_places=0,blank=True)
    comment = models.CharField(max_length=225,blank=True)
    image = models.ImageField(blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name