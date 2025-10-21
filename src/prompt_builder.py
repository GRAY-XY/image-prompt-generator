import json
from src.analyzer import describe_image
from src.matcher import match_keywords

def load_prompt_library(path="prompt_library.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def flatten_dict(d):
    result = []
    for v in d.values():
        if isinstance(v, dict):
            result += flatten_dict(v)
        elif isinstance(v, list):
            result += v
    return result

def generate_prompts(image_path: str, top_k: int = 15):
    library = load_prompt_library()
    caption = describe_image(image_path)
    all_keywords = flatten_dict(library["positive"])
    matched = match_keywords(caption, all_keywords, top_k=top_k)
    
    positive = ", ".join(
        [f"({w}:1.2)" for w in library["positive_default"][:10]] +
        [f"({m}:1.4)" for m in matched]
    )
    negative = ", ".join(library["negative_default"][:30])
    
    return caption, positive, negative
