实现长按蓄力的机制

## 必要的变量


| 变量           | 类型    | 初始值 |  描述                                       |
|:-------------- |:------ |:------ |:------------------------------------------- |
| ChargeTime     | Number | 0      | 当前蓄力的时间进度。                          | 
| MaxChargeTime  | Number | 60     | 可以蓄力的最大时间，数值越大，需要蓄力越久。    | 
| ChargeSpeed    | Number | 1      | 每次蓄力增加的时间，数值越大，蓄力速度越快。    | 
  
这里，我是将它作为实例变量使用。    

<img width="460" src="https://user-images.githubusercontent.com/45864744/152939384-1f43afc8-5b51-4d83-9567-e413f6ca81c1.png">

Sprite 对象剪贴板（粘贴到Layout）
```
{"is-c3-clipboard-data":true,"type":"world-instances","items":[{"type":"Sprite","properties":{"initially-visible":true,"initial-animation":"Animation 1","initial-frame":0,"enable-collisions":true,"live-preview":false},"instanceVariables":{"ChargeTime":0,"ChargeSpeed":1,"MaxChargeTime":60},"behaviors":{},"world":{"x":232,"y":168,"width":64,"height":64,"originX":0.5,"originY":1,"color":[1,1,1,1],"angle":0,"zElevation":0}}],"object-types":[{"name":"Sprite","plugin-id":"Sprite","isGlobal":false,"instanceVariables":[{"name":"ChargeTime","type":"number","desc":""},{"name":"ChargeSpeed","type":"number","desc":""},{"name":"MaxChargeTime","type":"number","desc":""}],"behaviorTypes":[],"effectTypes":[],"animations":{"items":[{"frames":[{"width":64,"height":64,"originX":0.5,"originY":1,"originalSource":"","exportFormat":"png","exportQuality":0.8,"imageDataIndex":0,"useCollisionPoly":true,"duration":1}],"name":"Animation 1","isLooping":false,"isPingPong":false,"repeatCount":1,"repeatTo":0,"speed":0}],"subfolders":[],"name":"Animations"}}],"imageData":["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAIBJREFUeF7t1wERADAIAzHwLxqEfCahN5rr3s1N+K0A/AAnoAPCHThKkAIUoAAFKBBOAIMYxCAGMRhGwBjCIAYxiEEMYjCcAAYxiEEMYjCMgDWIQQxiEIMYxGA4AQxiEIMYxGAYAWsQgxjEIAYxiMFwAhjEIAYxiMEwAtYgBusMPv/Jv4H6VP2RAAAAAElFTkSuQmCC"]}
```

## 事件表

### 计算蓄力时间
   
长按空格键时，进行蓄力。

<img width="1000" src="https://user-images.githubusercontent.com/45864744/152938988-1993d3cd-2735-46b7-838d-dfaae6f18807.png">

表达式
```
clamp(Self.ChargeTime + Self.ChargeSpeed * 60 * dt, 0, Self.MaxChargeTime)
```

事件表剪贴板（需 Keyboard 对象）
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32}}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"clamp(Self.ChargeTime + Self.ChargeSpeed * 60 * dt, 0, Self.MaxChargeTime)"}}]},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"},{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32},"isInverted":true}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"0"}}]}]}
```


### 判断蓄力进度

数据有了，接下来只需要判断数值，就可以计算蓄力进度了。  

例如分为 4 个等级：

| 等级           | 时间点               |  
|:-------------- |:------------------- |
| Too Fast       | t < 25%             | 
| Good           | 25% <=  t <  85%    | 
| Perfect        | 85% <=  t <  99.9%  | 
| Max            | t =  100%           | 

<img width="680" src="https://user-images.githubusercontent.com/45864744/153011504-e393bde9-0cee-4ab9-8dac-87d423bfdb08.png">

然后就看实际的使用场景，是想在蓄力过程中计算呢，还是在松开蓄力键之后才计算呢。
其实都可以，他们方法是一样的~  

这里为了测试方便，额外加了一个变量 ` ChargeLevel ` 来测试蓄力的等级。  

如果想实现类似洛克人那样，蓄力过程有不同的动画反馈，可以将计算蓄力进度的事件放在 ` Key is Down ` 的子条件里面。    

<img width="1000" src="https://user-images.githubusercontent.com/45864744/153017218-70fc8565-42c1-4447-a8cb-74d22c3e371d.png">

事件表剪贴板
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"variable","name":"ChargeLevel","type":"string","initialValue":"None","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32}}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"clamp(Self.ChargeTime + Self.ChargeSpeed * 60 * dt, 0, Self.MaxChargeTime)"}}],"children":[{"eventType":"comment","text":"Max"},{"eventType":"block","conditions":[{"id":"compare-two-values","objectClass":"System","parameters":{"first-value":"Sprite.ChargeTime","comparison":0,"second-value":"Sprite.MaxChargeTime"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Max\""}}]},{"eventType":"comment","text":"Too Fast:  t  <  25%"},{"eventType":"block","conditions":[{"id":"compare-two-values","objectClass":"System","parameters":{"first-value":"Sprite.ChargeTime","comparison":2,"second-value":"Sprite.MaxChargeTime * 0.25"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Too Fast\""}}]},{"eventType":"comment","text":"Good:  25  <  t  <  85%"},{"eventType":"block","conditions":[{"id":"is-between-values","objectClass":"System","parameters":{"value":"Sprite.ChargeTime","lower-bound":"Sprite.MaxChargeTime * 0.25","upper-bound":"Sprite.MaxChargeTime * 0.85"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Good\""}}]},{"eventType":"comment","text":"Prefect:  85  <  t  <  99%"},{"eventType":"block","conditions":[{"id":"is-between-values","objectClass":"System","parameters":{"value":"Sprite.ChargeTime","lower-bound":"Sprite.MaxChargeTime * 0.85","upper-bound":"Sprite.MaxChargeTime - 1"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Prefect\""}}]}]},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"},{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32},"isInverted":true}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"0"}},{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"None\""}}]}]}
```

如果想实现QTE、音游等需要快速反应那样，可以将计算蓄力进度的事件放在  ` On Key released ` 的子条件里面。   

<img width="1000" src="https://user-images.githubusercontent.com/45864744/153018223-80bf2ded-731b-49a8-93d0-6eeab7925993.png">

事件表剪贴板
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"variable","name":"ChargeLevel","type":"string","initialValue":"None","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32}}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"clamp(Self.ChargeTime + Self.ChargeSpeed * 60 * dt, 0, Self.MaxChargeTime)"}}]},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"},{"id":"key-is-down","objectClass":"Keyboard","parameters":{"key":32},"isInverted":true}],"actions":[{"id":"set-instvar-value","objectClass":"Sprite","parameters":{"instance-variable":"ChargeTime","value":"0"}}]},{"eventType":"block","conditions":[{"id":"on-key-pressed","objectClass":"Keyboard","parameters":{"key":32}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"None\""}}]},{"eventType":"block","conditions":[{"id":"on-key-released","objectClass":"Keyboard","parameters":{"key":32}}],"actions":[],"children":[{"eventType":"comment","text":"Max"},{"eventType":"block","conditions":[{"id":"compare-two-values","objectClass":"System","parameters":{"first-value":"Sprite.ChargeTime","comparison":0,"second-value":"Sprite.MaxChargeTime"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Max\""}}]},{"eventType":"comment","text":"Too Fast:  t  <  25%"},{"eventType":"block","conditions":[{"id":"compare-two-values","objectClass":"System","parameters":{"first-value":"Sprite.ChargeTime","comparison":2,"second-value":"Sprite.MaxChargeTime * 0.25"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Too Fast\""}}]},{"eventType":"comment","text":"Good:  25  <  t  <  85%"},{"eventType":"block","conditions":[{"id":"is-between-values","objectClass":"System","parameters":{"value":"Sprite.ChargeTime","lower-bound":"Sprite.MaxChargeTime * 0.25","upper-bound":"Sprite.MaxChargeTime * 0.85"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Good\""}}]},{"eventType":"comment","text":"Prefect:  85  <  t  <  99%"},{"eventType":"block","conditions":[{"id":"is-between-values","objectClass":"System","parameters":{"value":"Sprite.ChargeTime","lower-bound":"Sprite.MaxChargeTime * 0.85","upper-bound":"Sprite.MaxChargeTime - 1"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"ChargeLevel","value":"\"Prefect\""}}]}]}]}
```

