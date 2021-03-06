from rest_framework import serializers
from app.models import *


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.movie_name= validated_data.get('movie_name',instance.movie_name)
        instance.language = validated_data.get('language', instance.language)
        instance.year = validated_data.get('year', instance.year)
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance

