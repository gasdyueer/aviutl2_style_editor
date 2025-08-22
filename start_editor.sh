#!/bin/bash

# AviUtl2 样式配置编辑器启动脚本
# AviUtl2 Style Configuration Editor Startup Script

set -e

# 设置编码
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

# 脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/aviutl2_style_editor.py"

# 检查Python脚本是否存在
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "错误：未找到脚本文件 $SCRIPT_PATH"
    echo "Error: Script file not found: $SCRIPT_PATH"
    exit 1
fi

# 检查Python环境
check_python_env() {
    # 首先检查是否激活了虚拟环境
    if [ -n "$VIRTUAL_ENV" ]; then
        PYTHON_CMD="python"
        echo "使用已激活的虚拟环境 / Using activated virtual environment"
        return 0
    fi

    # 检查本地虚拟环境
    if [ -f "$SCRIPT_DIR/.venv/bin/python" ]; then
        PYTHON_CMD="$SCRIPT_DIR/.venv/bin/python"
        echo "使用本地虚拟环境 / Using local virtual environment"
        return 0
    fi

    # 检查用户指定的Python路径
    if [ -n "$PYTHON_PATH" ] && [ -f "$PYTHON_PATH" ]; then
        PYTHON_CMD="$PYTHON_PATH"
        echo "使用指定的Python路径 / Using specified Python path: $PYTHON_CMD"
        return 0
    fi

    # 查找系统Python
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        echo "使用系统Python3 / Using system Python3"
        return 0
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        echo "使用系统Python / Using system Python"
        return 0
    else
        echo "错误：未找到可用的Python环境"
        echo "Error: No available Python environment found"
        echo "请确保已安装Python或激活虚拟环境"
        echo "Please ensure Python is installed or activate virtual environment"
        exit 1
    fi
}

# 选择语言
select_language() {
    echo "========================================"
    echo "   AviUtl2 样式配置编辑器"
    echo "   AviUtl2 Style Configuration Editor"
    echo "========================================"
    echo ""
    echo "选择界面语言 / Choose Language:"
    echo "[1] 中文 (Chinese)"
    echo "[2] 英文 (English)"
    echo "[3] 日文 (Japanese)"
    echo ""

    while true; do
        read -p "请输入选择 (1-3) / Enter choice (1-3): " lang_choice
        case $lang_choice in
            1)
                LANG_CODE="zh"
                LANG_NAME="中文"
                break
                ;;
            2)
                LANG_CODE="en"
                LANG_NAME="English"
                break
                ;;
            3)
                LANG_CODE="ja"
                LANG_NAME="日本語"
                break
                ;;
            *)
                echo "无效选择，请重新输入 / Invalid choice, please try again"
                ;;
        esac
    done

    echo ""
    echo "启动语言：$LANG_NAME / Starting language: $LANG_NAME"
}

# 主函数
main() {
    check_python_env
    select_language

    echo "正在启动编辑器... / Starting editor..."
    echo ""

    # 启动编辑器
    cd "$SCRIPT_DIR"
    "$PYTHON_CMD" "$SCRIPT_PATH" --lang "$LANG_CODE"

    # 检查退出状态
    exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo ""
        echo "启动失败 / Start failed"
        echo "请检查错误信息 / Please check error messages"
        exit $exit_code
    fi
}

# 运行主函数
main "$@"