from django.shortcuts import render
from .models import Book
from rest_framework.response import Response
from .serializer import BookSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
class BookAPI(GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = {'user' : request.user.id}
        for i in request.data:
            data[i] = request.data[i]
        print(data)
        serializer = BookSerializer(data = data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)
    def get(self, request):
        serializer = BookSerializer(Book.objects.filter(user = request.user), many = True)
        return Response(serializer.data)
    def patch(self, request):
        try:
            serializer = BookSerializer(Book.objects.get(id = request.data['id'] , user = request.user), data = request.data, partial = True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        except KeyError:
            return Response({'id':['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        try:
            book = Book.objects.get(id = request.data['id'], user = request.user)
            book.delete()
            return Response({'message':'book deleted successfully'})
        except KeyError:
            return Response({'id':['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)