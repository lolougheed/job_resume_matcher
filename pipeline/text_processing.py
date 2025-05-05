import os
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Stopwords
nltk.download('stopwords')

# Simple Cleaner
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)  # remove new lines
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)  # remove punctuation
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)

# Load and clean all files
folder_path = 'data/'
def load_and_clean_folder(folder_path):
    texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                texts[filename] = clean_text(text)
    return texts

# Compare Resume to Jobs
def calculate_similarity(resume_text, job_texts):
    corpus = [resume_text] + list(job_texts.values())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = (tfidf_matrix[0] @ tfidf_matrix[1:].T).toarray()[0]
    
    results = {}
    for idx, job_name in enumerate(job_texts.keys()):
        results[job_name] = similarity_scores[idx] * 100  # %
    return results
