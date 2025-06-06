import streamlit as st
import pandas as pd
from joblib import load

# Load model and vectorizer
try:
    model = load('recommendation_model.joblib')
    tfidf = load('tfidf_vectorizer.joblib')
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# Load dataset
try:
    movies_data = pd.read_csv(r"C:\Users\divya\Downloads\movies.csv")
except FileNotFoundError:
    st.error("movies.csv file not found in Downloads folder.")
    st.stop()

# Fill missing genres with empty string to avoid errors
movies_data['genres'] = movies_data['genres'].fillna('')

# Create TF-IDF matrix for genres
tfidf_matrix = tfidf.transform(movies_data['genres'])

st.title("🎬 Movies Recommendation System")
st.write("Enter a movie name to get recommendations based on genres.")

movie_name = st.text_input("Enter a movie title:")

if st.button("Recommend"):
    if movie_name:
        movie_name_lower = movie_name.lower()
        titles_lower = movies_data['title'].str.lower()

        if movie_name_lower in titles_lower.values:
            idx = titles_lower[titles_lower == movie_name_lower].index[0]
            distances, indices = model.kneighbors(tfidf_matrix[idx], n_neighbors=6)

            st.subheader("Top 5 Similar Movies:")
            for i in indices[0][1:]:
                st.write(f"🎞️ {movies_data['title'].iloc[i]}")
        else:
            st.error("Movie not found. Please check spelling or try another title.")
    else:
        st.warning("Please enter a movie title to get recommendations.")
