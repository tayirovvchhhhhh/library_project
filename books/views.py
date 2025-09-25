from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from yaml import serialize_all

from .serializers import BookSerializers
from .models import BooksModel
from rest_framework import generics, status


#
# class BookListApiView(generics.ListAPIView):
#     queryset = BooksModel.objects.all()
#     serializer_class = BookSerializers
#
class BookListApiView(APIView):
    def get(self, request):
        books = BooksModel.objects.all()
        serializer_data = BookSerializers(books, many=True).data

        data = {
            'count books':f"We have {len(books)} books",
            'books':serializer_data,
        }
        return Response(data)
#detail view
# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = BooksModel.objects.all()
#     serializer_class = BookSerializers

class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = BooksModel.objects.get(id=pk)
            serializers_data = BookSerializers(book).data
            data = {
                'status':'Succesfull',
                'book':serializers_data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status':"Doesn't exists",
                'message':"Book isn't found"}, status=status.HTTP_404_NOT_FOUND
            )




#delete view
class BookDeleteApiView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializers

#update view
class BookUpdateApiView(generics.UpdateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializers


# class BookUpdateApiView(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(BooksModel, id=pk)
#         serializer = BookSerializers(book)
#         return Response(serializer.data)
#
#
#
#
#     def put(self, request, pk):
#         book = get_object_or_404(BooksModel, id=pk)
#         data = request.data
#         serializer = BookSerializers(instance=book, data=data, partial=False)
#         if serializer.is_valid(raise_exception=True):
#             book_save = serializer.save()
#         return Response({
#
#
#             'status':True,
#             'message':f"Book {book_save.title} update successfully"
#
#         })
#






#create view
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = BooksModel.objects.all()
#     serializer_class = BookSerializers



class BookCreateApiView(APIView):
    def post(self, request):

        data = request.data
        serializer = BookSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"status" : f"Create data",
                    "books":data
                    }
        return Response(data)






#creat list api view


class BookCreateListApiView(generics.ListCreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializers


# class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BooksModel.objects.all()
#     serializer_class = BookSerializers

class BookUpdateDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = BooksModel.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    'status':"True",
                    'message':'Successfully deleted'
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response({
                'status':False,
                'message':'Book is not found'
            },status=status.HTTP_400_BAD_REQUEST)




# #function drf
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = BooksModel.objects.all()
#     serializers = BookSerializers(books, many=True)
#     return Response(serializers.data)















class BookViewSet(ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_name = BookSerializers
