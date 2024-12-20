from textblob import TextBlob

def determine_sentiment(sentence):
    analysis = TextBlob(sentence)
    
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        mood = "Positive"
    elif polarity < 0:
        mood = "Negative"
    else:
        mood = "Neutral"
    
    return mood, polarity

sentences = [
    "This product is great, I am very satisfied!",
    "I am disappointed, the product does not match the description.",
    "Neutral product, nothing special.",
    "I hate this stupid product",
    "This product is stupidly good!"
]

for sentence in sentences:
    mood, polarity = determine_sentiment(sentence)
    print(f"Sentence: \"{sentence}\"")
    print(f"Sentiment: {mood} (Polarity: {polarity:.2f})")
    print("-" * 40)
