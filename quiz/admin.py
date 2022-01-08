from django.contrib import admin
from .models import Attempt, Question, Attempter, Answer, Quizzes

# Register your models here.

admin.site.register(Attempt)
admin.site.register(Question)
admin.site.register(Attempter)
admin.site.register(Answer)
admin.site.register(Quizzes)
