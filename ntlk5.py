import re

def clean_text(raw_text):
    # Noņem lietotājvārdus (@...)
    text = re.sub(r"@\w+", "", raw_text)
    
    # Noņem URL
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    
    # Noņem liekos simbolus (emojis, !!!, ? u.c.)
    text = re.sub(r"[^\w\s]", "", text)
    
    # Pārveido uz mazajiem burtiem
    text = text.lower()
    
    # Noņem liekās atstarpes
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

# Neapstrādāts teksts
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Tīrīšana un normalizēšana
cleaned_text = clean_text(raw_text)

# Rezultāts
print("Oriģinālais teksts:", raw_text)
print("Tīrītais teksts:", cleaned_text)