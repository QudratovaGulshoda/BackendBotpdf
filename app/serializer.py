from rest_framework import serializers
from .models import *
class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
        read_only_fields = ['id']