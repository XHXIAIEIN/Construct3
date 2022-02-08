实现长按蓄力的机制

## 必要的变量

-ChargeTime
-ChargeSpeed
-MaxChargeTime

ChargeTime，当前蓄力的时间进度，以毫秒为单位。
MaxChargeTime，可以蓄力的最大时间，数值越大，需要蓄力越久。
ChargeSpeed，每次蓄力增加的时间，数值越大，蓄力速度越快。

这里，我是将它作为实例变量使用。

## 事件表

