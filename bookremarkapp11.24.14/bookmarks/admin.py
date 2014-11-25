from django.contrib import admin

from bookmarks.models import UserProfile
from bookmarks.models import Link
from bookmarks.models import LinkList


admin.site.register(UserProfile)
admin.site.register(Link)
admin.site.register(LinkList)


class LinkListAdmin(admin.ModelAdmin):
  list_display = ('name', 'link', 'tags')
  list_display_links = ('name', 'tags')
   
  
  
  
