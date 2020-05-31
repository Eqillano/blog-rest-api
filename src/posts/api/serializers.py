from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField

from posts.models import Post


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
    )
    delete_url = HyperlinkedIdentityField(
    view_name='posts-api:delete ',
    lookup_field='slug'
    )
    class Meta:
        model = Post
        fields = [
        'user',
        'title',
        'slug',
        'url',
        'content',
        'publish'
        ]


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
        'title',
        'content',
        'publish'
        ]




class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
        'id',
        'title',
        'slug',
        'content',
        'publish'
        ]
