from django.contrib import admin

from .models import Faq, Inquiry, Answer



@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'updated_at')
    search_fields = ('title',)
    list_filter=('category',)

class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    actions = ['make_messagemail']
    list_display = ('title','category', 'created_by','state')
    search_fields = ('title','email','phone','created_by__username',)
    list_filter=('category','state',)
    inlines = [
        AnswerInline,
    ]

    def make_messagemail(self, request, queryset):
        for post in list(queryset):
            if post.is_email == True:
                print("이메일 발송")
            if post.is_phone == True:
                print("메시지 발송")
    make_messagemail.short_description="답변 완료 문자&메일 발송"

