# 如何导入JSON

## 插件对象

首先，加入2个必要的插件对象。
- AJAX
- JSON

![0](https://user-images.githubusercontent.com/45864744/147193633-bb917fcf-b50d-4f9b-b898-3b217c8c3094.png)


## 文件
在 Files 文件夹中导入 JSON 文件。

![1](https://user-images.githubusercontent.com/45864744/147193533-583773f7-e3f5-451e-a282-4e71ac56d0f6.png)


## 事件表

过程思路

- 用 AJAX 执行 ` Request project file ` 来读取文件。 
- **等待 AJAX 读取完成。** 
- 让 JSON 执行 ` Parse ` 解析数据 ` AJAX.LastData `。

| AJAX  | JSON |
| ----- | ---- |
|  ![ajax_Request_project_file](https://user-images.githubusercontent.com/45864744/147197052-6ad3b6c8-6ab8-437e-9ba2-2af298ef74b4.png)  | ![json_parse](https://user-images.githubusercontent.com/45864744/147197183-edd2d8ed-6d19-4a57-af0a-728e6299fbf6.png) |

注意到了吗？ ajax 的动作后面都带有一个小时钟的图标，代表它是异步调用的。必须要等待它完成才可以进行下一步动作，否则如果数据还没请求完成，你就直接拿来用了，这样会拿不到完整数据的。所以，这中间需要加一个等待它完成的环节。

有 2 种方式，可以根据自己的使用需求选择：

第一种，直接等待它完成，再继续执行下一步。  
适用于你的项目比较简单，只是随便用用，不需要想那么多的情况。  

系统动作里有一个 ` Wait for previous actions ` 等待上个异步指令完成。
![04](https://user-images.githubusercontent.com/45864744/147194826-39497b88-a0b4-4cf1-af54-fe6c70ae5120.png)


第二种，监听AJAX请求完成的回调函数，再继续执行。  
适用于请求文件较多的项目，你需要认真的管理每个Tag的请求，

好处就是，更易于管理。  
![03](https://user-images.githubusercontent.com/45864744/147194744-761941c8-4884-4605-b573-b54b15b29f6b.png)



现在JSON数据已经在 JSON 里面了。下面讲讲怎么使用它。

---

# 如何导入JSON

例如，你的JSON结构是这样的

## 案例一

最简单的结构

```json
{
  "name": "Ashely",
  "age": 18,
  "score": 100
}
```

如何获取 ` Ashely ` 的数据
```
JSON.Get("name")
```

## 案例二

比起案例一，外面多了一层。

```json
{
  "team": 
  [
    { "name": "Ashely", "age": 18, "score": 100 },
    { "name": "Tom", "age": 17, "score": 95 }
  ]
}
```

如何获取 ` Ashely ` 的数据
```
JSON.Get("team.0.name")
```


## 案例三

比起案例二，多了一个 `fruit` 喜欢的水果列表。

```json
{
  "team": 
  [
    { "name": "Ashely", "age": 18, "score": 100, "fruit":["Apple", "Banana", "Cherry", "Durian"] },
    { "name": "Tom", "age": 17, "score": 95, "fruit":["Apple", "Berry"] }
  ]
}
```

如何获取 Ashely **第二款**喜欢的水果( ` Banana ` )

```
JSON.Get("team.0.fruit.1")
```

如何获取 Ashely **全部** 喜欢的水果

```

```

