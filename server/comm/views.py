from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, Tag, BlogPost, Comment, Like, Follow, Topic
from .serializers import BlogPostListSerializer, TopicListSerializer, UserSerializer, TagSerializer, TopicSerializer, BlogPostSerializer, CommentSerializer, LikeSerializer, FollowSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='find/(?P<username>\w+)')
    def find_user(self, request, username=None):
        user = User.objects.filter(username=username).first()
        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_serializer_context(self):
        # Pass the request object to the serializer context
        return {'request': self.request}

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>\d+)')
    def user_posts(self, request, user_id=None, *args, **kwargs):
        # Retrieve and return the user's blog posts
        user = get_object_or_404(User, pk=user_id)
        posts = BlogPost.objects.filter(user=user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     # Associate the current user with the 'user' field during creation
    #     serializer.save(user=self.request.user)

    def get_serializer_class(self):
        # Use different serializers for different request methods
        if self.request.method == 'POST':
            return BlogPostSerializer
        elif self.request.method == 'GET':
            # You need to create BlogPostListSerializer for GET requests
            return BlogPostListSerializer
        return BlogPostSerializer  # Fallback to the default serializer for other methods


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
