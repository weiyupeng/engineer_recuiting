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