from django.shortcuts import render
from account.models import Account
# Create your views here.
# this links the base.html and home.html
def home_screen_view(request):
	
	context = {}
	accounts = Account.objects.all()
	context['accounts'] =accounts
	return render(request,'personal/home.html',context) 