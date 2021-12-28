# 数字在范围内循环

常用于菜单、队列的光标索引。

## 变量：
- ` MaxOptions `
- ` CurrentOption `

## 公式
Set CurrentOption to `((CurrentOption +1) + MaxOptions) % MaxOptions`

