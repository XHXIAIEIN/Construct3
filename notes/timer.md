
# 方法1：使用 Timer 

| Expressions    | Description      |
| :------------- | :--------------- |
| CurrentTime    | 当前时间          |
| Duration       | 持续时间          |
| TotalTime      | 总计时时间        |

用法：    
- Sprite.Timer.CurrentTime(tag)
- Sprite.Timer.Duration(tag)
- Sprite.Timer.TotalTime(tag)

计算公式：  
``` 
ceil(Sprite.Timer.Duration("tag") - Sprite.Timer.CurrentTime("tag"))
```
  
<details><summary>clipboard</summary>

似乎可以直接复制这段东西，然后到事件表里面粘贴。  
但你需要提前创建好 Text, Sprite， Sprite 需要添加 Timer 的 behavior  
  
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"start-timer","objectClass":"Sprite","behaviorType":"Timer","parameters":{"duration":"5.0","type":"once","tag":"\"end\""}}]},{"eventType":"block","conditions":[{"id":"is-timer-running","objectClass":"Sprite","behaviorType":"Timer","parameters":{"tag":"\"end\""}}],"actions":[{"id":"set-text","objectClass":"Text","parameters":{"text":"ceil(Sprite.Timer.Duration(\"end\") - Sprite.Timer.CurrentTime(\"end\"))"}}]},{"eventType":"block","conditions":[{"id":"on-timer","objectClass":"Sprite","behaviorType":"Timer","parameters":{"tag":"\"end\""}}],"actions":[{"id":"set-text","objectClass":"Text","parameters":{"text":"\"\""}}]}]}
```
</details>

mm : ss
```
zeropad(floor((Sprite.Timer.Duration("tag") - Sprite.Timer.CurrentTime("tag")) / 60), 2) & " : " & zeropad(int((Sprite.Timer.Duration("tag") - Sprite.Timer.CurrentTime("tag")) % 60), 2) 
```

<details><summary>clipboard</summary>
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"start-timer","objectClass":"Sprite","behaviorType":"Timer","parameters":{"duration":"5.0","type":"once","tag":"\"end\""}}]},{"eventType":"block","conditions":[{"id":"is-timer-running","objectClass":"Sprite","behaviorType":"Timer","parameters":{"tag":"\"end\""}}],"actions":[{"id":"set-text","objectClass":"Text","parameters":{"text":"zeropad(floor((Sprite.Timer.Duration(\"end\") - Sprite.Timer.CurrentTime(\"end\")) / 60), 2) & \" : \" & zeropad(int((Sprite.Timer.Duration(\"end\") - Sprite.Timer.CurrentTime(\"end\")) % 60), 2) \r\n"}}]},{"eventType":"block","conditions":[{"id":"on-timer","objectClass":"Sprite","behaviorType":"Timer","parameters":{"tag":"\"end\""}}],"actions":[{"id":"set-text","objectClass":"Text","parameters":{"text":"\"\""}}]}]}
```
</details>



# 表达式解释：

| Expressions    | Description                        |
| :------------- | :--------------------------------- |
| ceil           | 向上取整，如 ceil(5.1) = 6          |
| floor          | 向下取整，如 floor(5.9) = 5         |
| round          | 四舍五入，如 round(5.6) = 6  ;  round(5.4) = 5   ;   round(5.5) = 6   |
| roundToDp      | 四舍五入保留小数，如 roundToDp(5.6123, 2) = 5.61  ;  roundToDp(5.489159, 2) = 5.49  |
| zeropad        | 补零，如 zeropad(3,2) = 03   ； zeropad(45,6) = 000045    |
| time/60%60     | 求时间分数     |
| time%60        | 求时间秒数     |






# 方法2：使用变量

|  Name          | Type          |  Description       |
| :------------- | :------------ | :----------------- |
|  started       | `<boolean>`   | 计时器是否已启动     |
|  countdown     | `<number>`    | 计时时长            |
|  t             | `<number>`    | 剩余时间            |

## 事件逻辑：  
当 t > 0 的时候，t 的数值持续减少，直到它小于 0，计时结束。  


<details><summary>clipboard</summary>

似乎可以直接复制这段东西，然后到事件表里面粘贴。  
但你需要提前创建好 Text

```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"variable","name":"timer_started","type":"boolean","initialValue":"false","comment":"","isStatic":false,"isConstant":false},{"eventType":"variable","name":"timer_countdown","type":"number","initialValue":"0","comment":"","isStatic":false,"isConstant":false},{"eventType":"variable","name":"t","type":"number","initialValue":"0","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"timer_countdown","value":"10"}},{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"t","value":"timer_countdown + 1"}},{"id":"set-boolean-eventvar","objectClass":"System","parameters":{"variable":"timer_started","value":"true"}}]},{"eventType":"block","conditions":[{"id":"compare-boolean-eventvar","objectClass":"System","parameters":{"variable":"timer_started"}}],"actions":[],"children":[{"eventType":"block","conditions":[{"id":"every-x-seconds","objectClass":"System","parameters":{"interval-seconds":"dt"}}],"actions":[],"children":[{"eventType":"block","conditions":[{"id":"compare-eventvar","objectClass":"System","parameters":{"variable":"t","comparison":4,"value":"0"}}],"actions":[{"id":"set-text","objectClass":"Text","disabled":true,"parameters":{"text":"ceil(t)"}},{"id":"set-text","objectClass":"Text","parameters":{"text":"zeropad(floor(t/60%60), 2) & \":\" & zeropad(floor(t%60), 2)\r\n"}},{"id":"set-eventvar-value","objectClass":"System","parameters":{"variable":"t","value":"max(0, t - dt)"}}]},{"eventType":"block","conditions":[{"id":"else","objectClass":"System"}],"actions":[{"id":"wait","objectClass":"System","parameters":{"seconds":"dt"}},{"id":"set-text","objectClass":"Text","parameters":{"text":"\"\""}},{"id":"set-boolean-eventvar","objectClass":"System","parameters":{"variable":"timer_started","value":"false"}}]}]}]}]}
```
</details>
