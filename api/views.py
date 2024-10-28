from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from api.serializers import MembroSerializer
from rest_framework import status
from .models import Membro

class MembroAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            membros = Membro.objects.get(pk=pk)
            serializer = MembroSerializer(membros)
        else:
            membros = Membro.objects.all()
            serializer = MembroSerializer(membros, many=True)
        return Response(serializer.data, status=status.HTTP_200_ok)
        
    def post(self, request):
        serializer = MembroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)