from django.contrib import admin
from .models import Leads
from .profile import ProfileRecords

class ProfileRecordsInline(admin.TabularInline):
    model = ProfileRecords
    extra = 0

@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'value')
    list_filter = ('source',)
    search_fields = ('name', 'description')
    inlines = [ProfileRecordsInline]

@admin.register(ProfileRecords)
class ProfileRecordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'leads', 'source', 'follower', 'following', 'company', 'email')
    list_filter = ('source',)
    search_fields = ('name', 'username', 'company', 'email')
    ordering = ('id',)
from django.contrib import admin
from .models import Leads, Task, LeadsEmail

 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'lead', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'lead__name')

@admin.register(LeadsEmail)
class LeadsEmailAdmin(admin.ModelAdmin):
    list_display = ('email_subject',)
    search_fields = ('email_subject',)

