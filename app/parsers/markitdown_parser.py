from markitdown import MarkItDown

def read_markitdown(path:str):
    
    md = MarkItDown()
    
    result= md.convert(path)
    
    return result.text_content