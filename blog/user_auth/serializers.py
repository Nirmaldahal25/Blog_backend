from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=False
    )
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=False
    )

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "password",
            "password2",
            "email",
            "username",
        )

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        password2 = validated_data.pop("password2", None)
        if password or password2:
            if password != password2:
                raise serializers.ValidationError({"password do not match"})
            else:
                validated_data["password"] = make_password(password)

        return super().update(instance, validated_data)
