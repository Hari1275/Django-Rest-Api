from django.contrib import admin
from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)


products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-review')
urlpatterns = router.urls + products_router.urls
# urlpatterns = [
#    path('blog',BlogList.as_view()),
#    path('blog/<int:pk>/',BlogDetails.as_view()),
#    path('author',AuthorList.as_view()),
#    path('author/<int:pk>',AuthorDetails.as_view())
# ]
