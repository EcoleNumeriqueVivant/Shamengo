function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 5,
    center: new google.maps.LatLng(46.2276,2.2137),
    map:map
  });
  // var marker = new google.maps.Marker({
  //   position: {lat: geo_address({{entry.adresse[0]}}), lng: geo_address({{entry.adresse[1]}})},
  //   map: map
  // });
  window.eqfeed_callback = function(results) {
    for (var i = 0; i < results.features.length; i++) {
    var coords = results.features[i].geometry.coordinates;
    var latLng = new google.maps.LatLng(geo_address({{entry.adresse[0]}}),geo_address({{entry.adresse[1]}}));
    var marker = new google.maps.Marker({
      position: latLng,
      map: map
    });
  }
}
