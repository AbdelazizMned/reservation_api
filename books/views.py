from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorator.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .modesl import books
from .serializers import BookSerializer


@csrf_exempt
def book_list(request):
  if request.method == 'GET':
    books_list = books.objects.all()
    serializer = BookSerializer(books_list, many=True)
    return JsonResponse(serializer.data, safe=False)