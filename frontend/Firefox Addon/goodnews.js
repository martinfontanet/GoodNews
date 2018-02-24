/*
var  i=0;
var jsonstring='{ "hrefs":[';
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

var color="rgb(0,0,0)";
*/
//jsonstring = jsonstring.slice(0, -1) + ']}';
//alert(jsonstring);
/*
var options = {
    host: 'localhost',
    port: 9999,
    method: 'POST',
    headers: {
        accept: 'application/json'
    }
};

console.log("Start");
var x = http.request(options,function(res){
    console.log("Connected");
    res.on('data',function(data){
        console.log(data);
    });
});

x.end();

*//*
var xhr = new XMLHttpRequest();
var url = "https://localhost:8080";
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        alert(xhr.responseText);
    }
}
xhr.open("POST", url, true);

xhr.send(jsonstring);*/


//xhr.setRequestHeader("Content-type", "application/json");
//xhr.onreadystatechange = function () {
//    if (xhr.readyState === 4 && xhr.status === 200) {
//        var json = "aa";
//    }
//};

//alert("done");



$(document).ready(function(){
/*
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


   /* $( "a" ).each(
    	function() {
    		
    		i = hrefs.indexOf($(this).attr('href'));

    		if(i>=0){
    			var color="\"rgb(0,"+colormap[$(this).attr('href')]+",0)\"";//+Math.round(255*(i+1)/hrefs.length)+",0)\"";
			$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill="+color+" /></svg>" );
    		}


		}


	);*/
	$("a").hover(
		function(){
			var xhr = new XMLHttpRequest();
			var url = "https://localhost:8080";
			xhr.onreadystatechange = function() {
			    if (xhr.readyState == XMLHttpRequest.DONE) {
			        
			        var intensity = xhr.responseText;
			        var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			       // alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			        document.getElementById("fakenessCircle").setAttribute("fill", color);
			    }
			}
			xhr.open("POST", url, true);
			jsonstring = '{"url":"'+$(this).attr('href')+'", "imagePath":""}';
			xhr.send(jsonstring);

			$(this).append( "<svg height=\"28\" width=\"28\"><circle id='fakenessCircle' cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='"+color+"' /></svg>" );
			
			
		},
		function(){
			$(this).find( "svg:last" ).remove();
			color="rgb(0,0,0)";
		}
	);
});


