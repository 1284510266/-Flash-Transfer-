# ⚡ 闪传 (Flash Transfer)

一款极简、高颜值的局域网跨设备文件与剪贴板互传工具。

## 🌟 特性

- **极速互传**：基于 FastAPI，支持任意格式文件的局域网高速传输。
- **剪贴板同步**：一键同步文字到云端，多设备实时共享。
- **现代化 UI**：深色模式、玻璃拟态设计，完美适配移动端。
- **零配置启动**：自动检测局域网 IP，即开即用。

## 🚀 快速开始

### 方式一：一键启动 (推荐 Windows 用户)
直接双击运行项目根目录下的 **`启动.bat`**。它会自动安装依赖并启动服务，随后自动为你打开浏览器。

### 方式二：命令行手动启动
1. **安装依赖**：
   ```bash
   pip install fastapi uvicorn python-multipart
   ```
2. **启动服务**：
   ```bash
   python main.py
   ```

### 3. 访问应用
- **本机访问**：[http://localhost:8000](http://localhost:8000)
- **多设备访问**：打开界面后，顶部会显示动态生成的**局域网访问地址**（例如 `http://192.168.x.x:8000`），在手机或其他设备的浏览器中输入该地址即可。

## 🌐 联机注意事项 (必读)

要确保手机与电脑互通，请检查以下几点：

1. **同 WiFi 环境**：所有设备必须连接到同一个路由器（同一局域网）。
2. **防火墙放行**：Windows 防火墙可能会拦截外部访问。如果手机打不开，请在 PowerShell (管理员) 运行以下命令：
   ```powershell
   New-NetFirewallRule -DisplayName "FastAPI Transfer" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
   ```
3. **网络属性**：确保电脑的 WiFi 设置为**“专用 (Private)”**模式而非“公用”。

## 🛠 技术栈

- **后端**: Python, FastAPI, Uvicorn
- **前端**: HTML5, Vanilla CSS (Glassmorphism), JavaScript (Fetch ES6)
- **图标**: Lucide Icons
