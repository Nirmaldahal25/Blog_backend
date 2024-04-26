from rest_framework import serializers
from content.models import BlogPost


class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(write_only=True, required=False)
    username = serializers.CharField(source="user.username", read_only=True)
    image_url = serializers.SerializerMethodField(method_name="get_image_url")

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "date",
            "content",
            "user",
            "thumbnail",
            "username",
            "image_url",
        )

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.thumbnail:
            return request.build_absolute_uri(obj.thumbnail.url)
        return ""
