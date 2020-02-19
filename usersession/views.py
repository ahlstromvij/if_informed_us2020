from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserInputForm

class HomePageView(TemplateView):
	template_name = 'home.html'

def questions(request):
    form = UserInputForm()
    return render(request, 'userinputform.html', {'form':form});
