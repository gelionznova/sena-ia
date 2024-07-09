from rest_framework.routers import DefaultRouter
from points.api.views import PointApiViewSet

router_point = DefaultRouter()
router_point.register(
    prefix= "points", basename= "points", viewset=PointApiViewSet
)