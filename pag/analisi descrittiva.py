import streamlit as st
import pandas as pd
import plotly.io as pio
from .func import Funz, GraficoInfrastruttura, GraficoRelazioni, GraficoFigure
from .descrizione import * #tutti i text1,text2...etc etc


def create_section(title, plot_function, explanation=None):
    """Create a section with a plot and optional explanation."""
    col_left, col_center, col_right = st.columns([1, 4, 1])
    with col_center:
        st.markdown(f"### {title}")
        plot_function()
        if explanation:
            st.markdown(explanation)
        st.markdown("<hr>", unsafe_allow_html=True)

def display_metrics(df):
    """Display key metrics about the dataset."""
    df_copy = df.copy() # Work on a copy

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

    # Add simplified maturity column to the copy
    df_copy['maturita_semplificata'] = df_copy['maturita_digitale'].apply(simplify_maturity)
    # Display metrics using the copy
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.metric("Numero totale aziende", len(df_copy)) # Use len(df_copy)
    with col4:
        # Ensure 'soddisfazione' is numeric on the copy for calculation
        df_copy['soddisfazione'] = pd.to_numeric(df_copy['soddisfazione'], errors='coerce')
        mean_satisfaction = df_copy['soddisfazione'].mean()
        st.metric("Media soddisfazione", f"{mean_satisfaction:.2f}" if pd.notna(mean_satisfaction) else "N/A")


def main():
    pio.templates.default = "plotly"    
    st.title('Analisi Descrittiva della Survey')
    DATASET_PATH = 'data/cleaned_data.xlsx' # Corrected path relative to app.py CWD
    df = None # Initialize df

    # Attempt to load data from session state first
    if 'data' in st.session_state and 'survey' in st.session_state['data']:
        df = st.session_state['data']['survey']
        # Check if data in session state is valid
        if df is None or df.empty:
             st.warning("Survey data in session state is empty or invalid. Attempting to reload from file.")
             df = None # Reset df to trigger file loading

    # If not loaded from session state or invalid, try loading from file
    if df is None:
        st.info(f"Attempting to load survey data from {DATASET_PATH}...")
        try:
            # Ensure the path exists before trying to read
            import os
            if not os.path.exists(DATASET_PATH):
                 raise FileNotFoundError(f"File not found at the specified path: {DATASET_PATH}")
            
            df = pd.read_excel(DATASET_PATH)
            
            # Basic validation after loading
            if df is None or df.empty:
                st.error(f"Loaded data from {DATASET_PATH} is empty or invalid.")
                return # Stop execution
                
            # Store successfully loaded data in session state
            if 'data' not in st.session_state:
                st.session_state['data'] = {}
            st.session_state['data']['survey'] = df
            st.success("Survey data loaded successfully from file and stored in session state.")
            
        except FileNotFoundError as fnf_error:
            st.error(f"Dataset file not found: {fnf_error}. Please ensure the file exists at '{DATASET_PATH}' relative to the main app script.")
            return # Stop execution
        except Exception as e:
            st.error(f"An unexpected error occurred during data loading from file: {e}")
            import traceback
            st.code(traceback.format_exc())
            return # Stop execution

    # Final check if df is valid before proceeding
    if df is None or df.empty:
        st.error("Failed to load or retrieve valid survey data. Cannot display plots for this page.")
        return # Stop execution if df is still invalid

    # Initialize function class only if df is valid
    funz = Funz()

    if 'selected_tab' not in st.session_state:
        st.session_state.selected_tab = "Analisi Descrittiva"
    if 'selected_subcategory' not in st.session_state:
        st.session_state.selected_subcategory = "Intervistato"

    subcategories = [
                    "Intervistato",
                    "Maturità Digitale",
                    "Figure con Competenze Digitali",
                    "Infrastrutture Digitali",
                    "Relazioni e Valore economico",
                    "Transizione Digitale",
                    "Soddisfazione e miglioramenti"
                    ]

    st.markdown("<h3 style='font-size: 36px; font-weight: bold;'>Seleziona una sottocategoria:</h3>", 
                unsafe_allow_html=True)

    # Subcategory selection
    selected_subcategory = st.radio(
                                    label=" ",
                                    options=subcategories,
                                    index=subcategories.index(st.session_state.get("selected_subcategory", subcategories[0])),
                                    key="subcategory_radio",
                                    help="Seleziona una sottocategoria per visualizzare i dati pertinenti."
                                    )

    if selected_subcategory != st.session_state.get("selected_subcategory"):
        st.session_state.selected_subcategory = selected_subcategory


###################################################  INTERVISTATO  #################################################
    if st.session_state.selected_subcategory == "Intervistato":
        st.markdown("### Analisi descrittiva - Intervistato")
    

        create_section(
                        title='Distribuzione Anni di Esperienza degli intervistati',
                        plot_function=lambda: funz.plot_fasce_anni(df),
                        explanation=text1,
                        )
        
        create_section(
                        title='Percentuale Intervistati con mansioni in ambito informatico',
                        plot_function=lambda: funz.plot_role_distribution(df),
                        explanation=text2,
                        )
        
        display_metrics(df) 
# OK
###################################################  Maturità Digitale  #################################################

    elif st.session_state.selected_subcategory == "Maturità Digitale":
        st.markdown("### Analisi descrittiva - Maturità Digitale")
        


        create_section(
                        title='Livello di maturità digitale presente in azienda',
                        plot_function=lambda: funz.analyze_digital_maturity(df),
                        explanation=text3
                        )
        
        create_section(
                        title='Fase del processo di trasformazione digitale',
                        plot_function=lambda: funz.analyze_fase_trans(df),
                        explanation=text4
                        )
        
        create_section(
                        title='Budget allocato per iniziative di trasformazione digitale (2023)',
                        plot_function=lambda: funz.analyze_budget_trans(df),
                        explanation=text5
                        )
                    
        display_metrics(df)

# OK
###################################################  Figure con Competenze Digitali  ######################################

    elif st.session_state.selected_subcategory == "Figure con Competenze Digitali":
        st.markdown("### Analisi descrittiva - Figure con Competenze Digitali")
        grafico_figure = GraficoFigure(df)
        
        create_section(
                        title='Strategie per attrarre e sviluppare personale con competenze digitali',
                        plot_function=lambda: funz.plot_strategie_talent(df),
                        explanation=text6
                        )
        
        create_section(
                        title='Presenza di figure con conoscenze digitali',
                        plot_function=lambda: grafico_figure.plot_cdh_conoscenze(),
                        explanation=text7
                    )
        
        create_section(
                        title='Presenza di figure con competenze tecniche',
                        plot_function=lambda: grafico_figure.plot_cdh_competenze_tecniche(),
                        explanation=text8
                        )
        
        create_section(
                        title='Presenza di figure con abilità analitiche e decisionali',
                        plot_function=lambda: grafico_figure.plot_cdh_abilita_analitiche(),
                        explanation=text9
                        )
        
        create_section(
                        title='Presenza di figure con capacità di innovazione',
                        plot_function=lambda: grafico_figure.plot_cdh_innovazione(),
                        explanation=text10
                        )
        
        create_section(
                        title='Formazione continua',
                        plot_function=lambda: grafico_figure.plot_cdh_formazione(),
                        explanation=text11
                        )
        
        display_metrics(df)
# OK
###################################################  Infrastrutture Digitali  #################################################

    elif st.session_state.selected_subcategory == "Infrastrutture Digitali":
        st.markdown("### Analisi descrittiva - Infrastrutture digitali")
        
        grafico_infr = GraficoInfrastruttura(df)
        
        create_section(
                        title='Presenza di risorse tecnologiche e strutture organizzative',
                        plot_function=lambda: funz.plot_infr(df),
                        explanation=text12
                        )
        
        create_section(
                        title='Hardware per elaborazione e archiviazione dati',
                        plot_function=lambda: grafico_infr.plot_hardware(),
                        explanation=text13
                        )
        
        create_section(
                        title='Software per elaborazione e gestione informazioni',
                        plot_function=lambda: grafico_infr.plot_software(),
                        explanation=text14
                        )
        
        create_section(
                        title='Servizi cloud',
                        plot_function=lambda: grafico_infr.plot_cloud(),
                        explanation=text15
                        )
        
        create_section(
                        title='Servizi per la sicurezza informatica',
                        plot_function=lambda: grafico_infr.plot_sicurezza(),
                        explanation=text16
                        )
        
        display_metrics(df)
# OK
###################################################  Relazioni e Valore economico  #################################################

    elif st.session_state.selected_subcategory == "Relazioni e Valore economico":
        st.markdown("### Analisi descrittiva - Relazioni e valore economico")
        
        grafico_rel = GraficoRelazioni(df)
        
        create_section(
                        title='Relazioni e creazione di valore attraverso tecnologie digitali',
                        plot_function=lambda: funz.plot_Rel(df),
                        explanation=text17
                        )
        
        create_section(
                        title='Interazioni tra risorse digitali',
                        plot_function=lambda: grafico_rel.plot_cdh_interazione(),
                        explanation=text18
                        )
        
        create_section(
                        title='Piattaforme digitali per la collaborazione',
                        plot_function=lambda: grafico_rel.plot_cdh_piattaforme(),
                        explanation=text19
                        )
        
        create_section(
                        title='Digitalizzazione dei processi aziendali',
                        plot_function=lambda: grafico_rel.plot_cdh_processi(),
                        explanation=text20
                        )
        
        display_metrics(df)
# OK
###################################################  Transizione Digitale  #################################################

    elif st.session_state.selected_subcategory == "Transizione Digitale":
        st.markdown("### Analisi descrittiva - Transizione Digitale")
        
        create_section(
                        title='Processo di Trasformazione Digitale',
                        plot_function=lambda: funz.plot_trans(df),
                        explanation=text21
                        )
        
        create_section(
                        title='Inizio della trasformazione digitale strutturata',
                        plot_function=lambda: funz.inizio_trans(df),
                        explanation=text22
                        )
        
        create_section(
                        title='Stimoli per la trasformazione digitale',
                        plot_function=lambda: funz.plot_stimoli_trans_funnel(df),
                        explanation=text23
                        )
        
        create_section(
                        title='Responsabilizzazione dei dipendenti',
                        plot_function=lambda: funz.plot_resp_dipendenti_funnel(df),
                        explanation=text24
                        )
        
        create_section(
                        title='Coinvolgimento dei leader aziendali',
                        plot_function=lambda: funz.plot_coinvolgimento_leader(df),
                        explanation=text25
                        )
        
        create_section(
                        title='Utilizzo delle risorse digitali nei processi',
                        plot_function=lambda: funz.plot_processi_digit(df),
                        explanation=text26
                        )
        
        # create_section(
        #     title='Criticità nel processo di trasformazione',
        #     # plot_function=lambda: funz.plot_criticita(df),
        #     explanation="Analisi delle criticità riscontrate"
        # )
        
        display_metrics(df)
# OK
###################################################  Soddisfazione e miglioramenti  #################################################

    elif st.session_state.selected_subcategory == "Soddisfazione e miglioramenti":
        st.markdown("### Analisi descrittiva - Soddisfazione e miglioramenti")
        
        create_section(
                        title='Soddisfazione del vertice aziendale',
                        plot_function=lambda: funz.analyze_soddisfazione(df),
                        explanation=text27
                        )
        
        create_section(
                        title='Impatto sulla efficienza aziendale',
                        plot_function=lambda: funz.analyze_impatto_efficienza(df),
                        explanation=text28
                        )
        
        create_section(
                        title='Miglioramenti apportati',
                        plot_function=lambda: funz.analyze_miglioramenti(df),
                        explanation=text29
                        )
        
        display_metrics(df)
# OK
###################################################################################################################################


if __name__ == "__main__":
    main()
