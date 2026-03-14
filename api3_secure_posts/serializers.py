from rest_framework import serializers
from . models import SecurePost

class SecurePostSerializers(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SecurePost
        fields = '__all__'
        read_only_fields= ['owner']