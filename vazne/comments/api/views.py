from django.db.models import Q
from rest_framework.filters import (SearchFilter , OrderingFilter)
from rest_framework.generics import (CreateAPIView , DestroyAPIView , ListAPIView , UpdateAPIView , RetrieveAPIView , RetrieveUpdateAPIView)
from rest_framework.permissions import (AllowAny , IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly )
from comments.api.models import Comment
from .serializers import commentSerializer

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    
class CommentListAPIView(ListAPIView):
    serializer_class = commentSerializer
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ['content' , 'user__first_name']
    
    def get_queryset(self , *args , **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query :
            queryset_list = queryset_list.filter(
                Q(content__icontains = query)|
                Q(User__first_name__icontains = query)|
                Q(User__last_name__icontains = query)).distinct()
            return queryset_list
    