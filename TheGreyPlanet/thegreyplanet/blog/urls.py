from django.urls import include, path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about-us',views.about,name='about'),
    path('posts/<post_title>',views.post,name='posts'),
    path('section/<section>',views.section,name='section'),
    path('donate',views.donate,name='donate'),
    path('search',views.search,name='search'),
    path('contact',views.contact,name='contact'),
    path('preview',views.preview, name='preview'),
    path('preview/posts/<post_title>',views.preview_posts, name='preview_posts'),

]