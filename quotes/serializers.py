# from django.contrib.auth.models import Group, User
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

from quotes.models import Quote
from rest_framework import serializers
from taggit.serializers import TagListSerializerField


class QuoteSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Quote
        fields = ['quote', 'tags']