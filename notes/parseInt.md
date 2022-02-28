# 16进制数据处理

## 思路
调用 JS 自带的 `parseInt` 方法将数据转换为16进制。  

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
