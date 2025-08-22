@echo off
chcp 65001 > nul
title AviUtl2 样式配置编辑器 - 中文

REM 快速启动中文版本
if exist "%~dp0.venv\Scripts\python.exe" (
    "%~dp0.venv\Scripts\python.exe" "%~dp0aviutl2_style_editor.py" --lang zh
) else (
    echo 错误：未找到虚拟环境
    pause
)