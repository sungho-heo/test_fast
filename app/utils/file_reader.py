# 파일 읽기만 하는용도..
def read_txt(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()