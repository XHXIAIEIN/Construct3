# Scripting cheatsheet [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)


## 全局变量(Global variable)

用脚本获取全局变量。

```javascript
runtime.globalVars.Variable1
```

## 局部变量(Local variable)

在事件表的事件条内，用脚本获取本地变量。备注，获取函数传入参数 `Function parameter` 也是使用这个方法获取。

```javascript
localVars.Variable2
```

在某些情况下，如果你的变量名称可能不是有效的标识符，此时，你还可以用字符串来引用。

```javascript
runtime.globalVars["Score"]
localVars["Score"]
instVars["Score"]
```

## 实例变量(Instances variable)

获取实例对象的实例变量。需要先获取到 `instance` 对象，才可以引用它的属性。

```javascript
instance.instVars.Variable1
```

## 实例对象(Instances Object)


## 获取第一个实例对象

```javascript
runtime.objects.Sprite.getFirstInstance()
```

## 获取所有实例对象

返回的是一个数组。

```javascript
runtime.objects.Sprite.getAllInstances()
```

## 遍历所有实例对象的实例变量

遍历所有 Sprite 对象的实例变量 `Score` ，同时销毁所有变量小于 60 的实例。

```javascript
for (const player of runtime.objects.Sprite.instances())
{
    const score = inst.instVars["Score"];

    if (score <= 60) 
    {
        player.destroy();
    }
}
```

