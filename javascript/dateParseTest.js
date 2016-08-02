/**
 * Created by jelly on 8/2/16.
 */

var receiver = function(key, value) {

};


var beforeObject = {
    "name" : "jelly",
    "birthDay": new Date(1994, 07, 03)
};

var jsonString = JSON.stringify(beforeObject);

var afterObject = JSON.parse(jsonString, receiver);


if(afterObject != null && beforeObject.birthDay === afterObject.birthDay) {
    console.log("Wow! It is Successful");
} else {
    console.log("Woooops, It looks like fail");
}

