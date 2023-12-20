import streamlit as st
import heapq
import string
from nltk.corpus import stopwords
import re
import itertools
# from wordcloud import WordCloud
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import heapq
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load your data
# Assuming 'new_series' is your DataFrame
# You might need to adjust the path or data loading method based on your actual data
new_series = pd.read_csv('clean_data.csv')

# Preprocess text function
def preprocess_text(text):
    if text is None or isinstance(text, list):
        return ""
    text = str(text).lower()

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Remove digits
    text = re.sub(r'\d+', '', text)

    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]

    cleaned_text = ' '.join(words)
    return cleaned_text

# Preprocess synopsis
new_series['synopsis_cleaned'] = new_series['synopsis'].apply(preprocess_text)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(new_series['synopsis_cleaned'])

# Cosine Similarity for TF-IDF
cosine_sim_tfidf = linear_kernel(tfidf_matrix, tfidf_matrix)

# Attribute-based algorithm
new_series['Tag_cleaned'] = new_series['synopsis'].apply(preprocess_text)
new_series['Genre_cleaned'] = new_series['genres'].apply(preprocess_text)
new_series['Cast_cleaned'] = new_series['cast'].apply(preprocess_text)

# Concatenate columns
def concatenate_columns(row):
    concatenated_values = []

    for column in ['Tag_cleaned', 'Genre_cleaned', 'Cast_cleaned']:
        value = row[column]

        # Check if the value is a list, and join its elements into a string
        if isinstance(value, list):
            value = ' '.join(value)

        concatenated_values.append(value)

    return ' '.join(concatenated_values)

new_series['attribute_based'] = new_series.apply(concatenate_columns, axis=1)

# Count Vectorization
count_vectorizer = CountVectorizer(stop_words='english')
count_matrix_attribute = count_vectorizer.fit_transform(new_series['attribute_based'])
cosine_sim_attribute = linear_kernel(count_matrix_attribute, count_matrix_attribute)

# Create indices
def create_indices(data):
    return data.index.to_series(index=data['name']).drop_duplicates()

indices = create_indices(new_series)

# Recommendation function
def drama_recommendations(title, ind=indices, cosine_sim_tfidf=cosine_sim_tfidf, cosine_sim_attribute=cosine_sim_attribute, top_n=5):
    idx = ind.get(title)
    if idx is None:
        print(f"Drama '{title}' not found.")
        return pd.Series()
    
    # TF-IDF recommendations
    sim_scores_tfidf = cosine_sim_tfidf[idx]
    top_indices_tfidf = heapq.nlargest(top_n, range(len(sim_scores_tfidf)), sim_scores_tfidf.__getitem__)
    recommendations_tfidf = new_series['name'].iloc[top_indices_tfidf]

    # Attribute-based recommendations
    sim_scores_attribute = cosine_sim_attribute[idx]
    top_indices_attribute = heapq.nlargest(top_n, range(len(sim_scores_attribute)), sim_scores_attribute.__getitem__)
    recommendations_attribute = new_series['name'].iloc[top_indices_attribute]

    return recommendations_tfidf, recommendations_attribute

# Streamlit app
st.title("Drama Recommendation App")

# Dropdown to select a drama
selected_drama = st.selectbox("Select a Drama:", new_series['name'].values)

# Display recommendations
st.header("Recommended Dramas (TF-IDF):")
recommended_dramas_tfidf, recommended_dramas_attribute = drama_recommendations(selected_drama)
st.write(recommended_dramas_tfidf)

st.header("Recommended Dramas (Attribute-based):")
st.write(recommended_dramas_attribute)