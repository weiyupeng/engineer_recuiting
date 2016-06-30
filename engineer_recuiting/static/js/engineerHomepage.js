
  $(function() {
    $( "#id_beg_data" ).datepicker({
      defaultDate: "+1w",
	  minDate: 0,
      changeMonth: true,
      numberOfMonths: 1,
      onClose: function( selectedDate ) {
        $( "#id_end_data" ).datepicker( "option", "minDate", selectedDate );
      }
    });
    $( "#id_end_data" ).datepicker({

      defaultDate: "+1w",
      changeMonth: true,
      numberOfMonths: 1,
      onClose: function( selectedDate ) {
        $( "#id_beg_data" ).datepicker( "option", "maxDate", selectedDate );
      }
    });
  });


 $(function (){
var oDiv=document.getElementById("tab");
var aBtn=oDiv.getElementsByTagName("li");
var aDiv=oDiv.getElementsByTagName("div");

for (var i = 0; i < aBtn.length; i++) {
aBtn[i].index=i;
aBtn[i].onmouseover=function (){
for (var i = 0; i < aBtn.length; i++) {
aBtn[i].className="";
aDiv[i].style.display="none";
};
this.className="active";
aDiv[this.index].style.display="block";

};
};
});