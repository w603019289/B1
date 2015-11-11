from django.contrib import admin

# Register your models here.
from books.models import book,Author
 
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
    search_fields=('first_name','last_name')

admin.site.register(book)
admin.site.register(Author)   
    