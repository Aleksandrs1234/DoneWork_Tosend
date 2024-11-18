from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download required NLTK data
nltk.download('punkt')

def calculate_match_rate(text1, text2):
    # Tokenize texts
    words1 = word_tokenize(text1)
    words2 = word_tokenize(text2)
    
    # Normalize to lowercase and filter only alphabetical words
    words1 = {word.lower() for word in words1 if word.isalpha()}
    words2 = {word.lower() for word in words2 if word.isalpha()}
    
    # Find the intersection (common words)
    common_words = words1.intersection(words2)
    
    # Calculate match percentage
    total_words = len(words1.union(words2))
    match_percentage = (len(common_words) / total_words) * 100 if total_words > 0 else 0
    
    return common_words, match_percentage

# Example texts
text1 = "Fall leaves are yellow and orange. Leaves cover the ground and make it colorful."
text2 = "Colorful autumn leaves are falling to the ground. The leaves are orange and yellow."

# Calculate matches and match rate
common_words, match_percentage = calculate_match_rate(text1, text2)

# Display results
print(f"Common Words: {common_words}")
print(f"Match Percentage: {match_percentage:.2f}%")