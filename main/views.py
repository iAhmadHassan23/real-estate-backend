from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Homepage, HomeBlog, HomeCategory, HomeReview, HomeStep, BlogImage, BlogPost, MainSite
from .serializers import HomePageSerializer, HomeBlogSerializer, HomeCategorySerializer, HomeReviewSerializer, HomeStepSerializer, BlogImageSerializer, BlogPostSerializer, MainSiteSerializer

# Create your views here.


@api_view(['GET'])
def getHomePageDetails(request):
    home = Homepage.objects.all()
    serailizer = HomePageSerializer(home, many=True)
    return Response({'home detail':serailizer.data})


@api_view(['POST'])
def createHomePage(request):
    data = request.data

    print(data)

    home_category = HomeCategory.objects.create(
        title = data['title'],
        icon = data['icon']
    )
    home_category.save()

    home_step = HomeStep.objects.create(
        title = data['title'],
        description = data['description'],
        icon = data['icon'],
        icon_color = data['icon_color'],
        icon_color_bg = data['icon_color_bg']
    )
    home_step.save()

    blog_posts = BlogPost.objects.create(
        title = data['title'],
        price = data['price'],
        star = data['star'],
        image = data['image']
    )
    blog_posts.save()

    blog_images = BlogImage.objects.create(
        image = data['image']
    )
    blog_images.save()

    home_blog = HomeBlog.objects.create(
        title = data['title'],
        description = data['description'],
        title_direction = data['title_direction'],
        Blog_image = blog_images,
        Blog_posts = blog_posts
    )
    home_blog.save()

    home_review = HomeReview.objects.create(
        name = data['name'],
        profession = data['profession'],
        star = data['star'],
        comment = data['comment'],
        image = data['image'],
    )
    home_review.save()

    home = Homepage.objects.create(
        Home_title= data['Home_title'],
        Home_tagline= data['Home_tagline'],
        Home_button= data['Home_button'],
        Home_button_link= data['Home_button_link'],
        Home_bgimg= data['Home_bgimg'],
        Home_category= home_category,

        HIW_title= data['HIW_title'],
        HIW_tagline= data['HIW_tagline'],
        HIW_steps= home_step,

        Experts_title= data['Experts_title'],
        Experts_tagline= data['Experts_tagline'],
        Experts_blogs= home_blog,

        Rev_title= data['Rev_title'],
        Rev_tagline= data['Rev_tagline'],
        Rev_reviews= home_review,
    )
    home.save()

    serailizer = HomePageSerializer(home, many=True)
    return Response({'home detail created':serailizer.data})