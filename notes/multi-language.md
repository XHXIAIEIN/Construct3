在游戏中实现多语言系统

## 必要的插件对象
- AJAX 
- JSON 
- Dictionary 
  
AJAX 负责在游戏中加载翻译文件。  
JSON 负责接收从 AJAX 传递过来的文件数据，进行解析。
Dictionary 负责储存翻译文本数据，游戏中也是从这里调用对话。


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

<img width="120" src="https://user-images.githubusercontent.com/45864744/152724410-e28d63a2-8787-4e97-bb12-49ff54b2796c.png">

2. 在场景安排一个 Text 对象。  

<img width="460" src="https://user-images.githubusercontent.com/45864744/152724455-3794572d-5523-4060-bbab-f000cd8cd204.png">

3. 给 Text 对象添加一个实例变量，MessageID

<img width="460" src="https://user-images.githubusercontent.com/45864744/152724527-b75b067c-f208-4fa0-8e4d-70d579f950e4.png">


## 事件表

1. 准备一个全局变量，Default_language，默认值：zh_CN

<img width="240" src="https://user-images.githubusercontent.com/45864744/152727006-802fc74f-faac-4b87-b7f2-fbdcb3c3e40d.png">

2. AJAX，加载翻译文件，基本操作了。

<img width="460" src="https://user-images.githubusercontent.com/45864744/152727071-9c748a8b-d706-4c45-8b4e-4400c4198024.png">
  
如果此时预览游戏，可以看到数据已经可以加载到了。  

<img width="240" src="https://user-images.githubusercontent.com/45864744/152727787-cf75ebe7-22f9-4db3-9825-02e6c37f53e7.png"> <img width="240" src="https://user-images.githubusercontent.com/45864744/152727942-ed11ecae-4e24-4453-8436-e335f7950f41.png">  


3. 打算
															   
															   
															   

