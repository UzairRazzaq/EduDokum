from django.http import HttpResponse
from .models import University, Program
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def programs(request):
    program_list = Program.objects.order_by('id')
    context = {'program_list': program_list}
    return render(request, 'eduPk/programs.html', context)
    # return HttpResponse(output)