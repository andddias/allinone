from django.urls import path, include
from .views import IndexView, upload

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('upload/', upload, name='upload'),
]
