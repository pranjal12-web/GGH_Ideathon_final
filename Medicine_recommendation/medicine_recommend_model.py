
import pandas as pd
import numpy as np
import re
import pickle
import nltk
import webbrowser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS



from flask import Flask, request, jsonify,render_template

def recommend_medicines(user_reason, user_input):
    import warnings
    warnings.filterwarnings("ignore")

    # Import NLTK packages
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

    # Read your data using pd.read_csv
    df1= pd.read_csv("Company_Name.csv")
    df2= pd.read_csv("Medicine_description.csv")
    df2['Description'] = df2['Description'].str.lower()

    # Create a dictionary mapping letters to their corresponding values
    rating_mapping = {
    'S': 4.8,
    'R': 4.7,
    'D': 4.5,
    'C': 4.3,
    'B': 4.1,
    'AU': 3.9,
    'T': 3.5,
    'L': 3.4,
    'CA': 3.3,
    'ABB': 3.25,
    'AL': 3.2,
    'G': 3.1,
    'I': 3,
    'ALEM': 2.9,
    'GL': 2.7,
    'JB': 2.5
    }

# Replace the values in the 'rating' column using the mapping
    df1['Rating'] = df1['Rating'].replace(rating_mapping)
# columns_to_drop=['Industry']
    df1.drop(columns=['Industry','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8'], inplace=True)

    data = pd.concat([df1, df2], axis=1)

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    def preprocess_text(text):
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        lemmatized_words = [word for word in lemmatized_words if word not in string.punctuation]
        unique_lemmatized_words = list(set(lemmatized_words))
        return ' '.join(unique_lemmatized_words)

    data['preprocessed_Description'] = data['Description'].apply(preprocess_text)

    new_df = data[data['Reason'] == user_reason]
    new_df.reset_index(drop=True, inplace=True)


    user_words = word_tokenize(user_input)
    filtered_user_words = [word for word in user_words if word.lower() not in stop_words]

    lemmatized_user_words = [lemmatizer.lemmatize(word) for word in filtered_user_words]
    lemmatized_user_words = [word for word in lemmatized_user_words if word not in string.punctuation]
    unique_lemmatized_user_words = ' '.join(list(set(lemmatized_user_words)))

    vectorizer = CountVectorizer()
    user_keyword_vector = vectorizer.fit_transform([unique_lemmatized_user_words])

    cosine_similarity_scores = []

    for row_index in range(len(new_df)):
        keyword_vector = vectorizer.transform([new_df['preprocessed_Description'][row_index]])
        cosine_similarity_score = cosine_similarity(user_keyword_vector, keyword_vector)
        cosine_similarity_scores.append(cosine_similarity_score[0][0])

    cosine_similarity_df = pd.DataFrame({
        'Cosine Similarity': cosine_similarity_scores,
        'Description': new_df['Description'],
        'Drug_Name':new_df['Drug_Name'],
        'Rating':new_df['Rating'],
        'Reason':new_df['Reason']
    })

    cosine_similarity_df = cosine_similarity_df.sort_values(by='Cosine Similarity', ascending=False)

    top_3_similarities = cosine_similarity_df.head(3)
    top_3_similarities = top_3_similarities.sort_values(by='Rating', ascending=False)

    recommendations = []
    for index, row in top_3_similarities.iterrows():
        recommendations.append({
            'Medicine Name': row['Drug_Name'],
            'Description': row['Description']
        })

    return recommendations

pickle.dump(recommend_medicines,open("model.pkl","wb"))

app = Flask(__name__,template_folder='templates')
CORS(app)

print("hello")
# Load your trained model
with open('model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/recommend',  methods=['GET', 'POST'])
def recommend():
    try:
        user_reason = request.form.get('user_reason')
        user_input = request.form.get('user_input')

        recommendations = recommend_medicines(user_reason, user_input)
        
        return render_template('index.html', recommendations=recommendations)

    except Exception as e:
        return render_template('index.html', error=str(e))

# webbrowser.open("http://127.0.0.1:5000/")
app.run(host='127.0.0.1', port=5000, debug=True)
