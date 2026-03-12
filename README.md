# 📚 Book Recommendation System

A **Machine Learning based Book Recommendation System** that suggests similar books based on user ratings.
This project uses **Collaborative Filtering** with the **K-Nearest Neighbors (KNN)** algorithm.

The application is built using **Python, Pandas, Scikit-learn, and Streamlit**.

---

## 🚀 Features

* 📖 Recommend similar books instantly
* 🧠 Uses **KNN Machine Learning algorithm**
* 👥 Filters active users for better recommendations
* ⭐ Uses real user ratings
* 🖼 Displays recommended books with their **posters**
* 🌐 Interactive web interface using **Streamlit**

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Scipy

---

## 📂 Project Structure

```
Book-Recommendation-System
│
├── app.py               # Streamlit user interface
├── data_handle.py       # Data processing and ML model
├── requirements.txt     # Project dependencies
├── README.md
├── .gitignore
│
├── BX-Books.csv
├── BX-Users.csv
└── BX-Book-Ratings.csv
```

---

## 📊 Dataset

This project uses the **Book-Crossing Dataset**.

Dataset files:

* `BX-Books.csv`
* `BX-Users.csv`
* `BX-Book-Ratings.csv`

Source:
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Mithun1805/Book-Recommendation-System.git
```

### 2️⃣ Navigate to the project folder

```
cd Book-Recommendation-System
```

### 3️⃣ Create virtual environment

```
python -m venv venv
```

### 4️⃣ Activate environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 5️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

The application will open in your browser.

---

## 📸 Application Preview

Select a book and the system will recommend **5 similar books with posters**.

---

## 🧠 Machine Learning Workflow

1. Data Cleaning
2. Merge Books and Ratings datasets
3. Filter active users
4. Create Pivot Table (User vs Book matrix)
5. Convert to Sparse Matrix
6. Train **KNN Model**
7. Find nearest neighbor books

---

## 📌 Example Recommendation

Input:

```
A Bend in the Road
```

Output:

```
The Notebook
The Rescue
Message in a Bottle
Nights in Rodanthe
True Believer
```

---

## 👨‍💻 Author

Mithun

GitHub:
https://github.com/Mithun1805

---

⭐ If you like this project, consider giving it a **star on GitHub**!
