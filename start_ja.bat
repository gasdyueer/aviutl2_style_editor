@echo off
chcp 65001 > nul
title AviUtl2 スタイル設定エディター - 日本語

REM 快速启动日文版本
if exist "%~dp0.venv\Scripts\python.exe" (
    "%~dp0.venv\Scripts\python.exe" "%~dp0aviutl2_style_editor.py" --lang ja
) else (
    echo エラー：仮想環境が見つかりません
    pause
)