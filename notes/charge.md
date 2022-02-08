实现长按蓄力的机制

## 必要的变量


| 变量           | 类型  | 初始值 |  描述  |
|:-------------- |:---- |:----- |:------- |
| ChargeTime     | Number | 0 | 当前蓄力的时间进度，以毫秒为单位。| 
| MaxChargeTime  | Number | 60 | 可以蓄力的最大时间，数值越大，需要蓄力越久。    | 
| ChargeSpeed    | Number | 1 | 每次蓄力增加的时间，数值越大，蓄力速度越快。    | 
  
这里，我是将它作为实例变量使用。    

<img width="460" src="https://user-images.githubusercontent.com/45864744/152939384-1f43afc8-5b51-4d83-9567-e413f6ca81c1.png">

Sprite 对象剪贴板（粘贴到Layout）
```
{"is-c3-clipboard-data":true,"type":"world-instances","items":[{"type":"Sprite","properties":{"initially-visible":true,"initial-animation":"Animation 1","initial-frame":0,"enable-collisions":true,"live-preview":false},"instanceVariables":{"ChargeTime":0,"ChargeSpeed":1,"MaxChargeTime":60},"behaviors":{},"world":{"x":232,"y":168,"width":64,"height":64,"originX":0.5,"originY":1,"color":[1,1,1,1],"angle":0,"zElevation":0}}],"object-types":[{"name":"Sprite","plugin-id":"Sprite","isGlobal":false,"instanceVariables":[{"name":"ChargeTime","type":"number","desc":""},{"name":"ChargeSpeed","type":"number","desc":""},{"name":"MaxChargeTime","type":"number","desc":""}],"behaviorTypes":[],"effectTypes":[],"animations":{"items":[{"frames":[{"width":64,"height":64,"originX":0.5,"originY":1,"originalSource":"","exportFormat":"png","exportQuality":0.8,"imageDataIndex":0,"useCollisionPoly":true,"duration":1}],"name":"Animation 1","isLooping":false,"isPingPong":false,"repeatCount":1,"repeatTo":0,"speed":0}],"subfolders":[],"name":"Animations"}}],"imageData":["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAIBJREFUeF7t1wERADAIAzHwLxqEfCahN5rr3s1N+K0A/AAnoAPCHThKkAIUoAAFKBBOAIMYxCAGMRhGwBjCIAYxiEEMYjCcAAYxiEEMYjCMgDWIQQxiEIMYxGA4AQxiEIMYxGAYAWsQgxjEIAYxiMFwAhjEIAYxiMEwAtYgBusMPv/Jv4H6VP2RAAAAAElFTkSuQmCC"]}
```

## 事件表

1 长按空格键时，进行蓄力。松开则重置

<img width="1000" src="https://user-images.githubusercontent.com/45864744/152938988-1993d3cd-2735-46b7-838d-dfaae6f18807.png">

```
clamp(Self.ChargeTime + Self.ChargeSpeed * 60 * dt, 0, Self.MaxChargeTime)
```

事件表剪贴板（需 Keyboard 对象）
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32}}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"clamp(Self.ChargeTime + Self.ChargeSpeed * 60 * dt, 0, Self.MaxChargeTime)"}}]},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"},{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32},"isInverted":true}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"0"}}]}]}
```

