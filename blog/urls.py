from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.get_all_blogs, name='home'),
    path('blog/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('myblogs/', views.get_user_blogs, name='myblogs'),
    path('delete-task/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]