from .views import BlogPostRudView

from django.urls import path
from django.conf.urls import url
from .views import BlogPostRudView, BlogPostAPIView

app_name = 'postings'

urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name ='post-create'),
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name ='post-rud')
]