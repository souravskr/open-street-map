var mymap = L.map("mapid").setView([47.533935, -52.750408], 13);

L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
    accessToken:
      "pk.eyJ1Ijoic291cmF2c2tlciIsImEiOiJja2trZnRucmoxNGhqMm9xa2xtaDQ4M2NyIn0.YnBUzjEk9B-QfhglG1P96w",
  }
).addTo(mymap);

var marker = L.marker([47.533935, -52.750408]).addTo(mymap);

var circle = L.circle([47.533935, -52.750408], {
  color: "red",
  fillColor: "#f03",
  fillOpacity: 0.5,
  radius: 50,
}).addTo(mymap);

var polygon = L.polygon([
  [47.533935, -52.750408],
  [47.533935, -52.750408],
  [47.533935, -52.750408],
]).addTo(mymap);

var popup = L.popup();

function onMapClick(e) {
  popup
    .setLatLng(e.latlng)
    .setContent("You clicked the map at " + e.latlng.toString())
    .openOn(mymap);
}

mymap.on("click", onMapClick);
