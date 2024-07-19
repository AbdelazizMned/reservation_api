from rest_framework import serializers
from .models import books

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = books
    fields = ('title', 'author')
    