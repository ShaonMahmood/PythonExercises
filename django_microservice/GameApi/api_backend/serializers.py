from rest_framework import serializers
from .models import Game


class GamesListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = ('name', 'image_url', 'category')

    def get_image_url(self, game):
        request = self.context.get('request')
        photo_url = game.image.url
        return request.build_absolute_uri(photo_url)
