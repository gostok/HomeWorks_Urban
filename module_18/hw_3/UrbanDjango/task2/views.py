from django.shortcuts import render
from django.views.generic import TemplateView


class Temp1(TemplateView):
    template_name = 'class_template.html'

def temp2(request):
    return render(request, 'func_template.html')

