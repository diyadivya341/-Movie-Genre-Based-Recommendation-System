🎬 Movie Genre-Based Recommendation System
📌 Project Summary:

This project implements a content-based movie recommendation system using machine learning techniques to suggest movies similar to a user-provided title based on movie genres. The system leverages TF-IDF vectorization to encode movie genres and a K-Nearest Neighbors (KNN) model to find and recommend movies with similar genre profiles.

An interactive Streamlit web app provides an easy-to-use interface where users can input a movie title and receive top 5 similar movie recommendations instantly.

📂 Dataset Details:

- Dataset contains movie titles and associated genres.

Key features include:

- title — the movie name

- genres — genre description (used for vectorization and similarity search)

- The dataset is preprocessed for missing or invalid genre data.

🛠️ Technologies Used:

Python Libraries:

- Streamlit — for building the interactive web app

- Pandas — for data handling and manipulation

- Scikit-learn — TF-IDF vectorizer and KNN model for recommendations

- Joblib — for loading pre-trained model and vectorizer

🛠️ Project Workflow:

- Load dataset and preprocess missing genres

- Load pre-trained TF-IDF vectorizer and KNN model from disk

- Vectorize movie genres using TF-IDF

- Implement KNN to find nearest neighbors based on genre similarity

- Develop Streamlit app for user input and displaying recommendations

- Handle input errors (movie not found) gracefully with user-friendly messages

📈 Key Features:

- Input movie title to get genre-based similar movie recommendations

- Shows top 5 closest movies by genre similarity

- Interactive and intuitive UI using Streamlit

- Fast real-time recommendation using precomputed TF-IDF and KNN model

- Error handling for invalid or unknown movie titles





![Screenshot 2025-06-06 184805](https://github.com/user-attachments/assets/9caa9381-1972-49a6-a05f-3698a588047e)
![Screenshot 2025-06-06 184825](https://github.com/user-attachments/assets/69b092c7-af6b-4f21-b23d-72575ee3001b)
![Screenshot 2025-06-06 184904](https://github.com/user-attachments/assets/693a6d27-547f-40da-b3e4-45a4a74c3abc)
![Screenshot 2025-06-06 184924](https://github.com/user-attachments/assets/a90adfe7-ae8e-45af-b552-f6ad370b421b)
![Screenshot 2025-06-06 185056](https://github.com/user-attachments/assets/40b848bd-6a87-4c2b-b092-989677463318)
![Screenshot 2025-06-06 185109](https://github.com/user-attachments/assets/84b2bbbb-aae7-4704-b95f-09bb656260fe)
