# 如何使用随机数

## Example 1
生成 0 到 1 之间的随机数，不包含 1 。
```
random(1)
```

## Example 1.2
生成 0 到 6 之间的随机正整数，不包含 6 。
```
floor(random(6))
```
结果范围：
```
0  1  2  3  4  5
```

补充知识点：

`floor` 向下取整，如：`floor(5.9) = 5`
`ceil`  向上取整，如：`ceil(5.1) = 6`
`round` 四舍五入，如：`round(5.6) = 6`

-
`int` 将浮点数，或包含数字开头的文本转换为整数，如：`int("3.14159abcd") = 3`
`float` 将整数，或包含数字开头的文本转换为浮点数，如：`float("3.1415abcd") = 3.1415`
`str` 将整数或浮点数转换为字符串。可以不使用，因为可以通过 `"Your score is " & score` 拼接字符串


## Example 3
生成 1 到 6 之间的随机正整数。类似抛骰子。
```
1 + floor(random(6))
```
结果范围：
```
1  2  3  4  5  6
```

## Example 4
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

## Example 5
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


