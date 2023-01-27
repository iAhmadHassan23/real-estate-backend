from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Homepage, HomeBlog, HomeCategory, HomeReview, HomeStep, BlogImage, BlogPost, MainSite, HomeBlogArticle

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']
    
    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class HomePageSerializer(serializers.ModelSerializer):
    Home_category = serializers.SerializerMethodField(read_only=True)
    HIW_steps = serializers.SerializerMethodField(read_only=True)
    Experts_blogs = serializers.SerializerMethodField(read_only=True)
    Blog_articles = serializers.SerializerMethodField(read_only=True)
    Rev_reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Homepage
        fields = '__all__'
    
    def get_Home_category(self, obj):
        Home_category = obj.Home_category.all()
        serializer = HomeCategorySerializer(Home_category, many=True)
        return serializer.data
    
    def get_HIW_steps(self, obj):
        HIW_steps = obj.HIW_steps.all()
        serializer = HomeStepSerializer(HIW_steps, many=True)
        return serializer.data
    
    def get_Experts_blogs(self, obj):
        Experts_blogs = obj.Experts_blogs.all()
        serializer = HomeBlogSerializer(Experts_blogs, many=True)
        return serializer.data

    def get_Blog_articles(self, obj):
        Blog_articles = obj.Blog_articles.all()
        lastTwo = Blog_articles[::-1]
        serializer = HomeBlogArticleSerializer(lastTwo[:3], many=True)
        return serializer.data
    
    def get_Rev_reviews(self, obj):
        Rev_reviews = obj.Rev_reviews.all()
        serializer = HomeReviewSerializer(Rev_reviews, many=True)
        return serializer.data


class HomeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeCategory
        fields = '__all__'


class HomeStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeStep
        fields = '__all__'


class HomeBlogSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    Blog_image = serializers.SerializerMethodField(read_only=True)
    Blog_posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = HomeBlog
        fields = '__all__'
    
    def get_Blog_image(self, obj):
        Blog_image = obj.Blog_image.all()
        serializer = BlogImageSerializer(Blog_image, many=True)
        return serializer.data
    
    def get_Blog_posts(self, obj):
        Blog_posts = obj.Blog_posts.all()
        serializer = BlogPostSerializer(Blog_posts, many=True)
        return serializer.data
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'


class HomeBlogArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = HomeBlogArticle
        fields = '__all__'
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class HomeReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HomeReview
        fields = '__all__'


class MainSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainSite
        fields = '__all__'