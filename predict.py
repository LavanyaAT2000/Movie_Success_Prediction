import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import joblib

# Load the dataset
df = pd.read_csv('movie_rating.csv')

# Split the dataset into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(df[['actor_rating', 'director_rating', 'music_director_rating']], df['movie_rating'], test_size=0.2, random_state=42)

# Train a Gaussian Naive Bayes classifier
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Save the trained classifier to a file
joblib.dump(gnb, 'naive_bayes.pkl')

def predict(actor_rating,director_rating,music_director_rating):
    # Load the trained Naive Bayes classifier
    clf = joblib.load('naive_bayes.pkl')
    # Use the trained classifier to predict the movie rating based on the input ratings
    movie_rating = clf.predict([[actor_rating, director_rating, music_director_rating]])
    return movie_rating[0]
