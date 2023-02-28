安装本地服务器


# 用于测试游戏

https://servefolder.dev/



# 用于测试插件

https://www.construct.net/en/make-games/manuals/addon-sdk


```python
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=50000)
```

http://localhost:50000/addon.json
