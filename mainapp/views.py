from django.shortcuts import render,redirect
from mainapp.models import helping_hand
# Create your views here.

def home_page(request):
    return render(request, 'mainapp/home.html')


def map(request):
    if request.method == 'POST':
        lon = request.POST.get('lon')
        lat = request.POST.get('lat')
        print(f'lon: {lon}, lat: {lat}')
        new_req=helping_hand(event_name=request.POST['eventOrganizer'],date=request.POST['eventDate'],
        place_name=request.POST['placeName'],longt=request.POST['lon'],lati=request.POST['lat'])
        new_req.save()
        return redirect('mainapp:map')
    return render(request, 'mainapp/map.html')
