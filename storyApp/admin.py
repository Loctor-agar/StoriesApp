from django.contrib import admin

from .models import Subscriber,UserStoryFile,StoryFile,Story,Project
# Register your models here.
admin.site.register(Subscriber)
admin.site.register(UserStoryFile)
admin.site.register(StoryFile)
admin.site.register(Story)
admin.site.register(Project)

admin.site.site_title = "Strories admin"
admin.site.site_header = "Strories admin"