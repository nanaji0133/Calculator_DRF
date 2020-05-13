from django.urls import path
from .views import CalcApiView

urlpatterns = [path("", CalcApiView.as_view(), name="calculator")]
