/**
 * Created by jelly on 8/1/16.
 */

var testArray = [];
for(var i = 0; i < 4294967294; i++) {
    if(i % 10000000 == 0) console.log(i);
    testArray.push(null);
}

console.log(testArray);
