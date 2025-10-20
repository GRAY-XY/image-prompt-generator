from src.prompt_builder import generate_prompts

if __name__ == "__main__":
    path = input("请输入图片路径：").strip('"')
    caption, pos, neg = generate_prompts(path)
    
    print("\n 图像描述：", caption)
    print("\n 正向提示词：\n", pos)
    print("\n 负向提示词：\n", neg)
