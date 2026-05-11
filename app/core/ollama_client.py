import requests

def summarize(text: str):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"gemma4",
            "prompt":f"문서를 요약해줘:\n{text}",
            "stream":False
        }
    )
    
    return res.json()["response"]