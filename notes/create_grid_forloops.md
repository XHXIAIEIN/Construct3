# 利用循环创建棋盘

## 双重循环方案

```
起始X位置 + (方块宽度+左右间距) × loopindex("X")
起始Y位置 + (方块高度+上下间距) × loopindex("Y")
```

例如，在 (10, 10) 的位置，创建 5x5 的棋盘。格子尺寸为 32x32, 格子间距 2 像素。 

```
For "X" from 0 to 4
For "Y" from 0 to 4
Create object at
    10 + (32+2) × loopindex("X") 
    10 + (32+2) × loopindex("Y")
```

剪贴板(需要 Sprite 对象)
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[],"children":[{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"X\"","start-index":"0","end-index":"4"}},{"id":"for","objectClass":"System","parameters":{"name":"\"Y\"","start-index":"0","end-index":"4"}}],"actions":[{"id":"create-object","objectClass":"System","parameters":{"object-to-create":"Sprite","layer":"0","x":"10 + (32 + 2) * loopindex(\"X\")","y":"10 + (32 + 2) * loopindex(\"Y\")","create-hierarchy":false,"template-name":"\"\""}}]}]}]}
```


## 单循环方案 

```
起始X位置 + (左右间距 + 方块宽度) × loopindex % 每行数量 
起始Y位置 + (上下间距 + 方块高度) × floor(loopindex / 每行数量)
```

例如，在 (10, 10) 的位置，创建 20 个格子，每行 5 个。格子尺寸为 32x32, 格子间距 2 像素。 

```
For "" from 0 to 19
Create object at
    10 + (32 + 2) × loopindex % 5
    10 + (32 + 2) × floor(loopindex ÷ 5)
```

剪贴板(需要 Sprite 对象)
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[],"children":[{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"\"","start-index":"0","end-index":"19"}}],"actions":[{"id":"create-object","objectClass":"System","parameters":{"object-to-create":"Sprite","layer":"0","x":"10 + (32 + 2) * loopindex % 5","y":"10 + (32 + 2) * floor(loopindex / 5)","create-hierarchy":false,"template-name":"\"\""}}]}]}]}
```

## 在中心创建向两边创建列表

function
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"functionName":"centerCreate","functionDescription":"","functionCategory":"","functionReturnType":"none","functionCopyPicked":false,"functionIsAsync":false,"functionParameters":[{"name":"spawnCount","type":"number","initialValue":"1","comment":""},{"name":"padding","type":"number","initialValue":"10","comment":""},{"name":"direction","type":"string","initialValue":"Horizontal","comment":"Horizontal or Vertical"}],"eventType":"function-block","conditions":[],"actions":[],"children":[{"eventType":"block","conditions":[{"id":"compare-eventvar","objectClass":"System","parameters":{"variable":"direction","comparison":0,"value":"\"Horizontal\""}}],"actions":[],"children":[{"eventType":"variable","name":"itemWidth","type":"number","initialValue":"0","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"repeat","objectClass":"System","parameters":{"count":"spawnCount"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"itemWidth","value":"Sprite.Width + padding"}},{"id":"create-object","objectClass":"System","parameters":{"object-to-create":"Sprite","layer":"0","x":"line.BBoxMidX  - (itemWidth * floor(spawnCount/2)) + (itemWidth * loopindex)","y":"line.BBoxMidY","create-hierarchy":false,"template-name":"\"\""}}]}]},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"},{"id":"compare-eventvar","objectClass":"System","parameters":{"variable":"direction","comparison":0,"value":"\"Vertical\""}}],"actions":[],"children":[{"eventType":"variable","name":"itemHeight","type":"number","initialValue":"0","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"repeat","objectClass":"System","parameters":{"count":"spawnCount"}}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"itemHeight","value":"Sprite.Height + padding"}},{"id":"create-object","objectClass":"System","parameters":{"object-to-create":"Sprite","layer":"0","x":"line.BBoxMidX","y":"line.BBoxMidY - (itemHeight * floor(spawnCount/2)) + (itemHeight * loopindex)","create-hierarchy":false,"template-name":"\"\""}}]}]}]}]}
```


