@echo off
chcp 65001 > nul
title AviUtl2 样式配置编辑器 - 自动安装和启动器

echo ========================================
echo    AviUtl2 样式配置编辑器
echo    AviUtl2 Style Configuration Editor
echo ========================================
echo.

REM 设置项目目录
set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%.venv
set SCRIPT_PATH=%PROJECT_DIR%aviutl2_style_editor.py
set REQUIREMENTS_PATH=%PROJECT_DIR%requirements.txt

REM 颜色设置
color 0F

echo [1/8] 检查系统环境...
echo [1/8] Checking system environment...

REM 检查Python是否已安装
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ 错误：未找到Python / Error: Python not found
    echo.
    echo 请安装Python 3.7或更高版本：
    echo Please install Python 3.7 or higher:
    echo.
    echo 访问 https://www.python.org/downloads/
    echo Visit https://www.python.org/downloads/
    echo.
    echo 安装时请勾选"Add Python to PATH"选项
    echo Please check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python已安装 / Python is installed

REM 检查pip是否可用
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ 错误：pip不可用 / Error: pip is not available
    echo 请确保Python已正确安装 / Please ensure Python is properly installed
    pause
    exit /b 1
)

echo ✅ pip可用 / pip is available

echo.

echo [2/8] 检查项目文件...
echo [2/8] Checking project files...

REM 检查主脚本文件
if not exist "%SCRIPT_PATH%" (
    echo ❌ 错误：未找到主程序文件 / Error: Main script file not found
    echo 路径：%SCRIPT_PATH%
    echo Path: %SCRIPT_PATH%
    pause
    exit /b 1
)
echo ✅ 主程序文件存在 / Main script file exists

REM 检查依赖文件
if not exist "%REQUIREMENTS_PATH%" (
    echo ❌ 错误：未找到依赖文件 / Error: Requirements file not found
    echo 路径：%REQUIREMENTS_PATH%
    echo Path: %REQUIREMENTS_PATH%
    pause
    exit /b 1
)
echo ✅ 依赖文件存在 / Requirements file exists

REM 检查语言文件
if not exist "%PROJECT_DIR%locales" (
    echo ❌ 错误：未找到语言文件目录 / Error: Language files directory not found
    echo 这可能导致程序无法正常启动 / This may cause the program to fail to start
    pause
    exit /b 1
)
echo ✅ 语言文件存在 / Language files exist

echo.

echo [3/8] 检查虚拟环境...
echo [3/8] Checking virtual environment...

REM 检查虚拟环境是否存在
if not exist "%VENV_DIR%" (
    echo ⚠️  未找到虚拟环境，正在创建... / Virtual environment not found, creating...
    echo.

    python -m venv "%VENV_DIR%"
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ 错误：创建虚拟环境失败 / Error: Failed to create virtual environment
        echo 请检查Python安装或权限设置 / Please check Python installation or permissions
        pause
        exit /b 1
    )
    echo ✅ 虚拟环境创建成功 / Virtual environment created successfully
) else (
    echo ✅ 虚拟环境已存在 / Virtual environment exists
)

REM 激活虚拟环境
echo 正在激活虚拟环境... / Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"
if %ERRORLEVEL% NEQ 0 (
    echo ❌ 错误：激活虚拟环境失败 / Error: Failed to activate virtual environment
    pause
    exit /b 1
)

echo ✅ 虚拟环境已激活 / Virtual environment activated

echo.

echo [4/8] 升级pip...
echo [4/8] Upgrading pip...

python -m pip install --upgrade pip >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️  警告：pip升级失败，继续使用旧版本 / Warning: pip upgrade failed, continuing with old version
) else (
    echo ✅ pip升级成功 / pip upgraded successfully
)

echo.

echo [5/8] 检查和安装依赖...
echo [5/8] Checking and installing dependencies...

REM 检查gradio是否已安装
python -c "import gradio" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 📦 正在安装依赖包... / Installing dependencies...
    echo 这可能需要几分钟时间，请耐心等待...
    echo This may take a few minutes, please be patient...

    pip install -r "%REQUIREMENTS_PATH%"
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ 错误：依赖安装失败 / Error: Dependency installation failed
        echo 请检查网络连接或Python环境 / Please check network connection or Python environment
        echo 或者尝试手动安装：pip install gradio
        echo Or try manual installation: pip install gradio
        pause
        exit /b 1
    )
    echo ✅ 依赖安装成功 / Dependencies installed successfully
) else (
    echo ✅ 依赖已安装 / Dependencies already installed
)

echo.

echo [6/8] 验证安装...
echo [6/8] Verifying installation...

REM 测试导入
python -c "import gradio; import configparser; print('✅ 所有依赖验证通过 / All dependencies verified')" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ 错误：依赖验证失败 / Error: Dependency verification failed
    echo 请尝试重新运行此脚本 / Please try running this script again
    pause
    exit /b 1
)

echo.

echo [7/8] 启动程序准备...
echo [7/8] Preparing to start program...

REM 检查是否有语言参数
if "%1"=="" (
    goto language_select
) else (
    set LANG_CODE=%1
    goto skip_language_select
)

:language_select
echo.
echo 选择界面语言 / Choose Language:
echo [1] 中文 (Chinese) - 推荐 / Recommended
echo [2] 英文 (English)
echo [3] 日文 (Japanese)
echo.

set /p lang_choice="请输入选择 (1-3) 或按回车使用默认语言 / Enter choice (1-3) or press Enter for default language: "

if "%lang_choice%"=="" (
    set LANG_CODE=zh
    set LANG_NAME=中文 (默认)
) else if "%lang_choice%"=="1" (
    set LANG_CODE=zh
    set LANG_NAME=中文
) else if "%lang_choice%"=="2" (
    set LANG_CODE=en
    set LANG_NAME=English
) else if "%lang_choice%"=="3" (
    set LANG_CODE=ja
    set LANG_NAME=日本語
) else (
    echo ⚠️  无效选择，使用默认语言 / Invalid choice, using default language
    set LANG_CODE=zh
    set LANG_NAME=中文 (默认)
)

:skip_language_select

echo.
echo [8/8] 启动编辑器...
echo [8/8] Starting editor...

echo ========================================
echo 启动信息 / Start Information:
echo 语言 / Language: %LANG_NAME%
echo 虚拟环境 / Virtual Environment: 已激活 / Activated
echo 依赖状态 / Dependencies: 已安装 / Installed
echo ========================================
echo.

REM 启动编辑器
python "%SCRIPT_PATH%" --lang %LANG_CODE%

REM 检查启动结果
set EXIT_CODE=%ERRORLEVEL%
if %EXIT_CODE% EQU 0 (
    echo.
    echo ✅ 编辑器已成功关闭 / Editor closed successfully
) else (
    echo.
    echo ❌ 编辑器异常退出 / Editor exited with error
    echo 退出代码 / Exit code: %EXIT_CODE%
    echo.
    echo 故障排除建议 / Troubleshooting:
    echo 1. 确保没有其他程序占用端口
    echo    Make sure no other program is using the port
    echo 2. 检查防火墙设置
    echo    Check firewall settings
    echo 3. 尝试重新运行此脚本
    echo    Try running this script again
)

echo.
echo 按任意键退出... / Press any key to exit...
pause >nul

REM 退出虚拟环境
call "%VENV_DIR%\Scripts\deactivate.bat" >nul 2>&1

exit /b %EXIT_CODE%