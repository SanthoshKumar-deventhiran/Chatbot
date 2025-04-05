
# 🤖 Simple Chatbot using Flask + Firebase + NLTK

This is a lightweight chatbot web app built with **Flask** for the backend and **HTML/CSS/JS** for the frontend. It uses **NLTK** for basic NLP, stores conversations in **Firebase Firestore**, and provides responses from a predefined JSON file.

---

## 📁 Files Included

- `chatbot.py` – Main Flask backend script.
- `index.html` – Frontend chat interface.
- `chatbot.json` – Predefined categories and bot responses.

---

## 🔧 Requirements

- Python 3.7 or higher
- Firebase Project + Service Account Key
- Install Python packages:

```bash
pip install flask nltk firebase-admin
```

---

## 🚀 How to Run

1. Place your `serviceAccountKey.json` in the same folder.
2. Run the app:

```bash
python chatbot.py
```

3. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 How It Works

- User inputs a message.
- Input is tokenized and cleaned using **NLTK**.
- Tokens are matched against the `Category` fields in `chatbot.json`.
- A matching response is returned.
- The conversation is saved in **Firebase Firestore**.

---

## 📄 Example chatbot.json Format

```json
[
  {
    "Category": "Aadhaar center",
    "Response": "ID verification, biometric registration, government services."
  },
  {
    "Category": "Abbey",
    "Response": "monastery, religious community, historical site."
  }
]
```

---

## 📌 Notes

- Ensure NLTK resources are downloaded:
```python
nltk.download('punkt')
nltk.download('stopwords')
```
- You can add more categories/responses by editing `chatbot.json`.

---

## 📬 Author

Made with ❤️ by Santhosh Kumar D

---

## 📃 License

MIT License
```
