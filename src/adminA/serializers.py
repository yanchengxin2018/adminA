from rest_framework import serializers
from adminA import models


# AdminA配置文件
class AdminAConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdminAConfModel
        fields = ('id', 'created_at', 'updated_at', 'code', 'data', 'close',)
