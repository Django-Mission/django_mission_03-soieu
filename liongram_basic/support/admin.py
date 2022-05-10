from django.contrib import admin

from .models import Faq, Inquiry, Answer

@admin.register(Faq)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'updated_at')
    search_fields = ('title',)
    list_filter=('category',)

class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Inquiry)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'created_by')
    search_fields = ('title','email','phone',)
    list_filter=('category',)
    inlines = [
        AnswerInline,
    ]
