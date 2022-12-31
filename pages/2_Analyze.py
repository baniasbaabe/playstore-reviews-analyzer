import streamlit as st
from bertopic import BERTopic


st.markdown("# Get your Data")

def plot_bertopic(reviews_df):
    # try:
        topic_model = BERTopic(low_memory=True)
        topics, probs = topic_model.fit_transform(reviews_df["Review"])
        st.write(topic_model.get_topic_info())

        # topic_model.get_representative_docs()

        fig = topic_model.visualize_documents(reviews_df["Review"], topics)
        st.plotly_chart(fig)

        fig = topic_model.visualize_barchart()
        st.plotly_chart(fig)

        fig = topic_model.visualize_heatmap()
        st.plotly_chart(fig)
        
if "data" not in st.session_state:
    st.write("You first have to scrape your Playstore Reviews.")
    
else:
    plot_bertopic(st.session_state["data"])