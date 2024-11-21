from langdetect import detect, detect_langs

def detect_language(text):
    try:
        language = detect(text)
        
        languages_with_probabilities = detect_langs(text)
        
        return language, languages_with_probabilities
    except Exception as e:
        return f"Error: {e}", []

texts = [
    "Šodien ir saulaina diena.",  
    "Today is a sunny day.",      
    "Сегодня солнечный день."     
]


for text in texts:
    lang, probabilities = detect_language(text)
    print(f"Text: {text}")
    print(f"Detected Language: {lang}")
    print(f"Probabilities: {probabilities}")
    print("-" * 40)
