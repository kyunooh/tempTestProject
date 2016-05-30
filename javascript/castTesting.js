/**
 * Created by jelly on 5/30/16.
 */

/* 아... 이번주엔 정말 집중이 안된다.
 * 집중이 안될 때는 역시 단순 노가다
 * 그동안 확인해보고 싶었지만 노가다여서 안했던 걸 해보자
 *
 * null, undefined, "", " ", " 123456","0", "123", "text",
 * 0, -0, NaN, Infinity, -Infinity, 123,
 * [], [null], [undefined], [true], [fasle], [1], [1,2,3], ["abc"], ["1"] ["abcd", "efg"],
 * {}, {a: "abc"},
 * true, false,
 * function() {}, function() { return 0; }, function() { return 1; }
 *
 * 노가다로 하려했는데 웬지 노가다로 안해도 될 것 같다.
 */
var _emptyStr = "";
var _spaceStr = " ";
var _spaceWithNumberStr = " 123456";
var _spaceWithNagativeNumberStr = " -123456";
var _zeroStr = "0";
var _numStr = "123";
var _textStr = "text";
var _emptyArr = [];
var _nullArr = [null];
var _undefinedArr = [undefined];
var _trueArr = [true];
var _falseArr = [false];
var _aNumberArr = [1];
var _numbersArr = [1,2,3];
var _aStrArr = ["abc"];
var _aNumberStrArr = ["1"];
var _strsArr = ["abcd", "efg"];
var _emptyObject = {};
var _notEmptyObject = { a: "abc"};
var _functionVar = function() {};




var varArray = [null, undefined, true, false, 0, 1, -0, NaN, Infinity, -Infinity, _emptyStr, _spaceStr, _zeroStr, _spaceWithNumberStr, _spaceWithNagativeNumberStr, _numStr, _textStr, _emptyArr, _nullArr, _undefinedArr,
_trueArr, _falseArr, _aNumberArr, _numbersArr, _aStrArr, _aNumberStrArr, _strsArr, _emptyObject, _notEmptyObject, _functionVar];

var testCasting = function(_varArr, _function){
    for(var index = 0; index < _varArr.length; index++) {
        if(typeof(_varArr[index]) == "string")
            console.log(_function.name + "(\"" + _varArr[index] + "\") : " + (_function(_varArr[index])));
        else if(_varArr[index] === _emptyArr)
            console.log(_function.name + "([]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _nullArr)
            console.log(_function.name + "([null]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _undefinedArr)
            console.log(_function.name + "([undefined]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _aNumberArr)
            console.log(_function.name + "([1]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _numbersArr)
            console.log(_function.name + "([1,2,3]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _emptyObject)
            console.log(_function.name + "({}) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _notEmptyObject)
            console.log(_function.name + "({ a: \"abc\"}) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _trueArr)
            console.log(_function.name + "([true]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === _falseArr)
            console.log(_function.name + "([false]) : " + (_function(_varArr[index])));
        else if(_varArr[index] === -0)
            console.log(_function.name + "(-0) : " + (_function(_varArr[index])));                        
        else
            console.log(_function.name + "(" + _varArr[index] + ") : " + (_function(_varArr[index])));
    }
};


//testCasting(varArray, Number);
//testCasting(varArray, String);
//testCasting(varArray, Boolean);
testCasting(varArray, Object);
