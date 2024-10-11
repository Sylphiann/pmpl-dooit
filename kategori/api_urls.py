from django.urls import path
from .api_views import KategoriListCreateAPIView

urlpatterns = [
    path('', KategoriListCreateAPIView.as_view(), name='kategori-list-create'),
]
