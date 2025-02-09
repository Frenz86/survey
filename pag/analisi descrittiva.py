import streamlit as st
import pandas as pd
import plotly.io as pio
from .func import Funz, GraficoInfrastruttura, GraficoRelazioni, GraficoFigure

def main():
    # Set default plotly template
    pio.templates.default = "plotly"
    
    # Set page title
    st.title('Digital Transformation Dashboard')

    # Load data
    DATASET_PATH = '../data/cleaned_data.xlsx'
    try:
        df = st.session_state.get('data', {}).get('survey')
    except AttributeError:
        df = pd.read_excel(DATASET_PATH)

    # Initialize function class
    funz = Funz()

    # Initialize session state variables
    if 'selected_tab' not in st.session_state:
        st.session_state.selected_tab = "Analisi Descrittiva"
    if 'selected_subcategory' not in st.session_state:
        st.session_state.selected_subcategory = "Intervistato"

    # Define subcategories
    subcategories = [
                    "Intervistato",
                    "Maturità Digitale",
                    "Figure con Competenze Digitali",
                    "Infrastrutture Digitali",
                    "Relazioni e Valore economico",
                    "Transizione Digitale",
                    "Soddisfazione e miglioramenti"
                    ]
    # Main content
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

    # Update session state
    if selected_subcategory != st.session_state.get("selected_subcategory"):
        st.session_state.selected_subcategory = selected_subcategory

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

###################################################  INTERVISTATO  #################################################
    if st.session_state.selected_subcategory == "Intervistato":
        st.markdown("### Analisi descrittiva - Intervistato")
        
        create_section(
                        title='Distribuzione Anni di Esperienza degli intervistati',
                        plot_function=lambda: funz.plot_fasce_anni(df),
                        explanation='Questi dati suggeriscono una varietà di esperienze tra i partecipanti.'
                        )
        
        create_section(
                        title='Percentuale Intervistati con mansioni in ambito informatico',
                        plot_function=lambda: funz.plot_role_distribution(df),
                        explanation="""Il fatto che il 30% degli intervistati ricopra un ruolo informatico in azienda evidenzia che una parte significativa del personale 
                        è direttamente coinvolta nella gestione, implementazione e manutenzione delle tecnologie digitali."""
                        )
        
        display_metrics(df) 
# OK
###################################################  maturità digitale  #################################################

    elif st.session_state.selected_subcategory == "Maturità Digitale":
        st.markdown("### Analisi descrittiva - Maturità Digitale")
        
        create_section(
                        title='Livello di maturità digitale presente in azienda',
                        plot_function=lambda: funz.analyze_digital_maturity(df),
                        explanation="Analisi del livello di maturità digitale nelle aziende"
                        )
        
        create_section(
            title='Fase del processo di trasformazione digitale',
            plot_function=lambda: funz.analyze_fase_trans(df),
            explanation="Analisi della fase di trasformazione digitale"
        )
        
        create_section(
            title='Budget allocato per iniziative di trasformazione digitale (2023)',
            plot_function=lambda: funz.analyze_budget_trans(df),
            explanation="Analisi dell'allocazione del budget per la trasformazione digitale"
        )
        
        display_metrics(df)

    elif st.session_state.selected_subcategory == "Figure con Competenze Digitali":
        st.markdown("### Analisi descrittiva - Figure con Competenze Digitali")
        grafico_figure = GraficoFigure(df)
        
        create_section(
            title='Strategie per attrarre e sviluppare personale con competenze digitali',
            plot_function=lambda: funz.plot_strategie_talent(df),
            explanation="Analisi delle strategie di talent acquisition e development"
        )
        
        create_section(
            title='Presenza di figure con conoscenze digitali',
            plot_function=lambda: grafico_figure.plot_cdh_conoscenze(),
            explanation="""La maggior parte delle aziende riconosce la presenza di figure con competenze digitali, 
            con una discreta percentuale che afferma di avere risorse altamente qualificate."""
        )
        
        create_section(
            title='Presenza di figure con competenze tecniche',
            plot_function=lambda: grafico_figure.plot_cdh_competenze_tecniche(),
            explanation="""La maggior parte delle aziende è consapevole dell'importanza delle competenze tecniche 
            e ha fatto progressi nel dotarsi di figure adeguate."""
        )
        
        create_section(
            title='Presenza di figure con abilità analitiche e decisionali',
            plot_function=lambda: grafico_figure.plot_cdh_abilita_analitiche(),
            explanation="""Molte aziende stanno facendo progressi nel dotarsi di figure con competenze analitiche e decisionali,
            ma c'è ancora una parte significativa che non ha una visione chiara di queste competenze."""
        )
        
        create_section(
            title='Presenza di figure con capacità di innovazione',
            plot_function=lambda: grafico_figure.plot_cdh_innovazione(),
            explanation="""La presenza di figure con capacità di innovazione è variabile tra le aziende,
            con spazio per miglioramenti in molte organizzazioni."""
        )
        
        create_section(
            title='Formazione continua',
            plot_function=lambda: grafico_figure.plot_cdh_formazione(),
            explanation="""I dati mostrano una tendenza generalmente favorevole alla formazione continua,
            sebbene non emergano segnali di consenso unanime."""
        )
        
        display_metrics(df)

    elif st.session_state.selected_subcategory == "Infrastrutture Digitali":
        st.markdown("### Analisi descrittiva - Infrastrutture digitali")
        grafico_infr = GraficoInfrastruttura(df)
        
        create_section(
            title='Presenza di risorse tecnologiche e strutture organizzative',
            plot_function=lambda: funz.plot_infr(df),
            explanation="""Il 94% delle aziende conferma la presenza di infrastrutture necessarie 
            per gestire il flusso di informazioni digitali."""
        )
        
        create_section(
            title='Hardware per elaborazione e archiviazione dati',
            plot_function=lambda: grafico_infr.plot_hardware(),
            explanation="""La maggior parte delle aziende è ben equipaggiata con hardware per gestire i dati,
            ma il 16.4% di risposte mancanti evidenzia possibili lacune."""
        )
        
        create_section(
            title='Software per elaborazione e gestione informazioni',
            plot_function=lambda: grafico_infr.plot_software(),
            explanation="""La maggior parte delle aziende è dotata di software per la gestione digitale,
            con margini di miglioramento per alcune."""
        )
        
        create_section(
            title='Servizi cloud',
            plot_function=lambda: grafico_infr.plot_cloud(),
            explanation="""I servizi cloud mostrano una divisione tra aziende molto soddisfatte 
            e altre che mostrano incertezza o insoddisfazione."""
        )
        
        create_section(
            title='Servizi per la sicurezza informatica',
            plot_function=lambda: grafico_infr.plot_sicurezza(),
            explanation="""La sicurezza informatica è un punto di forza per molte aziende,
            ma resta spazio per miglioramenti in alcune organizzazioni."""
        )
        
        display_metrics(df)

    elif st.session_state.selected_subcategory == "Relazioni e Valore economico":
        st.markdown("### Analisi descrittiva - Relazioni e valore economico")
        grafico_rel = GraficoRelazioni(df)
        
        create_section(
            title='Relazioni e creazione di valore attraverso tecnologie digitali',
            plot_function=lambda: funz.plot_Rel(df),
            explanation="Analisi delle relazioni e della creazione di valore"
        )
        
        create_section(
            title='Interazioni tra risorse digitali',
            plot_function=lambda: grafico_rel.plot_cdh_interazione(),
            explanation="Analisi delle interazioni tra risorse digitali"
        )
        
        create_section(
            title='Piattaforme digitali per la collaborazione',
            plot_function=lambda: grafico_rel.plot_cdh_piattaforme(),
            explanation="Analisi delle piattaforme collaborative"
        )
        
        create_section(
            title='Digitalizzazione dei processi aziendali',
            plot_function=lambda: grafico_rel.plot_cdh_processi(),
            explanation="Analisi del livello di digitalizzazione dei processi"
        )
        
        display_metrics(df)

    elif st.session_state.selected_subcategory == "Transizione Digitale":
        st.markdown("### Analisi descrittiva - Transizione Digitale")
        
        create_section(
            title='Processo di Trasformazione Digitale',
            plot_function=lambda: funz.plot_trans(df),
            explanation="Analisi del processo di trasformazione digitale"
        )
        
        create_section(
            title='Inizio della trasformazione digitale strutturata',
            plot_function=lambda: funz.inizio_trans(df),
            explanation="Timeline dell'inizio della trasformazione digitale"
        )
        
        create_section(
            title='Stimoli per la trasformazione digitale',
            plot_function=lambda: funz.plot_stimoli_trans_funnel(df),
            explanation="Analisi degli stimoli che hanno portato alla trasformazione"
        )
        
        create_section(
            title='Responsabilizzazione dei dipendenti',
            plot_function=lambda: funz.plot_resp_dipendenti_funnel(df),
            explanation="Analisi del coinvolgimento dei dipendenti"
        )
        
        create_section(
            title='Coinvolgimento dei leader aziendali',
            plot_function=lambda: funz.plot_coinvolgimento_leader(df),
            explanation="Analisi del coinvolgimento della leadership"
        )
        
        create_section(
            title='Utilizzo delle risorse digitali nei processi',
            plot_function=lambda: funz.plot_processi_digit(df),
            explanation="Analisi dell'utilizzo delle risorse digitali"
        )
        
        create_section(
            title='Criticità nel processo di trasformazione',
            plot_function=lambda: funz.plot_criticita(df),
            explanation="Analisi delle criticità riscontrate"
        )
        
        display_metrics(df)

    elif st.session_state.selected_subcategory == "Soddisfazione e miglioramenti":
        st.markdown("### Analisi descrittiva - Soddisfazione e miglioramenti")
        
        create_section(
            title='Soddisfazione del vertice aziendale',
            plot_function=lambda: funz.analyze_soddisfazione(df),
            explanation="Analisi della soddisfazione della leadership"
        )
        
        create_section(
            title='Impatto sulla efficienza aziendale',
            plot_function=lambda: funz.analyze_impatto_efficienza(df),
            explanation="Analisi dell'impatto sulla efficienza"
        )
        
        create_section(
            title='Miglioramenti apportati',
            plot_function=lambda: funz.analyze_miglioramenti(df),
            explanation="Analisi dei miglioramenti conseguiti"
        )
        
        display_metrics(df)

if __name__ == "__main__":
    main()