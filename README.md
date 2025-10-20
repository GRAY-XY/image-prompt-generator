# image-prompt-generator
An image-prompt-generator

自动根据图像内容生成 Stable Diffusion / AI 绘图 提示词。

## ✨ 功能
- 自动分析图片（BLIP 生成描述）
- 使用 CLIP 语义匹配提示词库
- 自动拼接正向 / 负向提示词
- 支持命令行与 Web 界面

## 🛠 安装
```bash
git clone https://github.com/yourname/image-prompt-generator.git
cd image-prompt-generator
pip install -r requirements.txt
