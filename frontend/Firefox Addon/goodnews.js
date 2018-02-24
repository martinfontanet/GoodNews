var  i=0;
var jsonstring='{ "hrefs":['
//var links = document.getElementsByTagName("a");
var hrefs = [], colormap = [], links = document.links;
for(var i=0; i<links.length; i++) {
	//seenHrefs.push(links[i].href);
	if(hrefs.indexOf(links[i].href) < 0){
	  	hrefs.push(links[i].href);	
	  	colormap[links[i].href] = 255;//.push({"href":links[i].href, "color":155});
	  	jsonstring += '"'+links[i].href+'",'; 	
	}
	else{
	//	alert(links[i].innerHTML);
	}

}
jsonstring = jsonstring.slice(0, -1) + ']}';
	alert(jsonstring);

var xhr = new XMLHttpRequest();
var url = "localhost:8080";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json.email + ", " + json.password);
    }
};
var data = JSON.stringify(jsonstring);
xhr.send(data);

$(document).ready(function(){/*
	$( "a" ).each(function( index ) {
		for(var i=0; i<l.length; i++) {
 if(hrefs[i]==$(this).attr('href')){
  	//$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"red\" stroke-width=\"2\" fill=\"lightred\" /></svg>" );
  	$(this).append( "<p>"+hrefs[0]+"<p/>" );
  }
}
});*//*
	$("a").each(function(){
		//if(!($(this).attr('href') in seenHrefs)){
	  	hrefs.push({"href":$(this).attr('href'),"nb":i});
	 // 	i = i + 1;
	  	seenHrefs.push($(this).attr('href'));
	//}
	});*/

    $( "a" ).each(
    	function() {
    		
    		i = hrefs.indexOf($(this).attr('href'));

    		if(i>=0){
    			var color="\"rgb(0,"+colormap[$(this).attr('href')]+",0)\"";//+Math.round(255*(i+1)/hrefs.length)+",0)\"";
			$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill="+color+" /></svg>" );
    		}


/*
			for(var i=0; i<hrefs.length; i++) {
				if(hrefs[i]["href"]==$(this).attr('href')){
				  	//$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"red\" stroke-width=\"2\" fill=\"lightred\" /></svg>" );
				  	//$(this).append( "<p>"+hrefs[i]["nb"]+"<p/>" );
				  	var color="\"rgb(0,"+Math.round(255*hrefs[i]["nb"]/hrefs.length)+",0)\"";
			$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill="+color+" /></svg>" );
				}
			}
			*/
		}
		/*,
		function() {
		  $(this).find( "svg:last" ).remove();
		  //$(this).find( "p:last" ).remove();
		}*/
	);
});


