$(document).ready(function(){
    $( "a" ).hover(function() {
  $(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill=\"lightgreen\" /></svg>" );
},
function() {
  $(this).find( "svg:last" ).remove();
}
);
});