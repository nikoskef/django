from django.shortcuts import render
from django.http import HttpResponse

from rooms.models import Room
from companies.models import Company


def index(request):
    rooms2 = Room.objects.order_by('-list_date').filter(is_published=True)[:2]
    rooms3 = Room.objects.order_by('-list_date').filter(is_published=True)[2:5]
    category_choices = Room.CATEGORY_CHOICES
    duration_choices = Room.DURATION_CHOICES

    context = {
        'rooms2': rooms2,
        'rooms3': rooms3,
        'category_choices': category_choices,
        'duration_choices': duration_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    companies = Company.objects.order_by('name')

    mvp_companies = Company.objects.all().filter(is_mvp=True)

    context = {
        'companies': companies,
        'mvp_companies': mvp_companies
    }

    return render(request, 'pages/about.html', context)
