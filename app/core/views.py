from django.shortcuts import render
from rest_framework.views import APIView
from .models import Carro
from rest_framework.response import Response
from rest_framework import status
class MyApiView(APIView):
    def get(self,request):
        carros = Carro.objects.all()[0]
        return Response({"Carro":carros.modelo},status.HTTP_202_ACCEPTED)


# Create your views here.
