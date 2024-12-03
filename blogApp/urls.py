from  django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('blog_list/',views.blog_list,name='blog_list'),
    path('more/<int:pk>',views.more,name='more'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('remove/<int:pk>',views.remove,name='remove'),
    path('editBlog/<int:pk>',views.editBlog,name="editBlog")

]