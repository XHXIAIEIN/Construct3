# Scripting cheatsheet [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

Scripting in Construct 3 脚本备忘笔记


## 全局变量(Global variable)

用脚本获取全局变量。直接对它进行赋值操作也是可以的。

```javascript
runtime.globalVars.Variable1
```


## 局部变量(Local variable)

在事件条范围内，用脚本获取本地变量。备注，函数的传入参数(`Function parameter`) 也是通过它来获取。

```javascript
localVars.Variable2
```

提示，在某些情况下，变量名称可能不是有效的标识符，例如可能跟保留关键字冲突了。此时你还可以用字符串来引用这个变量。

```javascript
runtime.globalVars["Score"]
localVars["Score"]
instVars["Score"]
```


## 实例变量(Instances variable)

获取实例对象的实例变量。注意，需要先获取到 `instance` 对象才可以引用它的属性。

```javascript
instance.instVars.Variable1
```

## 调用函数(Call Function)

例如，事件表里有一个自定义函数 add 
```
runtime.callFunction("add")
```


## 获取第一个实例对象(First Instance Object)

```javascript
runtime.objects.Sprite.getFirstInstance()
```


## 获取所有实例对象(All Instances objects)

返回的是一个数组。

```javascript
runtime.objects.Sprite.getAllInstances()
```


## 获取实例对象的行为属性(Instance behaviors)

```javascript
instance.behaviors.Bullet.speed
```

在某些情况下，有些名称可能不是有效的标识符，此时，还可以用字符串来引用。

```javascript
instance.instVars["8Direction"]
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


## 调用函数

在 Function 用脚本调用参数

```javascript
localVars.Parameter0
```

在 Function 用脚本返回值

```javascript
runtime.setReturnValue();
```


## 编辑文本

```javascript
const textObject = runtime.objects.Text;
const textInstance = textObject.getFirstPickedInstance();

textInstance.text = "Hello World"
```


## 加载文件

在脚本中代替事件表AJAX加载文件的操作。
  
```javascript
async function OnBeforeProjectStart(runtime)
{
	const InfoData = await runtime.assets.fetchJson('info.json')
	runtime.objects.JSON.getFirstInstance().setJsonDataCopy(InfoData);
}
```

## 读取JSON

```javascript
const Data = runtime.objects.JSON.getFirstInstance().getJsonDataCopy();
console.log(Data['Name'])
```
