from django.contrib import admin

from .models import Choice, Question

# Register your models here.

class ChoiceInline(admin.TabularInline):    #StackedInline took up too much screen space.
    model = Choice # Choice objects are edited on the Question admin page.
    extra = 3   # Default: provide 3 fields for 3 choices.

class QuestionAdmin(admin.ModelAdmin):
    """ Customize the admin change list """
    # The default display is a str() of each object. I changed it below to display a tuple of field names, as columns.
    list_display =('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date'] # Adds a Filter sidebar that allows users to filter the change list by the pub_date field.

    search_fields = ['question_text']
    # Adds a search box at the top of the change list
    # which Django can use to search, using a LIKE ques the question_text field when someone enters search terms.

    fieldsets = [
    (None,                  {'fields': ['question_text']}), # The first element of each tuple in fieldsets is the title of the fieldset.
    ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    #'pub_date', 'question_text'
    ] # Makes the "publication date" come before the "Question" field.
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin) #register Question objects with an admin interface.
