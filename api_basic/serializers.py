from rest_framework import serializers
from .models import Article, Devices, Sells
from django.contrib.auth.models import User


# model serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article  # what model you want to serialize
        # fields = ['id', 'title', 'author','email']
        fields = '__all__'


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'


class SellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sells
        fields = '__all__'

