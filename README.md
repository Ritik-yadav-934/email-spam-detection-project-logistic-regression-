# 📧 Email Spam Detection using Logistic Regression

A machine learning web application that classifies emails as **Spam** or **Ham (Not Spam)** using **Logistic Regression** and **TF-IDF vectorization**. The model is deployed using **Flask**, allowing users to input email text and get real-time predictions with confidence scores.

---

## 🚀 Features

* ✅ Spam vs Ham classification
* 📊 Probability (confidence) score display
* 🧠 Logistic Regression model
* 🔤 Text preprocessing (cleaning, stopword removal, etc.)
* ⚡ Real-time prediction via Flask web app
* 🎨 Simple and clean UI

---

## 🧠 How It Works

1. User inputs email text
2. Text is preprocessed using `clean_text()`
3. Converted to numerical features using **TF-IDF Vectorizer**
4. Passed into trained **Logistic Regression model**
5. Model predicts:

   * Spam / Ham
   * Probability score
6. Result displayed on UI

---

## 📂 Project Structure

```
EMAIL SPAM FILTERING/
│
├── data/
│   └── raw/
│       └── emails.csv
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── spam_analysis.ipynb
│
├── src/
│   └── preprocess.py
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/email-spam-detection-project-logistic-regression-.git
cd email-spam-detection-project-logistic-regression-
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Then open in browser:

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Inputs

### Spam Example

```
Congratulations! You have won a free lottery prize. Click now!
```

### Ham Example

```
Hey, let's meet tomorrow to discuss the project.
```


---

## 📊 Model Details

* Algorithm: **Logistic Regression**
* Feature Extraction: **TF-IDF Vectorizer**
* Problem Type: **Binary Classification**
* Output:

  * Class (Spam / Ham)
  * Probability Score

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas & NumPy 📊
* HTML/CSS 🎨

---

## 📈 Future Improvements

* 🔥 Deploy on cloud (Render / AWS)
* 📊 Add visualization dashboard
* 🧠 Try advanced models (Naive Bayes, SVM, Deep Learning)
* 📩 Support email attachments

---

## 🙌 Acknowledgements

* Scikit-learn documentation
* Open datasets from Kaggle

---

## 📬 Contact

**Ritik Yadav**
📧 [technosftritik04@gamil.com](mailto:technosftritik04@gamil.com)
🔗 GitHub: https://github.com/Ritikyadav8271

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
