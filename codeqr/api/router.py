from rest_framework.routers import DefaultRouter
from codeqr.api.views import CodeqrApiViewSet

router_codeqr = DefaultRouter()

router_codeqr.register(prefix="codeqr", basename="codeqr", viewset=CodeqrApiViewSet)
