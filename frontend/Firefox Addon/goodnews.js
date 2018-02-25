
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
	$("#fakeNewsButton").remove();
	var button = document.createElement("div");
button.style = "top:5%;right:5%;position:fixed;z-index: 9999;"
button.id="fakeNewsButton";
document.body.appendChild(button);

$("#fakeNewsButton").append('<span id="fakenewsshape" title="Click to analyse the article on the current web page."><svg id="fakenewsshape" height="80" width="180"><g><rect x="3" y="3" rx="20" ry="20" width="174" height="74" stroke="darkblue" fill="lightblue" stroke-width="3"/><text x="17" y="46" font-family="Verdana" font-size="17" fill="darkblue">Fake News Scan</text></g></svg></span>');



$("#fakeNewsButton").click(function() {
			color="rgb(0,0,0)";
    	alert("okok");
    	var xhr = new XMLHttpRequest();
			var url = "https://localhost:8080";
			xhr.onreadystatechange = function() {
			    if (xhr.readyState == XMLHttpRequest.DONE) {
			    	alert(xhr.responseText);
			        var obj = JSON.parse(xhr.responseText);
			        alert(parseFloat(obj["isFake"]));
			    	if(obj["isArticle"]==1){
			    		alert(typeof obj["isFake"]);
			    		if(parseFloat(obj["isFake"])<0.5){
			    			$("#fakenewsshape").replaceWith('<span id="fakenewsshape" title="'+obj["message"]+'"><svg height="80" width="180"><g><rect x="3" y="3" rx="20" ry="20" width="174" height="74" stroke="darkred" fill="salmon" stroke-width="3"/><text x="50" y="50" font-family="Verdana" font-size="30" fill="darkred">Fake !</text></g></svg></span>');
			    		}
			    		else{
			    			$("#fakenewsshape").replaceWith('<span id="fakenewsshape" title="'+obj["message"]+'"><svg height="80" width="180"><g><rect x="3" y="3" rx="20" ry="20" width="174" height="74" stroke="darkgreen" fill="lightgreen" stroke-width="3"/><text x="50" y="50" font-family="Verdana" font-size="30" fill="darkgreen">Safe !</text></g></svg></span>');
			  		  	}

			    	}
			        //var intensity = xhr.responseText;
			        //var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			       // alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			        //document.getElementById("fakenessCircle").setAttribute("fill", color);
			    }
			}
			xhr.open("POST", url, true);
			
			var full_url = window.location.href;
			alert(full_url);
			jsonstring = '{"url":"'+full_url+'"}';
			alert(jsonstring);
			xhr.send(jsonstring);

			//$(this).append( "<svg height=\"28\" width=\"28\"><circle id='fakenessCircle' cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='"+color+"' /></svg>" );
			//$(this).append( "<svg height='230' width='250'><circle id='fakenessCircle' cx='7' cy='22' r='50' stroke='green' stroke-width='2' fill='"+color+"' /></svg>" );
			$("#fakenewsshape").replaceWith('<span id="fakenewsshape" title="Analyse in process..."><svg height="80" width="180"><g><rect x="3" y="3" rx="20" ry="20" width="174" height="74" stroke="orange" fill="yellow" stroke-width="3"/><text x="30" y="46" font-family="Verdana" font-size="24" fill="darkgreen">Loading...</text></g></svg></span>');
       //do something, alt was down when clicked
    
  });
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


	);*//*
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
			jsonstring = '{"url":"'+$(this).attr('href')+'", "imagePath":"'+$(this).attr('data-ploi')+'"}';
			xhr.send(jsonstring);

			$(this).append( "<svg height=\"28\" width=\"28\"><circle id='fakenessCircle' cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='"+color+"' /></svg>" );
			
			
		},
		function(){
			//$(this).find( "svg:last" ).remove();
			//color="rgb(0,0,0)";
		}
	);

	$('img').hover(
		function(){
			var xhr = new XMLHttpRequest();
			var url = "https://localhost:8080";
			xhr.onreadystatechange = function() {
			    if (xhr.readyState == XMLHttpRequest.DONE) {
			        var intensity = xhr.responseText;
			        var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			        alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			       // document.getElementById("fakenessCircle").setAttribute("fill", color);
			        //var intensity = xhr.responseText;
			        //var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			       // alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			        //document.getElementById("fakenessCircle").setAttribute("fill", color);
			    }
			}
			xhr.open("POST", url, true);
			jsonstring = '{"url":"", "imagePath":"'+$(this).attr('src')+'"}';
			xhr.send(jsonstring);

			$(this).append( "<svg height=\"230\" width=\"250\"><circle id='fakenessCircle' cx=\"7\" cy=\"22\" r=\"50\" stroke=\"green\" stroke-width=\"2\" fill='"+color+"' /></svg>" );
			
			
		},
		function(){
			$(this).find( "svg:last" ).remove();
			color="rgb(0,0,0)";
		}
	);*/

	$("a").bind("click",function(event) {
    if (event.altKey && event.ctrlKey) {
    	event.preventDefault();
    	$(this).find( "svg:last" ).remove();
			color="rgb(0,0,0)";
    	alert("okok");
    	var xhr = new XMLHttpRequest();
			var url = "https://localhost:8080";
			xhr.onreadystatechange = function() {
			    if (xhr.readyState == XMLHttpRequest.DONE) {
			    	alert(xhr.responseText);
			        var obj = JSON.parse(xhr.responseText);
			        alert(parseFloat(obj["isFake"]));
			    	if(obj["isArticle"]==1){
			    		alert(typeof obj["isFake"]);
			    		if(parseFloat(obj["isFake"])<0.5){
			    			$("#bubbleFakeNews").replaceWith('<span title="'+obj["message"]+'"><svg height="55" width="105" alt="test"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="darkred" fill="salmon" stroke-width="2"/><text x="27" y="43" font-family="Verdana" font-size="17" fill="darkred">Fake !</text></g></svg></span>');
			    		}
			    		else{
			    			$("#bubbleFakeNews").replaceWith('<span title="'+obj["message"]+'"><svg height="55" width="105" alt="test"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="green" fill="lightgreen" stroke-width="2"/><text x="27" y="43" font-family="Verdana" font-size="17" fill="darkgreen">Safe !</text></g></svg></span>');
			  		  	}

			    	}
			        //var intensity = xhr.responseText;
			        //var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			       // alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			        //document.getElementById("fakenessCircle").setAttribute("fill", color);
			    }
			}
			xhr.open("POST", url, true);
			var str = document.URL;
			var nbSlash = 0;
			var position = 0;
			for(var i=0; i<str.length; i++ ){
				if(str[i]=='/'){
					nbSlash++;
				}
				if(nbSlash==3){
					position = i;
					break;
				}
			}
			alert(str);
			alert(position);
			var full_url = $(this).attr('href');
			if(full_url.slice(0,4) != "http"){
				full_url = str.slice(0,position)+full_url;
			}
			alert(full_url);
			jsonstring = '{"url":"'+full_url+'"}';
			alert(jsonstring);
			xhr.send(jsonstring);

			//$(this).append( "<svg height=\"28\" width=\"28\"><circle id='fakenessCircle' cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='"+color+"' /></svg>" );
			//$(this).append( "<svg height='230' width='250'><circle id='fakenessCircle' cx='7' cy='22' r='50' stroke='green' stroke-width='2' fill='"+color+"' /></svg>" );
			$(this).append('<svg id="bubbleFakeNews" height="55" width="105"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="orange" fill="yellow" stroke-width="2"/><text x="10" y="43" font-family="Verdana" font-size="17 " fill="darkgreen">Loading...</text></g></svg>');
       //do something, alt was down when clicked
    }
  });


/*
	$("img").bind("click",function(event) {
    if (event.altKey && event.ctrlKey) {
    	event.preventDefault();
    	var xhr = new XMLHttpRequest();
			var url = "https://localhost:8080";
			xhr.onreadystatechange = function() {
			    if (xhr.readyState == XMLHttpRequest.DONE) {
			    	alert(xhr.responseText);
			        var obj = JSON.parse(xhr.responseText);

			    	if(obj["isArticle"]==1){
			    		if(obj["isFake"]==1){
			    			$("#bubbleFakeNews").replaceWith('<span title='+obj["message"]+'><svg height="55" width="105" alt="test"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="darkred" fill="salmon" stroke-width="2"/><text x="27" y="43" font-family="Verdana" font-size="17" fill="darkred">Fake !</text></g></svg></span>');
			    		}
			    		else{
			    			$("#bubbleFakeNews").replaceWith('<span title='+obj["message"]+'><svg height="55" width="105" alt="test"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="green" fill="lightgreen" stroke-width="2"/><text x="27" y="43" font-family="Verdana" font-size="17" fill="darkgreen">Safe !</text></g></svg></span>');
			  		  	}
			    	}
			        //var intensity = xhr.responseText;
			        //var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			        //alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			       // document.getElementById("fakenessCircle").setAttribute("fill", color);
			        //var intensity = xhr.responseText;
			        //var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			       // alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			        //document.getElementById("fakenessCircle").setAttribute("fill", color);
			    }
			}
			xhr.open("POST", url, true);
			jsonstring = '{"url":"", "imagePath":"'+$(this).attr('src')+'"}';
			xhr.send(jsonstring);

			//$(this).append( "<svg height='230' width='250'><circle id='fakenessCircle' cx='7' cy='22' r='50' stroke='green' stroke-width='2' fill='"+color+"' /></svg>" );
			$(this).append('<svg height="50" width="200"><g><rect x="5" y="5" rx="10" ry="10" width="190" height="40" stroke="orange" fill="yellow" stroke-width="5"/><text x="30" y="35" font-family="Verdana" font-size="30" fill="darkgreen">Loading...</text></g></svg>"');
       //do something, alt was down when clicked
    }
  });*/
/*
	$("a").contextmenu({
        selector: '.context-menu-one', 
        callback: function(key, options) {
            var m = "clicked: " + key;
            window.console && console.log(m) || alert(m); 
        },
        items: {
            "edit": {name: "Edit", icon: "edit"},
            "cut": {name: "Cut", icon: "cut"},
            "copy": {name: "Copy", icon: "copy"},
            "paste": {name: "Paste", icon: "paste"},
            "delete": {name: "Delete", icon: "delete"},
            "sep1": "---------",
            "quit": {name: "Quit", icon: function($element, key, item){ return 'context-menu-icon context-menu-icon-quit'; }}
        }
    });*/
});


$(document).on('scroll', function() {
	$('a').off('click');
    $("a").bind("click",function(event) {
    if (event.altKey && event.ctrlKey) {
    	event.preventDefault();
    	$(this).find( "svg:last" ).remove();
			color="rgb(0,0,0)";
    	alert("okok");
    	var xhr = new XMLHttpRequest();
			var url = "https://localhost:8080";
			xhr.onreadystatechange = function() {
			    if (xhr.readyState == XMLHttpRequest.DONE) {
			    	alert(xhr.responseText);
			        var obj = JSON.parse(xhr.responseText);

			    	if(obj["isArticle"]==1){
			    		alert(typeof obj["isFake"]);
			    		if(parseFloat(obj["isFake"])<0.5){
			    			$("#bubbleFakeNews").replaceWith('<span title="'+obj["message"]+'""><svg height="55" width="105" alt="test"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="darkred" fill="salmon" stroke-width="2"/><text x="27" y="43" font-family="Verdana" font-size="17" fill="darkred">Fake !</text></g></svg></span>');
			    		}
			    		else{
			    			$("#bubbleFakeNews").replaceWith('<span title="'+obj["message"]+'"><svg height="55" width="105" alt="test"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="green" fill="lightgreen" stroke-width="2"/><text x="27" y="43" font-family="Verdana" font-size="17" fill="darkgreen">Safe !</text></g></svg></span>');
			  		  	}

			    	}
			        //var intensity = xhr.responseText;
			        //var color = 'rgb('+(255-intensity)+','+intensity+',0)';
			       // alert(color);
			        //$(this).append( "<svg height=\"28\" width=\"28\"><circle cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='lightred' /></svg>" );
			        //document.getElementsById("fakenessCircle").style.color(color);
			        //document.getElementsById("fakenessCircle").style.fill("lightred");
			        //document.getElementById("fakenessCircle").setAttribute("fill", color);
			    }
			}
			var str = document.URL;
			var nbSlash = 0;
			var position = 0;
			for(var i=0; i<str.length; i++ ){
				if(str[i]=='/'){
					nbSlash++;
				}
				if(nbSlash==3){
					position = i;
					break;
				}
			}
			alert(str);
			alert(position);
			var full_url = $(this).attr('href');
			if(full_url.slice(0,4) != "http"){
				full_url = str.slice(0,position)+full_url;
			}
			alert(full_url);
			jsonstring = '{"url":"'+full_url+'"}';
			alert(jsonstring);
			xhr.send(jsonstring);

			//$(this).append( "<svg height=\"28\" width=\"28\"><circle id='fakenessCircle' cx=\"7\" cy=\"22\" r=\"5\" stroke=\"green\" stroke-width=\"2\" fill='"+color+"' /></svg>" );
			//$(this).append( "<svg height='230' width='250'><circle id='fakenessCircle' cx='7' cy='22' r='50' stroke='green' stroke-width='2' fill='"+color+"' /></svg>" );
			$(this).append('<svg id="bubbleFakeNews" height="55" width="105"><g><rect x="2.5" y="22" rx="10" ry="10" width="100" height="30" stroke="orange" fill="yellow" stroke-width="2"/><text x="10" y="43" font-family="Verdana" font-size="17 " fill="darkgreen">Loading...</text></g></svg>');
       //do something, alt was down when clicked
    }
  });
  });


