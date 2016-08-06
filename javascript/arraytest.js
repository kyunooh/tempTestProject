/**
 * Created by jelly on 8/1/16.
 */

// var testArray = [];
// for(var i = 0; i < 4294967294; i++) {
//     if(i % 10000000 == 0) console.log(i);
//     testArray.push(null);
// }
//
// console.log(testArray);
//

//var testArray2 = new Array(4294967294);

//console.log(testArray2);
var a1 = [,];         // 이 배열은 원소가 없으며 length 는 1 입니다.
var a2 = [undefined]; // 이 배열은 한개의 undefined 원소를 갖습니다.
console.log(0 in a1); // -> false: a1은 0번째 인덱스에 원소가 없습니다.
console.log(0 in a2); // -> true: a2는 0번째 인덱스에 undefined 값을 가지고 있습니다.

// (Firefox 3와 같은) 몇몇 오래된 구현체에서는 배열 리터럴 값에 빈값을 넣는 것이, 정확하게 삽입 되지 않습니다.
// 이렇게 구현된 경우엔  [1,,3]과 [1, undefined, 3]이 같게 동작 됩니다.

