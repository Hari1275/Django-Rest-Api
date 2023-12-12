from rest_framework import serializers

from .models import Author, Blog, Product, Collection, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')


class BlogSerializer(serializers.ModelSerializer):
    authorName = AuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'date_added', 'authorName']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
