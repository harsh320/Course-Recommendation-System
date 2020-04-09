from django.contrib import admin
from course.models import Subjects,Branch,Content,Thread,Comment,ItemTag,Tags
# Register your models here.
admin.site.register(Subjects)
admin.site.register(Content)
admin.site.register(Branch)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(ItemTag)
admin.site.register(Tags)