/**
 * Created by jelly on 8/2/16.
 */

var receiver = function(key, value) {
    if (typeof value === 'string') {
        if(key.toLowerCase().match(/.*[(day)(date)(dt)].*/)) {
            var utcDate;
            utcDate = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}(?:\.\d*)?)Z$/.exec(value);
            if (utcDate) {
                return new Date(Date.UTC(+utcDate[1], +utcDate[2] - 1, +utcDate[3], +utcDate[4], +utcDate[5], +utcDate[6]));
            } else if(value.match(/\d{8}/)) {
                var year = value.substring(0,4);
                var month = value.substring(4,6);
                var day = value.substring(6,8);
                return new Date(parseInt(year, 10), parseInt(month, 10) - 1, parseInt(day, 10));
            }
        }
    }
    return value;
};

var birthDay = new Date(1994, 6, 3, 0, 0, 0);
console.log(birthDay);
var beforeObject = {
    "name" : "jelly",
    "birthDay": "19940703"
};



var jsonString = JSON.stringify(beforeObject);
console.log(jsonString);
var afterObject = JSON.parse(jsonString, receiver);


if(afterObject != null && birthDay.toString() === afterObject.birthDay.toString()) {
    console.log("Wow! It is Successful");
} else {
    console.log("Woooops, It looks like fail");
}

console.log(afterObject);

