from django.contrib import admin
from .models import Author, Blog, Product, Promotion, Review, Collection
# Register your models here.

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Review)
admin.site.register(Collection)
