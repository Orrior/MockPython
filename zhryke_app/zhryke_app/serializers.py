from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Message
        read_only_fields = ('id', 'pub_date', 'edit_date')
        fields = ['id', 'owner', 'username', 'text', 'pub_date', 'edit_date']


class UserSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Message.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'messages']
