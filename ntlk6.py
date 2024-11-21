from transformers import pipeline

def summarize_article(article, max_length=50, min_length=25):
    # Load the summarization pipeline
    summarizer = pipeline("summarization")
    
    # Generate a summary
    summary = summarizer(article, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Input article
article = """
Latvia is a country in the Baltic region. Its capital is Riga, which is famous for its historic center and beautiful buildings.
Latvia borders Lithuania, Estonia, and Russia, and has access to the Baltic Sea. It is one of the member states of the European Union.
"""

# Summarize the article
summary = summarize_article(article)

print("Original Article:", article)
print("\nSummary:", summary)