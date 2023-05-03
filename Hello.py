import streamlit as st
import nltk
nltk.download("punkt")

st.markdown("# Topic Modeling and Sentiment Analysis with Playstore Reviews")
st.sidebar.markdown("# Main page")
st.markdown("You can scrape app reviews from Playstore apply Topic Modeling with BERTopic + Aspect-based Sentiment Analysis.")