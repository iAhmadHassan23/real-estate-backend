from django.db import models

# Create your models here.


class MainSite(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    favicon = models.ImageField(null=True, blank=True, default='/placeholder.png')
    head_logo = models.ImageField(null=True, blank=True, default='/placeholder.png')
    foot_logo = models.ImageField(null=True, blank=True, default='/placeholder.png')
    facebook_link = models.CharField(max_length=225,blank=True,null=True)
    instagram_link = models.CharField(max_length=225,blank=True,null=True)
    twitter_link = models.CharField(max_length=225,blank=True,null=True)
    youtube_link = models.CharField(max_length=225,blank=True,null=True)
    linkin_link = models.CharField(max_length=225,blank=True,null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Homepage(models.Model):
    Home_title = models.CharField(max_length=225,blank=True,null=True)
    Home_tagline = models.CharField(max_length=225,blank=True,null=True)
    Home_button = models.CharField(max_length=225,blank=True,null=True)
    Home_button_link = models.CharField(max_length=225,blank=True,null=True)
    Home_bgimg = models.ImageField(null=True, blank=True, default='/placeholder.png')
    Home_category = models.ManyToManyField('HomeCategory', blank=True)

    HIW_title = models.CharField(max_length=225,blank=True,null=True)
    HIW_tagline = models.CharField(max_length=225,blank=True,null=True)
    HIW_steps = models.ManyToManyField('HomeStep', blank=True)

    Experts_title = models.CharField(max_length=225,blank=True,null=True)
    Experts_tagline = models.CharField(max_length=225,blank=True,null=True)
    Experts_blogs = models.ManyToManyField('HomeBlog', blank=True)

    Rev_title = models.CharField(max_length=225,blank=True,null=True)
    Rev_tagline = models.CharField(max_length=225,blank=True,null=True)
    Rev_reviews = models.ManyToManyField('HomeReview', blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Home_title


class HomeCategory(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    icon = models.ImageField(null=True, blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class HomeStep(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    description = models.CharField(max_length=225,blank=True,null=True)
    icon = models.ImageField(null=True, blank=True, default='/placeholder.png')
    icon_color = models.CharField(max_length=225,blank=True,null=True)
    icon_color_bg = models.CharField(max_length=225,blank=True,null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

DIRECTION_CHOICES =(
    ("1", "Left"),
    ("2", "Right"),
)

class HomeBlog(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    description = models.CharField(max_length=225,blank=True,null=True)
    title_direction = models.CharField(choices = DIRECTION_CHOICES, max_length=225,blank=True,null=True)
    Blog_image = models.ManyToManyField('BlogImage', blank=True)
    Blog_posts = models.ManyToManyField('BlogPost', blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0,null=True, blank=True)
    star = models.DecimalField(max_digits=9, decimal_places=0,null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')


class HomeReview(models.Model):
    name = models.CharField(max_length=225,blank=True,null=True)
    profession = models.CharField(max_length=225,blank=True,null=True)
    star = models.DecimalField(max_digits=9, decimal_places=0,null=True, blank=True)
    comment = models.CharField(max_length=225,blank=True,null=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')

    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name