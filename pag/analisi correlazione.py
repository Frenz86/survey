import streamlit as st
import plotly.io as pio
import pandas as pd
from .corr import Correlazione

def main():
    pio.templates.default = "plotly"    
    st.title('Digital Transformation Dashboard')
    DATASET_PATH = '../data/cleaned_data.xlsx'
    try:
        df = st.session_state.get('data', {}).get('survey')
    except AttributeError:
        df = pd.read_excel(DATASET_PATH)

    # Initialize function class
    corr = Correlazione(df)

    #####################################################################

















    #######################################################################

if __name__ == "__main__":
    main()