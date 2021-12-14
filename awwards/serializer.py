from rest_framework import serializers
from .models import Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio', 'user', 'phone','address']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description','technologies_used', 'post_date','project_image','repo_link','live_link','user']