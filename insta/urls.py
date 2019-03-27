from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.feed,name = 'feed'),
    url('^add/image/$',views.add_picture,name = 'add_pic'),
    url('^add/profile/$',views.add_profile,name = 'add_profile'),
    url('^my_profile/$',views.my_profile,name = 'my_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^profile/(\d+)',views.profile,name = 'profile'),
    url('^follow/(\d+)',views.follow,name = 'follow'),
    url('^like/(\d+)',views.like_image,name = 'like'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)