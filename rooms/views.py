from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Room


def index(request):
    rooms = Room.objects.order_by('-list_date').filter(is_published=True)
    category_choices = Room.CATEGORY_CHOICES
    duration_choices = Room.DURATION_CHOICES

    paginator = Paginator(rooms, 6)
    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)

    context = {
        'rooms': paged_rooms
    }

    return render(request, 'rooms/rooms.html', context)


def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    ratings = {
        'item': 3
    }

    context = {
        'room': room,
        'ratings': ratings
    }

    return render(request, 'rooms/room.html', context)


def search(request):
    queryset_list = Room.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        # if city:
            # queryset_list = queryset_list.filter(city__iexact=city)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    # Duration
    if 'duration' in request.GET:
        duration = request.GET['duration']
        if duration:
            queryset_list = queryset_list.filter(duration__iexact=duration)

    category_choices = Room.CATEGORY_CHOICES
    duration_choices = Room.DURATION_CHOICES
    context = {
        'category_choices': category_choices,
        'duration_choices': duration_choices,
        'rooms': queryset_list,
        'values': request.GET
    }
    
    return render(request, 'rooms/search.html', context)
