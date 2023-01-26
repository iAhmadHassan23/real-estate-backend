from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Homepage, HomeBlog, HomeCategory, HomeReview, HomeStep, BlogImage, BlogPost, MainSite
from .serializers import HomePageSerializer, MainSiteSerializer, UserSerializer, UserSerializerWithToken

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializers = UserSerializerWithToken(self.user).data
        for k, v in serializers.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serailizer = UserSerializerWithToken(user, many=False)
    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != "":
        user.password = make_password(data['password'])
    
    user.save()

    return Response(serailizer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serailizer = UserSerializer(user, many=False)
    return Response(serailizer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serailizer = UserSerializer(users, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def getHomePageDetails(request):
    home = Homepage.objects.all()
    serailizer = HomePageSerializer(home, many=True)
    return Response({'home detail':serailizer.data})


@api_view(['GET'])
def getMainDetails(request):
    main = MainSite.objects.all()
    serailizer = MainSiteSerializer(main, many=True)
    return Response({'main detail':serailizer.data})


# @api_view(['POST'])
# def createHomePage(request):
#     data = request.data

#     print(data)

#     home_category = HomeCategory.objects.create(
#         title = data['title'],
#         icon = data['icon']
#     )
#     home_category.save()

#     home_step = HomeStep.objects.create(
#         title = data['title'],
#         description = data['description'],
#         icon = data['icon'],
#         icon_color = data['icon_color'],
#         icon_color_bg = data['icon_color_bg']
#     )
#     home_step.save()

#     blog_posts = BlogPost.objects.create(
#         title = data['title'],
#         price = data['price'],
#         star = data['star'],
#         image = data['image']
#     )
#     blog_posts.save()

#     blog_images = BlogImage.objects.create(
#         image = data['image']
#     )
#     blog_images.save()

#     home_blog = HomeBlog.objects.create(
#         title = data['title'],
#         description = data['description'],
#         title_direction = data['title_direction'],
#         Blog_image = blog_images,
#         Blog_posts = blog_posts
#     )
#     home_blog.save()

#     home_review = HomeReview.objects.create(
#         name = data['name'],
#         profession = data['profession'],
#         star = data['star'],
#         comment = data['comment'],
#         image = data['image'],
#     )
#     home_review.save()

#     home = Homepage.objects.create(
#         Home_title= data['Home_title'],
#         Home_tagline= data['Home_tagline'],
#         Home_button= data['Home_button'],
#         Home_button_link= data['Home_button_link'],
#         Home_bgimg= data['Home_bgimg'],
#         Home_category= home_category,

#         HIW_title= data['HIW_title'],
#         HIW_tagline= data['HIW_tagline'],
#         HIW_steps= home_step,

#         Experts_title= data['Experts_title'],
#         Experts_tagline= data['Experts_tagline'],
#         Experts_blogs= home_blog,

#         Rev_title= data['Rev_title'],
#         Rev_tagline= data['Rev_tagline'],
#         Rev_reviews= home_review,
#     )
#     home.save()

#     serailizer = HomePageSerializer(home, many=True)
#     return Response({'home detail created':serailizer.data})


@api_view(['PUT'])
def updateHomePage(request, id):
    user = request.user
    data = request.data

    home = Homepage.objects.filter(id=id)
    home_category = HomeCategory.objects.filter(id=data['home_category'])
    home_step = HomeStep.objects.filter(id=data['home_step'])
    blog_posts = BlogPost.objects.filter(id=data['blog_posts'])
    blog_images = BlogImage.objects.filter(id=data['blog_images'])
    home_blog = HomeBlog.objects.filter(id=data['home_blog'])
    home_review = HomeReview.objects.filter(id=data['home_review'])

    home_category.title = data['hc_title']
    home_category.icon = request.FILES.get('hc_icon')

    home_step.title = data['hs_title']
    home_step.description = data['hs_description']
    home_step.icon = request.FILES.get('hs_icon')
    home_step.icon_color = data['hs_icon_color']
    home_step.icon_color_bg = data['hs_icon_color_bg']

    blog_posts.title = data['bp_title'],
    blog_posts.price = data['bp_price'],
    blog_posts.star = data['bp_star'],
    blog_posts.image = request.FILES.get('bp_image')

    blog_images.image = request.FILES.get('bi_image')

    home_blog.title = data['hb_title'],
    home_blog.user = user,
    home_blog.description = data['hb_description'],
    home_blog.title_direction = data['hb_title_direction'],
    home_blog.blog_options = data['hb_blog_options'],
    home_blog.Blog_image = blog_images,
    home_blog.Blog_posts = blog_posts

    home_review.name = data['hr_name'],
    home_review.profession = data['hr_profession'],
    home_review.star = data['hr_star'],
    home_review.comment = data['hr_comment'],
    home_review.image = request.FILES.get('hr_image'),

    home.Home_title= data['Home_title'],
    home.Home_tagline= data['Home_tagline'],
    home.Home_button= data['Home_button']
    home.Home_button_link= data['Home_button_link']
    home.Home_bgimg= request.FILES.get('Home_bgimg')
    home.Home_category= home_category
    home.HIW_title= data['HIW_title']
    home.HIW_tagline= data['HIW_tagline']
    home.HIW_steps= home_step
    home.Experts_title= data['Experts_title']
    home.Experts_tagline= data['Experts_tagline']
    home.Experts_blogs= home_blog
    home.Rev_title= data['Rev_title']
    home.Rev_tagline= data['Rev_tagline']
    home.Rev_reviews= home_review,

    serailizer = HomePageSerializer(home, many=True)
    return Response({'home detail updated':serailizer.data})


@api_view(['PUT'])
def updateMain(request, id):
    data = request.data

    main = MainSite.objects.filter(id=id)

    main.title= data['title']
    main.favicon = request.FILES.get('favicon')
    main.head_logo = request.FILES.get('head_logo')
    main.foot_logo = request.FILES.get('foot_logo')
    main.facebook_link = data['facebook_link']
    main.instagram_link = data['instagram_link']
    main.twitter_link = data['twitter_link']
    main.youtube_link = data['youtube_link']
    main.linkin_link = data['linkin_link']

    
    serailizer = MainSiteSerializer(main, many=True)
    return Response({'main detail updated':serailizer.data})
