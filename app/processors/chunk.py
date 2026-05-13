# ollama 임베딩을 통한 의미 유사도 계산해 청킹작업.
from ollama import Client
import numpy as np

# def fixed_chunk(text:str, chunk_size:int=500, overlap:int =50):
#     chunks = []
#     start =0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start += chunk_size - overlap
#     return chunks


def recursive_chunk(text:str, chunk_size:int =500, overlap:int =50):
    # 분리 기준 우선순위는 =>문단 문장 단어순.
    separators = ["\n\n","\n", ". ", " "]
    
    for sep in separators:
        if sep in text and len(text) > chunk_size:
            parts = text.split(sep)
            chunks = []
            current = ""
            
            for part in parts:
                if len(current) + len(part) <= chunk_size:
                    current += part +sep
                else:
                    if current:
                        chunks.append(current.strip())
                    current = current[-overlap:] + part + sep # overlap 유지합니다.
            
            if current:
                chunks.append(current.strip())
            return chunks
    
    return [text]

# ollama = Client()

# def cosine_similarity(a,b):
#     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# def semantic_chunk(text:str, threshold: float = 0.8):
#     sentences = text.split(". ")
    
#     # 각 문장 임베딩
#     embeddings = []
#     for s in sentences:
#         res = ollama.embeddings(model="nomic-embed-text", prompt=s)
#         embeddings.append(res["embedding"])
        
#     chunks = []
#     current_chunk = [sentences[0]]
    
#     for i in range(1, len(sentences)):
#         # 유사도를 코사인 유사도 계산으로 구함.
#         similarity = cosine_similarity(embeddings[i-1], embeddings[i])
        
#         if similarity >= threshold:
#             current_chunk.append(sentences[1]) #유사하면 같은 청크로인식.
#         else:
#             chunks.append(". ".join(current_chunk)) # 다를경우 새 청크로만듬.
#             current_chunk = [sentences[1]]
    
#     chunks.append(". ".join(current_chunk))
#     return chunks