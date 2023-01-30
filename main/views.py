from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Homepage, HomeBlog, HomeCategory, HomeReview, HomeStep, BlogImage, BlogPost, MainSite, HomeBlogArticle
from .serializers import HomePageSerializer, MainSiteSerializer, UserSerializer, UserSerializerWithToken, HomeBlogArticleSerializer

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
    serailizer = HomePageSerializer(home[:1], many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def getMainDetails(request):
    main = MainSite.objects.all()
    serailizer = MainSiteSerializer(main, many=True)
    return Response(serailizer.data)


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
def updateHomePage(request):
    user = request.user
    data = request.data
    home = Homepage.objects.get(id=data['id'])
    
    
    for category in data['Home_category']:
        home_category = HomeCategory.objects.get(id=category['id'])
        home_category.title = category['title']
        print(category['icon'])
        if '/images/'+str(home_category.icon) != category['icon']:
            home_category.icon = category['icon']
        home_category.save()
    for steps in data['HIW_steps']:
        home_step = HomeStep.objects.get(id=steps['id'])
        home_step.title = steps['title']
        home_step.description = steps['description']
        if '/images/'+str(home_step.icon) != steps['icon']:
            home_step.icon = steps['icon']
        home_step.icon_color = steps['icon_color']
        home_step.icon_color_bg = steps['icon_color_bg']
        home_step.save()
    for blogs in data['Experts_blogs']:
        home_blog = HomeBlog.objects.get(id=blogs['id'])
        home_blog.title = blogs['title']
        home_blog.user = user
        home_blog.description = blogs['description']
        home_blog.title_direction = blogs['title_direction']
        home_blog.blog_options = blogs['blog_options']
        if len(blogs['Blog_image']) == 0:
            for posts in blogs['Blog_posts']:
                blog_posts = BlogPost.objects.get(id=posts['id'])
                blog_posts.title = posts['title']
                blog_posts.price = posts['price']
                blog_posts.star = posts['star']
                if '/images/'+str(blog_posts.image) != posts['image']:
                    blog_posts.image = posts['image']
                blog_posts.save()
        else:
            for image in blogs['Blog_image']:
                blog_images = BlogImage.objects.get(id=image['id'])
                if '/images/'+str(blog_images.image) != image['image']:
                    blog_images.image = image['image']
                blog_images.save()
        home_blog.save()
    for article in data['Blog_articles']:
        home_blog_article = HomeBlogArticle.objects.get(id=article['id'])
        home_blog_article.title = article['title']
        home_blog_article.user = user
        home_blog_article.description = article['description']
        if '/images/'+str(home_blog_article.image) == article['image']:
            home_blog_article.image = article['image']
        home_blog_article.save()
    for review in data['Rev_reviews']:
        home_review = HomeReview.objects.get(id=review['id'])
        home_review.name = review['name']
        home_review.profession = review['profession']
        home_review.star = review['star']
        home_review.comment = review['comment']
        if '/images/'+str(home_review.image) == review['image']:
            home_review.image = review['image']
        home_review.save()

    home.Home_title= data['Home_title']
    home.Home_tagline= data['Home_tagline']
    home.Home_button= data['Home_button']
    home.Home_button_link= data['Home_button_link']
    if '/images/'+str(home.Home_bgimg) != data['Home_bgimg']:
        home.Home_bgimg= data['Home_bgimg']
    home.HIW_title= data['HIW_title']
    home.HIW_tagline= data['HIW_tagline']
    home.Experts_title= data['Experts_title']
    home.Experts_tagline= data['Experts_tagline']
    home.Rev_title= data['Rev_title']
    home.Rev_tagline= data['Rev_tagline']

    home.save()

    serailizer = HomePageSerializer(home, many=False)
    return Response({'home detail updated':serailizer.data})


@api_view(['PUT'])
def updateMain(request):
    data = request.data

    main = MainSite.objects.get(id=data['id'])
    main.title= data['title']
    if '/images/'+str(main.favicon) != data['favicon']:
        main.favicon = data['favicon']
    if '/images/'+str(main.head_logo) != data['head_logo']:
        main.head_logo = data['head_logo']
    if '/images/'+str(main.foot_logo) != data['foot_logo']:
        main.foot_logo = data['foot_logo']
    main.foot_copyright = data['foot_copyright']
    main.facebook_link = data['facebook_link']
    main.facebook_link = data['facebook_link']
    main.instagram_link = data['instagram_link']
    main.twitter_link = data['twitter_link']
    main.youtube_link = data['youtube_link']
    main.linkin_link = data['linkin_link']
    main.save()
    
    serailizer = MainSiteSerializer(main, many=False)
    return Response({'main detail updated':serailizer.data})









