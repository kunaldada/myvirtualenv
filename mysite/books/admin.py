from django.contrib import admin
from .models import Publisher, Author, Book, FoodItems

class FoodItemsAdmin(admin.ModelAdmin):
    list_display = ('desc', 'image')
    search_fields = ('desc', 'image')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(FoodItems, FoodItemsAdmin)
# Register your models here.
