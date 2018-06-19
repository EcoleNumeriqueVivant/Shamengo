function initMap() {
  map = new google.maps.Map(document.getElementById('map-details'), {
    zoom: 10,
    center: new google.maps.LatLng(46.2276,2.2137),
    map:map
  });
  var marker = new google.maps.Marker({
    position: {lat: geo_address({{entry.adresse[0]}}), lng: geo_address({{entry.adresse[1]}})},
    map: map
  });

}
