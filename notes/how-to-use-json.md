# 如何使用 JSON

## Example 1
```json
{
  "name": "Love"
}
```
```js
JSON.Get("name")  // Love
```

## Example 2
```json
{
  "array": [123, 456]
}
```
```js
JSON.Get("array.0")  // 123
```

## Example 3
```json
{
    "window": {
        "title": "Construct 3",
        "name": "main",
        "width": 500,
        "height": 500
    },
}
```
```js
JSON.Get("window.name")  // main
```

## Example 4
```json
{
    "window": {
        "title": "Construct 3",
        "name": "main",
        "width": 500,
        "height": 500,
        "style": ["normal", "bold", "inherit"]
    },
}
```
```js
JSON.Get("window.style.0") // normal
```

## Example 5
```json
{
    "window": {
        "title": "Construct 3",
        "name": "main",
        "width": 500,
        "height": 500,
        "image": { 
            "name": "pig",
            "width": 250,
            "height": 250
        },
    },
}
```
```js
JSON.Get("window.image.name") // pig
```

## Example 6
```json
{  
    "window": {
        "title": "Construct 3",
        "name": "main",
        "example": [ 
            { "color": "Red", "width": 500, "height": 500, "list":[0, 1, 2, 3]},
            { "color": "Blue", "width": 500, "height": 500, "list":[5, 6, 7, 8]}
        ]
    },
}
```
```js
JSON.Get("window.example.0.color") // Red
JSON.Get("window.example.1.list.0") // 5
```

---

# 如何加载 JSON 文件

在 C3 中加载 JSON 文件，必须要通过 AJAX 对象请求加载项目文件，请求成功后得到 `AJAX.LastData`。然后将数据传入 JSON 对象，使用 Parse 动作将数据解析成字符串，就可以使用了。

## 插件对象

首先，加入2个必要的插件对象。
- AJAX
- JSON

![0](https://user-images.githubusercontent.com/45864744/147193633-bb917fcf-b50d-4f9b-b898-3b217c8c3094.png)


## 文件
在 Files 文件夹中导入 JSON 文件。

![1](https://user-images.githubusercontent.com/45864744/147193533-583773f7-e3f5-451e-a282-4e71ac56d0f6.png)


## 事件表

### 过程思路

- 使用 AJAX 对象执行 ` Request project file ` 动作来读取文件  
- **等待 AJAX 读取完成**   
- 使用 JSON 对象执行 ` Parse ` 动作解析数据 ` AJAX.LastData `  


### 截图演示 

| AJAX  | JSON |
| ----- | ---- |
|  ![ajax_Request_project_file](https://user-images.githubusercontent.com/45864744/147197052-6ad3b6c8-6ab8-437e-9ba2-2af298ef74b4.png)  | ![json_parse](https://user-images.githubusercontent.com/45864744/147197183-edd2d8ed-6d19-4a57-af0a-728e6299fbf6.png) |


### 异步指令

注意到了吗？ AJAX 的动作后面都带有小时钟的图标，代表它是异步调用的。必须要等待它完成才可以进行下一步动作，否则如果数据还没请求完成，你就直接拿来用了，这样会拿不到完整数据的。所以，这中间需要加一个等待它完成的环节。  

有 2 种方式，可以根据自己的使用需求选择：  

第一种，直接等待它完成，再继续执行下一步。  
适用于你的项目比较简单，只是随便用用，不需要想那么多的情况。  

系统动作里的 ` Wait for previous actions `， 等待上个异步指令完成。  

![04](https://user-images.githubusercontent.com/45864744/147194826-39497b88-a0b4-4cf1-af54-fe6c70ae5120.png)


第二种，监听AJAX请求完成的回调函数，再继续执行。  
适用于请求文件较多的项目，你需要认真的管理每个Tag的请求，好处就是，更易于管理。    
  
![03](https://user-images.githubusercontent.com/45864744/147194744-761941c8-4884-4605-b573-b54b15b29f6b.png)  


快速剪贴板:
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"request-project-file","objectClass":"AJAX","parameters":{"tag":"\"file\"","file":"file.json"}}]},{"eventType":"block","conditions":[{"id":"on-completed","objectClass":"AJAX","parameters":{"tag":"\"file\""}}],"actions":[{"id":"parse","objectClass":"JSON","parameters":{"data":"AJAX.LastData"}}]}]}
```
  
  
现在JSON数据已经在 JSON 里面了。下面讲讲怎么使用它。

---

# 如何访问 JSON 数据

例如，你的JSON结构是这样的

## 案例一

最简单的数据结构

```json
{
  "name": "Ashely",
  "age": 18,
  "score": 100
}
```

读取到 ` name ` 的数据 (Ashely) ：  

```
JSON.Get("name")
```


## 案例二

比起案例一，外面多了一层数组。数组的路径就是索引下标。

```json
{
  "team": 
  [
    { "name": "Ashely", "age": 18, "score": 100 },
    { "name": "Tom", "age": 17, "score": 95 }
  ]
}
```

获取 ` Ashely ` 的名字

```
JSON.Get("team.0.name")
```


获取 ` Tom ` 的分数

```
JSON.Get("team.1.score")
```


## 案例三

比起案例二，每个人的数据里，多了一个 `fruit` 喜欢的水果，它是一个数组。

```json
{
  "team": 
  [
    { "name": "Ashely", "age": 18, "score": 100, "fruit":["Apple", "Banana", "Cherry", "Durian"] },
    { "name": "Tom", "age": 17, "score": 95, "fruit":["Apple", "Berry"] }
  ]
}
```

获取 Ashely 喜欢的 **第二种** 水果( ` Banana ` )

```
JSON.Get("team.0.fruit.1")
```

如何获取 Ashely **全部** 喜欢的水果

```

```


---

扩展阅读：
[在游戏中实现多语言菜单](https://github.com/XHXIAIEIN/Construct3/blob/main/notes/multi-language.md)
