import os

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from adminA import serializers
from all_model import models
from server import settings
from pathlib import Path


# 得到静态网页的二进制数据
def get_html_data():
    parent = Path(__file__).resolve().parent
    index_path = parent / 'static' / 'adminA' / 'index.html'

    if not os.path.exists(index_path):
        return None
    with open(index_path, 'rb') as file_obj:
        data = file_obj.read()
        try:
            data = data.decode('utf8')
        except UnicodeDecodeError:
            data = data.decode('gbk')
    return data


class TestViewSet(ModelViewSet):
    serializer_class = serializers.TestSerializer
    queryset = models.UserModel.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        html_data = get_html_data()
        if not html_data:
            data = '404'
            return HttpResponse(content=data, status=404)
        return HttpResponse(content=html_data, status=200)
