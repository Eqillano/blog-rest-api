from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from posts.models import Post
from .serializers import PostDetailSerializer,PostListSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    #def get_queryset(self,*args,**kwargs):


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
