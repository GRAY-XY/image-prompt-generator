import torch
from transformers import CLIPProcessor, CLIPModel

device = "cuda" if torch.cuda.is_available() else "cpu"

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def match_keywords(caption: str, keywords: list[str], top_k: int = 10):
    inputs = clip_processor(text=[caption] + keywords, return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        text_features = clip_model.get_text_features(**inputs)
    caption_feat = text_features[0].unsqueeze(0)
    word_feats = text_features[1:]
    sim = torch.nn.functional.cosine_similarity(caption_feat, word_feats)
    idx = sim.argsort(descending=True)[:top_k]
    return [keywords[i] for i in idx]
