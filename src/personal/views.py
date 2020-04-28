from django.shortcuts import render

# Create your views here.
# this links the base.html and home.html
def home_screen_view(request):
	
	context = {}
	context['some_string'] = 'Four Themes of UWP'
	context['Themes'] = ' \n- W\n- A\n- S\n- H'

	list_of_values = []
	list_of_values.append('Weather')
	list_of_values.append('Ash')
	list_of_values.append('Sustain')
	list_of_values.append('Health')
	context['list_of_values'] = list_of_values					
	#print(request.headers)
	return render(request,'personal/home.html',context)