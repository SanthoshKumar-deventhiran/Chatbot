from flask import Flask, request, jsonify, render_template
import json
import firebase_admin
from firebase_admin import credentials, firestore
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import tensorflow as tf  # Import TensorFlow

app = Flask(__name__)

# Load chatbot data from JSON file with utf-8 encoding
with open('chatbot.json', encoding='utf-8') as f:  # Ensure encoding is set to utf-8
    chatbot_data = json.load(f)

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")  # Update the path if needed
firebase_admin.initialize_app(cred)
db = firestore.client()

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess input
def preprocess_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return filtered_tokens

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    # Preprocess the input using NLTK
    processed_input = preprocess_input(user_input)

    # Implement simple matching logic
    response = "I'm sorry, I didn't understand that."  # Default response
    for item in chatbot_data:
        if any(token in item['Category'].lower() for token in processed_input):
            response = item['Response']
            break

    # Save the conversation to Firebase
    db.collection('conversations').add({
        'user_input': user_input,
        'response': response
    })

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
