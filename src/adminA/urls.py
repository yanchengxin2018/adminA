from rest_framework.routers import DefaultRouter
from adminA import views
from django.conf import settings

ROUTER = settings.ADMIN_A.get('ROUTER', {})

router_admin = DefaultRouter()

# 配置文件
# router_admin.register(r'^.*assistant/$', views.AdminAConfViewSet, basename='conf')
router_admin.register(r'conf', views.AdminAConfViewSet, basename='conf')

# 主页
router_index = ROUTER.get('index', {})
prefix = router_index.get('prefix', 'adminA')
basename = router_index.get('basename', prefix)
router_admin.register(prefix, views.IndexViewSet, basename=basename)
