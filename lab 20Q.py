from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love python programming",
    "Python is easy",
    "I love machine learning"
]

query = input("Enter query: ")

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

scores = (tfidf_matrix * query_vector.T).toarray()

print("Document Scores:")
print(scores)
