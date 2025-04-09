import streamlit as st
import plotly.io as pio
import pandas as pd
from ..pag.key import Key
from .descrizione import * #tutti i text1,text2...etc etc

def create_section(title, function, df=None, explanation=None):
    """Create a section with a plot and optional explanation."""
    col_left, col_center, col_right = st.columns([1, 4, 1])
    with col_center:
        st.markdown(f"### {title}")
        if callable(function):
            function()
        if explanation:
            st.markdown(explanation)
        st.markdown("<hr>", unsafe_allow_html=True)

def main():
    # Set default plotly template
    pio.templates.default = "plotly"    
    st.title('Digital Transformation Dashboard')

    DATASET_PATH = '../data/cleaned_data.xlsx'
    try:
        df = st.session_state.get('data', {}).get('survey')
        if df is None:
            df = pd.read_excel(DATASET_PATH)
    except AttributeError:
        df = pd.read_excel(DATASET_PATH)
    
    def display_metrics(df):
        """Display key metrics about the dataset."""
        def simplify_maturity(x):
            if pd.isna(x):
                return "Non specificato"
            elif "totalmente Digital Oriented" in x:
                return "Totalmente Digital"
            elif "relativamente digitale" in x:
                return "Relativamente Digital"
            elif "progetto pilota" in x:
                return "Fase Pilota"
            else:
                return "Nessuna Trasformazione"
        
        # Add simplified maturity column
        df['maturita_semplificata'] = df['maturita_digitale'].apply(simplify_maturity)
        
        # Display metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            st.metric("Numero totale aziende", len(df))
        with col4:
            df['soddisfazione'] = pd.to_numeric(df['soddisfazione'], errors='coerce')
            st.metric("Media soddisfazione", f"{df['soddisfazione'].mean():.2f}")

    #st.dataframe(df)   
    chiave = Key(df)

    create_section(
                    title='Maturità Digitale e Soddisfazione',
                    function= lambda: chiave.hist_soddisfazione_maturita(),
                    explanation="""
                        - Aggiungo spiegazione
                    """
                    )
    
    create_section(
                    title='Maturità Digitale e Infrastrutture Digitali',
                    function= lambda: chiave.visualizza_maturita_infrastrutture(),
                    explanation="""
                        - Ogni livello di maturità digitale possiede un gruppo di barre.
                        - Ogni barra rappresenta l'average score delle infrastrutture (hardware, software, cloud, sicurezza)
                        - I colori aiutano a visualizzare immediatamente la densità delle aziende in ciascun gruppo.
                    """
                    )
    
    create_section(
                    title='Maturità Digitale e Presenza Figure Competenti',
                    function= lambda: chiave.visualizza_maturita_figure(),
                    explanation="""
                        - Aggiungo spiegazione
                    """
                    )
    
    create_section(
                    title='Periodo di Inizio Transizione Digitale e Maturità Digitale Raggiunta',
                    function=lambda: chiave.analizza_relazione_inizio_maturita_heatmap(),
                    explanation="""
                        - Aggiungo spiegazione
                    """
                    )
    
    create_section(
                    title='Grado di Coinvolgimento del Leader e Maturità Digitale Raggiunta',
                    function=lambda: chiave.analizza_maturita_leader(),
                    explanation="""
                        - Aggiungo spiegazione
                    """
                    )
    
    display_metrics(df)

if __name__ == "__main__":
    main()