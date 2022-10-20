// owl carousel settings 

var p = document.querySelectorAll('p')[0];
var d = document.getElementById('div');

$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        items:2,
        margin:30,
        loop:true,
        stagePadding: 315,
        startPosition:6,
        nav:false,
    });
});