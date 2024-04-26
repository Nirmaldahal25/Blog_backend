from django.urls import path
from content.views import (
    BlogListCreateView,
    BlogRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("<int:pk>/", BlogRetrieveUpdateDestroyView.as_view(), name="blog_rud"),
    path("", BlogListCreateView.as_view(), name="blog_list_create"),
]
