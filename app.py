import streamlit as st
from data_handle import books_name, recommend

st.title("📚 Book Recommendation System")

selected_book = st.selectbox(
    "Select a Book",
    books_name
)

if st.button("Show Recommendation"):

    recommended_books, posters = recommend(selected_book)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.caption(recommended_books[0])

    with col2:
        st.image(posters[1])
        st.caption(recommended_books[1])

    with col3:
        st.image(posters[2])
        st.caption(recommended_books[2])

    with col4:
        st.image(posters[3])
        st.caption(recommended_books[3])

    with col5:
        st.image(posters[4])
        st.caption(recommended_books[4])
