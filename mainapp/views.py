from django.shortcuts import render,redirect
from mainapp.models import Events
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    events = Events.objects.all()
    return render(request, 'mainapp/home.html', {'events': events})



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
        event = Events(event_organizer=event_organizer, event_name=event_name,
                       event_date=event_date, description=description,
                       place_name=place_name, event_type=event_type,
                       lat=lat, lon=lon)
        event.save()
        return redirect('mainapp:home_page')
    return render(request, 'mainapp/create_event.html')
