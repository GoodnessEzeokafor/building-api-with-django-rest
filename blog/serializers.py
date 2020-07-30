
from rest_framework import serializers
from blog.models import Tag, Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "email")
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("pk", "name")


class PostSerializers(serializers.ModelSerializer):
    tags = TagSerializer(many=True,required=False,read_only=True)
    author  = UserSerializer(required=False,read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)


    class Meta:
        model = Post
        fields = ("pk", "title", "text", "tags", "author", "image")
        