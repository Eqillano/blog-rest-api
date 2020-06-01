from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from comments.api.serializers import CommentSerializer

from posts.models import Post
from comments.models import Comment

from accounts.api.serializers import UserDetailSerializer


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
    )
    #delete_url = HyperlinkedIdentityField(
    #view_name='posts-api:delete ',
    #lookup_field='slug'
    #)
    user = UserDetailSerializer(read_only=True)
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
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
        'id',
        'title',
        'slug',
        'content',
        'markdown',
        'publish',
        'user',
        'image',
        'comments'
        ]

    def get_markdown(self,obj):
        return obj.get_markdown()


    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments
