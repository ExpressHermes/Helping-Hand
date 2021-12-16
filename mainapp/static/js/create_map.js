mapboxgl.accessToken = 'pk.eyJ1IjoiamFudXNpaSIsImEiOiJjazl6d2IzdmYxMnJsM21wazB3a2llY2lwIn0.pLRf45aHIwdJ6dypoH0qSA';
var map = new mapboxgl.Map({
container: 'map', // Container ID
style: 'mapbox://styles/mapbox/streets-v11', // Map style to use
center: [80.33111, 26.4725], // Starting position [lng, lat]
zoom: 10, // Starting zoom level
});

// var marker = new mapboxgl.Marker() // Initialize a new marker
// 	.setLngLat([-122.25948, 37.87221]) // Marker [lng, lat] coordinates
// 	.addTo(map); // Add the marker to the map

var geocoder = new MapboxGeocoder({ // Initialize the geocoder
accessToken: mapboxgl.accessToken, // Set the access token
mapboxgl: mapboxgl, // Set the mapbox-gl instance
marker: true, // Use the default marker style
placeholder: 'Search for places in Kanpur', // Placeholder text for the search bar
bbox: [80.1158526594972, 26.18205430711, 80.5538117327514, 26.6400085677318], // Boundary for Berkeley
proximity: {
  longitude: 80.33111,
  latitude: 26.4725
} // Coordinates of Kanpur
});

// Add the geocoder to the map
// map.addControl(geocoder);
document.getElementById('geocoder').appendChild(geocoder.onAdd(map));
map.addControl(new mapboxgl.NavigationControl());

// After the map style has loaded on the page,

map.on('load', function() {
  // Listen for the `result` event from the Geocoder
  // `result` event is triggered when a user makes a selection
  // Add a marker at the result's coordinates
  geocoder.on('result', function(ev) {
    var lon = ev.result.geometry.coordinates[0]
    var lat = ev.result.geometry.coordinates[1]
    document.querySelector('#lon').value = lon
    document.querySelector('#lat').value = lat
    document.querySelector('#place_name').value = ev.result.text
    // console.log(typeof(lon))
    // console.log(typeof(lat))
    console.log(ev.result.text)

    // create DOM element for the marker
    var el = document.createElement('div');
    el.id = 'marker';

    // create the marker
    new mapboxgl.Popup()
        .setLngLat(ev.result.geometry.coordinates.slice())
        .setHTML(ev.result.text)
        .addTo(map);
    });
});