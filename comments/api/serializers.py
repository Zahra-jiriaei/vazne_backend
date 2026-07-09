from rest_framework.serializers import (HyperlinkedIdentityField, ModelSerializer, SerializerMethodField)
from comments.api.models import Comment

class commentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'parent', 'content']
        
        