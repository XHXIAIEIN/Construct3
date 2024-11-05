# 使用 random 生成随机数的高级用法

## Example 1
生成 0 到 1 之间的随机数，不包含 1 。
```
random(1)
```

## Example 2
生成 0 到 6 之间的随机正整数，不包含 6 。
```
floor(random(6))
```
结果范围：
```
0  1  2  3  4  5
```

## Example 3
生成 a 到 b 之间的随机正整数，不包含 b 。
```
floor(random(a, b))
```
举例
```
floor(random(2, 5))
```
结果范围：
```
2  3  4
```

补充知识点：

`floor` 向下取整，如：`floor(5.9) = 5`

`ceil`  向上取整，如：`ceil(5.1) = 6`

`round` 四舍五入，如：`round(5.6) = 6`

## Example 4
生成 1 到 6 之间的随机正整数。类似抛骰子。
```
1 + floor(random(6))
```
结果范围：
```
1  2  3  4  5  6
```
补充：
```
start + floor(random(end))
```
结果范围 \[start, start + end - 1]


## Example 5
生成 start 到 end 之间的随机正整数。
```
start + floor(random((end - start + 1)))
```
举例：生成 2 到 5 之间的随机正整数。
```
2 + floor(random((5 - 2 + 1)))
```
结果范围：
```
2  3  4  5
```

## Example 6
生成 start 到 end 之间，间隔为 step 的随机正整数。
```
start + floor(random((floor((end - start) / step) + 1))) * step
```
举例：生成 2 到 32 之间，间隔为 5 的随机正整数。
```
2 + floor(random((floor((32 - 2) / 5) + 1))) * 5
```
结果范围：
```
2  7  12  17  22  27  32
```

## Example 7

[Eerp](https://x.com/FreyaHolmer/status/1813629237187817600)
适合用在设置音频播放速度，让随机数集中在偏高的音调，也就是更多集中在头部，尾部逐渐减弱
```
a * exp(random(1) * ln(b / a))
```
