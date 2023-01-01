import streamlit as st
import pandas as pd
import itertools
from pyabsa import ATEPCCheckpointManager

@st.cache
def load_model():
    return ATEPCCheckpointManager.get_aspect_extractor(checkpoint="multilingual", auto_device=False)

def predict_aspect_sentiment(model, examples):
    return model.extract_aspect(inference_source=examples, pred_sentiment=True)

def extract_aspect_sentiment(results):
    return [(result["aspect"], result["sentiment"]) for result in results]

def convert_to_df(results):
    return pd.DataFrame(results, columns=["Aspect", "Sentiment"])

def explode_df(df):
    return (df.apply(lambda x: list(itertools.zip_longest(x['Aspect'], x['Sentiment'])), axis=1)
       .explode()
       .apply(lambda x: pd.Series(x, index=['Aspect', 'Sentiment']))
       .groupby(level=0).ffill()
       .reset_index(drop=True))
    
def group_df(df):
    return df.groupby(["Aspect", "Sentiment"]).size().sort_values(ascending=False)