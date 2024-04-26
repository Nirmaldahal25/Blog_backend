from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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


class BlogRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [BlogPostPermissions]
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]
