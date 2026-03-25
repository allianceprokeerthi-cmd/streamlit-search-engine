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
    }

    response = requests.get(url, params=params)
    data = response.json()

    results_found = False

    # ✅ Try Abstract (main answer)
    if data.get("AbstractText"):
        st.subheader(data.get("Heading", "Answer"))
        st.write(data["AbstractText"])
        st.write(data.get("AbstractURL", ""))
        st.write("---")
        results_found = True

    # ✅ Try Related Topics
    for topic in data.get("RelatedTopics", []):
        if isinstance(topic, dict):

            if "Text" in topic:
                st.subheader(topic["Text"])
                st.write(topic.get("FirstURL", ""))
                st.write("---")
                results_found = True

            # nested topics
            if "Topics" in topic:
                for sub in topic["Topics"]:
                    st.subheader(sub["Text"])
                    st.write(sub.get("FirstURL", ""))
                    st.write("---")
                    results_found = True

    # ❗ Fallback if nothing found
    if not results_found:
        st.warning("No instant results found 😕")
        st.markdown(f"[👉 Search on DuckDuckGo](https://duckduckgo.com/?q={query})")
