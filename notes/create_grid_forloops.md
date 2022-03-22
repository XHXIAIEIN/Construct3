# 利用循环创建棋盘

## 双重循环方案 

```
起始X位置 + loopindex("X") * (方块宽度+左右间距)
起始Y位置 + loopindex("Y") * (方块高度+上下间距)
```

例如，在 (10, 10) 的位置，创建 5*5 的棋盘，每个网格尺寸 32x32, 上下左右间距 2 像素。 

```
For "X" from 0 to 10-1
For "Y" from 0 to 10-1
    Create object Sprite on layer 0 at (10 + loopindex("X") × (32+2), 10 + loopindex("Y") × (32+2))
```

剪贴板(需要 Sprite 对象)
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"X\"","start-index":"0","end-index":"10-1"}},{"id":"for","objectClass":"System","parameters":{"name":"\"Y\"","start-index":"0","end-index":"10-1"}}],"actions":[{"id":"create-object","objectClass":"System","parameters":{"object-to-create":"Sprite","layer":"0","x":"10 + loopindex(\"X\") * (32+2)","y":"10 + loopindex(\"Y\") * (32+2)","create-hierarchy":false,"use-template":null}}]}]}
```


## 单循环方案 

```
起始X位置 + 左右间距 + 方块宽度 * loopindex % 每行数量 
起始Y位置 + 上下间距 + 方块高度 * floor(loopindex / 每行数量)
```


例如，在 (10, 10) 的位置，每行 4 个，共创建 32 个网格，每个网格尺寸 16x16, 上下左右间距 2 像素。

```
For "" from 0 to 32-1
    Create object Sprite on layer 0 at (10 + 2 + 16 × loopindex % 4, 10 + 2 + 16 × floor(loopindex÷4)), create hierarchy: False, template: (none)
```

剪贴板(需要 Sprite 对象)
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[],"children":[{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"\"","start-index":"0","end-index":"32-1"}}],"actions":[{"id":"create-object","objectClass":"System","parameters":{"object-to-create":"Sprite","layer":"0","x":"10 + 2 + 16 * loopindex % 4","y":"10 + 2 + 16 * floor(loopindex/4)","create-hierarchy":false,"use-template":null}}]}]}]}
```


