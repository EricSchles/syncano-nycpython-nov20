from django.contrib import admin
from forms.models import Question,Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ 
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
        ('Question Text',{'fields':['question_text'], 'classes':['collapse']} ),
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
