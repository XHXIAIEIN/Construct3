# Number of digits

计算一个数字的位数，例如：
- 32 是 2位数。
- 125 是 3 位数。
- 1998 是 4 位数。
  

## 数学函数
```
round(log10(float(n))+1)
```

## 字符串
```
len(str(abs(round(float(n)))))
```

## 快速剪贴板

带检测字符串是否是个数字 
Function
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"functionName":"GetDigits","functionDescription":"","functionCategory":"","functionReturnType":"number","functionIsAsync":false,"functionParameters":[{"name":"value","type":"string","initialValue":"","comment":""}],"eventType":"function-block","conditions":[],"actions":[],"children":[{"eventType":"comment","text":"Number"},{"eventType":"block","conditions":[{"id":"compare-two-values","objectClass":"System","parameters":{"first-value":"int(value)","comparison":0,"second-value":"value"}}],"actions":[{"id":"set-function-return-value","objectClass":"Functions","parameters":{"value":"round(log10(float(value))+1)"}}]},{"eventType":"comment","text":"String"},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"}],"actions":[{"id":"set-function-return-value","objectClass":"Functions","parameters":{"value":"len(str(abs(round(float(value)))))"}}]}]}]}
```
