from transformers import MarianMTModel, MarianTokenizer

def translate_to_english(texts, source_lang="lv", target_lang="en"):
    # Load the pre-trained translation model for Latvian to English
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Translate each text
    translations = []
    for text in texts:
        # Tokenize and generate translation
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        translated = model.generate(**inputs)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        translations.append(translated_text)
    
    return translations

# Input texts in Latvian
latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

# Translate to English
translations = translate_to_english(latvian_texts)

# Display results
for i, (lv_text, en_text) in enumerate(zip(latvian_texts, translations), start=1):
    print(f"Sentence {i} in Latvian: {lv_text}")
    print(f"Translation to English: {en_text}\n")
