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
