# FastFood Recommender Web Application

## Project Overview
The **FastFood Recommender** is a web application designed to help users discover new fast food items based on their preferences. The app provides personalized recommendations based on food item similarities and nutritional information, such as calories, fat content, protein, sodium, and more.

Users can browse different food items, view nutritional details, and get personalized suggestions based on their choices. There is also an option to filter recommendations to healthier options by focusing on lower-calorie and higher-protein items.

This project uses **Streamlit** for creating a simple yet interactive user interface and **scikit-learn** for building a food similarity model using cosine similarity.


## Features
- **Browse and search**: Users can browse various food items from different restaurants.
- **Item details**: View detailed nutritional information for each food item, including calories, fat content, protein, etc.
- **Personalized recommendations**: Get recommendations based on food similarity using the cosine similarity model.
- **Healthy options filter**: Filter recommendations to show only healthier options (low-calorie and high-protein).


## Tech Stack
- **Python**: The main programming language for the backend.
- **Streamlit**: Web application framework for creating interactive dashboards.
- **Pandas**: Data manipulation and analysis library.
- **NumPy**: Numerical computing library for data operations.
- **scikit-learn**: Machine learning library for data preprocessing, similarity calculations, and building recommendation models.
- **Cosine Similarity**: Used for calculating the similarity between food items based on nutritional information.
