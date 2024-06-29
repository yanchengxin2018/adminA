from rest_framework import serializers
from all_model import models


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ('id', 'username', 'name',)
