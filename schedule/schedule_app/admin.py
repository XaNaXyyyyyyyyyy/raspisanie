from django.contrib import admin

from . models import Group, Event, Weekday, Schedule, Lesson

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Weekday)
admin.site.register(Schedule)
admin.site.register(Lesson)


