from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Homepage, HomeBlog, HomeCategory, HomeReview, HomeStep, BlogImage, BlogPost, MainSite, HomeBlogArticle, MetaData
from .serializers import HomePageSerializer, MainSiteSerializer, UserSerializer, UserSerializerWithToken, HomeBlogSerializer, HomeReviewSerializer

import json

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

from PIL import Image  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadImage(request):
    data = request.data
    print(data['image'])
    picture = Image.open(data['image'])  
    picture = picture.save('images/' + str(data['image_name']) + '.' + str(data['image_format'])) 
    return Response({'/' + str(data['image_name']) + '.' + str(data['image_format'])})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateHomePage(request):
    user = request.user
    data = request.data
    home = Homepage.objects.get(id=data['id'])

    for category in data['Home_category']:
        if category['id'] != '':
            home_category = HomeCategory.objects.get(id=category['id'])
            home_category.title = category['title']
            print(category['icon'])
            if '/images/'+str(home_category.icon) != category['icon']:
                home_category.icon = category['icon']
            home_category.save()
        else:
            home_category = HomeCategory.objects.create(
                title = category['title'],
                icon = category['icon']
            )
            home_category.save()
            home.Home_category.add(home_category)


    for steps in data['HIW_steps']:
        if steps['id'] != '':
            home_step = HomeStep.objects.get(id=steps['id'])
            home_step.title = steps['title']
            home_step.description = steps['description']
            if '/images/'+str(home_step.icon) != steps['icon']:
                home_step.icon = steps['icon']
            home_step.save()
        else:
            home_step = HomeStep.objects.create(
                title = steps['title'],
                description = steps['description'],
                icon = steps['icon']
            )
            home_step.save()
            home.HIW_steps.add(home_step)

    for blogs in data['Experts_blogs']:
        home_blog=HomeBlog.objects.get(id=blogs['id'])
        home_blog.title=blogs['title']
        home_blog.user=user
        home_blog.description=blogs['description']
        home_blog.short_description=blogs['short_description']
        home_blog.title_direction=blogs['title_direction']
        home_blog.blog_options=blogs['blog_options']
        if len(blogs['Blog_image']) == 0:
            for posts in blogs['Blog_posts']:
                blog_posts=BlogPost.objects.get(id=posts['id'])
                blog_posts.title=posts['title']
                blog_posts.price=posts['price']
                blog_posts.star=posts['star']
                if '/images/'+str(blog_posts.image) != posts['image']:
                    blog_posts.image=posts['image']
                blog_posts.save()
        else:
            for image in blogs['Blog_image']:
                blog_images=BlogImage.objects.get(id=image['id'])
                if '/images/'+str(blog_images.image) != image['image']:
                    blog_images.image=image['image']
                blog_images.save()
        home_blog.save()
        

        
    for article in data['Blog_articles']:
        home_blog_article=HomeBlogArticle.objects.get(id=article['id'])
        home_blog_article.title=article['title']
        home_blog_article.user=user
        home_blog_article.description=article['description']
        if '/images/'+str(home_blog_article.image) == article['image']:
            home_blog_article.image=article['image']
        home_blog_article.save()
    for review in data['Rev_reviews']:
        if review['id'] != '':
            home_review=HomeReview.objects.get(id=review['id'])
            home_review.name=review['name']
            home_review.profession=review['profession']
            home_review.star=review['star']
            home_review.comment=review['comment']
            if '/images/'+str(home_review.image) == review['image']:
                home_review.image=review['image']
            home_review.save()
        else:
            home_review = HomeReview.objects.create(
                name = review['name'],
                profession = review['profession'],
                star = review['star'],
                comment = review['comment'],
                image = review['image'],
            )
            home_review.save()
            home.Rev_reviews.add(home_review)
            

    home.Home_title=data['Home_title']
    home.Home_tagline=data['Home_tagline']
    home.Home_button=data['Home_button']
    home.Home_button_link=data['Home_button_link']
    if '/images/'+str(home.Home_bgimg) != data['Home_bgimg']:
        home.Home_bgimg=data['Home_bgimg']
    home.HIW_title=data['HIW_title']
    home.HIW_tagline=data['HIW_tagline']
    home.Experts_title=data['Experts_title']
    home.Experts_tagline=data['Experts_tagline']
    home.Rev_title=data['Rev_title']
    home.Rev_tagline=data['Rev_tagline']

    home.save()

    serailizer=HomePageSerializer(home, many=False)
    return Response({'home detail updated': serailizer.data})


@ api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMain(request):
    data=request.data

    main=MainSite.objects.get(id=data['id'])

    metaSet = json.loads(data['Main_metadata'])

    all_meta = main.Main_metadata.all()

    meta_id_list = all_meta.values_list('id')


    for meta in all_meta:
        in_list = ['true' for item in metaSet if item['id'] == meta.id]

        if 'true' not in in_list:
            ingrDelete = MetaData.objects.get(id=meta.id)
            ingrDelete.delete()
            print('work3')

    for metadata in metaSet:
        in_list = ['true' for item in meta_id_list if item[0] == metadata['id']]

        if 'true' in in_list:
            main_metadata=MetaData.objects.get(id=metadata['id'])
            main_metadata.name=metadata['name']
            main_metadata.content=metadata['content']
            main_metadata.save()
        elif 'true' not in in_list:
            main_metadata=MetaData.objects.create(
                name=metadata['name'],
                content=metadata['content']
            )
            main_metadata.save()
            main.Main_metadata.add(main_metadata)
    


    main.title=data['title']
    if '/images/'+str(main.favicon) != data['favicon']:
        main.favicon=data['favicon']
    if '/images/'+str(main.head_logo) != data['head_logo']:
        main.head_logo=data['head_logo']
    if '/images/'+str(main.foot_logo) != data['foot_logo']:
        main.foot_logo=data['foot_logo']
    main.foot_copyright=data['foot_copyright']
    main.facebook_link=data['facebook_link']
    main.facebook_link=data['facebook_link']
    main.instagram_link=data['instagram_link']
    main.twitter_link=data['twitter_link']
    main.youtube_link=data['youtube_link']
    main.linkin_link=data['linkin_link']


    main.save()

    serailizer=MainSiteSerializer(main, many=False)
    return Response({'main detail updated': serailizer.data})


@api_view(['GET'])
def allReviews(request):
    review = HomeReview.objects.all()
    serailizer = HomeReviewSerializer(review, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def getReview(request, id):
    review = HomeReview.objects.get(id=id)
    serailizer = HomeReviewSerializer(review, many=False)
    return Response(serailizer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createReview(request):
    data = request.data

    if data['name'] == '':
        return Response('Please Enter Name')
    if data['profession'] == '':
        return Response('Please Enter Profession')
    if data['star'] == '':
        return Response('Please Enter Star')
    if data['comment'] == '':
        return Response('Please Enter Comment')
    if data['image'] == '':
        return Response('Please Enter Image')
    
    else:
        review = HomeReview.objects.create(
            name = data['name'],
            profession = data['profession'],
            star = data['star'],
            comment = data['comment'],
            image = data['image'],
        )
        review.save()
        serailizer = HomeReviewSerializer(review, many=False)
        return Response(serailizer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateReview(request, id):
    data = request.data

    if data['name'] == '':
        return Response('Please Enter Name')
    if data['profession'] == '':
        return Response('Please Enter Profession')
    if data['star'] == '':
        return Response('Please Enter Star')
    if data['comment'] == '':
        return Response('Please Enter Comment')
    if data['image'] == '':
        return Response('Please Enter Image')

    review = HomeReview.objects.get(id=id)
    review.name = data['name']
    review.profession = data['profession']
    review.star = data['star']
    review.comment = data['comment']
    if '/images/'+str(review.image) != data['image']:
        review.image = data['image']
    review.save()
    serailizer = HomeReviewSerializer(review, many=False)
    return Response(serailizer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteReview(request, id):
    review = HomeReview.objects.get(id=id)
    review.delete()
    serailizer = HomeReviewSerializer(review, many=False)
    return Response("Review Deleted")


@api_view(['GET'])
def allBlogs(request):
    blogs = HomeBlog.objects.all()
    serailizer = HomeBlogSerializer(blogs, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def getBlog(request, id):
    blog = HomeBlog.objects.get(id=id)
    serailizer = HomeBlogSerializer(blog, many=False)
    return Response(serailizer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createBlog(request):
    data = request.data
    user = request.user

    if data['title'] == '':
        return Response('Please Enter Title')
    if data['description'] == '':
        return Response('Please Enter Description')
    if data['blog_options'] == '':
        return Response('Please Enter Blog_options')
    if len(data['Blog_image']) == 0:
        for post in data['Blog_posts']:
            if post['image'] == '':
                return Response('Please Enter Post Image')
            if post['title'] == '':
                return Response('Please Enter Post Title')
            if post['star'] == '':
                return Response('Please Enter Post Star')
            if post['price'] == '':
                return Response('Please Enter Post Price')
    else:
        for image in data['Blog_image']:
            if image['image'] == '':
                return Response('Please Enter Post Image')

    blog = HomeBlog.objects.create(
        user = user,
        title = data['title'],
        description = data['description'],
        short_description = data['short_description'],
        blog_options = data['blog_options']
    )
    blog.save()

    if len(data['Blog_image']) != 0:
        for image in data['Blog_image']:
            blog_image = BlogImage.objects.create(
                image = image['image']
            )
            blog_image.save()
            blog.Blog_image.add(blog_image)
    else:
        for post in data['Blog_posts']:
            blog_post = BlogPost.objects.create(
                title= post['title'],
                star = post['star'],
                price = post['price'],
                image = post['image']
            )
            blog_post.save()
            blog.Blog_image.add(blog_post)

    serailizer = HomeBlogSerializer(blog, many=False)
    return Response(serailizer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateBlog(request, id):
    data = request.data
    user = request.user
    blog = HomeBlog.objects.get(id=id)

    if data['title'] == '':
        return Response('Please Enter Title')
    if data['description'] == '':
        return Response('Please Enter Description')
    if data['blog_options'] == '':
        return Response('Please Enter Blog_options')
    if len(data['Blog_image']) == 0:
        for post in data['Blog_posts']:
            if post['image'] == '':
                return Response('Please Enter Post Image')
            if post['title'] == '':
                return Response('Please Enter Post Title')
            if post['star'] == '':
                return Response('Please Enter Post Star')
            if post['price'] == '':
                return Response('Please Enter Post Price')
    else:
        for image in data['Blog_image']:
            if image['image'] == '':
                return Response('Please Enter Post Image')

    blog.title=data['title']
    blog.user=user
    blog.description=data['description']
    blog.short_description=data['short_description']
    blog.blog_options=data['blog_options']

    if len(blog['Blog_image']) == 0:
        for posts in blog['Blog_posts']:
            blog_posts = BlogPost.objects.get(id=posts['id'])
            blog_posts.title=posts['title']
            blog_posts.price=posts['price']
            blog_posts.star=posts['star']
            if '/images/'+str(blog_posts.image) != posts['image']:
                blog_posts.image=posts['image']
            blog_posts.save()
    else:
        for image in blog['Blog_image']:
            blog_images=BlogImage.objects.get(id=image['id'])
            if '/images/'+str(blog_images.image) != image['image']:
                blog_images.image=image['image']
            blog_images.save()

    blog.save()
    serailizer = HomeBlogSerializer(blog, many=False)
    return Response(serailizer.data)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBlog(request, id):
    blog = HomeBlog.objects.get(id=id)
    print(blog)
    blog.delete()
    serailizer = HomeBlogSerializer(blog, many=False)
    return Response("Blog Deleted")