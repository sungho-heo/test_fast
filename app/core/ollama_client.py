import requests

def summarize(text: str):
    prompt ="""
    
    """
    
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"qwen2.5:3b",
            "prompt":f"문서를 요약해줘 korean language로:\n{text}",
            "stream":False
        }
    )
    
    return res.json()["response"]