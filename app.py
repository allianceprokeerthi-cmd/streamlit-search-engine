import streamlit as st
import requests

st.set_page_config(page_title="My Search Engine", page_icon="🔎")

st.title("My Search Engine 🔎")

query = st.text_input("Search the web")

if st.button("Search") and query:

    url = "https://api.duckduckgo.com/"

    params = {
        "q": query,
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    results_found = False

    # 🔹 Main abstract result
    if data.get("AbstractText"):
        st.subheader(data.get("Heading", "Result"))
        st.write(data["AbstractText"])
        if data.get("AbstractURL"):
            st.write(data["AbstractURL"])
        st.write("---")
        results_found = True

    # 🔹 Related topics (acts like search results)
    for topic in data.get("RelatedTopics", []):
        if "Text" in topic:
            st.subheader(topic["Text"])
            st.write(topic.get("FirstURL", ""))
            st.write("---")
            results_found = True

        elif "Topics" in topic:  # nested results
            for sub in topic["Topics"]:
                st.subheader(sub["Text"])
                st.write(sub.get("FirstURL", ""))
                st.write("---")
                results_found = True

    if not results_found:
        st.error("No results found")
        
