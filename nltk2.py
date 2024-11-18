from langdetect import detect, detect_langs

def detect_language(text):
    try:
        # Detect the primary language of the text
        language = detect(text)
        
        # Get probabilities of detected languages
        languages_with_probabilities = detect_langs(text)
        
        return language, languages_with_probabilities
    except Exception as e:
        return f"Error: {e}", []

# Example texts
texts = [
    "Šodien ir saulaina diena.",  # Latvian
    "Today is a sunny day.",      # English
    "Сегодня солнечный день."     # Russian
]

# Analyze each text
for text in texts:
    lang, probabilities = detect_language(text)
    print(f"Text: {text}")
    print(f"Detected Language: {lang}")
    print(f"Probabilities: {probabilities}")
    print("-" * 40)