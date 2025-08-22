#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AviUtl2 样式配置编辑器
使用Gradio构建的Web界面，用于直观地编辑style.conf文件
支持多语言界面：中文、英文、日文
"""

import gradio as gr
import configparser
import os
import json
import argparse
from pathlib import Path
import re

class AviUtlStyleEditor:
    def __init__(self, language='zh'):
        self.config = configparser.ConfigParser()
        # 保持键的大小写
        self.current_file = None
        self.language = language
        self.load_language_pack()

    def load_language_pack(self):
        """加载语言包"""
        try:
            language_file = f"locales/{self.language}.json"
            with open(language_file, 'r', encoding='utf-8') as f:
                self.lang = json.load(f)
        except FileNotFoundError:
            print(f"语言文件 {language_file} 未找到，使用默认中文")
            self.language = 'zh'
            self.load_language_pack()
        except Exception as e:
            print(f"加载语言文件失败: {e}")
            # 使用内置的默认语言包
            self.lang = self.get_default_language_pack()

    def get_default_language_pack(self):
        """获取默认中文语言包"""
        return {
            "app": {
                "title": "AviUtl2 样式配置编辑器",
                "description": "用于直观编辑AviUtl2的style.conf配置文件"
            },
            "file": {
                "load_success": "文件加载成功",
                "load_failed": "文件加载失败: {error}",
                "save_success": "文件已保存: {filename}",
                "save_failed": "保存失败: {error}",
                "select_file": "请选择一个文件",
                "no_file_selected": "请选择style.conf文件"
            }
        }

    def _(self, key_path, **kwargs):
        """获取翻译文本的辅助方法"""
        keys = key_path.split('.')
        value = self.lang
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return key_path  # 返回键路径作为回退

        # 格式化字符串
        if isinstance(value, str) and kwargs:
            try:
                return value.format(**kwargs)
            except:
                return value
        return value

    def parse_style_file(self, file_path):
        """解析style.conf文件"""
        try:
            self.current_file = file_path
            # 使用UTF-8编码读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 解析INI格式
            self.config.read_string(content)
            return True, self._("file.load_success")
        except Exception as e:
            return False, self._("file.load_failed", error=str(e))

    def generate_config_content(self):
        """生成配置文件内容"""
        header = self._("config.header_comment")
        output = f"{header}\n"

        for section in self.config.sections():
            output += f"[{section}]\n"

            # 添加注释和配置项
            for key, value in self.config[section].items():
                # 为每个配置项添加适当的注释
                comment = self.get_comment_for_key(section, key)
                if comment:
                    output += f"; {comment}\n"
                output += f"{key}={value}\n"
            output += "\n"

        return output

    def get_comment_for_key(self, section, key):
        """为配置项生成注释"""
        try:
            # 从语言包中获取注释
            section_key = section.lower()
            key_key = key
            comment_key = f"{section_key}.{key_key}.comment"

            # 构建语言包路径
            lang_section = self.lang.get(section, {})
            if key in lang_section:
                key_data = lang_section[key]
                if isinstance(key_data, dict) and 'comment' in key_data:
                    return key_data['comment']

            # 如果语言包中没有找到，使用默认英文注释
            return f"{key} parameter"

        except:
            return f"{key} parameter"

    def validate_color(self, color):
        """验证颜色值格式"""
        if not color:
            return True
        # 支持6位或8位十六进制颜色值，多个颜色用逗号分隔
        pattern = r'^[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?(?:,[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?)*$'
        return bool(re.match(pattern, color.replace(',', '')))

    def validate_number(self, value):
        """验证数值"""
        try:
            int(value)
            return True
        except:
            return False

    def generate_section_text(self, section_name):
        """生成单个section的文本"""
        if section_name not in self.config:
            return ""

        text = f"[{section_name}]\n"
        for key, value in self.config[section_name].items():
            comment = self.get_comment_for_key(section_name, key)
            if comment:
                text += f"; {comment}\n"
            text += f"{key}={value}\n"
        return text

    def parse_text_to_config(self, section_name, text):
        """从文本解析配置到config对象"""
        if section_name not in self.config:
            self.config.add_section(section_name)

        lines = text.strip().split('\n')
        current_key = None

        for line in lines:
            line = line.strip()
            if not line or line.startswith(';') or line.startswith('['):
                continue

            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                self.config[section_name][key] = value

    def get_parameter_info(self, section, key):
        """获取参数的详细信息"""
        try:
            # 从语言包中获取参数信息
            lang_section = self.lang.get(section, {})
            if key in lang_section:
                key_data = lang_section[key]
                if isinstance(key_data, dict):
                    # 构建参数信息
                    param_info = {
                        'label': key_data.get('label', key),
                        'description': key_data.get('description', f'{key} parameter')
                    }

                    # 根据类型添加特定参数
                    if section == 'Font':
                        if key == 'DefaultFamily':
                            param_info.update({'type': 'text', 'default': 'Yu Gothic UI'})
                        elif key in ['Control', 'PreviewTime', 'LayerObject', 'TimeGauge', 'Footer']:
                            param_info.update({'type': 'slider', 'min': 8, 'max': 24, 'default': 13})
                        else:  # EditControl, TextEdit, Log
                            param_info.update({'type': 'text', 'default': '13,Consolas'})
                    elif section == 'Color':
                        param_info.update({'type': 'color', 'default': '#202020'})
                    elif section == 'Layout':
                        param_info.update({'type': 'slider', 'min': 1, 'max': 100, 'default': 20})
                    elif section == 'Format':
                        param_info.update({'type': 'text', 'default': ''})

                    return param_info

            # 默认参数信息
            return {'type': 'text', 'label': key, 'default': '', 'description': f'{key} parameter'}

        except:
            return {'type': 'text', 'label': key, 'default': '', 'description': f'{key} parameter'}

    def create_gradio_interface(self):
        """创建Gradio界面"""

        def load_file(file):
            if file is None:
                return self._("file.select_file"), "", 13, "13,Consolas", 16, 16, 13, 14, "16,Consolas", "12,Consolas", "#202020", "#ffffff", "#585858", "#606060", "#e0e0e0", "#304080", "", 7, 20, 24, 32, 32, 42, "{CurrentTime} / {TotalTime}  |  {CurrentFrame} / {TotalFrame}", "{SceneName}  |  {Resolution}  |  {FrameRate}  |  {SamplingRate}"

            success, message = self.parse_style_file(file.name)
            if not success:
                return message, "", 13, "13,Consolas", 16, 16, 13, 14, "16,Consolas", "12,Consolas", "#202020", "#ffffff", "#585858", "#606060", "#e0e0e0", "#304080", "", 7, 20, 24, 32, 32, 42, "{CurrentTime} / {TotalTime}  |  {CurrentFrame} / {TotalFrame}", "{SceneName}  |  {Resolution}  |  {FrameRate}  |  {SamplingRate}"

            # 直接返回每个控件的值，确保类型正确
            try:
                font_default_family = self.config['Font'].get('DefaultFamily', 'Yu Gothic UI')
                font_control = int(self.config['Font'].get('Control', '13'))
                font_edit_control = self.config['Font'].get('EditControl', '13,Consolas')
                font_preview_time = int(self.config['Font'].get('PreviewTime', '16'))
                font_layer_object = int(self.config['Font'].get('LayerObject', '16'))
                font_time_gauge = int(self.config['Font'].get('TimeGauge', '13'))
                font_footer = int(self.config['Font'].get('Footer', '14'))
                font_text_edit = self.config['Font'].get('TextEdit', '16,Consolas')
                font_log = self.config['Font'].get('Log', '12,Consolas')

                color_background = f"#{self.config['Color'].get('Background', '202020')}"
                color_text = f"#{self.config['Color'].get('Text', 'ffffff')}"
                color_window_border = f"#{self.config['Color'].get('WindowBorder', '585858')}"
                color_button_body = f"#{self.config['Color'].get('ButtonBody', '606060')}"
                color_border_select = f"#{self.config['Color'].get('BorderSelect', 'e0e0e0')}"
                color_footer = f"#{self.config['Color'].get('Footer', '304080')}"
                color_layer = f"#{self.config['Color'].get('Layer', '404040')}"
                color_object_video = f"#{self.config['Color'].get('ObjectVideo', '3040e0')}"
                color_object_audio = f"#{self.config['Color'].get('ObjectAudio', 'd04030')}"
                color_footer_progress = self.config['Color'].get('FooterProgress', '903838,b84848')
                color_other = ""  # 其他颜色参数

                layout_window_separator_size = int(self.config['Layout'].get('WindowSeparatorSize', '7'))
                layout_scroll_bar_size = int(self.config['Layout'].get('ScrollBarSize', '20'))
                layout_footer_height = int(self.config['Layout'].get('FooterHeight', '24'))
                layout_layer_height = int(self.config['Layout'].get('LayerHeight', '32'))
                layout_time_gauge_height = int(self.config['Layout'].get('TimeGaugeHeight', '32'))
                layout_player_control_height = int(self.config['Layout'].get('PlayerControlHeight', '42'))

                format_footer_left = self.config['Format'].get('FooterLeft', '{CurrentTime} / {TotalTime}  |  {CurrentFrame} / {TotalFrame}')
                format_footer_right = self.config['Format'].get('FooterRight', '{SceneName}  |  {Resolution}  |  {FrameRate}  |  {SamplingRate}')

                return (message, font_default_family, font_control, font_edit_control, font_preview_time,
                       font_layer_object, font_time_gauge, font_footer, font_text_edit, font_log,
                       color_background, color_text, color_window_border, color_button_body,
                       color_border_select, color_footer, color_layer, color_object_video,
                       color_object_audio, color_footer_progress, color_other, layout_window_separator_size,
                       layout_scroll_bar_size, layout_footer_height, layout_layer_height,
                       layout_time_gauge_height, layout_player_control_height,
                       format_footer_left, format_footer_right)

            except Exception as e:
                return message, "Yu Gothic UI", 13, "13,Consolas", 16, 16, 13, 14, "16,Consolas", "12,Consolas", "#202020", "#ffffff", "#585858", "#606060", "#e0e0e0", "#304080", "#404040", "#3040e0", "#d04030", "903838,b84848", "", 7, 20, 24, 32, 32, 42, "{CurrentTime} / {TotalTime}  |  {CurrentFrame} / {TotalFrame}", "{SceneName}  |  {Resolution}  |  {FrameRate}  |  {SamplingRate}"

        def save_config(filename, *args):
            """保存配置文件"""
            if not filename.strip():
                filename = "style_new.conf"

            try:
                # 参数映射
                param_values = args
                expected_params = [
                    'Font_DefaultFamily', 'Font_Control', 'Font_EditControl', 'Font_PreviewTime',
                    'Font_LayerObject', 'Font_TimeGauge', 'Font_Footer', 'Font_TextEdit', 'Font_Log',
                    'Color_Background', 'Color_Text', 'Color_WindowBorder', 'Color_ButtonBody',
                    'Color_BorderSelect', 'Color_Footer', 'Color_Layer', 'Color_ObjectVideo',
                    'Color_ObjectAudio', 'Color_FooterProgress', 'Color_Other', 'Layout_WindowSeparatorSize',
                    'Layout_ScrollBarSize', 'Layout_FooterHeight', 'Layout_LayerHeight',
                    'Layout_TimeGaugeHeight', 'Layout_PlayerControlHeight', 'Format_FooterLeft', 'Format_FooterRight'
                ]

                # 更新配置
                for i, param_key in enumerate(expected_params):
                    if i < len(param_values) and param_values[i] is not None:
                        section, key = param_key.split('_', 1)
                        if section not in self.config:
                            self.config.add_section(section)
                        self.config[section][key] = str(param_values[i])

                # 生成内容
                content = self.generate_config_content()

                # 保存文件
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)

                return self._("file.save_success", filename=filename)
            except Exception as e:
                return self._("file.save_failed", error=str(e))

        # 创建界面
        with gr.Blocks(title=self._("app.title")) as interface:
            gr.Markdown(f"# 🎨 {self._('app.title')}")
            gr.Markdown(self._("app.description"))

            with gr.Row():
                with gr.Column(scale=1):
                    file_input = gr.File(label=self._("ui.labels.file_input"), file_types=['.conf', '.txt'])
                    load_btn = gr.Button(self._("ui.buttons.load_file"), variant="primary")
                    status_text = gr.Textbox(label=self._("ui.labels.status"), interactive=False)

                with gr.Column(scale=1):
                    save_filename = gr.Textbox(
                        label=self._("ui.labels.save_filename"),
                        value=self._("defaults.save_filename"),
                        placeholder=self._("ui.placeholders.save_filename")
                    )
                    save_btn = gr.Button(self._("ui.buttons.save_config"), variant="secondary")
                    save_status = gr.Textbox(label=self._("ui.labels.save_status"), interactive=False)

            # 创建参数控件字典
            param_controls = {}

            with gr.Tabs():
                with gr.TabItem(self._("ui.tabs.font")):
                    gr.Markdown(self._("ui.tabs.font_description"))
                    with gr.Row():
                        with gr.Column():
                            gr.Markdown("**主要字体设置**")
                            # 主要字体设置使用专用控件
                            param_controls['Font_DefaultFamily'] = gr.Textbox(
                                label="默认字体", value="Yu Gothic UI",
                                info="界面默认使用的字体名称"
                            )
                            param_controls['Font_Control'] = gr.Slider(
                                label="控件字体大小", minimum=8, maximum=20, value=13, step=1,
                                info="控件显示的字体大小"
                            )
                            param_controls['Font_PreviewTime'] = gr.Slider(
                                label="预览时间字体大小", minimum=8, maximum=24, value=16, step=1,
                                info="预览窗口时间显示的字体大小"
                            )
                        with gr.Column():
                            gr.Markdown("**编辑器字体设置**")
                            param_controls['Font_EditControl'] = gr.Textbox(
                                label="编辑框字体", value="13,Consolas",
                                info="编辑框的字体大小和字体名"
                            )
                            param_controls['Font_LayerObject'] = gr.Slider(
                                label="图层对象字体大小", minimum=8, maximum=24, value=16, step=1,
                                info="图层和对象编辑区域的字体大小"
                            )
                            param_controls['Font_TimeGauge'] = gr.Slider(
                                label="时间刻度字体大小", minimum=8, maximum=20, value=13, step=1,
                                info="时间轴刻度显示的字体大小"
                            )
                            param_controls['Font_Footer'] = gr.Slider(
                                label="底部栏字体大小", minimum=8, maximum=20, value=14, step=1,
                                info="底部信息栏的字体大小"
                            )
                            param_controls['Font_TextEdit'] = gr.Textbox(
                                label="文本编辑字体", value="16,Consolas",
                                info="文本编辑器的字体大小和字体名"
                            )
                            param_controls['Font_Log'] = gr.Textbox(
                                label="日志字体", value="12,Consolas",
                                info="日志窗口的字体大小和字体名"
                            )

                with gr.TabItem(self._("ui.tabs.color")):
                    gr.Markdown(self._("ui.tabs.color_description"))

                    # 主要颜色设置 - 选择最重要的参数作为颜色选择器
                    main_color_params = [
                        ('Background', '背景色', '#202020'),
                        ('Text', '文本色', '#ffffff'),
                        ('WindowBorder', '窗口边框色', '#585858'),
                        ('ButtonBody', '按钮背景色', '#606060'),
                        ('BorderSelect', '选中边框色', '#e0e0e0'),
                        ('Footer', '底部栏背景色', '#304080'),
                        ('Layer', '图层背景色', '#404040'),
                        ('ObjectVideo', '视频对象色', '#3040e0'),
                        ('ObjectAudio', '音频对象色', '#d04030')
                    ]

                    gr.Markdown("**主要颜色参数**（使用颜色选择器）")
                    for i in range(0, len(main_color_params), 3):
                        with gr.Row():
                            for j in range(3):
                                if i + j < len(main_color_params):
                                    param_key, label, default = main_color_params[i + j]
                                    param_controls[f'Color_{param_key}'] = gr.ColorPicker(
                                        label=label, value=default,
                                        info=f"{label}的颜色设置"
                                    )

                    # 其他颜色设置使用文本编辑
                    gr.Markdown("**其他颜色参数**（包含复杂参数和剩余参数）")
                    param_controls['Color_FooterProgress'] = gr.Textbox(
                        label="进度条颜色", value="903838,b84848",
                        info="底部栏进度条的颜色设置（格式：颜色1,颜色2）"
                    )
                    param_controls['Color_Other'] = gr.Textbox(
                        label="其他颜色参数", lines=8,
                        placeholder="在此添加其他颜色参数，每行一个，如：Border=909090"
                    )

                with gr.TabItem(self._("ui.tabs.layout")):
                    gr.Markdown(self._("ui.tabs.layout_description"))

                    # 主要布局设置
                    with gr.Row():
                        with gr.Column():
                            param_controls['Layout_WindowSeparatorSize'] = gr.Slider(
                                label="窗口分隔条宽度", minimum=1, maximum=20, value=7, step=1,
                                info="窗口间分隔条的宽度"
                            )
                            param_controls['Layout_ScrollBarSize'] = gr.Slider(
                                label="滚动条宽度", minimum=10, maximum=30, value=20, step=1,
                                info="滚动条的宽度"
                            )
                            param_controls['Layout_FooterHeight'] = gr.Slider(
                                label="底部栏高度", minimum=15, maximum=50, value=24, step=1,
                                info="底部信息栏的高度"
                            )
                        with gr.Column():
                            param_controls['Layout_LayerHeight'] = gr.Slider(
                                label="图层高度", minimum=20, maximum=60, value=32, step=1,
                                info="图层条目的高度"
                            )
                            param_controls['Layout_TimeGaugeHeight'] = gr.Slider(
                                label="时间轴高度", minimum=20, maximum=60, value=32, step=1,
                                info="时间轴区域的高度"
                            )
                            param_controls['Layout_PlayerControlHeight'] = gr.Slider(
                                label="播放控制栏高度", minimum=30, maximum=60, value=42, step=1,
                                info="播放控制栏的高度"
                            )

                with gr.TabItem(self._("ui.tabs.format")):
                    gr.Markdown(self._("ui.tabs.format_description"))
                    param_controls['Format_FooterLeft'] = gr.Textbox(
                        label="底部栏左侧格式",
                        value="{CurrentTime} / {TotalTime}  |  {CurrentFrame} / {TotalFrame}",
                        lines=2,
                        info="底部栏左侧显示的格式"
                    )
                    param_controls['Format_FooterRight'] = gr.Textbox(
                        label="底部栏右侧格式",
                        value="{SceneName}  |  {Resolution}  |  {FrameRate}  |  {SamplingRate}",
                        lines=2,
                        info="底部栏右侧显示的格式"
                    )

                with gr.TabItem("📄 完整配置预览"):
                    preview_text = gr.Textbox(label="完整配置文件内容", lines=25, interactive=False)

            # 事件绑定
            load_btn.click(
                fn=load_file,
                inputs=[file_input],
                outputs=[status_text] + [param_controls[key] for key in [
                    'Font_DefaultFamily', 'Font_Control', 'Font_EditControl', 'Font_PreviewTime',
                    'Font_LayerObject', 'Font_TimeGauge', 'Font_Footer', 'Font_TextEdit', 'Font_Log',
                    'Color_Background', 'Color_Text', 'Color_WindowBorder', 'Color_ButtonBody',
                    'Color_BorderSelect', 'Color_Footer', 'Color_Layer', 'Color_ObjectVideo',
                    'Color_ObjectAudio', 'Color_FooterProgress', 'Color_Other', 'Layout_WindowSeparatorSize',
                    'Layout_ScrollBarSize', 'Layout_FooterHeight', 'Layout_LayerHeight',
                    'Layout_TimeGaugeHeight', 'Layout_PlayerControlHeight', 'Format_FooterLeft', 'Format_FooterRight'
                ]]
            )

            save_btn.click(
                fn=save_config,
                inputs=[save_filename] + [param_controls[key] for key in [
                    'Font_DefaultFamily', 'Font_Control', 'Font_EditControl', 'Font_PreviewTime',
                    'Font_TextEdit', 'Font_Log', 'Color_Background', 'Color_Text', 'Color_WindowBorder',
                    'Color_ButtonBody', 'Color_BorderSelect', 'Color_Footer', 'Color_Other', 'Layout_WindowSeparatorSize',
                    'Layout_ScrollBarSize', 'Layout_FooterHeight', 'Layout_LayerHeight', 'Layout_TimeGaugeHeight',
                    'Layout_PlayerControlHeight', 'Format_FooterLeft', 'Format_FooterRight'
                ]],
                outputs=[save_status]
            )

            # 实时预览 - 为每个控件添加change事件
            preview_inputs = [param_controls[key] for key in [
                'Font_DefaultFamily', 'Font_Control', 'Font_EditControl', 'Font_PreviewTime',
                'Font_TextEdit', 'Font_Log', 'Color_Background', 'Color_Text', 'Color_WindowBorder',
                'Color_ButtonBody', 'Color_BorderSelect', 'Color_Footer', 'Color_Other', 'Layout_WindowSeparatorSize',
                'Layout_ScrollBarSize', 'Layout_FooterHeight', 'Layout_LayerHeight', 'Layout_TimeGaugeHeight',
                'Layout_PlayerControlHeight', 'Format_FooterLeft', 'Format_FooterRight'
            ]]

            for control in preview_inputs:
                control.change(
                    fn=lambda *args: self.generate_config_content() if self.config.sections() else "",
                    inputs=preview_inputs,
                    outputs=[preview_text]
                )

        return interface

    def create_section_controls(self, section_name, param_controls):
        """为指定section创建控件"""

        # 为每个参数创建合适的控件
        for key in ['DefaultFamily', 'Control', 'EditControl', 'PreviewTime', 'LayerObject', 'TimeGauge', 'Footer', 'TextEdit', 'Log'] if section_name == 'Font' else \
                   ['Background', 'WindowBorder', 'WindowSeparator', 'Footer', 'FooterProgress', 'TitleHeader', 'BorderSelect', 'Border', 'BorderFocus', 'Text', 'TextDisable', 'TextSelect', 'ButtonBody', 'ButtonBodyHover', 'ButtonBodyPress', 'ButtonBodyDisable', 'ButtonBodySelect'] if section_name == 'Color' else \
                   ['WindowSeparatorSize', 'ScrollBarSize', 'FooterHeight', 'TitleHeaderHeight', 'TimeGaugeHeight', 'LayerHeight', 'LayerHeaderWidth', 'SettingItemHeaderWidth', 'SettingItemHeight', 'SettingItemMarginWidth', 'SettingHeaderHeight', 'PlayerControlHeight', 'ExplorerHeaderHeight', 'ExplorerWindowNum', 'ListItemHeight'] if section_name == 'Layout' else \
                   ['FooterLeft', 'FooterRight'] if section_name == 'Format' else []:

            param_info = self.get_parameter_info(section_name, key)
            param_key = f"{section_name}_{key}"

            with gr.Row():
                with gr.Column(scale=2):
                    if param_info['type'] == 'slider':
                        control = gr.Slider(
                            label=param_info['label'],
                            minimum=param_info['min'],
                            maximum=param_info['max'],
                            value=param_info['default'],
                            step=1,
                            info=param_info['description']
                        )
                    elif param_info['type'] == 'color':
                        control = gr.ColorPicker(
                            label=param_info['label'],
                            value=param_info['default'],
                            info=param_info['description']
                        )
                    else:
                        control = gr.Textbox(
                            label=param_info['label'],
                            value=param_info['default'],
                            placeholder=param_info['description']
                        )

                with gr.Column(scale=1):
                    gr.Markdown(f"**说明**: {param_info['description']}")

            param_controls[param_key] = control

def main():
    parser = argparse.ArgumentParser(description="AviUtl2 样式配置编辑器")
    parser.add_argument('--lang', '-l', default='zh', choices=['zh', 'en', 'ja'],
                       help='选择界面语言 (zh: 中文, en: 英文, ja: 日文)')
    args = parser.parse_args()

    editor = AviUtlStyleEditor(language=args.lang)
    interface = editor.create_gradio_interface()
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        inbrowser=True
    )

if __name__ == "__main__":
    main()