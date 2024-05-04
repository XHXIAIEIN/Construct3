# 使用 JSON 对象操作 JSON

示例1: 基本数据结构

```json
{
    "name": "Cheems",
    "age": 16,
    "score": 100
}
```

使用 `Set value` 动作

![Snipaste_2024-01-05_14-53-26](https://github.com/XHXIAIEIN/Construct3/assets/45864744/fdd26193-1468-43e6-a15e-2d09cc226658)


示例2: 嵌套字典结构

比起前面的案例，外面多了一层 "team"。

```json
{
    "team": {
        "name": "Cheems",
        "age": 16,
        "score": 100
    }
}
```

先用 `Set object` 动作，将 "team" 作为对象。

使用 `Set value` 动作设置其他值。

方法1：绝对路径

在指定路径时，前面加上 "team." 引用绝对路径。

![Snipaste_2024-01-05_15-01-41](https://github.com/XHXIAIEIN/Construct3/assets/45864744/427e1c51-4627-47b2-b6a3-421f36986702)

方法2：相对路径

先使用 `Set Path` 进入到指定的路径。
使用 `Set value` 动作设置其他值，前面只需加上 "." 即可使用相对路径。

![Snipaste_2024-01-05_15-12-31](https://github.com/XHXIAIEIN/Construct3/assets/45864744/d2a3b919-0c90-47d2-88c0-76dd00e6cc7d)

方法3：连续使用相对路径

![Snipaste_2024-01-05_15-16-50](https://github.com/XHXIAIEIN/Construct3/assets/45864744/e3a9c19c-f41a-4083-b6ee-d30325c36677)

```json
{
    "team": {
        "name": "Cheems",
        "age": 16,
        "score": 100,
        "hobby": {
            "sing": 1,
            "dance": 1,
            "basketball": 0
        }
    }
}
```

如何区分绝对路径，还是相对路径？

绝对路径，包含完整的路径。而相对路径，则以 `.` 开头。

如果路径层数较多，使用绝对路径每次都需要写很长：`team.hobby.basketball`

使用相对路径，后面引用值得时候只需要前面加 "." 即可。


示例3: 数组结构

```json
{
    "team": [
        "Red",
        "Blue",
        "Green"
    ]
}
```

先用 `Set array` 动作，将 "team" 作为数组。

方法1： 使用 `Set value` 动作。

数组使用下标索引作为路径，例如 `team.0` 是数组第 1 个元素，这里的设置值是 "Red"

![Snipaste_2024-01-05_15-25-39](https://github.com/XHXIAIEIN/Construct3/assets/45864744/bc810a54-2ca1-42e7-92ff-1f7e6741c786)


方法2： 使用 `Push value` 动作。

将元素添加到数组的末尾/开头，并动态增加数组的长度。

![Snipaste_2024-01-05_15-28-28](https://github.com/XHXIAIEIN/Construct3/assets/45864744/52c188bf-2063-4c20-b73c-2aff4423c10c)




# 如何加载 JSON 文件

在 C3 中加载 JSON 文件，必须要通过 AJAX 对象请求加载项目文件，请求成功后得到 `AJAX.LastData`。然后将数据传入 JSON 对象，使用 Parse 动作将数据解析成字符串，就可以使用 `JSON.Get()` 获取对应数据了。

## 插件对象

首先，加入2个必要的插件对象。
- AJAX
- JSON

![0](https://user-images.githubusercontent.com/45864744/147193633-bb917fcf-b50d-4f9b-b898-3b217c8c3094.png)

## 文件
在 Files 文件夹中导入 JSON 文件。

![1](https://user-images.githubusercontent.com/45864744/147193533-583773f7-e3f5-451e-a282-4e71ac56d0f6.png)

## 事件表

### 加载步骤

1. 使用 AJAX 对象执行 `Request project file` 动作加载文件。  
2. **异步等待 AJAX 读取完成**   
3. 使用 JSON 对象执行 `Parse` 动作解析 `AJAX.LastData` 的数据  

### 截图演示 

| AJAX  | JSON |
| ----- | ---- |
|  ![ajax_Request_project_file](https://user-images.githubusercontent.com/45864744/147197052-6ad3b6c8-6ab8-437e-9ba2-2af298ef74b4.png)  | ![json_parse](https://user-images.githubusercontent.com/45864744/147197183-edd2d8ed-6d19-4a57-af0a-728e6299fbf6.png) |


#### 关于异步动作

注意到了吗？ AJAX 的动作后面带有小时钟的图标，代表它是异步调用的。

必须要等待它完成才可以进行下一步动作，否则如果数据此时还没请求完成，你就直接拿来使用，这样会拿不到完整数据的，C3会给你返回 0 的结果。所以，这中间需要加一个等待它完成的环节，确保获取到了数据。  

有 2 种方式，可以根据自己的使用需求选择：  

**第一种**：直接等待它完成，再继续执行下一步。适用于你的项目比较简单，只是随便用用，不需要想那么多的情况。  

系统动作里的 ` Wait for previous actions `， 等待上个异步指令完成。  

![04](https://user-images.githubusercontent.com/45864744/147194826-39497b88-a0b4-4cf1-af54-fe6c70ae5120.png)

**第二种**: 监听AJAX请求完成的回调函数，再继续执行。适用于请求文件较多的项目，你需要认真的管理每个 Tag 的请求，好处就是，更易于管理，方便的结构化组织项目。    
  
![03](https://user-images.githubusercontent.com/45864744/147194744-761941c8-4884-4605-b573-b54b15b29f6b.png)  


快速剪贴板:
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"request-project-file","objectClass":"AJAX","parameters":{"tag":"\"file\"","file":"file.json"}}]},{"eventType":"block","conditions":[{"id":"on-completed","objectClass":"AJAX","parameters":{"tag":"\"file\""}}],"actions":[{"id":"parse","objectClass":"JSON","parameters":{"data":"AJAX.LastData"}}]}]}
```

#### 动态引用文件路径

上面使用 `Request project file` 加载项目中的文件，但如果你的文件比较多，从下拉框里面选文件会变得非常繁琐，这时候你肯定希望能使用动态字符串引用变量来加载项目文件。

那么就可以使用它旁边的 `Request URL` 动作，在 `URL` 填入文件名即可。

| Request URL  | URL  |
| ------------ | ---- |
| ![ajax_Request_url](https://user-images.githubusercontent.com/45864744/211976126-26d37f42-a786-4fae-ab76-0a5a980070e5.png)  | ![request_url](https://user-images.githubusercontent.com/45864744/211976400-6cab7c88-5a51-4d08-b963-b1d9358fc537.png) |

如果想要在文件夹中使用变量，就需要用 `"字符串" & 变量名 & ".文件后缀名"` 组合字符串。

```
"file" & variable & ".json"
```

# 如何读取 JSON 数据

## Example 1 

最简单的 JSON 数据结构

```json
{
  "name": "Cheems",
  "age": 18,
  "score": 100
}
```

如何读取 `name` 的数据 (Cheems) ：  

```
JSON.Get("name")
```

## Example 2

比起前面的案例，外面多了一层 "team"。

```json
{
    "team": 
    {
        "name": "Cheems",
        "age": 18,
        "score": 100
    }
}
```

获取 `Cheems` 的名字

```
JSON.Get("team.name")
```

## Example 3

最简单的数组结构，数组的路径就是索引下标，从 0 开始计数。

```json
{
  "array": [123, 456]
}
```

获取 `array` 的第 1 项目数据，也就是 123 的数字。

```js
JSON.Get("array.0")
```

## Example 4

比起前面的案例，又多了一层数组，数组的路径就是索引下标，从 0 开始计数。

```json
{
  "team": 
  [
    { "name": "Cheems", "age": 18, "score": 100 },
    { "name": "Marmot", "age": 17, "score": 95 }
  ]
}
```

获取 `Cheems` 的名字

```
JSON.Get("team.0.name")
```

获取 `Marmot` 的分数

```
JSON.Get("team.1.score")
```

## Example 5

注意看前面，它不再是 {} 的开头，而是 [] 作为 JSON 数组

```json
[
    {
        "name": "Cheems",
        "age": 18,
        "score": 100
    },
    {
        "name": "Marmot",
        "age": 17,
        "score": 95
    }
]
```

获取到 `Cheems` 的名字

```
JSON.Get("0.name")
```

获取 `Marmot` 的分数

```
JSON.Get("0.score")
```

## Example 6

比起之前的案例，现在每个人的数据里，多了一个 `fruit` 喜欢的水果，它是一个数组。

```json
{
    "team": [
        {
            "name": "Cheems",
            "age": 18,
            "score": 100,
            "fruit": ["Apple", "Banana", "Cherry", "Durian"]
        },
        {
            "name": "Marmot",
            "age": 17,
            "score": 95,
            "fruit": ["Apple","Berry"]
        }
    ]
}
```

获取 `Cheems` 喜欢的 **第2种** 水果 (Banana)

```
JSON.Get("team.0.fruit.1")
```


## Example 7.1

如何获取 Cheems **全部** 喜欢的水果

这里需要用到 "循环" 的概念，让事件通过 JSON 对象的 'For each' 条件，遍历整个 `team.0.fruit"` 节点，这时就可以用 `JSON.CurrentKey` 和 `JSON.CurrentValue` 获取到当前循环的键名和键值。

![image](https://github.com/XHXIAIEIN/Construct3/assets/45864744/cabb2de4-8c19-46e6-b7be-d348071b2b35)

![image](https://github.com/XHXIAIEIN/Construct3/assets/45864744/eece798b-3d6a-4258-92e6-929ca59d1923)

运行结果：  
```
0 : Apple
1 : Banana
2 : Cherry
3 : Durian
```

## Example 7.2

如何获取 Cheems **全部** 喜欢的水果，并将它们存到数组里

和前面的步骤类似，但这次直接用 Aray 对象的 Push 动作，将 `JSON.CurrentValue` 推入数组中。  

![image](https://github.com/XHXIAIEIN/Construct3/assets/45864744/c22e964d-0ed5-46b1-be7f-9aa3c3cc6500)

运行结果：  
![image](https://github.com/XHXIAIEIN/Construct3/assets/45864744/2f8a98d5-b6fd-4c82-b7b0-5743b5a1c6f1)

如何获取数据？
```
Array.At(0)
```

## Example 7.3
希望存到数组里面的是一个二维数组

和前面的步骤类似，但这次 Array 的尺寸不同，并且多了一个 Set Value 的操作

![Snipaste_2023-06-29_11-32-04](https://github.com/XHXIAIEIN/Construct3/assets/45864744/fd128f49-ea95-476c-a377-aec408088a5a)

运行结果：  
![Snipaste_2023-06-29_11-31-41](https://github.com/XHXIAIEIN/Construct3/assets/45864744/d8ea3688-9819-44c6-8fbd-7ba30a0238b8)

如何获取 Array 的数据？ `Array.At(X,Y)`   

![image](https://github.com/XHXIAIEIN/Construct3/assets/45864744/8ef3aaf3-2f06-4781-a501-0cc5bfa84c0d)


---

# 修改 JSON 对象的数据

## 在位置插入 JSON 数据

现有：
```json
{
    "array":
    [
        {"foo": "1"},
        {"bar": "2"}
    ]
}
```

目标: 在 `array` 的数组中，插入一段 json 数据。

```json
{
    "array":
    [
        {"foo": "1"},
        {"bar": "2"},
        {"new": "3"}
    ]
}
```

步骤：
1. 使用 `Insert value` 动作，在 `array` 的前面位置插入任意的数据。
2. 用 `Set JSON` 动作，修改 `array.0` 的内容为 `"{""new"": ""3""}"`。 

注意，如果要在字符串的表达式中使用双引号 `"`，必须用连续两个 `""` 来代替。

![Snipaste_2023-01-11_23-55-44](https://user-images.githubusercontent.com/45864744/211978066-c3442983-6036-4288-97ab-18fba5fdb239.png)


## 插入数组类型的JSON

例如，想要在 JSON 中创建这样的数据

```json
[
	{ "id": 111, "name": ""},
	{ "id": 233, "name": ""},
]
```

在事件表中，会稍微麻烦点。需要先将路径转换成不同的对象类型。

<img width="664" alt="Snipaste_2024-05-04_22-04-13" src="https://github.com/XHXIAIEIN/Construct3/assets/45864744/dd9b7abf-1e0a-42f5-8c96-7c37b7b36971">


```json
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"parse","objectClass":"JSON","parameters":{"data":"\"[]\""}},{"id":"set-array","objectClass":"JSON","parameters":{"path":"\".\"","size":"0"}}],"children":[{"eventType":"block","conditions":[{"id":"repeat","objectClass":"System","parameters":{"count":"2"}}],"actions":[{"id":"push-value","objectClass":"JSON","parameters":{"where":"back","path":"\".\"","value":"0"}},{"id":"set-object","objectClass":"JSON","parameters":{"path":"\".\" & loopindex"}},{"id":"set-value","objectClass":"JSON","parameters":{"path":"StringSub(\".{0}.id\", loopindex)","value":"0"}},{"id":"set-value","objectClass":"JSON","parameters":{"path":"StringSub(\".{0}.name\", loopindex)","value":"\"\""}}]}]}]}
```

但是用脚本倒是会方便很多：

```js
const dataInst = runtime.objects.JSON.getFirstInstance();

const data = [
	{ "id": 111, "name": ""},
	{ "id": 233, "name": ""},
]

dataInst.setJsonDataCopy(data);
```

```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"type":"script","script":"const dataInst = runtime.objects.JSON.getFirstInstance();\n\nconst data = [\n\t{ \"id\": 111, \"name\": \"\"},\n\t{ \"id\": 233, \"name\": \"\"},\n]\n\ndataInst.setJsonDataCopy(data);"}]}]}
```


---

# 脚本

## 使用脚本将数据保存到 JSON 对象

```javascript
const tempdata = {
    "Levels": [
        {
            "LevelName" : "Home office",
            "ObjectsCoordinates": [
                {
                    "x": 20,
                    "y": 10
                },
                {
                    "x": 30,
                    "y": 60
                }
            ]
        },
        {
            "LevelName" : "Living room",
            "ObjectsCoordinates": [
                {
                    "x": 220,
                    "y": 110
                },
                {
                    "x": 30,
                    "y": 660
                }
            ]
        },
        {
            "LevelName" : "Master room",
            "ObjectsCoordinates": [
                {
                    "x": 100,
                    "y": 100
                },
                {
                    "x": 30,
                    "y": 100
                }
            ]
        }
    ]
}

const jsonObject = runtime.objects.JSON;
const jsonInstance = jsonObject.getFirstPickedInstance();

jsonInstance.setJsonDataCopy(tempdata)
```

![Snipaste_2023-01-12_11-32-01](https://user-images.githubusercontent.com/45864744/211977894-d88b4d25-4893-490c-9a2f-120732c54f24.png)


---

# 数组

## 将 JSON 对象中的数组储存到 Array 对象

先看个最简单简单的例子，这个适合最简单的一维数组。

```json
{
  "array": [100, 200]
}
```

将它储存到 JSON 后， 通过 System: For `0` to `JSON.ArraySize("array")-1` 进行遍历，使用 Array 的 Push 动作将 `JSON.Get("array." & loopindex)` 推入数组即可。 

由于是对数组进行 Push， 所以需要先对 Array 进行初始化，将 Size 设置为 0，确保没有多余的数据。

![image](https://github.com/XHXIAIEIN/Construct3/assets/45864744/9cd804b5-ba84-4d3a-9c2a-f7d0a1fc8724)


**例子2**

现在扩展一下，外面多一层数组，然后以 \[name, score] 来储存数据。

```json
{
	"array": [
		["Cheems",100],
		["Marmot",95],
		["Roger",60]
	]
}
```

操作和上面几乎相同，但多了一个Y轴，所以 Push 的时候只推入第 0 项 `JSON.Get("array." & loopindex & ".0")`

然后对 Y 轴进行赋值 Set Value: (loopindex, 1) `JSON.Get("array." & loopindex & ".1")` 

![Snipaste_2023-06-12_15-24-38](https://github.com/XHXIAIEIN/Construct3/assets/45864744/fe8bd73e-f6e9-4a0e-9aeb-72e51cc41a3b)


快速剪贴板（子条件）
```json
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[],"actions":[{"id":"set-size","objectClass":"Array","parameters":{"width":"0","height":"JSON.ArraySize(\"array.0\")","depth":"1"}}]},{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"\"","start-index":"0","end-index":"JSON.ArraySize(\"array\")-1"}}],"actions":[{"id":"push","objectClass":"Array","parameters":{"where":"back","value":"JSON.Get(\"array.\" & loopindex & \".0\")","axis":"x"}},{"id":"set-at-xy","objectClass":"Array","parameters":{"x":"loopindex","y":"1","value":"JSON.Get(\"array.\" & loopindex & \".1\")"}}]}]}
```

**例子3**

基于上面的例子，但数组是任意长度的，根据第1项填充数组大小。

```json
{
	"array": [
		["Cheems",100,123,456,6,10],
		["Marmot",95,456,123,7,20],
		["Roger",60,789,654,8,30]
	]
}
```

这就需要用到双重循环来操作，

![Snipaste_2023-06-12_15-38-41](https://github.com/XHXIAIEIN/Construct3/assets/45864744/af5daecd-8b9d-42aa-b26b-1d62e12bcefb)


快速剪贴板（子条件）

```json
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[],"actions":[{"id":"set-size","objectClass":"Array","parameters":{"width":"0","height":"JSON.ArraySize(\"array.0\")","depth":"1"}}]},{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"x\"","start-index":"0","end-index":"JSON.ArraySize(\"array\")-1"}}],"actions":[{"id":"push","objectClass":"Array","parameters":{"where":"back","value":"JSON.Get(\"array.\" & loopindex(\"x\") & \".0\")","axis":"x"}}],"children":[{"eventType":"block","conditions":[{"id":"for","objectClass":"System","parameters":{"name":"\"y\"","start-index":"1","end-index":"JSON.ArraySize(\"array.0\")-1"}}],"actions":[{"id":"set-at-xy","objectClass":"Array","parameters":{"x":"loopindex(\"x\")","y":"loopindex(\"y\")","value":"JSON.Get(\"array.\" & loopindex(\"x\") & \".\" & loopindex(\"y\"))"}}]}]}]}
```

**例子4** (FYI)

在前面数组补充一个标题列，但是存入数组时希望能跳过它。

```json
{
	"array":[
		["name","score","age"],
		["Cheems",100,17],
		["Marmot",95,8],
		["Roger",60,21]
	]
}
```


---

扩展阅读：
[在游戏中实现多语言菜单](https://github.com/XHXIAIEIN/Construct3/blob/main/notes/multi-language.md)
