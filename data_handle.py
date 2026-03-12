import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Load datasets
books = pd.read_csv("BX-Books.csv", sep=";", on_bad_lines="skip", encoding="latin-1")
users = pd.read_csv("BX-Users.csv", sep=";", on_bad_lines="skip", encoding="latin-1")
ratings = pd.read_csv("BX-Book-Ratings.csv", sep=";", on_bad_lines="skip", encoding="latin-1")

books = books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-L']]

books.rename(columns={
    "Book-Title":"title",
    "Book-Author":"author",
    "Year-Of-Publication":"year",
    "Publisher":"publisher",
    "Image-URL-L":"img_url"
}, inplace=True)

ratings.rename(columns={
    "User-ID":"user_id",
    "Book-Rating":"rating"
}, inplace=True)

# Active users filter
x = ratings['user_id'].value_counts() > 200
y = x[x].index
ratings = ratings[ratings['user_id'].isin(y)]

ratings_with_books = ratings.merge(books, on="ISBN")

num_rating = ratings_with_books.groupby('title')['rating'].count().reset_index()
num_rating.rename(columns={'rating':'num_of_ratings'}, inplace=True)

final_rating = ratings_with_books.merge(num_rating, on='title')
final_rating = final_rating[final_rating['num_of_ratings'] >= 50]

final_rating.drop_duplicates(['user_id','title'], inplace=True)

# Pivot table
book_pivot = final_rating.pivot_table(columns='user_id', index='title', values='rating')
book_pivot.fillna(0, inplace=True)

# Model
book_sparse = csr_matrix(book_pivot)
model = NearestNeighbors(algorithm='brute')
model.fit(book_sparse)

books_name = book_pivot.index


def fetch_poster(book_titles):

    posters = []

    for title in book_titles:
        idx = np.where(final_rating['title'] == title)[0][0]
        posters.append(final_rating.iloc[idx]['img_url'])

    return posters


def recommend(book_name):

    book_id = np.where(book_pivot.index == book_name)[0][0]

    distance, suggestion = model.kneighbors(
        book_pivot.iloc[book_id,:].values.reshape(1,-1),
        n_neighbors=6
    )

    recommended_books = []

    for i in range(1, len(suggestion[0])):
        recommended_books.append(book_pivot.index[suggestion[0][i]])

    posters = fetch_poster(recommended_books)

    return recommended_books, posters
