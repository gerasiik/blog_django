from django.urls import path
from coder.views import coder

urlpatterns = [
    path("", coder, name="coder"),
]
