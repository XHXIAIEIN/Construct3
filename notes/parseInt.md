# 数据转换16进制整数

## 思路
调用 JS 自带的 `parseInt` 方法将字符转换为16进制的整数。  

## 事件表

<img width="1000" src="https://user-images.githubusercontent.com/45864744/155926312-665a4b8c-7a5a-4d59-8319-b39ff42c83c6.png">


脚本
```
runtime.setReturnValue(parseInt(localVars.string, localVars.radix))
```

表达式
```
Functions.parseInt("FD 01", 16)
```

输出结果
```
253
```


## 剪贴板

Function 剪贴板(粘贴到事件表)
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"functionName":"parseInt","functionDescription":"","functionCategory":"","functionReturnType":"any","functionIsAsync":false,"functionParameters":[{"name":"string","type":"string","initialValue":"","comment":""},{"name":"radix","type":"number","initialValue":"0","comment":""}],"eventType":"function-block","conditions":[],"actions":[{"type":"script","script":"runtime.setReturnValue(parseInt(localVars.string, localVars.radix))"}]}]}
```


---

# 字符转换16进制

## 思路
调用 `charCodeAt()` 方法将数据转换为16进制。  


示例1
```
'ABC'.charCodeAt(0).toString(16);  // returns 41
'ABC'.charCodeAt(1).toString(16);  // returns 42
'ABC'.charCodeAt(2).toString(16);  // returns 43
```

示例2
```
str = "ABC"
code = ""

for (var i = 0; i < str.length; i++) {
  code += str.charCodeAt(i).toString(16);  
}

// returns 414243
```

示例3
```
str = "ABC"
code = ""

for (var i = 0; i < str.length; i++) {
 if(code == "")
    code += str.charCodeAt(i).toString(16);  
 else
    code += " " + str.charCodeAt(i).toString(16);
}

// returns 41 42 43
```


