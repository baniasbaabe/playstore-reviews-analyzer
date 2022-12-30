import streamlit as st
import pandas as pd
from pyabsa import ATEPCCheckpointManager

@st.cache
def load_model():
    return ATEPCCheckpointManager.get_aspect_extractor(checkpoint="multilingual", auto_device=False)

def predict_aspect_sentiment(model, examples):
    return model.extract_aspect(inference_source=examples, pred_sentiment=True)

def extract_aspect_sentiment(results):
    return [(result["aspect"], result["sentiment"]) for result in results]

def convert_to_df(results):
    pass