import os
import shutil
from src.prompt_builder import generate_prompts
from src.utils import ensure_dir, get_timestamp, random_filename, save_json

def main():
    # 当前工作目录
    cwd = os.getcwd()

    # 输入、输出目录
    input_dir = ensure_dir(os.path.join(cwd, "input"))
    output_dir = ensure_dir(os.path.join(cwd, "output"))

    # 支持的图片格式
    valid_exts = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(valid_exts):
            continue

        img_path = os.path.join(input_dir, filename)
        name, _ = os.path.splitext(filename)
        folder_path = ensure_dir(os.path.join(
            output_dir,
            name
        ))

        print(f"正在处理：{filename}")

        try:
            caption, pos, neg = generate_prompts(img_path)
            result = {
                "image": img_path,
                "caption": caption,
                "positive_prompt": pos,
                "negative_prompt": neg,
                "time": get_timestamp()
            }
            output_path = os.path.join(
                folder_path,
                random_filename(name, ".json")
            )
            save_json(result, output_path)
            shutil.copy(img_path, os.path.join(folder_path, filename))
            print(f"✅ 已保存：{folder_path}\n")

        except Exception as e:
            print(f"❌ 处理 {filename} 时出错：{e}\n")

if __name__ == "__main__":
    main()
