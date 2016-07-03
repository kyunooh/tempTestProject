var startShift = new Date();

var a = 2048;
var b = 0;
for(var i = 0; i < 1000000000; i++) {
    b = a >> 10;
}
var endShift = new Date();
console.log("a >> 10 : " + b);
console.log("loop b = a >> 10 : "+ (endShift - startShift));


var startDivide = new Date();

var c = 2048;
var d = 0;

for(var i = 0; i < 1000000000; i++) {
    d = c / 1024;
}

var endDivide = new Date();

console.log("c / 1024 : " + d);
console.log("loop c / 1024 : " + (endDivide - startDivide));
