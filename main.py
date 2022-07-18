import streamlit as st
import pandas as pd
import json
import requests
from pathlib import Path
st.title('Books Recommender System')

path = Path(__file__)
path = str(path.resolve().parents[0]) + "/data/filtered.csv"
a= list(pd.read_csv(path)["Book-Title"].unique())

option = st.selectbox(
    'Select a book',
    (a)
)
number = st.slider('How many recommendations do you want?', 0, 20, 5)


if st.button('Get Recommendations'):
    if option is not None:
        st.write('Recommendations:')
        option = json.dumps({"name": option ,
                             "n":number})
        res = requests.post(f"https://books-recommender-lucca.herokuapp.com/recomend_item", data= option)


        for n,book in enumerate(res.json().get("list")):
            st.write(f"{n+1} : {book}")

