from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import BooksModel


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.replace(" ", "").isalpha():
            raise ValidationError({
                'status':False,
                'message':'iltimos kitobni sarlavhasi hariflardan tashkil topgan bolishi kerak '
            })
        if BooksModel.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status':False,
                    'message':"title and author shoulded pair"
                }
            )
        return data

    def validate_price(self, price):
        if price<0 or price > 10000000:
            raise ValidationError(
                {
                    'status':'False',
                    'message':"No to'g'ri narh kiritlgan"
                }
            )
        return price
