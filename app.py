# deploy the model on the frontend
from flask import Flask, request, render_template
import pickle

from src.preprocess import clean_text

app = Flask(__name__)

# Load Model and Vectorizer
with open("models/spam_model.pkl","rb") as f:
    model = pickle.load(f)

with open("models/vectorizer.pkl","rb") as f:
    vectorizer = pickle.load(f)


# Routes
@app.route("/",methods=["GET","POST"])
def index():
    prediction = None
    probability = None
    
    if request.method =="POST":
        email_text = request.form["email"]

        cleaned_text = clean_text(email_text)
        vector = vectorizer.transform([cleaned_text])

        pred = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0][1]

        prediction = "Spam " if pred == 1 else "Ham (Not Spam)"
        probability = prob
    is_spam = True if pred == 1 else False
    return render_template(
        "index.html",
        prediction = prediction,
        probability = probability,
        is_spam = is_spam

    )

if __name__ == "__main__":
    app.run(debug=True)