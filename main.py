import os
from src.prompt_builder import generate_prompts

def main():
    input_dir = os.path.join(os.getcwd(), "input")
    output_dir = os.path.join(os.getcwd(), "output")

    # 创建 output 文件夹（若不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 支持的图片格式
    valid_exts = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(valid_exts):
            continue

        img_path = os.path.join(input_dir, filename)
        name, _ = os.path.splitext(filename)
        output_path = os.path.join(output_dir, f"{name}.txt")

        # 如果已有同名txt则跳过
        if os.path.exists(output_path):
            print(f"跳过已存在文件：{output_path}")
            continue

        print(f"正在处理：{filename}")

        try:
            caption, pos, neg = generate_prompts(img_path)

            # 创建并写入新文件
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"图像描述：{caption}\n\n")
                f.write("正向提示词：\n")
                f.write(pos + "\n\n")
                f.write("负向提示词：\n")
                f.write(neg + "\n")

            print(f"已创建并保存：{output_path}")

        except Exception as e:
            print(f"处理 {filename} 时出错：{e}")

if __name__ == "__main__":
    main()
