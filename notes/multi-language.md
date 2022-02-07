
## 必要的插件对象

- AJAX 
- Dictionary 
- JSON 

<img width="120" src="https://user-images.githubusercontent.com/45864744/152724375-26a90101-ec3f-490e-b9ef-a1404402c474.png">


## 翻译文件

新建一个 JSON 文件，重命名为 translations.json   

<img width="120" src="https://user-images.githubusercontent.com/45864744/152725165-170460cf-c286-4692-9a9c-6e7a2db4ab5a.png">

双击编辑它，就可以进行编辑了。 

数据结构思路：  
根据不同的场景(Layout)，读取其中不同的文本索引标签(MessageID)，找到语言代码(language)对应的翻译文本。

```json
{
	"Layout_Name": {
		"Message_ID": {
			"language": "text",
			"language": "text"
		},
		"Message_ID": {
			"language": "text",
			"language": "text"
		}
	},
	"Layout_Name": {
		"Message_ID": {
			"language": "text",
			"language": "text"
		}
	}
}
```
  
实际例子：  
例如现在有 2 个场景(Layout)，Menu 和 Tutorial

```json
{
	"Menu": {
		"GameStart": {
			"en_US": "Start",
			"zh_CN": "开始游戏"
		},
		"GameSetting": {
			"en_US": "Setting",
			"zh_CN": "设置"
		}
	},
	"Tutorial": {
		"welcome": {
			"en_US": "Welcome",
			"zh_CN": "欢迎"
		}
	}
}
```

例如，想读取 Menu 场景中的 GameStart 文本。  
中文语言：`Menu.GameStart.zh_CN`，读取的结果就是 `开始游戏`  
英文语言：`Menu.GameStart.en_US`，读取的结果就是 `Start`

这里就使用国际通用的语言代码来对不同语言进行索引。

|语言代码  | 语言                           |                |
|:------- |:------------------------------ |----------------|
| en_US   | English                        |                |
| zh_CN   | Chinese Simplified             | 简体中文        |
| zh_TW   | Chinese Traditional            | 繁體中文        |
| ja_JP   | Japanese                       | 日本語          |
| ko_KR   | Korean                         | 韓國語          |
| pt_BR   | Português                      | 葡萄牙語        |
| fr_FR   | Français                       | 法語            |
| ru_RU   | Russian                        | 俄語            |
 
## 场景

1. 准备一个场景(Layout)，重命名为 Menu  

<img width="84" src="https://user-images.githubusercontent.com/45864744/152724410-e28d63a2-8787-4e97-bb12-49ff54b2796c.png">

2. 在场景安排一个 Text 对象。  

<img width="460" src="https://user-images.githubusercontent.com/45864744/152724455-3794572d-5523-4060-bbab-f000cd8cd204.png">

3. 给 Text 对象添加一个实例变量，MessageID

<img width="460" src="https://user-images.githubusercontent.com/45864744/152724527-b75b067c-f208-4fa0-8e4d-70d579f950e4.png">

4. 再复制出1个实例对象，把它们的实例变量分别设置为：GameStart 和 GameSetting  

<img width="460" src="https://user-images.githubusercontent.com/45864744/152724642-e2479d78-a8c9-43fc-a13c-bdf7e63a8860.png">

小提示：按住 Ctrl + 鼠标左键拖动实例对象时，可以复制出一个实例对象。当然，你选中 Ctrl + C / Ctrl + V 也是同样的效果。


## 事件表

1. 准备一个全局变量，Default_language，默认值：zh_CN

<img width="240" src="https://user-images.githubusercontent.com/45864744/152727006-802fc74f-faac-4b87-b7f2-fbdcb3c3e40d.png">

2. AJAX，加载翻译文件，基本操作了

<img width="460" src="https://user-images.githubusercontent.com/45864744/152727071-9c748a8b-d706-4c45-8b4e-4400c4198024.png">





