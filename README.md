# ⚔️ Game of Thrones Personality Matcher

An interactive **Streamlit web application** that matches **Game of Thrones characters** based on dialogue similarity using **Natural Language Processing (NLP)** and **dimensionality reduction (t-SNE)**.

🔗 **Live App:**  
https://game-of-thrones-personality-matcher-by-hp.streamlit.app/

---

## 📌 Overview

This project analyzes character dialogues from *Game of Thrones* and represents them as numerical embeddings using **Bag of Words**.  
Using **t-SNE**, characters are projected into a 2D space, where **Euclidean distance** is used to find the closest personality match.

The app allows users to:
- Select a character
- Find the most similar character
- View character images fetched via an external API

---

## 🧠 How It Works

1. **Dialogue Aggregation**
   - All dialogues are grouped character-wise
   - Total word count is calculated per character

2. **Text Vectorization**
   - Bag of Words using `CountVectorizer`
   - English stopwords removed

3. **Dimensionality Reduction**
   - High-dimensional vectors reduced to 2D using **t-SNE**

4. **Similarity Matching**
   - Euclidean distance used to find the closest character

5. **Deployment**
   - Final processed dataset serialized using `pickle`
   - Streamlit used for UI & interaction

---

## 📂 Dataset

- **Game of Thrones Dataset (Kaggle)**  
  https://www.kaggle.com/datasets/mathurinache/game-of-thrones-data

The dataset contains structured dialogue data used to build character profiles.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas & NumPy**
- **Scikit-learn**
- **t-SNE**
- **Streamlit**
- **Pickle**
- **Thrones API** (for character images)

---
## 📁 Project Structure

├── app.py

├── got_processed_data.pkl

├── requirements.txt

└── README.md

---
**✨ Author**

Harsh Pandey

**Connect with me on LinkedIn:** [Harsh Pandey](https://www.linkedin.com/in/harsh-pandey-891261354/)



