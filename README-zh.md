# 🎨 AviUtl2 样式配置编辑器

一个用于直观编辑 AviUtl2 `style.conf` 配置文件的 Web 界面工具，提供专门的控件进行参数调整。

## ✨ 功能特性

- 🎨 **直观的 Web 界面** - 使用 Gradio 构建的现代化 Web 界面
- 📝 **字体设置** - 调整界面中使用的各种字体和字号
- 🎨 **颜色设置** - 可视化颜色选择器，支持 RGB 颜色调整
- 📐 **布局设置** - 调整界面尺寸、间距和布局参数
- ⚙️ **格式设置** - 自定义显示格式和模板
- 🌐 **多语言支持** - 支持中文、英文、日文界面
- 💾 **实时保存** - 即时保存配置到文件

## 🚀 快速开始

### 环境要求

- Python 3.7+（如果未安装，启动脚本会引导您安装）
- 现代浏览器（Chrome、Firefox、Safari 等）
- 网络连接（用于初始依赖安装）

### 🚀 一键安装和启动（新手推荐）

#### Windows用户（最简单方法）
1. **双击 `start_editor.bat`**
2. 脚本将自动执行：
   - ✅ 检查Python是否已安装
   - ✅ 创建虚拟环境（如需要）
   - ✅ 安装所有必需的依赖包
   - ✅ 让您选择界面语言
   - ✅ 在浏览器中启动编辑器

#### Linux/macOS用户
1. **设置脚本可执行权限**（首次运行）：
   ```bash
   chmod +x start_editor.sh
   ```

2. **运行启动脚本**：
   ```bash
   ./start_editor.sh
   ```

3. 脚本将自动执行：
   - ✅ 检查Python是否已安装
   - ✅ 创建虚拟环境（如需要）
   - ✅ 安装所有必需的依赖包
   - ✅ 让您选择界面语言
   - ✅ 在浏览器中启动编辑器

#### 智能启动脚本的功能

智能启动脚本提供以下功能：

1. **🔍 环境检测**
   - 检查Python安装和版本
   - 验证pip可用性
   - 验证项目文件完整性

2. **🏠 虚拟环境管理**
   - 自动创建虚拟环境
   - 自动激活虚拟环境
   - 保持系统Python环境清洁

3. **📦 依赖包管理**
   - 检查必需包（gradio）
   - 自动安装缺失的依赖
   - 升级pip到最新版本

4. **🌐 语言选择**
   - 交互式语言选择（中文/英文/日文）
   - 记住您的语言偏好设置
   - 支持命令行语言参数

5. **🚨 错误处理**
   - 中英文双语错误提示
   - 有用的故障排除建议
   - 优雅的故障恢复

### 手动安装（高级用户）

#### 方法一：命令行安装

1. **克隆项目**
   ```bash
   git clone https://github.com/your-username/aviutl2_style_editor.git
   cd aviutl2_style_editor
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv .venv
   ```

3. **激活虚拟环境**
   - **Windows**: `.venv\Scripts\activate`
   - **Linux/macOS**: `source .venv/bin/activate`

4. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

5. **运行编辑器**
   ```bash
   python aviutl2_style_editor.py --lang zh  # 中文
   python aviutl2_style_editor.py --lang en  # 英文
   python aviutl2_style_editor.py --lang ja  # 日文
   ```

6. **打开浏览器**
   访问 `http://localhost:7860` 开始使用

#### 方法二：快速语言指定启动

运行主启动脚本一次后，您可以使用快速启动脚本：

- **Windows**: `start_zh.bat`, `start_en.bat`, `start_ja.bat`
- **Linux/macOS**: 创建别名或使用主脚本带语言参数

### 故障排除

#### 常见问题

**❌ "未找到Python" 错误**
- 从 https://www.python.org/downloads/ 安装 Python 3.7+
- 安装时务必勾选"Add Python to PATH"选项

**❌ "创建虚拟环境失败" 错误**
- 检查在项目目录是否有写入权限
- 尝试以管理员身份运行脚本（Windows）或使用sudo（Linux）

**❌ "依赖安装失败" 错误**
- 检查网络连接
- 尝试手动运行：`pip install gradio`
- 如果在代理环境下，请配置pip代理设置

**❌ "端口已被占用" 错误**
- 关闭其他占用7860端口的程序
- 或修改Python脚本中的端口设置

#### 获取帮助

如果遇到问题：
1. 查看错误信息（双语显示）
2. 按照提供的故障排除建议操作
3. 尝试重新运行启动脚本
4. 检查项目目录中所有文件是否完整

## 📁 项目结构

```
aviutl2_style_editor/
├── aviutl2_style_editor.py    # 主程序文件
├── locales/                   # 语言文件目录
│   ├── zh.json               # 中文语言包
│   ├── en.json               # 英文语言包
│   └── ja.json               # 日文语言包
├── requirements.txt          # Python 依赖包
├── README.md                 # 项目说明文档（英文）
├── README-zh.md              # 项目说明文档（中文）
├── README-ja.md              # 项目说明文档（日文）
├── LICENSE                   # 开源许可证
└── start_editor.bat          # Windows 启动脚本
```

## 🌐 多语言支持

本项目支持三种语言界面：

- **中文 (zh)** - 默认语言
- **English (en)** - 英文界面
- **日本語 (ja)** - 日文界面

### 使用不同语言启动

#### 方法一：直接命令行启动
```bash
# 中文界面
python aviutl2_style_editor.py --lang zh

# 英文界面
python aviutl2_style_editor.py --lang en

# 日文界面
python aviutl2_style_editor.py --lang ja
```

#### 方法二：使用启动器脚本（推荐）

**Windows用户：**
- `start_editor.bat` - 交互式语言选择启动器
- `start_zh.bat` - 直接启动中文版本
- `start_en.bat` - 直接启动英文版本
- `start_ja.bat` - 直接启动日文版本

**Linux/Unix用户：**
- `./start_editor.sh` - 交互式语言选择启动器（需要执行权限）

#### 方法三：使用原始命令
```bash
# 使用您现有的Python环境
& E:\somepys\test312\.venv\Scripts\python.exe aviutl2_style_editor.py --lang zh
```

## 🎯 支持的配置参数

### 字体设置 (Font)
- DefaultFamily - 默认字体名称
- Control - 控件字体大小
- EditControl - 编辑框字体
- PreviewTime - 预览时间字体大小
- LayerObject - 图层对象字体大小
- TimeGauge - 时间刻度字体大小
- Footer - 底部栏字体大小
- TextEdit - 文本编辑字体
- Log - 日志字体

### 颜色设置 (Color)
- Background - 背景色
- WindowBorder - 窗口边框色
- Text - 文本色
- ButtonBody - 按钮背景色
- BorderSelect - 选中边框色
- Footer - 底部栏背景色
- Layer - 图层背景色
- ObjectVideo - 视频对象色
- ObjectAudio - 音频对象色
- 等等...

### 布局设置 (Layout)
- WindowSeparatorSize - 窗口分隔条宽度
- ScrollBarSize - 滚动条宽度
- FooterHeight - 底部栏高度
- LayerHeight - 图层高度
- TimeGaugeHeight - 时间轴高度
- 等等...

### 格式设置 (Format)
- FooterLeft - 底部栏左侧显示格式
- FooterRight - 底部栏右侧显示格式

## 🔧 开发说明

### 添加新的语言支持

1. 在 `locales/` 目录下创建新的语言文件 (如 `fr.json`)
2. 参考现有语言文件的格式翻译所有文本
3. 在主程序中添加新的语言选项

### 自定义配置参数

在 `get_parameter_info` 方法中可以添加或修改支持的配置参数：

```python
param_info = {
    'SectionName': {
        'ParameterKey': {
            'type': 'slider',  # 控件类型：slider, text, color
            'label': '显示标签',
            'min': 0,          # 最小值（slider类型）
            'max': 100,        # 最大值（slider类型）
            'default': 50,     # 默认值
            'description': '参数描述'
        }
    }
}
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [Gradio](https://gradio.app/) - 用于构建 Web 界面的优秀框架
- [AviUtl2](http://aviutl.info/) - 强大的视频编辑软件

## 📞 联系方式

如果您有任何问题或建议，请通过以下方式联系：

- 提交 GitHub Issue
- 发送邮件至项目维护者

---

**注意**: 本工具仅用于编辑 AviUtl2 的样式配置文件，请确保您有相应的使用权限。