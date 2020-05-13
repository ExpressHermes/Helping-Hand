from django.shortcuts import render,redirect
from mainapp.models import Event
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    events = Event.objects.all()
    events_food = Event.objects.filter(event_type='Food')
    events_clothes = Event.objects.filter(event_type='Clothes')
    events_medical = Event.objects.filter(event_type='Medical')
    events_other = Event.objects.filter(event_type='Other')
    # print(events_food, events_clothes, events_other, events_medical)
    context = {
                'events': events,
                'events_clothes': events_clothes,
                'events_food': events_food,
                'events_medical': events_medical,
                'events_other': events_other,
    }
    return render(request, 'mainapp/home.html', context)



@login_required
def create_event(request):
    if request.method == 'POST':
        event_organizer = request.POST.get('event_organizer')
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        event_type = request.POST.get('event_type')
        place_name = request.POST.get('place_name')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        event = Event(event_organizer=event_organizer, event_name=event_name,
                       event_date=event_date, description=description,
                       place_name=place_name, event_type=event_type,
                       lat=lat, lon=lon)
        event.save()
        return redirect('mainapp:home_page')
    return render(request, 'mainapp/create_event.html')
