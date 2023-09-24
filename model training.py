
import os

# Get the current directory of your script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the file path relative to the script's directory
file_path = os.path.join(script_dir, 'spotify_millsongdata.csv')



# because I hate pickle
import pandas as p


# Now, read the CSV file
f = p.read_csv(file_path)

# we won't need links
f = f.drop('link', axis = 1).reset_index(drop=True)

# text cleaing
f['text'].str.lower().replace(r'^\w\s',' ').replace(r'\n', ' ', regex = True)


# most important thing
# tokenization
# what tokenization is it simplyfies 
# the text here if their meaning is similar
 

import nltk as n
n.download('punkt')
from nltk.stem.porter import PorterStemmer as p
st = p ()


def token(txt):
    token = n.word_tokenize(txt)
    return " ".join([st.stem(w) for w in token])

f['text'].apply(lambda x : token(x))


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample size, adjust as needed
sample_size = 30000

# Sample a subset of your data
sampled_data = f.sample(n=sample_size, random_state=42)  # Adjust random_state as needed

# TF-IDF vectorization for the sampled data
tfidf_vectorizer = TfidfVectorizer(analyzer='word', stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(sampled_data['text'])

# Compute cosine similarity for the sampled data
similar = cosine_similarity(tfidf_matrix)

# Now you can use 'similar' for recommendations based on the sampled data


# now I got everything for the recommendation to begin

# behold

def recommend(song):
    matching_songs = f[f['song'] == song]
    if not matching_songs.empty:
        ix = matching_songs.index[0]
        distance = sorted(list(enumerate(similar[ix])), reverse=True, key=lambda x: x[1])
        recommended_songs = []
        for s_id in distance[1:11]:
            recommended_songs.append(f.iloc[s_id[0]]['song'])
        return recommended_songs
    else:
        return []  # Return an empty list if the song is not found in the DataFrame

recommended_songs = recommend("Just lose it")
print(recommended_songs)

fav_song = input("\n\nEnter your Favourite song\n"
                 "God help your spelling and availablity in the data set"
                 "\n>>")
recommend(fav_song)

