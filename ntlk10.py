from transformers import MarianMTModel, MarianTokenizer

def translate_to_english(texts, source_lang="lv", target_lang="en"):h
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    translations = []
    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        translated = model.generate(**inputs)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        translations.append(translated_text)
    
    return translations

latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translations = translate_to_english(latvian_texts)

for i, (lv_text, en_text) in enumerate(zip(latvian_texts, translations), start=1):
    print(f"Sentence {i} in Latvian: {lv_text}")
    print(f"Translation to English: {en_text}\n")
