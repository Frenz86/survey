import streamlit as st
import plotly.io as pio
import pandas as pd
from .corr import Correlazione
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
    pio.templates.default = "plotly"    
    st.title('Driver di Trasformazione')

    st.markdown("""
                <div style="text-align: justify;">

                L'obiettivo conoscitivo di questa sezione è di illustrare la correlazione tra diversi fattori:

                * **maturità digitale raggiunta dall'azienda e l'esperienza dell'intervistato**
                * **budget investito e il grado di soddisfazione del vertice aziendale**
                * **budget investito e le criticità riscontrate**
                * **budget investito e l'efficienza riscontrata**

                Di seguito tutte le correlazioni analizzate secondo le matrici di correlazioni lineari:

                * **Sinergia intergenerazionale come fattore di successo digitale**: Il grafico rivela una relazione complessa tra esperienza professionale e maturità digitale, suggerendo che il successo nella trasformazione digitale non dipende tanto dall'anzianità professionale quanto dalla capacità organizzativa di creare sinergie produttive tra diverse generazioni. L'esperienza consolidata contribuisce con conoscenza settoriale e visione strategica, mentre le competenze più recenti portano familiarità tecnologica e apertura al cambiamento. La diffusa cautela nell'autodichiarare elevati livelli di maturità digitale potrebbe riflettere una consapevolezza più sofisticata delle reali potenzialità della digitalizzazione, oltre a una certa incertezza su cosa costituisca effettivamente "maturità digitale" in un panorama tecnologico in continua evoluzione.
                * **Equilibrio tra investimento e allocazione efficace delle risorse**: Emerge una correlazione positiva tra budget investito in digitalizzazione e soddisfazione del vertice aziendale, ma questa relazione non è strettamente proporzionale. Anche investimenti moderati (5%-10%) generano livelli significativi di soddisfazione, suggerendo che l'efficacia nell'allocazione delle risorse può risultare più determinante dell'entità assoluta dell'investimento. La significativa percentuale di aziende che non specificano il budget investito riflette probabilmente una combinazione di fattori: difficoltà oggettive nel tracciare i costi della digitalizzazione distribuiti tra diversi centri di costo, possibili carenze nella governance finanziaria dedicata ai progetti digitali, e una comprensibile reticenza strategica nel condividere informazioni considerate sensibili per il posizionamento competitivo.
                * **Persistenza delle sfide implementative oltre la disponibilità di risorse**: L'analisi evidenzia come le aziende con budget limitato (inferiore al 5%) affrontino difficoltà più pervasive nell'intero spettro del processo trasformativo. Tuttavia, è particolarmente significativo osservare che le problematiche di implementazione persistono anche in presenza di investimenti più consistenti, suggerendo che la trasformazione digitale comporta sfide intrinseche che trascendono la mera disponibilità finanziaria: complessità nell'integrazione tecnologica con sistemi esistenti, necessità di gestire il cambiamento organizzativo e culturale, difficoltà nel reperire competenze specialistiche, e sfide nella gestione della complessità progettuale.
                * **Evoluzione degli obiettivi di digitalizzazione con l'aumentare degli investimenti**: Si osserva un'interessante progressione negli obiettivi perseguiti dalle aziende in base al livello di investimento. Le organizzazioni con investimenti minimi (meno del 5%) adottano principalmente strategie difensive orientate alla riduzione dei costi, specialmente quelli relativi al personale, suggerendo un approccio alla digitalizzazione come strumento di razionalizzazione. Al contrario, le aziende nella fascia intermedia di investimento (5%-10%) riportano un portfolio di benefici più bilanciato che abbraccia sia l'ottimizzazione interna sia il miglioramento delle relazioni con i clienti e l'incremento della marginalità, indicando un approccio più strategico e meno tattico alla trasformazione digitale.                </div>
                """,unsafe_allow_html=True)

    DATASET_PATH = '../data/cleaned_data.xlsx'
    try:
        df = st.session_state.get('data', {}).get('survey')
    except AttributeError:
        df = pd.read_excel(DATASET_PATH)

    # Initialize function class
    corr = Correlazione(df)

    #####################################################################
       
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
    create_section(     title='Correlazione tra la maturità digitale raggiunta dall\'azienda e l\'esperienza dell\'intervistato',
                        function= lambda: corr.heatmap_anni_maturita(),
                        explanation=text35
                        )
    create_section(     title='Correlazione tra il budget investito e il grado di soddisfazione del vertice aziendale',
                        function= lambda: corr.correlazione1_budget(),
                        explanation=text36
                        )
    create_section(     title='Correlazione tra il budget investito e le criticità riscontrate',
                        function= lambda: corr.plot_criticita_budget(),
                        explanation=text37
                        )
    create_section(     title='Correlazione tra il budget investito e l\'efficienza riscontrata',
                        function= lambda: corr.cor_budget_efficienza(),
                        explanation=text38
                        )
    display_metrics(df)
    #######################################################################

if __name__ == "__main__":
    main()