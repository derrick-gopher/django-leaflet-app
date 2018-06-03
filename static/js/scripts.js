var mymap;
var lyrOSM;
var lyrImagery;
var lyrTopo;
var lyrWaterColor;
var lyrOutdoors;
var lyrSearch;
var lyrReports;
var lyrMarkerCluster;
var popZocalo;
var ctlAttribute;
var ctlScale;
var ctlPan;
var ctlZoomslider;
var ctlMouseposition;
var ctlMeasure;
var ctlEasybutton;
var ctlSidebar;
var ctlSearch;
var ctlLayers;
var ctlStyle;
var ctlRouting;

var objBasemaps;
var ObjOverlays;

var markerCurrentLocation;
$(document).ready(function(){
  mymap = L.map('mapdiv',{center:[-0.245, 35.567],zoom:16, zoomControl: false, attributionControl: false})
  ctlPan = L.control.pan().addTo(mymap);
  ctlZoomslider = L.control.zoomslider({position:'topright'}).addTo(mymap);
  ctlSidebar = L.control.sidebar('side-bar').addTo(mymap);
  ctlEasybutton = L.easyButton('glyphicon-transfer', function(){
  ctlSidebar.toggle();}).addTo(mymap);
  ctlSearch = L.Control.openCageSearch({ limit:10}).addTo(mymap);
  ctlAttribute = L.control.attribution({position:'bottomleft'}).addTo(mymap);
  ctlAttribute.addAttribution('OSM');
  ctlAttribute.addAttribution('&copy; <a href="http://reactgis"</a>');
  // **********layer initialization *************

                lyrOSM = L.tileLayer.provider('OpenStreetMap.Mapnik');
                lyrImagery = L.tileLayer.provider('Esri.WorldImagery');
                lyrTopo = L.tileLayer.provider('OpenTopoMap');
                lyrWaterColor = L.tileLayer.provider('Stamen.Watercolor');
                lyrOutdoors = L.tileLayer.provider('Thunderforest.Outdoors');
                mymap.addLayer(lyrOSM);


//    **********************overlay layer control ************

                objBasemaps = {
                    "Open Street Maps" : lyrOSM,
                    "Topo Map" : lyrTopo,
                    "Imagery" : lyrImagery,
                    "Outdoors" : lyrOutdoors,
                    "Watercolor" : lyrWaterColor
                  };

                //   overlays
                lyrMarkerCluster =L.markerClusterGroup();
                lyrReports = L.geoJSON.ajax('http://localhost:8000/data',{pointToLayer:returnIncidenceMarker}).addTo(mymap);
                ObjOverlays = {
                    // "incidences" : lyrReports,
                    "incidences" :lyrMarkerCluster,
                }
               
               
                // all
                ctlLayers = L.control.layers(objBasemaps, ObjOverlays).addTo(mymap);
                lyrReports.on('data:loaded', function(){
                    mymap.fitBounds(lyrReports.getBounds());
                    lyrMarkerCluster.addLayer(lyrReports);
                    lyrMarkerCluster.addTo(mymap);
                
                });
                // ctlRouting = L.Routing.control({waypoints:[L.latLng(-0.245, 35.567),L.latLng(-0.378268, 36.7612328)], router: L.Routing.mapbox('pk.eyJ1IjoiZGVyeSIsImEiOiJjaWY5anJyN3YwMDI5dGNseHoyZzM4Z3R4In0.dToOXYIZ30LH_7VtFbKW4A')}).addTo(mymap);

                $('#btnLocate').click((event)=>{
                    mymap.locate();
                });
                $("#report").click((event)=>{
                    alert("please click on the map.")
                    mymap.on("click", (e)=>{
                        var popupContent = 
                        "<form role='form' id='form' class='form-horizontal'>"+
                        "<div class='form-group'>"+
                        "<label>Date </label"+
                        "<input type='date' id='date'>"+
                        "</div>"+
                        "</form>";
                        L.marker(e.latlng).addTo(mymap).bindPopup(popupContent, {keepInView:true, closeButton:false}).openPopup();
                    })
                })
                mymap.on('locationfound', function(e){
                    console.log(e);
                    if(markerCurrentLocation){
                        markerCurrentLocation.remove();
                    }
                    markerCurrentLocation =  L.circle(e.latlng,
                    {radius: e.accuracy/2}).addTo(mymap);
                    mymap.setView(e.latlng, 14 )
                });
                mymap.on('locationerror', function(e){
                   console.log(e);
                   alert('location was not found');
                });

               


            });

function returnIncidenceMarker(json, latlng){
    var att = json.properties;
    return L.circleMarker(latlng, {radius:10, color:'red'}).bindTooltip("<h5> Incidence id: "+ att.pk +
    "</h5>"+"<h5> description: "+att.description+"</h5>"+"<h5> Time: "+ new Date(att.date)+"</h5>");

}