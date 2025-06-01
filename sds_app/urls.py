from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SDSRecordViewSet, SDSUploadView

router = DefaultRouter()
router.register(r'sds', SDSRecordViewSet)

urlpatterns = [
    path('upload/', SDSUploadView.as_view()),
    path('', include(router.urls)),
]
