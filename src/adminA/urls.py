from rest_framework.routers import DefaultRouter
from adminA import views

router_admin = DefaultRouter()
router_admin.register('adminA', views.TestViewSet, basename='adminA')
