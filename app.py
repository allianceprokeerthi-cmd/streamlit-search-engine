import streamlit as st
import requests
pip install python-dotenv

API_KEY = st.secrets["API_KEY"]
SEARCH_ENGINE_ID = st.secrets["SEARCH_ENGINE_ID"]

st.title("My Search Engine 🔎")

query = st.text_input("Search the web")

if st.button("Search") and query:

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data:
        for item in data["items"]:
            st.subheader(item["title"])
            st.write(item["snippet"])
            st.write(item["link"])
            st.write("---")
    else:
        st.write("No results found")
