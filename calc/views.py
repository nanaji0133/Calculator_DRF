from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class CalcApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "calc/index.html"

    def get(self, request):
        return Response({})
