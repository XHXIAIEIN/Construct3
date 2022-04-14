# 如何使用 NW.js 读写文件


### 写入

检测游戏目录里某个文件夹是否存在。  
如果不存在，则创建文件夹，并在文件夹里新建文件 `readme.txt` 。    
如果已经存在，读取文本数据。  

![01](https://user-images.githubusercontent.com/45864744/147338391-3b9d02c1-c1bf-473e-b065-cf3be1f65540.png)


### 读取

Nw.js 自带一个表达式 ` NWjs.ReadFile(path) `  
如果直接填写文件名，则是读取游戏根目录的文件。

例如上面的例子，我想在游戏目录创建一个文件夹，文件夹里面创建一个文件。则路径就是这样的：

```
NWjs.ReadFile("mydata/readme.txt")
```

在游戏中读取到的结果就是，怎么写入的，读取出来也是一样的数据。  

```
Hello World
```

![03](https://user-images.githubusercontent.com/45864744/147339645-31d8428b-a814-4ae0-a84e-c0d55abeaaea.png)



---


## 读写特定格式的数据


### 数据格式

```
name=Ashley
age=18
money=infinite
```

### 写入

(根据自己的实际情景替换变量)

```
"name=" & "Ashely" &newline &
"age=" & "18" &newline &
"money=" & "infinite"
```

![02](https://user-images.githubusercontent.com/45864744/147338728-35a32221-cd90-4b80-9df8-0fc379751692.png)


### 读取

用 `tokenat` 对字符串进行拆分。  
第一步拆分换行，提取出 `name=Ashley`  
第二步拆分=号，提取出 `Ashley`  

```
tokenat(tokenat(userdata, 0, newline), 1, "=")
```

结果就是

```
Ashley
```


