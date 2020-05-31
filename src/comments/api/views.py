
from django.db.models import Q


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin,UpdateModelMixin

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

#from rest_framework.pagination import LimitOffSetPagination,PageNumberPagination

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from comments.models import Comment

from posts.api.pagination import PostLimitOffsetPagination,PostPagePagination
from posts.api.permissions import IsOwnerOrReadOnly

from .serializers import (
    CommentSerializer,
    CommentDetailSerializer,
    CommentChildSerializer,
    create_comment_serializer
    )


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get('slug')
        parent_id = self.request.GET.get('parent_id',None)
        return create_comment_serializer(model_type='post',slug=slug,parent_id=parent_id,user=self.request.user)






class CommentDetailAPIView(DestroyModelMixin,UpdateModelMixin,RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def put(self,request,*args,**kwargs):
        return self.update(reqeust,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)







class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagenation_class = PostPagePagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list
