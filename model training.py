import os
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize NLTK and other components
nltk.download('punkt')
st = PorterStemmer()

# Load your dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'small_songdata.csv')  # Update with the new CSV filename
f = pd.read_csv(file_path)

# Preprocess the text data
f['text'] = f['text'].str.lower().replace(r'\n', ' ', regex=True)

def token(txt):
    token = nltk.word_tokenize(txt)
    return " ".join([st.stem(w) for w in token])

f['text'] = f['text'].apply(lambda x: token(x))

# TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(f['text'])  # Automatically handles all rows

# Compute cosine similarity
similar = cosine_similarity(tfidf_matrix)

# Recommendation function
def recommend(song):
    matching_songs = f[f['song'].str.lower() == song.lower()]
    if not matching_songs.empty:
        ix = matching_songs.index[0]
        distance = sorted(list(enumerate(similar[ix])), reverse=True, key=lambda x: x[1])
        recommended_songs = []
        for s_id in distance[1:11]:  # Skip the first item as it is the song itself
            recommended_songs.append(f.iloc[s_id[0]]['song'])
        return recommended_songs
    else:
        return []  # Return an empty list if the song is not found in the DataFrame

# Example usage
recommended_songs = recommend("Just Lose It")
print(recommended_songs)

fav_song = input("\n\nEnter your Favourite song\n"
                 "God help your spelling and availability in the dataset"
                 "\n>>")
recommendations = recommend(fav_song)
print(f"\nRecommended Songs:\n{recommendations}")
