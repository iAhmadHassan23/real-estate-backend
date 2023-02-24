from django.urls import path
from main import views



urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name="user-profile"),
    path('users/profile/update/', views.updateUserProfile, name="user-profile-update"),

    path('users/', views.getUsers, name="users"),

    path('get/homepage/', views.getHomePageDetails, name="homepage"),
    path('get/main/', views.getMainDetails, name="main"),
    path('upload/image/', views.uploadImage, name="upload-image"),
    path('update/main/', views.updateMain, name="update-main"),
    path('update/home/', views.updateHomePage, name="update-homepage"),

    path('all/reviews/', views.allReviews, name="all-reviews"),
    path('create/review/', views.createReview, name="create-review"),
    path('get/review/<str:id>/', views.getReview, name="get-review"),
    path('update/review/<str:id>/', views.updateReview, name="update-review"),
    path('delete/review/<str:id>/', views.deleteReview, name="delete-review"),

    path('all/blogs/', views.allBlogs, name="all-Blogs"),
    path('create/blog/', views.createBlog, name="create-Blog"),
    path('get/blog/<str:id>/', views.getBlog, name="get-Blog"),
    path('update/blog/<str:id>/', views.updateBlog, name="update-Blog"),
    path('delete/blog/<str:id>/', views.deleteBlog, name="delete-Blog"),

    path('all/blog/articles/', views.allBlogArticles, name="all-Blog-Articles"),
    path('create/blog/articles/', views.createBlogArticles, name="create-Blog-Articles"),
    path('get/blog/articles/<str:id>/', views.getBlogArticles, name="get-Blog-Articles"),
    path('update/blog/articles/<str:id>/', views.updateBlogArticles, name="update-Blog-Articles"),
    path('delete/blog/articles/<str:id>/', views.deleteBlogArticles, name="delete-Blog-Articles"),

    path('send/quotation/', views.sendQuotation, name="send-quotation"),
    path('send/contactus/', views.sendContactUs, name="send-ContactUs"),
]
