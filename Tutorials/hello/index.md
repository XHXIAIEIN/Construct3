---
cover: https://gitbookio.github.io/onboarding-template-images/header.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# 如何评价 Construct3

[Construct 3](https://www.construct.net/a/260259?t=construct3) 是一款小而美的游戏开发工具，轻巧且功能强大，完全基于浏览器环境运行。

**我认为 Construct 3 是当下世界，最友好、最容易上手的 2D 游戏开发引擎。**

即使从未有游戏制作经验的人，也可以在短时间学会，制作出一个效果比较不错的游戏 Demo。

对于入门初学者或较擅长关卡设计、艺术表达的创作型开发者，C3 使用可视化事件表的编程方式，无需写代码，事件表的逻辑非常贴近人类自然语言。

当你希望做什么事情的时候，它能提供给你的是非常直观，随想即可得的编辑体验。编辑器内置了许多组件，帮助你快速实现某些功能的原型，常见的交互逻辑如果写代码可能要花掉一整个下午，而在 Construct 3 几分钟就能很好的解决\~

即便你完全没有程序基础，或编程能力较弱但又特别想尝试制作游戏的同学，强烈推荐你尝试它。还特别推荐给美术选手，这样你可以专心去设计游戏的交互玩法，并且会得到个不错的游戏表现。特别适合在 [GameJam](https://zhida.zhihu.com/search?content_id=490749515\&content_type=Answer\&match_order=1\&q=GameJam\&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDA3MjkxNjMsInEiOiJHYW1lSmFtIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6NDkwNzQ5NTE1LCJjb250ZW50X3R5cGUiOiJBbnN3ZXIiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.useIyASx47hcW-ZFzuRS5AGEkGBHAYpL4IpVUjASK50\&zhida_source=entity) 活动、游戏类毕设作品的场景使用。

事件表功能演示：

{% hint style="info" %}
【触发条件】  🐭 老鼠 碰撞到 🧀 奶酪\
【执行动作】  🧀 奶酪 消失
{% endhint %}

翻译成人类语言意思是，老鼠走到奶酪面前，吃掉了奶酪。

{% embed url="https://construct-static.com/videos/v1447/construct3/simple-event.mp4" %}

发挥你的想象力，然后[点击这里，自己动手试试](https://www.construct.net/a/260259?t=construct3tour)吧！就作为你的第一款游戏练习！ (C3自带中文，在设置里切换语言)

#### 对新手友好，但不只是可视化编程

对于专业的 Web 程序员，C3支持使用原生 [Javascript](https://www.construct.net/en/tutorials/construct-javascript-2866)、[Typescript](https://www.construct.net/en/tutorials/using-typescript-construct-3003) 编写代码，允许完全脱离事件表，仅用 JS/TS 进行开发，将 C3 作为场景编辑器来使用，结合 JavaScript 编写游戏([C3 SDK](https://www.construct.net/en/make-games/manuals/construct-3/scripting/using-scripting/javascript-construct))。即享受现代 Web 技术带来的高性能，C3 提供的 Runtime 也会帮你优化许多内存管理方面的工作，极大提高工作效率。Web性能很慢？大人，时代变了：[测试 60 FPS 可以同屏渲染多少Sprite对象](https://downloads.scirra.com/labs/piggyperf/)。

C3 提供了现代浏览器几乎所有的特性：支持 Web Worker 环境运行；支持 WebAssembly 模块；支持 WebGL 和 WebGPU 图形渲染器。支持 HTML Element 的 UI 工作流；支持基于 WebRTC 的[实时在线多人游戏](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/multiplayer)（点对点数据传输）；支持连接蓝牙、WebSocket、甚至提供了 [BBC micro:bit ](https://www.construct.net/en/tutorials/getting-started-bbc-microbit-3060)单片机的通信案例。

支持基于 WebView2 导出的 [Steam](https://www.construct.net/en/make-games/addons/1105/steamworks-webview2)、 [Epic Games](https://www.construct.net/en/make-games/addons/1106/epic-games-webview2)、 [Xbox UWP](https://www.construct.net/en/make-games/addons/1204/xbox-live-uwp) 平台集成，支持从 JavaScript 到 C++ 的通信，访问原生接口 ([Wrapper extensions](https://www.construct.net/en/make-games/manuals/addon-sdk/guide/wrapper-extensions))。集成了 [Game Center](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/game-center)、[Google Play](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/google-play) 移动游戏平台服务；集成了 [Admob advert](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/mobile-advert)(激励广告)、[Mobile IAP](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/mobile-iap) (游戏内购) 等变现渠道服务。

#### 一键导出到各个平台

C3的游戏支持导出到各个平台，游戏基于 WebView 环境运行。支持一键打包到 Web端([HTML5](https://www.construct.net/en/tutorials/publishing-web-10?vic=84))、移动端(基于 [Cordova](https://www.construct.net/en/tutorials/publish-mobile-apps-26))、桌面端([WebView2](https://www.construct.net/en/tutorials/exporting-windows-webview2-2685) / [WKWebView](https://www.construct.net/en/tutorials/exporting-macos-wkwebview-2718) / [Linux CEF](https://www.construct.net/en/tutorials/exporting-linux-steam-deck-3155)，或 NW.js )、主机端 [Xbox UWP (WebView2)](https://www.construct.net/en/blogs/ashleys-blog-2/construct-xbox-support-1873)、Playable AD (Facebook 试玩广告)。也可以导出原生工程 (Android Studio、Cordova project、Xcode) 自己本地打包或签名，轻松又方便！

#### 内置的案例宝库

编辑器内置[案例图书馆](https://www.construct.net/a/260259?t=construct3)，目前已经超过400+个游戏案例，几乎每周都会添加新的模板。从基础功能演示到完成度达到上线品质的完整DEMO，官方毫无保留的提供给用户去学习参考，开箱即用。这些案例无论是表现质量还是编码风格，拿出来都是非常能打的那种，每个案例都带有注释讲解。

值得一提的是，许多案例都是在免费版的限制内完成的。即便你没有订阅C3，不想花一分钱，也可以在相同的条件下完成这些小游戏。(注：注册账号并登录后，免费版可使用 50 行事件)

<figure><img src="../.gitbook/assets/ExampleBrower01.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/ExampleBrower02.png" alt=""><figcaption></figcaption></figure>

很多从流行的游戏中复刻的玩法案例

<figure><img src="../.gitbook/assets/ExampleBrower03.png" alt=""><figcaption></figcaption></figure>

有趣的是作为一款 2D 引擎，C3还支持基于深度视差的假3D功能。同样的提供了超级丰富的案例，而且每个玩法不带重样，完成度高的难以置信。都是开箱即用，即便是[免费版也能直接打开编辑](https://www.construct.net/a/260259?t=construct3)。它似乎真的试图想教会你做游戏，哪怕你还没有订阅。

<figure><img src="../.gitbook/assets/ExampleBrower04.png" alt=""><figcaption></figcaption></figure>

对于高级用户，还支持 JavaScript 或 Typescript 语言进行开发，甚至支持完全脱离可视化事件表，纯代码编程。自带案例中，也有非常多仅用 Javascript 进行开发的案例。

<figure><img src="../.gitbook/assets/ExampleBrower05.png" alt=""><figcaption></figcaption></figure>

官方维护非常积极，自从 2017 年发布以来，每周更新版本。真的很难看到有引擎能够保持这么高效且高质量的更新。

有必要强调一下，Construct 系列是从 2007 年发布的，这是一款迭代了 18 年的游戏制作工具！(是的，所以名字是 Construct 3)





