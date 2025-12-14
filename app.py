import streamlit as st
import pickle
import requests
import numpy as np


@st.cache_data
def load_api_data():
    return requests.get("https://thronesapi.com/api/v2/Characters").json()

api_data = load_api_data()


@st.cache_data
def load_data():
    with open("got_processed_data.pkl", "rb") as f:
        return pickle.load(f)

df = load_data()
df = df.head(25)


df['character'] = df['character'].str.replace('Jaime', 'Jamie')
df['character'] = df['character'].str.replace('Lord Varys', 'Varys')
df['character'] = df['character'].str.replace('Bronn', 'Lord Bronn')
df['character'] = df['character'].str.replace('Sandor Clegane', 'The Hound')
df['character'] = df['character'].str.replace('Robb Stark', 'Rob Stark')


def fetch_image(name, api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']
    return None


st.title(" Game of Thrones Personality Matcher")

characters = df['character'].values
selected_character = st.selectbox("Select a character", characters)

#CLOSE CHARACTER FIND KARKE
character_id = np.where(df['character'].values == selected_character)[0][0]
coords = df[['x', 'y']].values

distances = np.linalg.norm(coords - coords[character_id], axis=1)
recommended_id = np.argsort(distances)[1]
recommended_character = df['character'].values[recommended_id]

#IDHAR IMAGE AAYEGA
image_url = fetch_image(selected_character, api_data)
recommended_image_url = fetch_image(recommended_character, api_data)

#LAYOUT
col1, col2 = st.columns(2)

with col1:
    st.subheader(selected_character)
    if image_url:
        st.image(image_url)
    else:
        st.warning("Image not found")

with col2:
    st.subheader(recommended_character)
    if recommended_image_url:
        st.image(recommended_image_url)
    else:
        st.warning("Image not found")
