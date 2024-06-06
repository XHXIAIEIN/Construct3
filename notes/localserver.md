安装本地服务器

# 用于测试游戏

```cmd
python -m http.server 8000
```

或
https://servefolder.dev/
https://xhxiaiein.github.io/servefolder.dev/

# 运行本地服务器

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

    def translate_path(self, path):
        path = super().translate_path(path)
        rel_path = os.path.relpath(path, os.path.abspath('.'))
        return os.path.join(self.server.base_path, rel_path)

def start_server(port, folder_path):
    if not os.path.isdir(folder_path):
        folder_path = os.getcwd()

    httpd = HTTPServer(('', port), CORSRequestHandler)
    httpd.base_path = folder_path

    print(f"Starting server, serving {folder_path} at http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == '__main__':
    port = 50000
    folder_path = "D:/Project/Addons"
    start_server(port, folder_path)
```

## 用于测试插件
https://www.construct.net/en/make-games/manuals/addon-sdk

## SDK
https://github.com/Scirra/Construct-Addon-SDK

位置
```
http://localhost:50000/addon.json
```

---

## Effect

**effect.fx**
Sample WebGL 1 shader. this just outputs a red color.
```glsl
varying mediump vec2 vTex;
uniform lowp sampler2D samplerFront;
uniform lowp vec3 setColor;

void main(void)
{
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
```

**effect.webgl2.fx** 
Sample WebGL 2 shader. This just outputs a green color.
```glsl
#version 300 es
in mediump vec2 vTex;
out lowp vec4 outColor;
uniform lowp sampler2D samplerFront;

void main(void)
{
    outColor = vec4(0.0, 1.0, 0.0, 1.0);
}

```

**effect.wgsl**
Sample WebGPU shader. This just outputs a blue color.
```wgsl
%%FRAGMENTINPUT_STRUCT%%
%%FRAGMENTOUTPUT_STRUCT%%

@fragment
fn main(input : FragmentInput) -> FragmentOutput
{
    var output : FragmentOutput;
    output.color = vec4<f32>(0.0f, 0.0f, 1.0f, 1.0f);
    return output;
}
```


