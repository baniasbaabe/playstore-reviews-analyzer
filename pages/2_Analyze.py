import streamlit as st
import pandas as pd
from topic_modeling import preprocess, plot_bertopic

st.markdown("# Analyze your Data")
        
if "data" not in st.session_state:
    st.write("You first have to scrape your Playstore Reviews.")
    
else:
    if st.button("Analyze via BerTOPIC"):
        st.session_state["data"]["Review_Processed"] = st.session_state["data"]["Review"].apply(lambda x: preprocess(x))
        plot_bertopic(st.session_state["data"])