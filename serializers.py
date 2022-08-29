from rest_framework import serializers

from .models import Day
class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        # 出力したいフィールド名をタプルで(括弧とカンマ)で定義します。
        fields = '__all__'
