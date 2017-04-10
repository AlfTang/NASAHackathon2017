from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'message':'Hello DeSciNerds!'}
	return render(request, 'playground/index.html', context)