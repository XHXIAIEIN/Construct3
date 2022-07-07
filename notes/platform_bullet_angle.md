## Platform 子弹角度跟随玩家朝向

Bullet 行为默认的角度方向是 0°，也就是默认往右边发射。如果希望子弹向左方向飞，就是将角度调整为 180° 或 -180°。 或者使用 Sprite 的 Spawn Other Object 动作，这样新创建的子弹也将跟随 Sprite 的角度。

2种方法：

### 设置镜像：  
在**发射子弹**的事件下添加子条件，判断玩家是否镜像，如果玩家已经镜像，那么将子弹的角度调整为 180°  
<img width="1020" src="https://user-images.githubusercontent.com/45864744/123759739-c55fb080-d8f2-11eb-83f3-8257fe9228d1.png">


### 计算角度：  
set angle to `round(angle(0, 0, sign(Player.Width), 0))` 

<img width="1016" src="https://user-images.githubusercontent.com/45864744/123760509-7e25ef80-d8f3-11eb-8249-8b522965134d.png">


---

### 表达式讲解 

| **sign(x)**              |
| ------------------------ |
|  判断一个实数的正负号。   |
| - 如果 x 大于 1，则返回  1  <br> - 如果 x 小于 1，则返回 -1  <br> - 如果 x 等于 0，则返回  0  |


| **angle(x1, y1, x2, y2)**   |
| --------------------------- |
| 计算两个坐标之间的角度。     |


| **round(x)**         |
| -------------------- |
| 四舍五入，向上取整。  |
| 例 round(5.6) = 6    |


### 公式讲解

```
round(angle(0, 0, sign(Player.Width), 0))
```

当对象被设为 **镜像** (Set Mirrored)时，编辑器实际上是**将它的 `宽度` 设为 `-宽度`**，实现简单的左右镜像效果。  

那么就可以用 `宽度` 去判断，如果宽度是负数，它目前就是处于 "镜像" 的状态。
  
最终公式的计算方式就变成了：  
正常：angle(0, 0, 1, 0)  
镜像：angle(0, 0, -1, 0)
  
<img width="320" alt="Snipaste_2021-06-29_16-27-18" src="https://user-images.githubusercontent.com/45864744/123763949-e5916e80-d8f6-11eb-8585-4f5e0deb366a.png">
    
    
    
---
    
### 扩展阅读

还有 @hcatarrunas 制作的这张角度关系图，右边是子弹的角度方向：  

![by-hcatarrunas](https://user-images.githubusercontent.com/45864744/123764134-1671a380-d8f7-11eb-8486-3ac9b95cbc26.png)



如果想让子弹的 180° 方向角度，转换成 360° 方向角度，可以用这个公式：
```
(angle(x1, y1, x2, y2)+360)%360
```
