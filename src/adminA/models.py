from django.db import models


# auto配置文件
class AdminAConfModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    code = models.CharField(help_text="项目代码", max_length=100, )
    data = models.TextField(null=True, help_text="配置数据", )
    close = models.BooleanField(default=False, help_text="禁用", )
