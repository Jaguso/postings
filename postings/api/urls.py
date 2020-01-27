from .views import BlogPostRudView

from django.urls import path
from django.conf.urls import url
from .views import BlogPostRudView

app_name = 'postings'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name ='post-rud')
]