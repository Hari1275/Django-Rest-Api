from rest_framework import generics
from django.db.models.aggregates import Count

from .models import Author, Blog, Product, Collection, Review
from .serializers import AuthorSerializer, BlogSerializer, ProductSerializer, CollectionSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .filters import ProductFilter
from .pagination import DefaultPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['collection_id']
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    pagination_class = DefaultPagination

    # def get_queryset(self):

    #     queryset = Product.objects.all()

    #     collection_id = self.request.query_params.get('collection_id')

    #     if collection_id is not None:

    #         queryset = queryset.filter(collection_id=collection_id)

    #     return queryset

    def get_context_data(self):

        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'product cannot be deleted'})
        return self.destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):

    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(
        product_Count=Count('products')).all()

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'product cannot be deleted'})
        return self.destroy(request, *args, **kwargs)


class BlogList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        location = self.request.query_params.get('blog')
        if location is not None:
            queryset = queryset.filter(authorName=location)
        return queryset


class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Blog.objects.all()


class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Blog.objects.all()


class ReviewViewSet(ModelViewSet):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):

        return {'product_id': self.kwargs['product_pk']}
