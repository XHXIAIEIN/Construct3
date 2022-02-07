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

<img width="230" src="https://user-images.githubusercontent.com/45864744/152728167-077d39f2-8c4b-42bf-b67f-385b87ee31a0.png">  <img width="230" src="https://user-images.githubusercontent.com/45864744/152728171-567d8f05-7e02-4f69-90a0-ba7fa091ba86.png">

3. 为了更方便地管理数据，可以将他们储存在字典(Dictionary)里。

因为字典是 Key-Value 的结构，我们需要用 JSON 的 For-each 对每个键值进行遍历

<img width="460" src="https://user-images.githubusercontent.com/45864744/152728627-31ce8285-6e36-4d01-968e-af3d33cab22c.png">

如果此时预览游戏，可以看到数据已经可以加载到了。

<img width="460" src="https://user-images.githubusercontent.com/45864744/152728992-b680592c-9b08-451d-befc-1b8adf0a2d70.png">


4. 现在只需要将所有 Text 文本的内容进行替换就可以了~

<img width="460" src="https://user-images.githubusercontent.com/45864744/152729855-5df3c86b-c349-46e2-a301-2dcc438c07db.png">


还记得数据结构吗？

LayoutName + MessageID + language

> 根据不同的场景(Layout)，读取其中不同的文本索引标签(MessageID)，找到语言代码(language)对应的翻译文本。

```
Dictionary.Get(LayoutName & "." & Self.MessageID & "." & Default_language)
```

然后预览游戏，就完成了~  

<img width="120" src="https://user-images.githubusercontent.com/45864744/152731002-87d03169-75d8-44f4-bfb9-fde6041f4222.png"> <img width="213" src="https://user-images.githubusercontent.com/45864744/152731286-f8c4f2a5-97a3-479b-be59-1033ac3eebc5.png"> <img width="120" src="https://user-images.githubusercontent.com/45864744/152731166-bfae4781-5f11-43c9-80e6-6ee012b31bca.png">



## 最终结果

<img width="460" src="https://user-images.githubusercontent.com/45864744/152730214-d753137f-59b4-4aee-bb04-57b2fb70d52a.png">

事件表剪贴板
```
{"is-c3-clipboard-data":true,"type":"events","items":[{"eventType":"variable","name":"Default_language","type":"string","initialValue":"zh_CN","comment":"","isStatic":false,"isConstant":false},{"eventType":"block","conditions":[{"id":"on-start-of-layout","objectClass":"System"}],"actions":[{"id":"request-project-file","objectClass":"AJAX","parameters":{"tag":"\"translations\"","file":"translations.json"}}]},{"eventType":"block","conditions":[{"id":"on-completed","objectClass":"AJAX","parameters":{"tag":"\"translations\""}}],"actions":[{"id":"parse","objectClass":"JSON","parameters":{"data":"AJAX.LastData"}}],"children":[{"eventType":"comment","text":"Layout"},{"eventType":"block","conditions":[{"id":"for-each","objectClass":"JSON","parameters":{"path":"JSON.Path"}}],"actions":[],"children":[{"eventType":"comment","text":"Message"},{"eventType":"block","conditions":[{"id":"for-each","objectClass":"JSON","parameters":{"path":"JSON.Path"}}],"actions":[],"children":[{"eventType":"comment","text":"Language"},{"eventType":"block","conditions":[{"id":"for-each","objectClass":"JSON","parameters":{"path":"JSON.Path"}}],"actions":[{"id":"add-key","objectClass":"Dictionary","parameters":{"key":"JSON.Path","value":"JSON.CurrentValue"}}]}]}]},{"eventType":"comment","text":"Text"},{"eventType":"block","conditions":[{"id":"for-each","objectClass":"System","parameters":{"object":"Text"}}],"actions":[{"id":"set-text","objectClass":"Text","parameters":{"text":"Dictionary.Get( LayoutName & \".\" & Self.MessageID & \".\" & Default_language )"}}]}]}]}
```

Text对象剪贴板
```
{"is-c3-clipboard-data":true,"type":"world-instances","items":[{"type":"Text","properties":{"text":"Text","enable-bbcode":true,"font":"Arial","size":24,"line-height":0,"bold":false,"italic":false,"color":[0,0,0,1],"horizontal-alignment":"left","vertical-alignment":"top","wrapping":"word","initially-visible":true,"origin":"top-left"},"instanceVariables":{"MessageID":"GameStart"},"behaviors":{},"world":{"x":85,"y":148,"width":300,"height":46,"originX":0,"originY":0,"color":[1,1,1,1],"angle":0,"zElevation":0}},{"type":"Text","properties":{"text":"Text","enable-bbcode":true,"font":"Arial","size":24,"line-height":0,"bold":false,"italic":false,"color":[0,0,0,1],"horizontal-alignment":"left","vertical-alignment":"top","wrapping":"word","initially-visible":true,"origin":"top-left"},"instanceVariables":{"MessageID":"GameSetting"},"behaviors":{},"world":{"x":85,"y":222,"width":300,"height":46,"originX":0,"originY":0,"color":[1,1,1,1],"angle":0,"zElevation":0}}],"object-types":[{"name":"Text","plugin-id":"Text","isGlobal":false,"instanceVariables":[{"name":"MessageID","type":"string","desc":""}],"behaviorTypes":[],"effectTypes":[]}]}
```



