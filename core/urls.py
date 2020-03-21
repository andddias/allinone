from django.urls import path, include
from .views import IndexView, FileFildView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('upload/', FileFildView.as_view(), name='upload'),
]
