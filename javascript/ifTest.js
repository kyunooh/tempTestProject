var c1 = 0;

if(c1++) { console.log("0++ is true");     }
else     { console.log("0++ is not true"); }

c1 = 0;
if (++c1) { console.log("++0 is true");     }
else      { console.log("++0 is not true"); }

    c1 = 0;
var c2 = 0;

if(c2 && ++c1) { console.log("c2 && c1++ is true,  c1 is " + c1); }
else           { console.log("c2 && c1++ is false, c1 is " + c1); }

c1 = 0;
c2 = 0;
if(c2 || ++c1) { console.log("c2 || c1++ is true,  c1 is " + c1); }
else           { console.log("c2 || c1++ is false, c1 is " + c1); }

console.log("0 && 1 && true is " + (0 && 1 && true));


console.log("1 && false && true is " + (1 && false && true));

console.log("1 && true && 0 && false is " + (1 && true && 0 && false));

console.log("1 || true is " + (1 || true));

console.log("true || 1 is " + (true || 1));

console.log("true || false is " + (true || false));

console.log("(true || 1) == (1 || true) is " + ((true || 1) == (1 || true)));

console.log("(true || 1) === (1 || true) is " + ((true || 1) === (1 || true)));

   
