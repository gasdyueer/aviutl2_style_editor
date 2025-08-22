@echo off
chcp 65001 > nul
title AviUtl2 Style Configuration Editor - English

REM 快速启动英文版本
if exist "%~dp0.venv\Scripts\python.exe" (
    "%~dp0.venv\Scripts\python.exe" "%~dp0aviutl2_style_editor.py" --lang en
) else (
    echo Error: Virtual environment not found
    pause
)