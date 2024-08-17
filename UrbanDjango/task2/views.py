from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def get_template(request):
    return render(request,
                  'second_task/func_template.html')


class TaskView(TemplateView):
    template_name = 'second_task/class_template.html'
