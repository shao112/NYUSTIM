from django.contrib import admin
from .models import Members, Competition, Appointment

# Register your models here.

admin.site.site_header = '雲科大資管系系排管理中心'
admin.site.site_title = '雲科大資管系系排管理中心'
admin.site.index_title = '管理中心'

# 客製化欄位顯示
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'grade', 'position', 'created_date', 'update_date')
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'editor', 'type', 'created_date', 'update_date')
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'date', 'time', 'email', 'msg', 'created_date', 'update_date')

# admin要註冊才可以管理這些Table
admin.site.register(Members, MembersAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Appointment, AppointmentAdmin)