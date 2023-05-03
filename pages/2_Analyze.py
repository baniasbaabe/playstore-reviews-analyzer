import streamlit as st
import pandas as pd
from topic_modeling import preprocess, plot_bertopic
from sentiment import load_model, extract_aspect_sentiment, predict_aspect_sentiment, convert_to_df, explode_df, group_df

st.markdown("# Analyze your Data")
        
if "data" not in st.session_state:
    st.write("You first have to scrape your Playstore Reviews.")
    
else:
    if st.button("Analyze via BerTOPIC"):
        st.session_state["data"]["Review_Processed"] = st.session_state["data"]["Review"].apply(lambda x: preprocess(x))
        plot_bertopic(st.session_state["data"])
    
    if st.button("Run Aspect-based Sentiment Analysis"):
        model = load_model()
        df_sentiment = pd.DataFrame()
        result = predict_aspect_sentiment(model, st.session_state["data"]["Review"].to_list())
        aspect_sentiment = extract_aspect_sentiment(result)
        df = convert_to_df(aspect_sentiment)
        df = explode_df(df)
        df = group_df(df)
        
        st.write(df)
    
    