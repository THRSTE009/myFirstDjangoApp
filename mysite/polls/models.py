import datetime

from django.db import models
from django.utils import timezone

#each field is represented by an instance of a Field class that tells Django what type of data each field holds.
#Some fields have required arguments. Eg CharField requires max_length.
#The name of each field will be used as the column name by the db. E.g question_text in machine-friendly format.
#A relationship is defined using ForeignKey.

class Question(models.Model) :
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #defined a human-readable name for Question.pub_date.
    ##Each Choice is related to a single Question.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
            return self.choice_text    
