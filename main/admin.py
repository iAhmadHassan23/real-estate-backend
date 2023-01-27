from django.contrib import admin
from .models import Homepage, HomeBlog, HomeCategory, HomeReview, HomeStep, BlogImage, BlogPost, MainSite, HomeBlogArticle

# Register your models here.

admin.site.register(MainSite)
admin.site.register(Homepage)
admin.site.register(HomeBlog)
admin.site.register(HomeCategory)
admin.site.register(HomeReview)
admin.site.register(HomeStep)
admin.site.register(BlogImage)
admin.site.register(BlogPost)
admin.site.register(HomeBlogArticle)