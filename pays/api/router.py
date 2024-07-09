from rest_framework.routers import DefaultRouter
from pays.api.views import PayApiViewSet

router_pay = DefaultRouter()

router_pay.register(
    prefix="pays", basename="pays", viewset=PayApiViewSet
)