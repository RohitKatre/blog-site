from django.conf.urls import url
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',BlogListView.as_view(), name="blog_list_view" ),
    url(r'^create/$',BlogCreateView.as_view(), name="blog_create_view" ),
    url(r'^(?P<pk>\d+)/$',BlogDetailView.as_view(), name="blog_detail_view" ),
    url(r'^post/(?P<pk>\d+)/comment/$', AddComment.as_view(), name='add_comment_to_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
