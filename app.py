# deploy the model on the frontend
from flask import Flask, request, render_template
import pickle, os


from src.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


model_path = os.path.join(BASE_DIR, "models", "spam_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")


# Load Model and Vectorizer
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)


# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    is_spam = None   # ✅ initialize here

    if request.method == "POST":
        email_text = request.form["email"]

        cleaned_text = clean_text(email_text)
        vector = vectorizer.transform([cleaned_text])

        pred = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0][1]

        prediction = "Spam" if pred == 1 else "Ham (Not Spam)"
        probability = prob
        is_spam = True if pred == 1 else False

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        is_spam=is_spam
    )
if __name__ == "__main__":
    print("App started successfully")
    app.run()