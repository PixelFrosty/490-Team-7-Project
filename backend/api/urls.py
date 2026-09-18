from django.urls import path
from . import views

urlpatterns = [
    # go to /api/test/ to test the API
    path('test/', views.test_api, name='test_api'),
]