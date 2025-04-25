import streamlit as st
import pandas as pd
import plotly.io as pio
from .func import Funz, GraficoInfrastruttura, GraficoRelazioni, GraficoFigure
from .descrizione import * #tutti i text1,text2...etc etc

st.markdown("""
            <style>
            .justified-text {
                text-align: justify;
            }
            </style>
            """, unsafe_allow_html=True)

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
        st.markdown("""
                    <div class="justified-text">
                    
                    * **Equilibrio tra esperienza e rinnovamento**: Il campione mostra una significativa presenza di figure senior con esperienza consolidata, bilanciata da un'importante componente di professionisti relativamente nuovi nel settore. Questa distribuzione polarizzata suggerisce un ricambio generazionale in corso nelle aziende intervistate, dove la saggezza acquisita in decenni di attività professionale si integra con approcci freschi e innovativi portati dalle nuove leve. La minore presenza di figure con esperienza intermedia accentua questo contrasto generazionale, creando un panorama professionale dove tradizione e innovazione possono dialogare direttamente.
                    * **Diffusione trasversale delle competenze digitali**: Sebbene la maggioranza degli intervistati non operi in ruoli strettamente informatici, la digitalizzazione emerge come tema di interesse comune che attraversa tutte le funzioni aziendali. La varietà dei profili IT rappresentati, dai ruoli tradizionali come CIO e IT Manager a quelli più recenti come Innovation Manager, riflette l'evoluzione della governance digitale nelle organizzazioni. La forte partecipazione di figure non-IT alla survey dimostra come la trasformazione digitale sia ormai percepita come responsabilità condivisa, superando i confini dipartimentali per diventare elemento culturale integrato nell'intera struttura aziendale.
                    </div>
                    """,unsafe_allow_html=True)    

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
        # st.markdown("""
        #             xxx       
        #             """,unsafe_allow_html=True)  

    elif st.session_state.selected_subcategory == "Maturità Digitale":
        st.markdown("### Analisi descrittiva - Maturità Digitale") 
        st.markdown("""
                    <div class="justified-text">

                    * **Difficoltà autovalutativa**: La maggioranza delle aziende (74,3%) non risponde alla domanda sul livello di maturità digitale, riflettendo una sostanziale difficoltà nel comprendere e analizzare il complesso mondo della digital transformation. Questo fenomeno non è riconducibile a semplice reticenza strategica, ma evidenzia una più profonda incertezza nella comprensione dei paradigmi e delle implicazioni organizzative della trasformazione digitale. Le aziende sembrano mancare di parametri chiari e framework condivisi per autovalutare oggettivamente il proprio posizionamento nel percorso di digitalizzazione.
                    * **Approccio pragmatico**: Le aziende mostrano una significativa maggiore facilità nel riconoscere e descrivere azioni specifiche e progetti concreti rispetto a valutare uno stato complessivo di maturità digitale. Questo orientamento al "fare" piuttosto che al "pianificare strategicamente" riflette un approccio incrementale alla trasformazione, dove l'adozione di singole soluzioni tecnologiche prevale sulla definizione di una visione integrata. Tale comportamento potrebbe limitare la capacità di sfruttare appieno le sinergie tra diverse iniziative digitali.
                    * **Investimenti contenuti**: La maggioranza delle aziende destina meno del 10% del budget complessivo alla digitalizzazione (29,3% investe meno del 5% e 24,1% tra il 5% e il 10%), evidenziando una possibile sottovalutazione della complessità e dell'impatto potenziale della trasformazione digitale. Questo livello di investimento, sebbene consenta l'implementazione di soluzioni tattiche, risulta generalmente insufficiente per una trasformazione strategica e sistemica dei modelli di business e dei processi operativi. È significativo che il 27,6% delle aziende non sia in grado di quantificare gli investimenti effettuati, suggerendo una carenza di governance finanziaria specifica per i progetti digitali.
                    </div>
                    """, unsafe_allow_html=True)


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
        st.markdown("""
                    <div class="justified-text">

                    * **Polarizzazione delle esperienze**: Il campione evidenzia una forte presenza sia di professionisti con esperienza consolidata (oltre 20 anni) che di figure relativamente nuove (0-5 anni), con una distribuzione bimodale che riflette la natura emergente della trasformazione digitale. Questa composizione non è interpretabile come un ricambio generazionale in atto, ma piuttosto come la necessità di incorporare competenze digitali specifiche non sempre disponibili nelle aziende consolidate. Tale polarizzazione crea potenzialmente un terreno fertile per la cross-fertilization di competenze: da un lato l'esperienza di settore e la conoscenza profonda dei processi aziendali, dall'altro la familiarità con le nuove tecnologie e l'apertura all'innovazione.
                    * **Fiducia nelle competenze tecniche**: Le aziende mostrano una discreta fiducia nelle competenze tecniche (72,9%) e digitali di base (70,2%) del proprio personale. Questa percezione positiva riguarda principalmente capacità operative e funzionali, come l'utilizzo di software gestionali, sistemi ERP, strumenti di collaborazione e automatizzazione di base. Tale fiducia, se confrontata con i limitati investimenti in formazione, suggerisce una possibile sovrastima delle competenze effettivamente presenti o una sottovalutazione di quelle necessarie per affrontare una trasformazione digitale completa.
                    * **Gap nelle competenze avanzate**: Si registra una significativa carenza percepita nelle capacità strategiche, analitiche (58,1% di valutazioni positive) e innovative (63,5% di valutazioni positive) necessarie per capitalizzare strategicamente sugli investimenti tecnologici. Queste competenze avanzate - che includono la capacità di analizzare grandi quantità di dati, identificare pattern significativi, sviluppare soluzioni innovative e tradurle in vantaggio competitivo - risultano essenziali per evolvere da un approccio tattico a uno strategico nella trasformazione digitale. La difficoltà nel reperire e sviluppare tali competenze rappresenta uno dei principali ostacoli alla piena maturità digitale.
                    * **Approcci tradizionali al talent management**: Le strategie per attrarre e sviluppare talenti digitali si basano principalmente su metodi tradizionali come formazione (33,3%) e reclutamento (30,3%), con un utilizzo significativamente minore di metodologie innovative come hackathon e conferenze tecnologiche (5,05%) o programmi di mentoring e coaching (9,09%). Colpisce l'assenza di approcci come innovation lab, digital academy interne, reverse mentoring o collaborazioni strutturate con università. Questa predominanza di metodi convenzionali potrebbe limitare la capacità delle aziende di attrarre profili altamente specializzati in un mercato del lavoro digitale sempre più competitivo.
                    </div>
                    """,unsafe_allow_html=True)  


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

        st.markdown("""
                    <div class="justified-text">

                    * **Paradosso delle infrastrutture**: L'analisi rivela un significativo divario tra l'adozione di hardware tangibile (82,2%) e l'effettiva integrazione di questi strumenti nei processi aziendali (digitalizzazione processi 37%). Le aziende sembrano aver investito adeguatamente in infrastrutture fisiche e dispositivi, creando così una base tecnologica, ma mostrano lacune considerevoli nell'implementazione di soluzioni software avanzate e nell'integrazione tra diversi sistemi. Questo paradosso riflette una tendenza a concentrarsi sugli aspetti più visibili e concreti della digitalizzazione (computer, server, dispositivi mobili) piuttosto che sulle componenti architetturali e applicative che generano effettivo valore di business. Tale squilibrio può generare una "valle dell'implementazione" dove gli investimenti tecnologici non producono i ritorni attesi perché non adeguatamente integrati nei flussi di lavoro e nei processi decisionali.
                    * **Priorità alla sicurezza**: Gli investimenti in sicurezza informatica (79,4%) emergono come area prioritaria nell'allocazione delle risorse tecnologiche, posizionandosi subito dopo l'hardware nelle preferenze di investimento. Questa focalizzazione riflette probabilmente la crescente consapevolezza dei rischi cyber, amplificata da fattori come l'aumento degli attacchi informatici, l'evoluzione normativa (GDPR, NIS2) e la maggiore attenzione mediatica verso incidenti di sicurezza. La sicurezza sembra essere percepita come un prerequisito abilitante, una condizione necessaria per procedere con altre iniziative digitali, evidenziando un approccio prudente che antepone la protezione degli asset esistenti all'innovazione.
                    * **Adozione limitata del cloud**: I servizi cloud mostrano livelli di adozione significativamente inferiori rispetto ad altre tecnologie, emergendo come una delle aree di maggiore ritardo. Questa limitazione rappresenta un potenziale freno all'innovazione, alla scalabilità e alla flessibilità operativa delle aziende. La minore propensione verso soluzioni cloud potrebbe essere attribuibile a vari fattori: preoccupazioni sulla sicurezza e sovranità dei dati, resistenza culturale al cambiamento dei modelli operativi, mancanza di competenze specifiche per la gestione di ambienti cloud ibridi o multi-cloud, e difficoltà nella valutazione dei costi effettivi (passaggio da CapEx a OpEx). Questo ritardo nell'adozione del cloud rischia di ostacolare l'accesso delle aziende a tecnologie avanzate come AI, analytics distribuiti e microservizi, che si basano prevalentemente su architetture cloud-native.        
                    </div>
                    """,unsafe_allow_html=True)        

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
        st.markdown("""
                    <div class="justified-text">

                    * **Adozione disomogenea e focalizzazione operativa**: I dati mostrano un'adozione significativa delle tecnologie digitali (73,8% crea valore attraverso strumenti digitali nelle relazioni esterne), ma con una netta preferenza per la digitalizzazione dei processi operativi (50% di consenso) rispetto all'integrazione strategica delle risorse digitali (solo 28,4%). Questa disparità riflette il "Pattern della Discrepanza Infrastrutturale" identificato nell'analisi, dove l'alta adozione di hardware (82,2%) non corrisponde a un'equivalente digitalizzazione dei processi (37%), evidenziando un approccio ancora prevalentemente tattico e orientato all'efficienza operativa piuttosto che all'innovazione strategica.
                    * **Ecosistema digitale in formazione**: L'analisi delle piattaforme collaborative rivela che il 39,2% delle aziende utilizza strumenti digitali per la collaborazione, un dato che, combinato con l'elevata percentuale di "nessuna risposta" (36,5%) su questo tema, suggerisce un ecosistema digitale territoriale ancora in fase di consolidamento. Questa situazione rispecchia il più ampio contesto rilevato dall'Osservatorio, in cui si evidenzia un tessuto imprenditoriale in movimento (93,8% ha avviato percorsi di digitalizzazione) ma con livelli di maturità molto differenziati e con significative opportunità di sviluppo nell'orchestrazione delle relazioni digitali inter-aziendali e nella valorizzazione dei dati come asset strategico.
                    </div>
                    """,unsafe_allow_html=True)         

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
        st.markdown("""
                    <div class="justified-text">
                    
                    * **Fenomeno recente**: La trasformazione digitale strutturata emerge dall'analisi come un fenomeno significativamente recente nel panorama aziendale esaminato. Ben il 39,2% delle aziende ha avviato questo percorso solo dal 2020 in poi, evidenziando un punto di svolta temporale chiaramente identificabile. Questo timing non appare casuale ma coincide con l'inizio della pandemia COVID-19, che ha rappresentato un potente catalizzatore esterno, trasformando la digitalizzazione da opzione strategica a necessità operativa per garantire la continuità aziendale. I dati suggeriscono un "effetto compressione" nella curva di adozione: processi che in condizioni normali avrebbero richiesto anni sono stati condensati in pochi mesi, generando un'accelerazione forzata che, seppur positiva nell'immediato, potrebbe aver portato a implementazioni tattiche più che a trasformazioni strategiche pianificate.
                    * **Priorità all'operatività**: L'analisi della distribuzione delle tecnologie digitali nei diversi processi aziendali evidenzia una netta prevalenza dell'applicazione in aree amministrative (44 risposte) e operative come supply chain (34) e sviluppo prodotto (38), piuttosto che in funzioni più strategiche o innovative. Questo orientamento prevalentemente operativo riflette un approccio alla digitalizzazione ancora focalizzato sull'efficientamento dei processi esistenti e sulla riduzione dei costi, piuttosto che sulla creazione di nuove proposte di valore o sulla trasformazione radicale dei modelli di business. Le aree con minor penetrazione digitale risultano essere quelle relative alla sicurezza e all'ambiente (14), suggerendo una limitata attenzione agli aspetti di sostenibilità e gestione dei rischi, potenzialmente critici nel medio-lungo periodo.
                    * **Stimoli interni**: I dati rivelano che la trasformazione digitale nelle aziende analizzate è guidata principalmente da fattori interni (39 risposte per la creazione di un senso condiviso di responsabilità) e relazionali diretti (29 risposte per la promozione di un senso collettivo di responsabilità), con un'influenza significativamente minore di stimoli istituzionali o concorrenziali. Tra le motivazioni esterne, le collaborazioni con università e istituti di ricerca (18,2%) emergono come le più rilevanti, mentre gli incentivi da associazioni e canali di ricerca (3%) risultano i meno impattanti. Questa prevalenza di driver interni può essere interpretata positivamente come indice di una trasformazione guidata da convinzione e visione aziendale, ma potrebbe anche segnalare un insufficiente orientamento al mercato e una limitata percezione delle pressioni competitive emergenti nel panorama digitale globale.
                    * **Coinvolgimento parziale della leadership**: L'analisi del livello di coinvolgimento della leadership nei processi di trasformazione digitale evidenzia un quadro complesso: mentre circa il 46% dei leader risulta fortemente o completamente coinvolto, emerge un significativo 21,6% di "Per niente coinvolto" e un altro 22% solo "Parzialmente coinvolto". Questo limitato engagement di numerosi leader aziendali costituisce probabilmente uno dei principali ostacoli al pieno successo delle iniziative di trasformazione. La mancanza di sponsorship al vertice si traduce spesso in insufficiente allocazione di risorse, scarsa prioritizzazione strategica e difficoltà nel gestire efficacemente il cambiamento organizzativo e culturale necessario. Il dato suggerisce anche una polarizzazione dell'impegno dirigenziale ("tutto o niente"), riflettendo la consapevolezza che la trasformazione digitale richiede un coinvolgimento sostanziale per produrre risultati significativi.
                    </div>
                    """,unsafe_allow_html=True)        

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
        st.markdown("""
                    <div class="justified-text">

                    * **Focus sull'efficienza**: L'analisi dei benefici percepiti dalle iniziative di trasformazione digitale evidenzia una netta prevalenza di risultati legati all'efficienza operativa e all'ottimizzazione dei costi. Tra i principali miglioramenti segnalati emergono la riduzione dei costi diretti e indiretti (27 risposte), la riduzione del personale (26 risposte) e il miglioramento della produzione per i clienti (18 risposte). Significativamente minori risultano invece i riferimenti a benefici legati alla crescita strategica, all'espansione di mercato o all'innovazione di prodotto e servizio. Questa distribuzione conferma l'approccio prevalentemente tattico alla digitalizzazione, orientato al miglioramento incrementale dell'esistente piuttosto che alla generazione di nuove opportunità di business. Tale orientamento, sebbene comprensibile nell'immediato per il suo ROI più facilmente quantificabile, rischia di limitare il potenziale trasformativo delle tecnologie digitali, posizionando le aziende in una traiettoria di ottimizzazione piuttosto che di reinvenzione.
                    * **Miglioramenti tangibili**: Le aziende riportano miglioramenti concreti e misurabili in diverse aree operative. I benefici più frequentemente citati riguardano la maggiore disponibilità di dati (26,4%), il miglioramento della qualità del lavoro (19,5%) e la riduzione degli errori (17,8%). Seguono l'aumento della sicurezza nei processi (13,2%) e la miglior gestione dei fattori di rischio (8,05%). È interessante notare come i benefici percepiti riflettano una progressione logica: dall'accesso ai dati (disponibilità) all'utilizzo operativo degli stessi (qualità e riduzione errori) fino a impieghi più avanzati (gestione rischi). Questa distribuzione suggerisce un percorso evolutivo nell'uso dei dati aziendali, che parte dalla semplice disponibilità per arrivare gradualmente a utilizzi più sofisticati e strategici. La prevalenza della disponibilità di dati come beneficio principale indica che molte aziende si trovano ancora nelle fasi iniziali di questo percorso, con significative opportunità di evoluzione verso utilizzi più avanzati e a maggior valore aggiunto.
                    * **Soddisfazione diffusa**: Un dato particolarmente significativo emerge dall'analisi del livello di soddisfazione dei vertici aziendali rispetto ai risultati delle iniziative digitali: nonostante le limitazioni e i gap evidenziati in altre sezioni dell'analisi, ben il 67,6% dei decision maker si dichiara soddisfatto (32,4%), molto soddisfatto (28,4%) o pienamente soddisfatto (6,76%) dei risultati ottenuti. Solo l'8,11% esprime insoddisfazione. Questo elevato livello di approvazione, apparentemente in contrasto con la limitata profondità delle trasformazioni implementate, può essere interpretato attraverso diverse chiavi di lettura: potrebbe riflettere aspettative iniziali contenute, un focus prevalente sui benefici a breve termine piuttosto che sul potenziale strategico, o una limitata consapevolezza delle possibilità offerte da approcci più avanzati alla trasformazione digitale. È interessante notare che la soddisfazione risulta trasversale anche rispetto al grado di coinvolgimento diretto della leadership, suggerendo che anche i dirigenti meno attivamente impegnati riconoscono comunque il valore dei risultati ottenuti.
                    </div>
                    """,unsafe_allow_html=True)

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
