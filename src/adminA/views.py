import os
from pathlib import Path

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from adminA import serializers
from adminA import models
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.response import Response


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


# 主页
class IndexViewSet(ModelViewSet):

    def list(self, request, *args, **kwargs):
        html_data = get_html_data()
        if not html_data:
            data = '404'
            return HttpResponse(content=data, status=404)
        return HttpResponse(content=html_data, status=200)


# adminA配置
class AdminAConfViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        ):
    serializer_class = serializers.AdminAConfSerializer
    queryset = models.AdminAConfModel.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        conf_obj = models.AdminAConfModel.objects.filter().order_by('updated_at').last()
        if not conf_obj:
            return HttpResponse(content='配置文件没找到', status=404)
        serializer_obj = serializers.AdminAConfSerializer(conf_obj, context=self.get_serializer_context())
        data = serializer_obj.data

        return Response(data, status=200)
