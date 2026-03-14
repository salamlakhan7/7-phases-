from rest_framework import serializers
from . models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields= ['owner']