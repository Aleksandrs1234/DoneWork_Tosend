from transformers import AutoTokenizer, AutoModel
import torch
from scipy.spatial.distance import cosine

# Load a pre-trained transformer model (e.g., BERT)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def get_embedding(word):
    # Tokenize the input word
    tokens = tokenizer(word, return_tensors="pt")
    with torch.no_grad():
        # Obtain the hidden states from the model
        outputs = model(**tokens)
        # Get the embedding for the [CLS] token
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embedding

def semantic_similarity_with_bert(word1, word2):
    embedding1 = get_embedding(word1)
    embedding2 = get_embedding(word2)
    similarity = 1 - cosine(embedding1, embedding2)
    return similarity

# Input words
words = ["house", "apartment", "sea"]

# Obtain embeddings and compare similarity
print("Semantic Similarities (BERT):")
print(f"Similarity between 'house' and 'apartment': {semantic_similarity_with_bert('house', 'apartment'):.2f}")
print(f"Similarity between 'house' and 'sea': {semantic_similarity_with_bert('house', 'sea'):.2f}")
print(f"Similarity between 'apartment' and 'sea': {semantic_similarity_with_bert('apartment', 'sea'):.2f}")