from django.shortcuts import render,redirect
from mainapp.models import Event
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    id = request.GET.get('id')
    events = Event.objects.all()
    events_food = Event.objects.filter(event_type='Food')
    events_clothes = Event.objects.filter(event_type='Clothes')
    events_medical = Event.objects.filter(event_type='Medical')
    events_other = Event.objects.filter(event_type='Other')
    # print(events_food, events_clothes, events_other, events_medical)

    try:
        user = request.user
    except:
        user = None
    if user is not None and user.is_authenticated:
        if id:
            event = Event.objects.filter(id=id).first()
            if user in event.interested.all():
                event.interested.remove(user)
            else:
                event.interested.add(user)
            event.save()
        for event in events:
            print(event.interested.all())
            if user in event.interested.all():
                event.is_interested = True
            else:
                event.is_interested = False
    else:
        user = None
    context = {
                'events': events,
                'events_clothes': events_clothes,
                'events_food': events_food,
                'events_medical': events_medical,
                'events_other': events_other,
                'user': user,
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
