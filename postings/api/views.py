# generic views
from rest_framework import generics

from .serializers import BlogPostSerializer
from postings.models import BlogPost

class BlogPostAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return


class BlogPostRudView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)

    
