@echo off
title 闪传 - 跨设备文件互传
setlocal

:: Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python，请先安装 Python 并添加到环境变量。
    pause
    exit /b
)

echo [1/2] 正在检查依赖环境...
pip install fastapi uvicorn python-multipart --quiet

echo [2/2] 正在启动服务...
echo.
echo ==========================================
echo 启动成功！请保持此窗口开启。
echo 服务运行期间，手机访问界面显示的 IP 地址即可。
echo ==========================================
echo.

python main.py

pause
