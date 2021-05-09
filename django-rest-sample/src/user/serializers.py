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

        user.set_password(validated_data["password"])
        user.save()

        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    mobile_no = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("id", "name", "email", "mobile_no", "password", "company")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=validated_data["email"],
            name=validated_data["name"],
            mobile_no=validated_data["mobile_no"],
            company=validated_data["company"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
