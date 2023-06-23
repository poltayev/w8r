from django.urls import path

from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('merchants', views.RestaurantViewSet, basename='merchants')
router.register('branchs', views.BranchViewSet, basename='branchs')

branchs_router = routers.NestedDefaultRouter(router, 'branchs', lookup='branch')
branchs_router.register('menu', views.MenuViewSet, basename='branch-menu')

urlpatterns = router.urls + branchs_router.urls