import streamlit as st
import pycountry
import pandas as pd
from playstore_scrape import PlaystoreReview

st.markdown("# Get your Data")
st.markdown("First, you need to provide the URL for the app from Playstore.")
st.markdown("After that, a Python script will return the reviews.")
st.markdown("Small Limitation: To reduce the risk of the IP being blocked by Playstore, you can't scrape as many reviews as you want.")

st.sidebar.markdown("# Scrape 🕷️")

ALL_COUNTRIES_ALPHA_2 = [country.alpha_2.lower() for country in pycountry.countries]
DEFAULT_COUNTRY_INDEX_EN = ALL_COUNTRIES_ALPHA_2.index("en")
DEFAULT_COUNTRY_INDEX_US = ALL_COUNTRIES_ALPHA_2.index("us")


with st.form("info_form", clear_on_submit=False):
    st.write("Provide some information")
    input_url = st.text_input("URL")
    input_language = st.sidebar.selectbox("Language", ALL_COUNTRIES_ALPHA_2, index=DEFAULT_COUNTRY_INDEX_EN)
    input_location = st.sidebar.selectbox("Language", ALL_COUNTRIES_ALPHA_2, index=DEFAULT_COUNTRY_INDEX_US)
    input_count = st.number_input("# Reviews", min_value=50, max_value=200, step=5)
    input_stars = st.radio("How many stars", [1, 2, 3, 4, 5, "All"])
    submitted = st.form_submit_button("Submit")
    if submitted:
        if input_stars == "All":
            input_stars = None
        review = PlaystoreReview(input_url, input_language, input_location, input_count, input_stars)
        reviews = review.get_reviews()
        reviews = [r["content"] for r in reviews if r["content"]]
        df = pd.DataFrame(reviews, column=["Review"])

        st.session_state["data"] = df