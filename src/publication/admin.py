from django.contrib import admin
from publication.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated", )
    list_editable = ("published", "created_on", )
    
admin.site.register(BlogPost, BlogPostAdmin)