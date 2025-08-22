# 🎨 AviUtl2 Style Configuration Editor

[中文版](README-zh.md) | [日文版](README-ja.md)

A modern web-based interface built with Gradio for intuitive editing and customization of AviUtl2 interface style settings. This tool replaces tedious text editing with a contemporary web interface, making style configuration accessible and efficient.

## Program Feasibility Demonstration
[Program Feasibility Demonstration](test.png)

## ✨ Features

### 🎯 Core Features
- **Visual Editing Interface**: Replace tedious text editing with a modern web interface
- **Real-time Preview**: Preview configuration effects in real-time during editing
- **Batch Parameter Adjustment**: Adjust multiple related parameters simultaneously
- **Smart Validation**: Automatic validation of configuration parameter formats and ranges
- **Multilingual Support**: Complete interface and parameter descriptions in Chinese, English, and Japanese

### 🎨 Supported Configuration Items

#### Font Settings (Font)
- Default font, control font, editor font, etc.
- Individual settings for font size and font name
- Dedicated font settings for different interface elements

#### Color Theme (Color)
- Basic colors: background, text, border colors
- Control colors: buttons, sliders, progress bars
- Professional element colors: layers, objects, anchors
- Support for gradient colors and transparency settings

#### Layout Adjustment (Layout)
- Window size, separator width, scrollbar dimensions
- Layer height, timeline height, control bar dimensions
- Detailed adjustments: list item height, margins, etc.

#### Format Templates (Format)
- Customization of bottom bar display format
- Flexible settings with variable placeholders

## 🚀 Quick Start

### System Requirements
- Python 3.7+ (if not installed, the startup script will guide you)
- Modern web browser (Chrome, Firefox, Safari, etc.)
- Internet connection (for initial dependency installation)

### 🚀 One-Click Installation and Startup (Recommended for Beginners)

#### For Windows Users (Simplest Method)
1. **Double-click `start_editor.bat`**
2. The script will automatically:
   - ✅ Check if Python is installed
   - ✅ Create virtual environment (if needed)
   - ✅ Install all required dependencies
   - ✅ Ask you to choose language
   - ✅ Start the editor in your browser

#### For Linux/macOS Users
1. **Make script executable** (first time only):
   ```bash
   chmod +x start_editor.sh
   ```

2. **Run the startup script**:
   ```bash
   ./start_editor.sh
   ```

3. The script will automatically:
   - ✅ Check if Python is installed
   - ✅ Create virtual environment (if needed)
   - ✅ Install all required dependencies
   - ✅ Ask you to choose language
   - ✅ Start the editor in your browser

#### What the Startup Script Does

The intelligent startup script provides:

1. **🔍 Environment Detection**
   - Checks Python installation and version
   - Verifies pip availability
   - Validates project files integrity

2. **🏠 Virtual Environment Management**
   - Creates virtual environment automatically
   - Activates virtual environment
   - Keeps your system Python clean

3. **📦 Dependency Management**
   - Checks for required packages (gradio)
   - Installs missing dependencies automatically
   - Upgrades pip to latest version

4. **🌐 Language Selection**
   - Interactive language choice (Chinese/English/Japanese)
   - Remembers your language preference
   - Supports command-line language override

5. **🚨 Error Handling**
   - Clear error messages in both languages
   - Helpful troubleshooting suggestions
   - Graceful failure recovery

### Manual Installation (For Advanced Users)

#### Method 1: Command Line Installation

1. **Clone the Project**
   ```bash
   git clone https://github.com/your-username/aviutl2_style_editor.git
   cd aviutl2_style_editor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate Virtual Environment**
   - **Windows**: `.venv\Scripts\activate`
   - **Linux/macOS**: `source .venv/bin/activate`

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Editor**
   ```bash
   python aviutl2_style_editor.py --lang zh  # Chinese
   python aviutl2_style_editor.py --lang en  # English
   python aviutl2_style_editor.py --lang ja  # Japanese
   ```

6. **Open Browser**
   Visit `http://localhost:7860` to start using

#### Method 2: Quick Language-Specific Startup

After running the main startup script once, you can use quick start scripts:

- **Windows**: `start_zh.bat`, `start_en.bat`, `start_ja.bat`
- **Linux/macOS**: Create aliases or use the main script with language parameter

### Troubleshooting

#### Common Issues

**❌ "Python not found" Error**
- Install Python 3.7+ from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

**❌ "Virtual environment creation failed" Error**
- Check if you have write permissions in the project directory
- Try running the script as administrator (Windows) or with sudo (Linux)

**❌ "Dependency installation failed" Error**
- Check your internet connection
- Try running: `pip install gradio` manually
- If behind a proxy, configure pip proxy settings

**❌ "Port already in use" Error**
- Close any other applications using port 7860
- Or modify the port in the Python script

#### Getting Help

If you encounter any issues:
1. Check the error messages (displayed in both languages)
2. Follow the troubleshooting suggestions provided
3. Try running the startup script again
4. Check if all files are present in the project directory

## 📖 User Guide

### Basic Operation Flow

1. **Load Configuration File**
   - Click "Select style.conf file" button
   - Select AviUtl2 style configuration file
   - System automatically parses and loads configuration parameters

2. **Edit Configuration Parameters**
   - Adjust parameters in different tabs
   - Font Settings: Adjust fonts used in the interface
   - Color Settings: Use color picker to adjust theme colors
   - Layout Settings: Adjust interface size and spacing
   - Format Settings: Customize display formats

3. **Save Configuration**
   - Enter save filename (default: style_new.conf)
   - Click "Save Configuration" button
   - Copy the generated new configuration file to AviUtl2 settings directory

### Configuration Parameter Descriptions

#### Font Parameter Formats
- **Single Value**: e.g., `13` represents font size
- **Font Name**: e.g., `Yu Gothic UI` represents font name
- **Compound Parameter**: e.g., `16,Consolas` represents "font size,font name"

#### Color Parameter Formats
- **6-digit Hex**: e.g., `202020` represents RGB color
- **8-digit Hex**: e.g., `202020ff` represents RGBA color (with transparency)
- **Multiple Colors**: e.g., `903838,b84848` represents gradient colors

### Configuration File Locations

AviUtl2 style configuration files are typically located at:
- `%ProgramData%\aviutl2\style.conf` (Windows)
- `~/Library/Application Support/aviutl2/style.conf` (macOS)
- `/usr/share/aviutl2/style.conf` (Linux)

## 📁 Project Structure

```
aviutl2_style_editor/
├── aviutl2_style_editor.py    # Main program file
├── locales/                   # Language files directory
│   ├── zh.json               # Chinese language pack
│   ├── en.json               # English language pack
│   └── ja.json               # Japanese language pack
├── start_editor.bat          # 🚀 Windows one-click startup script
├── start_zh.bat              # 🚀 Chinese quick start
├── start_en.bat              # 🚀 English quick start
├── start_ja.bat              # 🚀 Japanese quick start
├── start_editor.sh           # 🚀 Linux/macOS startup script
├── test_languages.py         # ✅ Multilingual function test script
├── style-zh.conf             # Sample configuration file (Chinese comments)
├── README.md                 # 📖 English documentation
├── README-zh.md              # 📖 Chinese documentation
├── README-ja.md              # 📖 Japanese documentation
├── LICENSE                   # 📜 Open source license
└── requirements.txt          # 📦 Python dependency list
```

## 🌐 Multilingual Support

This project supports three language interfaces:

- **Chinese (zh)** - Default language
- **English (en)** - English interface
- **Japanese (ja)** - Japanese interface

### Launching with Different Languages

#### Method 1: Direct Command Line
```bash
# Chinese interface
python aviutl2_style_editor.py --lang zh

# English interface
python aviutl2_style_editor.py --lang en

# Japanese interface
python aviutl2_style_editor.py --lang ja
```

#### Method 2: Using Startup Scripts (Recommended)

**Windows Users:**
- `start_editor.bat` - Interactive language selection launcher
- `start_zh.bat` - Direct Chinese version startup
- `start_en.bat` - Direct English version startup
- `start_ja.bat` - Direct Japanese version startup

**Linux/Unix Users:**
- `./start_editor.sh` - Interactive language selection launcher (requires execution permission)

#### Method 3: Using Original Command
```bash
# Using your existing Python environment
& E:\somepys\test312\.venv\Scripts\python.exe aviutl2_style_editor.py --lang zh
```

## 🔧 Startup Scripts Description

### 🚀 Startup Script Features
The project provides convenient startup scripts that automatically complete:
- **Environment Check**: Automatically detect if Python environment is available
- **Dependency Installation**: Automatically check and install required Python packages
- **Program Launch**: Automatically launch AviUtl2 Style Configuration Editor
- **Friendly Prompts**: Provide clear status information and error handling

### Usage
- **Windows**: Double-click `start_editor.bat` to launch
- **Linux/macOS**: Run `./start_editor.sh` to launch the program

Startup scripts handle all complex environment setup, making it easy for beginner users!

## 🎯 Supported Configuration Parameters

### Font Settings (Font)
- DefaultFamily - Default font name
- Control - Control font size
- EditControl - Edit box font
- PreviewTime - Preview time font size
- LayerObject - Layer object font size
- TimeGauge - Time scale font size
- Footer - Footer font size
- TextEdit - Text edit font
- Log - Log font

### Color Settings (Color)
- Background - Background color
- WindowBorder - Window border color
- Text - Text color
- ButtonBody - Button background color
- BorderSelect - Selected border color
- Footer - Footer background color
- Layer - Layer background color
- ObjectVideo - Video object color
- ObjectAudio - Audio object color
- And more...

### Layout Settings (Layout)
- WindowSeparatorSize - Window separator width
- ScrollBarSize - Scroll bar width
- FooterHeight - Footer height
- LayerHeight - Layer height
- TimeGaugeHeight - Timeline height
- And more...

### Format Settings (Format)
- FooterLeft - Footer left display format
- FooterRight - Footer right display format

## 🔧 Development Notes

### Dependencies
- **gradio**: Web interface framework
- **configparser**: INI configuration file parsing
- **pathlib**: Path handling

### Code Structure
- `AviUtlStyleEditor` class: Core editor class
- `parse_style_file()`: Configuration file parsing
- `create_gradio_interface()`: Interface creation
- `generate_config_content()`: Configuration generation

### Adding New Language Support

1. Create new language file in `locales/` directory (e.g., `fr.json`)
2. Translate all text following the format of existing language files
3. Add new language option in main program

### Custom Configuration Parameters

You can add or modify supported configuration parameters in the `get_parameter_info` method:

```python
param_info = {
    'SectionName': {
        'ParameterKey': {
            'type': 'slider',  # Control type: slider, text, color
            'label': 'Display Label',
            'min': 0,          # Minimum value (for slider type)
            'max': 100,        # Maximum value (for slider type)
            'default': 50,     # Default value
            'description': 'Parameter description'
        }
    }
}
```

## 🤝 Contributing

Issues and Pull Requests are welcome!

1. Fork this project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- Thanks to KEN, the author of AviUtl2, for providing excellent video editing software
- Thanks to the Gradio team for providing an excellent web interface framework

## 📞 Contact

For questions or suggestions, please contact us through:
- Submit GitHub Issue

---

**Note**: This tool is only used for editing AviUtl2 style configuration files and does not modify AviUtl2's core program files. Use with confidence.