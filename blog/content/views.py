from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from content.serializers import PostSerializer
from content.models import BlogPost
from content.paginators import BlogPagination
from content.permissions import (
    BlogPostPermissions,
)


class BlogListCreateView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    serializer_class = PostSerializer
    pagination_class = BlogPagination
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get("user", None)
        if id:
            queryset = queryset.filter(user__id=id)
        return queryset


class BlogRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [BlogPostPermissions]
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]
    queryset = BlogPost.objects.all()
