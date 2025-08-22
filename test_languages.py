#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试多语言功能
Test multilingual functionality
"""

import json
import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aviutl2_style_editor import AviUtlStyleEditor

def test_language_pack(language):
    """测试指定语言包"""
    print(f"\n=== 测试语言: {language} ===")

    try:
        editor = AviUtlStyleEditor(language=language)

        # 测试基本翻译
        print(f"应用标题: {editor._('app.title')}")
        print(f"应用描述: {editor._('app.description')}")
        print(f"文件加载成功: {editor._('file.load_success')}")
        print(f"文件加载失败: {editor._('file.load_failed', error='测试错误')}")
        print(f"文件保存成功: {editor._('file.save_success', filename='test.conf')}")
        print(f"文件保存失败: {editor._('file.save_failed', error='测试错误')}")

        # 测试UI标签
        print(f"文件输入标签: {editor._('ui.labels.file_input')}")
        print(f"保存文件名标签: {editor._('ui.labels.save_filename')}")
        print(f"状态标签: {editor._('ui.labels.status')}")
        print(f"保存状态标签: {editor._('ui.labels.save_status')}")

        # 测试按钮文本
        print(f"加载文件按钮: {editor._('ui.buttons.load_file')}")
        print(f"保存配置按钮: {editor._('ui.buttons.save_config')}")

        # 测试字体参数（如果有的话）
        try:
            font_info = editor.get_parameter_info('Font', 'DefaultFamily')
            if font_info:
                print(f"默认字体参数信息: {font_info}")
        except:
            pass

        print(f"✅ 语言 {language} 测试成功")

    except Exception as e:
        print(f"❌ 语言 {language} 测试失败: {e}")
        return False

    return True

def test_language_files():
    """测试语言文件完整性"""
    print("=== 检查语言文件 ===")

    languages = ['zh', 'en', 'ja']
    results = {}

    for lang in languages:
        file_path = f"locales/{lang}.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # 检查必需的键
                required_keys = ['app.title', 'app.description', 'file.load_success']
                missing_keys = []

                for key in required_keys:
                    keys = key.split('.')
                    temp_data = data
                    for k in keys:
                        if k not in temp_data:
                            missing_keys.append(key)
                            break
                        temp_data = temp_data[k]

                if missing_keys:
                    print(f"⚠️  语言文件 {lang}.json 缺少键: {missing_keys}")
                else:
                    print(f"✅ 语言文件 {lang}.json 完整")

                results[lang] = True

            except json.JSONDecodeError as e:
                print(f"❌ 语言文件 {lang}.json JSON格式错误: {e}")
                results[lang] = False
            except Exception as e:
                print(f"❌ 读取语言文件 {lang}.json 时出错: {e}")
                results[lang] = False
        else:
            print(f"❌ 语言文件 {lang}.json 不存在")
            results[lang] = False

    return results

def main():
    """主函数"""
    print("AviUtl2 样式配置编辑器 - 多语言功能测试")
    print("AviUtl2 Style Configuration Editor - Multilingual Function Test")
    print("=" * 60)

    # 测试语言文件
    lang_results = test_language_files()

    # 测试语言功能
    success_count = 0
    for lang in ['zh', 'en', 'ja']:
        if lang_results.get(lang, False):
            if test_language_pack(lang):
                success_count += 1

    # 总结
    print("\n" + "=" * 60)
    print("测试总结 / Test Summary")
    print("=" * 60)
    print(f"语言文件检查: {sum(lang_results.values())}/3 通过")
    print(f"语言功能测试: {success_count}/3 通过")

    if success_count == 3:
        print("🎉 所有测试通过！多语言功能工作正常")
        print("🎉 All tests passed! Multilingual functionality is working correctly")
        return 0
    else:
        print("⚠️  部分测试失败，请检查上述错误信息")
        print("⚠️  Some tests failed, please check the error messages above")
        return 1

if __name__ == "__main__":
    exit(main())