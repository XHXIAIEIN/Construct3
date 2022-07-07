# 数字在范围内循环

常用于菜单、队列的光标索引。

## 变量：
- ` MaxOptions `
- ` CurrentOption `

## 公式
Set CurrentOption to `((CurrentOption +1) + MaxOptions) % MaxOptions`

快速剪贴板
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"variable","name":"CurrentOption","type":"number","initialValue":"0","comment":"","isStatic":false,"isConstant":false},{"eventType":"variable","name":"MaxOptions","type":"number","initialValue":"3","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"every-x-seconds","objectClass":"System","parameters":{"interval-seconds":"0.5"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"CurrentOption","value":"((CurrentOption +1) + MaxOptions) % MaxOptions"}}]}]}
```
