from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from comments.api.serializers import CommentSerializer

from posts.models import Post
from comments.models import Comment


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
    )
    #delete_url = HyperlinkedIdentityField(
    #view_name='posts-api:delete ',
    #lookup_field='slug'
    #)
    user = SerializerMethodField()
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

    def get_user(self,obj):
        return str(obj.user.username)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
        'title',
        'content',
        'publish'
        ]




class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
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

    def get_user(self,obj):
        return str(obj.user.username)

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
