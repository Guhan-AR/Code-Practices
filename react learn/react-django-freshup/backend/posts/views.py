from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.parsers import MultiPartParser, FormParser

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostSerializer
    # parsers are going to be used to handle file uploads
    parser_classes = (MultiPartParser, FormParser)