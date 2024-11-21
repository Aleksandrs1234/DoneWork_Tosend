import re

def clean_text(raw_text):
    text = re.sub(r"@\w+", "", raw_text)
    
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    
    text = re.sub(r"[^\w\s]", "", text)
    
    text = text.lower()
    
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

cleaned_text = clean_text(raw_text)

# Rezultāts
print("Oriģinālais teksts:", raw_text)
print("Tīrītais teksts:", cleaned_text)
