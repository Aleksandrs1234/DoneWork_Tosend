from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')

def calculate_match_rate(text1, text2):
    words1 = word_tokenize(text1)
    words2 = word_tokenize(text2)
        
    words1 = {word.lower() for word in words1 if word.isalpha()}
    words2 = {word.lower() for word in words2 if word.isalpha()}
    
    common_words = words1.intersection(words2)
    
    total_words = len(words1.union(words2))
    match_percentage = (len(common_words) / total_words) * 100 if total_words > 0 else 0
    
    return common_words, match_percentage

text1 = "Fall leaves are yellow and orange. Leaves cover the ground and make it colorful."
text2 = "Colorful autumn leaves are falling to the ground. The leaves are orange and yellow."

common_words, match_percentage = calculate_match_rate(text1, text2)

print(f"Common Words: {common_words}")
print(f"Match Percentage: {match_percentage:.2f}%")
