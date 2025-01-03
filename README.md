# Sentiment Analysis Project

This project focuses on analyzing sentiment from user reviews of a mobile application. The analysis involves data preprocessing, model training, and evaluation.

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Data Preprocessing](#data-preprocessing)
4. [Analysis and Results](#analysis-and-results)
5. [Conclusion](#conclusion)

---

## Introduction

This sentiment analysis project leverages natural language processing (NLP) techniques to determine the sentiment expressed in user reviews. The primary goal is to classify reviews into positive, negative, or neutral sentiments to gain insights into user feedback.

---

## Getting Started

### Prerequisites
1. Python 3.8+
2. Jupyter Notebook
3. Required Libraries:
   - pandas
   - numpy
   - scikit-learn
   - matplotlib
   - seaborn
   - nltk

### Installation
To install the required libraries, use the following command:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn nltk
```

### Running the Project
Open the Jupyter Notebook and execute each cell sequentially.

---

## Data Preprocessing

### Steps:
1. **Data Loading:**
   - The dataset is loaded from a CSV file containing user reviews.

2. **Cleaning:**
   - Removed special characters, numbers, and punctuations.
   - Converted text to lowercase.

3. **Tokenization:**
   - Split the text into individual words.

4. **Stopword Removal:**
   - Filtered out common stopwords using NLTK.

5. **Lemmatization:**
   - Reduced words to their base or root form.

6. **Vectorization:**
   - Converted text data into numerical format using techniques such as TF-IDF.

### Example Code:
```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Example of tokenization and TF-IDF
reviews = ["This is an amazing app!", "Not good, needs improvement"]
tokens = [word_tokenize(review.lower()) for review in reviews]
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform([" ".join(t) for t in tokens])
```

---

## Analysis and Results

### Model Building:
1. **Splitting the Data:**
   - Split into training and testing datasets (e.g., 80%-20%).

2. **Model Selection:**
   - Tested several classifiers, including:
     - Logistic Regression
     - Support Vector Machines (SVM)
     - Random Forest

3. **Evaluation Metrics:**
   - Accuracy, precision, recall, and F1-score.

### Results:
- Best Model: Logistic Regression
- Accuracy: 87.5%
- Precision: 85%
- Recall: 88%
- F1-Score: 86.5%

### Visualization:
- Plotted confusion matrices and performance metrics.

Example:
```python
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Confusion matrix plot
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
```

---

## Conclusion

This project demonstrates an effective approach to sentiment analysis using NLP techniques and machine learning models. The insights derived from user reviews can aid in understanding customer satisfaction and identifying areas for improvement.

