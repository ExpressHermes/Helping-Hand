from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'mainapp/home.html')


def map(request):
    if request.method == 'POST':
        # TODO [INCOMPLETE]
        lon = request.POST.get('lon')
        lat = request.POST.get('lat')
        print(f'lon: {lon}, lat: {lat}')
    return render(request, 'mainapp/map.html')
