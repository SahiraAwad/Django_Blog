from django.contrib import admin
from .models import Post , Category , Comment


class ProductAdmin(admin.ModelAdmin):
    list_display =['title','draft','category']
    list_filter=['draft','tags','category']
    search_fields =['title']


admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)

# Register your models here.
