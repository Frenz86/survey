import streamlit as st
import plotly.io as pio
import pandas as pd
from .key import Key
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
    st.title('Analisi Dimensionale')

    st.markdown("""
                <div style="text-align: justify;">

                * **Correlazione tra maturità digitale e soddisfazione aziendale**: Emerge una chiara tendenza che collega il livello di avanzamento nei progetti digitali con la soddisfazione complessiva dell'organizzazione. Le aziende che hanno implementato iniziative digitali riportano livelli di gratificazione superiori rispetto a quelle che non hanno intrapreso o hanno interrotto percorsi di digitalizzazione. Significativa è anche l'ampia presenza di aziende che non forniscono risposta sulla propria maturità digitale, suggerendo una diffusa difficoltà nel valutare oggettivamente il proprio posizionamento nel percorso di trasformazione.
                * **Ecosistema integrato come vero indicatore di maturità**: La vera maturità digitale si configura come un sistema olistico dove coesistono tre elementi fondamentali: l'integrazione efficace delle tecnologie in un'architettura unificata che supera i silos operativi, lo sviluppo mirato di competenze sia tecniche che trasversali, e l'allineamento strategico delle iniziative digitali con gli obiettivi di business. La maggior parte delle organizzazioni si trova ancora nelle fasi iniziali o intermedie di questo percorso, con un focus prevalentemente tattico su efficienza operativa e ottimizzazione dei costi, lasciando inesplorato il potenziale trasformativo più avanzato.
                * **Formazione continua più determinante delle competenze individuali**: Un paradosso interessante emerge dal confronto tra aziende con progetti interrotti e quelle con progetti avviati. Le prime, nonostante dispongano di figure professionali con competenze eccellenti nelle aree strategiche, falliscono nel sostenere le iniziative digitali a causa di carenze nei sistemi di formazione continua. Al contrario, le aziende con progetti attivi mostrano un profilo di competenze più moderato ma uniformemente distribuito, distinguendosi per un sistema di aggiornamento professionale più robusto che permette loro di adattarsi costantemente al cambiamento.
                * **Accelerazione post-pandemica della trasformazione digitale**: L'analisi temporale rivela una marcata concentrazione di iniziative digitali avviate dopo il 2020, evidenziando come la pandemia abbia agito da potente catalizzatore, trasformando la digitalizzazione da opzione strategica a necessità operativa. Questo "effetto compressione" ha condensato in pochi mesi processi che normalmente avrebbero richiesto anni, rappresentando uno dei più significativi cambiamenti nelle dinamiche di innovazione aziendale degli ultimi decenni.
                * **Leadership come facilitatore ma non condizione sufficiente**: La relazione tra coinvolgimento dirigenziale e maturità digitale rivela dinamiche complesse: se da un lato esiste una correlazione positiva tra leader attivamente impegnati e avanzamento dei progetti digitali, dall'altro emergono casi significativi di innovazione bottom-up in assenza di supporto dirigenziale. Inoltre, nessuna azienda ha raggiunto livelli avanzati di maturità digitale indipendentemente dal coinvolgimento dei leader, evidenziando come la trasformazione digitale richieda cambiamenti sistemici che vanno oltre il semplice impegno dirigenziale.
                </div>
                """,unsafe_allow_html=True)


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
                    explanation=text30
                    )
    
    create_section(
                    title='Maturità Digitale e Infrastrutture Digitali',
                    function= lambda: chiave.visualizza_maturita_infrastrutture(),
                    explanation=text31
                    )
    
    create_section(
                    title='Maturità Digitale e Presenza Figure Competenti',
                    function= lambda: chiave.visualizza_maturita_figure(),
                    explanation=text32
                    )
    
    create_section(
                    title='Periodo di Inizio Transizione Digitale e Maturità Digitale Raggiunta',
                    function=lambda: chiave.analizza_relazione_inizio_maturita_heatmap(),
                    explanation=text33
                    )
    
    create_section(
                    title='Grado di Coinvolgimento del Leader e Maturità Digitale Raggiunta',
                    function=lambda: chiave.analizza_maturita_leader(),
                    explanation=text34
                    )
    
    display_metrics(df)

if __name__ == "__main__":
    main()