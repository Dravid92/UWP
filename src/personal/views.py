from django.shortcuts import render
from personal.models import Question
# Create your views here.
# this links the base.html and home.html
def home_screen_view(request):
	
	context = {}
	questions = Question.objects.all()
	context['questions'] = questions
	return render(request,'personal/home.html',context) 