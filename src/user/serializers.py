from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "password")
        # fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"], name=validated_data["name"]
        )

        print("Validated Data", validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user
