from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.base.models import InfoUser,Secondary,Testim

admin.site.register(InfoUser)
admin.site.register(Secondary)
admin.site.register(Testim)
admin.site.unregister(User)
admin.site.unregister(Group)