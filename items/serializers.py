from rest_framework import serializers
from items.models import LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from todoapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'published_date', 'created_date', 'code', 'linenos', 'language', 'style', 'author')


#class UserSerializer(serializers.ModelSerializer):
#    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

#    class Meta:
#        model = User
#        fields = ('id', 'username', 'items')

# Hyperlinking the API, django-rest-framework tutorial part 5
class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'text', 'author', 'published_date', 'created_date',
                  'title', 'code', 'linenos', 'language', 'style')


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)

#    class Meta:
#        model = User
#        fields = ('url', 'id', 'username', 'items')
