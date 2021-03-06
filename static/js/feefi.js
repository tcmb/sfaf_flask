mapboxgl.accessToken = 'pk.eyJ1IjoidGNtYiIsImEiOiJjajJ4am9hczAwMDdpMndubzhyMDNkOXpzIn0.9HuZArmMyqiP-QzCY2diGA';

if (!document.offlineMode) {

    var map = new mapboxgl.Map({
        container: 'map-one', // container id
        style: 'mapbox://styles/mapbox/streets-v10',
        center: [13.45, 52.47], // starting position
        zoom: 11 // starting zoom
    });

    map.addControl(new mapboxgl.NavigationControl());

    map.on('click', function (e) {
        document.getElementById("home_loc_lat").value = e.lngLat.lat.toFixed(2);
        document.getElementById("home_loc_lon").value = e.lngLat.lng.toFixed(2);
    });
}

window.onload = function() {

    ride_button = document.getElementById('activity_type_ride');
    run_button = document.getElementById('activity_type_run');

    ride_button.onclick = activityTypeHandler;
    run_button.onclick = activityTypeHandler;
}

function activityTypeHandler(e) {
    if (ride_button.checked) {
        document.getElementById('min_activity_length').value = 100;
    } else {
        document.getElementById('min_activity_length').value = 10;
    };
}
