import streamlit as st
from bertopic import BERTopic
from nltk.tokenize import word_tokenize
from stopwords import STOP_WORDS

def preprocess(x):
  tokens = word_tokenize(x)
  no_stops = [word for word in tokens if word not in STOP_WORDS]
  x = " ".join(no_stops)
  return x

def plot_bertopic(reviews_df):
        topic_model = BERTopic(low_memory=True)
        topics, probs = topic_model.fit_transform(reviews_df["Review_Processed"])
        st.write(topic_model.get_topic_info())

        fig = topic_model.visualize_documents(reviews_df["Review"], topics)
        st.plotly_chart(fig)

        fig = topic_model.visualize_barchart()
        st.plotly_chart(fig)

        fig = topic_model.visualize_heatmap()
        st.plotly_chart(fig)