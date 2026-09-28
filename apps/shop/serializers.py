from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

    def validate_title(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                'Название магазина должно содержать минимум 2 символа.'
            )
        return value

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError(
                'Рейтинг должен быть от 0 до 5.'
            )
        return value