from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.AboutPage, name='about'),
    path('login/', views.User_Login, name='login'),
    path('logout/', views.User_Logout, name='logout'),
    path('signup/', views.User_SignUp, name='signup'),
    path('profile/<int:id>', views.User_Profile, name='profile'),
    path('post/', views.Post_Create, name='post'),
    path('dboard/', views.DashBoard, name='dboard'),
    path('delete/<int:id>', views.DeletePost, name='delete'),
    path('upadate/<int:id>', views.UpdatePost, name='update'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('refund/', views.refund, name='refund'),
    path('privacy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),


]
