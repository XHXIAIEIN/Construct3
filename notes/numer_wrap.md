# 数字在范围内循环

常用于菜单、队列、动画的光标索引。

## 简单运用
数字在 0 1 2 之间循环
```
(Index + 1) % 3
```

## 用于数组
```
(index + 1) % Array.Width
```

## 用于动画帧
```
(Self.AnimationFrame + 1) % Self.AnimationFrameCount
```

## 变量：
- `Max`
- `Current`

## 公式
Set CurrentOption to `( Current + 1) % Max`


