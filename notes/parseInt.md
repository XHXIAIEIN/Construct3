# 数据转换16进制整数 Hex To Number

## 思路
调用 `parseInt()` 方法将字符串转换为16进制整数。  

## 事件表

<img width="1000" src="https://user-images.githubusercontent.com/45864744/155926312-665a4b8c-7a5a-4d59-8319-b39ff42c83c6.png">


脚本
```
runtime.setReturnValue(parseInt(localVars.string, localVars.radix))
```

表达式
```
Functions.parseInt("0xA", 16) // returns 10
Functions.parseInt("A", 16) // returns 10

Functions.parseInt("0x11", 16) // returns 17
Functions.parseInt("FD 01", 16) // returns 253
```


## 剪贴板

Function 剪贴板(粘贴到事件表)
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"functionName":"parseInt","functionDescription":"","functionCategory":"","functionReturnType":"any","functionIsAsync":false,"functionParameters":[{"name":"string","type":"string","initialValue":"","comment":""},{"name":"radix","type":"number","initialValue":"0","comment":""}],"eventType":"function-block","conditions":[],"actions":[{"type":"script","script":"runtime.setReturnValue(parseInt(localVars.string, localVars.radix))"}]}]}
```


---

# 字符转换16进制

## 思路
调用 `charCodeAt()` 方法，返回指定位置的字符 Unicode 编码。再使用 `toString()` 将数据转换为16进制。  


## 示例

示例1
```javascript
'ABC'.charCodeAt(0).toString(16);  // returns 41
'ABC'.charCodeAt(1).toString(16);  // returns 42
'ABC'.charCodeAt(2).toString(16);  // returns 43
```

示例2
```javascript
let str = "ABC"
let code = ""

for (var i = 0; i < str.length; i++) {
  code += str.charCodeAt(i).toString(16);  
}

// returns 414243
```

示例3
```javascript
let str = "ABC"
let code = ""

for (var i = 0; i < str.length; i++) {
 if(code == "")
    code += str.charCodeAt(i).toString(16);  
 else
    code += " " + str.charCodeAt(i).toString(16);
}

// returns 41 42 43
```



## 其他

```javascript
function decoded(encoded) {

    switch (encoded) {
        case 0x30: // '0'
        case 0x31: // '1'
        case 0x32: // '2'
        case 0x33: // '3'
        case 0x34: // '4'
        case 0x35: // '5'
        case 0x36: // '6'
        case 0x37: // '7'
        case 0x38: // '8'
        case 0x39: // '9'
            return encoded - 0x30;
        case 0x41: // 'A'
        case 0x42: // 'B'
        case 0x43: // 'C'
        case 0x44: // 'D'
        case 0x45: // 'E'
        case 0x46: // 'F'
            return encoded - 0x37;
        case 0x61: // 'a'
        case 0x62: // 'b'
        case 0x63: // 'c'
        case 0x64: // 'd'
        case 0x65: // 'e'
        case 0x66: // 'f'
            return encoded - 0x57;
        default:
            return encoded
    }
}
```
