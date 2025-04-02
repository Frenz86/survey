import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import unicodedata

#df = pd.read_excel('cleaned_data.xlsx')

class Key:
    def __init__(self, df):
        self.df = df

    def mappa_maturita(self):
        values = {
            'Siamo una azienda relativamente digitale; alcuni processi aziendali sono stati digitalizzati con l introduzione di tecnologie digitali': 'Relativamente digitale',
            'È stato avviato qualche progetto pilota di trasformazione digitale che al momento è ancora in corso': 'Qualche progetto avviato',
            'Siamo una azienda totalmente Digital Oriented; tutti i nostri processi sono supportati dall utilizzo di tecnologie digitali': 'Totalmente Digital Oriented',
            'Al momento non è in corso un processo di trasformazione digitale né è stato avviato e concluso in passato': 'Non digitalizzato',
            'È stato avviato qualche progetto pilota di trasformazione digitale che è stato interrotto e non portato a compimento': 'Qualche progetto interrotto'
        }
        
        # Normalizza le stringhe nella colonna 'maturita_digitale'
        self.df['maturita_digitale'] = self.df['maturita_digitale'].apply(lambda x: unicodedata.normalize('NFKD', x) if isinstance(x, str) else x)
        
    # Funzione per la creazione del grafico
    def hist_soddisfazione_maturita(self):
        # Assicurati che la funzione 'mappa_maturita' sia stata applicata in precedenza
        self.mappa_maturita()  # Applica la mappatura sulla maturità digitale
        pastel_colors = ['#FAD02E', '#F28D35', '#D83367', '#1F4068', '#5B84B1', '#6B4226']
        # Creiamo un istogramma per Soddisfazione e Maturità Digitale insieme
        fig = px.histogram(
                            self.df,  # DataFrame con le colonne 'soddisfazione' e 'maturita_digitale'
                            x="soddisfazione",  # Asse X per Soddisfazione
                            color="maturita_digitale",  # Colori per la maturità digitale
                            nbins=5,  # Numero di barre (puoi aggiustarlo se necessario)
                            title=" ",
                            labels={"soddisfazione": "Livello di Soddisfazione", "maturita_digitale": "Maturità Digitale"},
                            template="plotly_white",  # Tema bianco
                            histfunc="count",  # Calcola il numero di occorrenze
                            color_discrete_sequence=pastel_colors
                            )
        

        # Personalizzazione del layout
        fig.update_layout(
                            title={'text': ' ', 'x': 0.5},
                            xaxis=dict(
                                title="Livello di Soddisfazione",
                                title_font=dict(size=14, family='Arial', weight='bold')  # Titolo in grassetto
                            ),
                            yaxis=dict(
                                title="Numero di Aziende",
                                title_font=dict(size=14, family='Arial', weight='bold')  # Titolo in grassetto
                            ),
                            font=dict(size=14),
                            width=800,
                            height=600
                            )

        # Mostriamo il grafico in Streamlit
        st.plotly_chart(fig, use_container_width=True)


#################################################################################################### Maturità Digitale e Infrastrutture Digitali ####################################################################################################
    def visualizza_maturita_infrastrutture(self):
        """
        Visualizza la relazione tra maturità digitale e infrastrutture con un grafico a barre.
        Utilizza session_state per mantenere il grafico tra i cambi di pagina.
        """
        import streamlit as st
        import plotly.graph_objects as go
        import pandas as pd
        import numpy as np
        import traceback
        
        try:
            # Crea una copia del dataframe per evitare modifiche indesiderate
            df_temp = self.df.copy()
            
            # Lista delle infrastrutture
            infrastrutture = ['infr_hardware', 'infr_software', 'infr_cloud', 'infr_sicurezza']
            
            # Mappa le risposte manualmente
            mappa_risposte = {
                'Molto D\'accordo': 4,
                'D\'accordo': 3,
                'Neutrale': 2,
                'In disaccordo': 1,
                'Nessuna risposta': 0,
                np.nan: 0  
            }
            
            # Assicurati che tutte le colonne esistano
            for col in infrastrutture:
                if col not in df_temp.columns:
                    df_temp[col] = np.nan
            
            # Sostituisci e mappa i valori
            df_temp[infrastrutture] = df_temp[infrastrutture].replace('Nessuna risposta', np.nan)
            
            # Applica la mappatura a tutte le colonne delle infrastrutture
            for col in infrastrutture:
                df_temp[col] = df_temp[col].map(mappa_risposte)
                df_temp[col] = pd.to_numeric(df_temp[col], errors='coerce').fillna(0)
            
            # Rimuovi le righe non valide
            df_valid = df_temp.dropna(subset=['maturita_digitale'])
            df_valid = df_valid[df_valid['maturita_digitale'] != 'Nessuna risposta']
            
            # Se non ci sono dati validi, mostra un messaggio e termina
            if len(df_valid) == 0:
                st.warning("Non ci sono dati validi da visualizzare.")
                return

            # Definisci l'ordine delle categorie di maturità digitale
            ordine_maturita = [
                "Non digitalizzato",
                "Qualche progetto interrotto",
                "Qualche progetto avviato",
                "Relativamente digitale",
                "Totalmente Digital Oriented"
            ]
            
            # Verifica che i valori siano nell'elenco delle categorie
            valid_categories = [cat for cat in df_valid['maturita_digitale'].unique() if cat in ordine_maturita]
            
            if not valid_categories:
                st.warning("Nessuna categoria di maturità valida trovata nei dati.")
                return
            
            # Usa solo le categorie realmente presenti nei dati
            df_valid['maturita_digitale'] = pd.Categorical(
                df_valid['maturita_digitale'],
                categories=valid_categories,  # Usa solo categorie presenti
                ordered=True
            )

            # Calcola medie e conteggi
            medie = []
            for infr in infrastrutture:
                # Calcola media e conteggio
                try:
                    df_temp = df_valid.groupby('maturita_digitale').agg({
                        infr: 'mean',
                        'maturita_digitale': 'size'
                    }).rename(columns={'maturita_digitale': 'conteggio'})
                    
                    # Resetta l'index e prepara il dataframe
                    df_temp = df_temp.reset_index()
                    df_temp['infrastruttura'] = infr
                    medie.append(df_temp)
                except Exception as e:
                    st.error(f"Errore nel calcolo delle medie per {infr}: {str(e)}")
                    continue
            
            if not medie:
                st.warning("Non è stato possibile calcolare le medie. Verifica i dati.")
                return
                
            df_grouped = pd.concat(medie, ignore_index=True)

            # Crea il grafico
            fig = go.Figure()

            # Mappa nomi delle infrastrutture per la visualizzazione
            nomi_infrastrutture = {
                'infr_hardware': 'Hardware',
                'infr_software': 'Software',
                'infr_cloud': 'Cloud',
                'infr_sicurezza': 'Sicurezza'
            }

            # Definisci i colori fissi per ogni tipo di infrastruttura
            colori_infrastrutture = {
                'infr_hardware': '#FAD02E',    # Giallo
                'infr_software': '#F28D35',    # Arancione
                'infr_cloud': '#D83367',       # Rosso
                'infr_sicurezza': '#1F4068'    # Blu scuro
            }

            # Aggiungi le barre per ogni infrastruttura
            for infr in infrastrutture:
                df_infr = df_grouped[df_grouped['infrastruttura'] == infr]
                
                # Verifica che ci siano dati da visualizzare
                if df_infr.empty:
                    st.warning(f"Nessun dato disponibile per {nomi_infrastrutture[infr]}")
                    continue
                
                # Usa un hover template semplificato per evitare problemi
                fig.add_trace(go.Bar(
                    name=nomi_infrastrutture[infr],
                    x=df_infr['maturita_digitale'],
                    y=df_infr[infr],
                    marker_color=colori_infrastrutture[infr],
                    # Hover template semplificato
                    hovertemplate="%{x}: %{y:.2f}<br>Numero aziende: %{customdata}<extra></extra>",
                    customdata=df_infr['conteggio']
                ))

            # Aggiorna il layout
            fig.update_layout(
                title={
                    'text': '',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {'size': 20}
                },
                xaxis={
                    'title': 'Livello di Maturità Digitale',
                    'tickangle': -45,
                    'title_font': {'size': 16},
                    'tickfont': {'size': 12}
                },
                yaxis={
                    'title': 'Media Punteggio Infrastrutture',
                    'title_font': {'size': 16},
                    'tickfont': {'size': 12},
                    'range': [0, 5]
                },
                barmode='group',
                bargap=0.15,
                bargroupgap=0.1,
                height=600,  # Altezza esplicita
                showlegend=True,
                legend={
                    'title': 'Infrastrutture',
                    'font': {'size': 12},
                    'yanchor': 'top',
                    'y': 0.99,
                    'xanchor': 'right',
                    'x': 0.99
                },
                margin={'l': 60, 'r': 30, 't': 80, 'b': 150}
            )

            # Mostra il grafico
            st.plotly_chart(fig, use_container_width=True)
            
            # Aggiungi un pulsante per scaricare il grafico come immagine
            st.markdown("""
            <div style="text-align: center; margin-top: 10px;">
                <p>Se il grafico non è visibile, prova a ricaricare la pagina o verificare i dati.</p>
            </div>
            """, unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"Si è verificato un errore durante la visualizzazione: {str(e)}")
            st.code(traceback.format_exc())


#################################################################################################### Maturità Digitale e Relazioni Digitali ####################################################################################################

    def mappa_risposte1(self):
        mappa_risposte = {
            'Molto D\'accordo': 4,
            'D\'accordo': 3,
            'Neutrale': 2,
            'In disaccordo': 1,
            np.nan: 0  
        }
        
        # Replace 'Nessuna risposta' with NaN
        self.df[['cdh_conoscenze', 'cdh_competenze_tecniche', 'cdh_abilita_analitiche', 'cdh_innovazione', 'cdh_formazione']] = self.df[['cdh_conoscenze', 'cdh_competenze_tecniche', 'cdh_abilita_analitiche', 'cdh_innovazione', 'cdh_formazione']].replace('Nessuna risposta', np.nan)
        
        # Apply mapping to all specified columns
        for col in ['cdh_conoscenze', 'cdh_competenze_tecniche', 'cdh_abilita_analitiche', 'cdh_innovazione', 'cdh_formazione']:
            self.df[col] = self.df[col].map(mappa_risposte)

        # Convert columns to numeric type to avoid issues with mean calculation
        for col in ['cdh_conoscenze', 'cdh_competenze_tecniche', 'cdh_abilita_analitiche', 'cdh_innovazione', 'cdh_formazione']:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

    # Function to create the chart with color intensity based on company count
    def visualizza_maturita_figure(self):
        try:
            # Check if DataFrame is initialized and not empty
            if self.df is None or self.df.empty:
                st.error("No data available. Please load data first.")
                return
                
            titles_dict = {
                'cdh_conoscenze': "figure conoscenze digitali",
                'cdh_competenze_tecniche': "figure competenze tecniche",
                'cdh_abilita_analitiche': "figure abilità analitiche/decisionali",
                'cdh_innovazione': "figure capacità di innovazione",
                'cdh_formazione': "formazione continua"
            }
            
            # Create a deep copy of the DataFrame to avoid modifying the original
            df_viz = self.df.copy(deep=True)
            
            # Force conversion to numeric values for these columns
            columns = ['cdh_conoscenze', 'cdh_competenze_tecniche', 'cdh_abilita_analitiche', 'cdh_innovazione', 'cdh_formazione']
            
            # Direct mapping to numerical values without calling mappa_risposte1
            value_map = {
                'Molto D\'accordo': 4,
                'D\'accordo': 3,
                'Neutrale': 2,
                'In disaccordo': 1,
                'Nessuna risposta': 0,
                np.nan: 0
            }
            
            # Apply mapping and ensure numeric data type
            for col in columns:
                df_viz[col] = df_viz[col].map(value_map)
                df_viz[col] = pd.to_numeric(df_viz[col], errors='coerce').fillna(0)
                # Double-check it's really numeric
                df_viz[col] = df_viz[col].astype(float)

            # Remove rows where there are no valid answers for 'maturita_digitale'
            df_viz = df_viz.dropna(subset=['maturita_digitale'])

            # Filter to remove "Nessuna risposta" and "Non digitalizzato" from the 'maturita_digitale' column
            df_viz = df_viz[df_viz['maturita_digitale'] != 'Nessuna risposta']
            df_viz = df_viz[df_viz['maturita_digitale'] != 'Non digitalizzato']

            # Check if we still have data after filtering
            if df_viz.empty:
                st.warning("No valid data after filtering. Please check your dataset.")
                return

            # Calculate the count of responses for each level of digital maturity
            conteggi = df_viz['maturita_digitale'].value_counts().reset_index()
            conteggi.columns = ['maturita_digitale', 'conteggio']
            
            # Prepare data for plotting
            plot_data = []
            
            for col in columns:
                # Compute mean manually for each group to avoid dtype issues
                group_means = []
                for group in df_viz['maturita_digitale'].unique():
                    group_data = df_viz[df_viz['maturita_digitale'] == group]
                    mean_val = group_data[col].mean()
                    group_means.append({
                        'maturita_digitale': group,
                        col: mean_val,
                        'colonna': col
                    })
                
                # Convert to DataFrame
                media_col = pd.DataFrame(group_means)
                plot_data.append(media_col)

            # Combine all data
            if plot_data:
                df_grouped = pd.concat(plot_data, ignore_index=True)
                
                # Add counts to column means
                df_grouped = df_grouped.merge(conteggi, on='maturita_digitale', how='left')
                
                # Create layout with 1 subplot
                fig = go.Figure()
                
                # Add charts for each column
                for i, col in enumerate(columns):
                    df_col = df_grouped[df_grouped['colonna'] == col]
                    
                    if not df_col.empty:
                        fig.add_trace(
                            go.Bar(
                                x=df_col['maturita_digitale'],  # Digital Maturity on X axis
                                y=df_col[col],                  # Mean scores on Y axis
                                name=titles_dict[col],          # Use title from dictionary
                                marker=dict(
                                    color=df_col['conteggio'],  # Color intensity based on count
                                    colorscale=['#FAD02E', '#F28D35', '#D83367', '#1F4068', '#5B84B1'],  # Specified colors
                                    colorbar=dict(title="Conteggio Aziende")  # Color bar
                                ),
                                hovertemplate='Colonna: %{text}<br>Maturità Digitale: %{x}<br>Media Punteggi: %{y}<br>Conteggio Aziende: %{marker.color}',
                                text=titles_dict[col]  # Add title
                            )
                        )
                
                # Update layout with titles, labels and other customizations
                fig.update_layout(
                    height=600,
                    width=800,
                    title_text="  ",
                    showlegend=False,  # Remove legend
                    barmode='group',   # Graphs will be grouped for each level of digital maturity
                    xaxis_title="Maturità Digitale",
                    yaxis_title="Media Punteggi",
                    font=dict(size=12)
                )
                
                # Display the chart
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available to plot after processing.")
                
        except Exception as e:
            st.error(f"An error occurred in visualizza_maturita_figure: {str(e)}")
            import traceback
            st.code(traceback.format_exc())



#################################################################################################### Maturità Digitale e Data di transizione ####################################################################################################


    def mappa_maturita(self):
        values = {
            'Siamo un\'azienda relativamente digitale; alcuni processi aziendali sono stati digitalizzati con l\'introduzione di tecnologie digitali': 'Relativamente digitale',
            'È stato avviato qualche progetto pilota di trasformazione digitale che al momento è ancora in corso': 'Qualche progetto avviato',
            'Siamo un\'azienda totalmente Digital Oriented; tutti i nostri processi sono supportati dall\'utilizzo di tecnologie digitali': 'Totalmente Digital Oriented',
            'Al momento non è in corso un processo di trasformazione digitale né è stato avviato e concluso in passato': 'Non digitalizzato',
            'È stato avviato qualche progetto pilota di trasformazione digitale che è stato interrotto e non portato a compimento': 'Qualche progetto interrotto'
        }
        ordine_maturita = [
                            "Non digitalizzato",
                            "Qualche progetto interrotto",
                            "Qualche progetto avviato",
                            "Relativamente digitale",
                            "Totalmente Digital Oriented",
                            "Nessuna risposta",]
        if 'maturita_digitale' in self.df.columns:
            self.df['maturita_digitale'] = self.df['maturita_digitale'].replace(values)
            temp_col = self.df['maturita_digitale'].astype(str)
            # Sostituiamo 'nan' con 'Nessuna risposta'
            temp_col = temp_col.replace('nan', 'Nessuna risposta')
            # Creiamo la nuova colonna categorica
            self.df['maturita_digitale'] = pd.Categorical(
                                                            temp_col,
                                                            categories=ordine_maturita,
                                                            ordered=True
                                                            )
    def analizza_relazione_inizio_maturita_heatmap(self):
        """
        Crea una heatmap che mostra la relazione tra il livello di maturità digitale 
        e l'anno di inizio della digitalizzazione delle aziende.
        """
        # Mappa la maturità digitale
        self.mappa_maturita()
        
        # Verifica che le colonne esistano
        if 'inizio_trans' not in self.df.columns or 'maturita_digitale' not in self.df.columns:
            st.error("Le colonne 'inizio_trans' e 'maturita_digitale' non sono presenti nel dataset.")
            return

        # Sostituisci i valori NaN con "Nessuna risposta"
        self.df['inizio_trans'].fillna('Nessuna risposta', inplace=True)

        # Definiamo l'ordine delle categorie
        ordine_inizio_trans = [
            "Prima del 2015 ",
            "Tra il 2015 e il 2019 ",
            "Dal 2020 in poi ",
            "Nessuna risposta"
        ]
        
        ordine_maturita = [
            "Non digitalizzato",
            "Qualche progetto interrotto",
            "Qualche progetto avviato",
            "Relativamente digitale",
            "Totalmente Digital Oriented"
        ]
        
        # Creiamo la tabella di contingenza e sommiamo eventuali duplicati
        tabella_contingenza = (self.df.groupby(["inizio_trans", "maturita_digitale"])
                            .size()
                            .reset_index(name="conteggio"))
        
        # Assicuriamoci che non ci siano duplicati sommando i conteggi
        tabella_contingenza = (tabella_contingenza.groupby(["inizio_trans", "maturita_digitale"])
                            .sum()
                            .reset_index())

        # Ordiniamo le categorie
        tabella_contingenza["inizio_trans"] = pd.Categorical(
            tabella_contingenza["inizio_trans"], 
            categories=ordine_inizio_trans, 
            ordered=True
        )
        tabella_contingenza["maturita_digitale"] = pd.Categorical(
            tabella_contingenza["maturita_digitale"], 
            categories=ordine_maturita, 
            ordered=True
        )

        # Creiamo la matrice pivot per la heatmap
        matrice_heatmap = (tabella_contingenza.pivot_table(
            index="inizio_trans",
            columns="maturita_digitale",
            values="conteggio",
            aggfunc='sum'  # Explicitly specify sum aggregation
        ).reindex(
            index=ordine_inizio_trans,
            columns=ordine_maturita
        ).fillna(0))

        # Creiamo la heatmap
        fig = px.imshow(
            matrice_heatmap.values,
            labels=dict(
                x="Maturità Digitale",
                y="Anno di inizio digitalizzazione",
                color="Numero di Aziende"
            ),
            text_auto=True,
            x=ordine_maturita,
            y=ordine_inizio_trans,
            color_continuous_scale=['#FAD02E', '#F28D35', '#D83367', '#1F4068', '#5B84B1']
        )

        # Personalizziamo il layout
        fig.update_layout(
            xaxis=dict(
                title=dict(text='Maturità Digitale', font=dict(size=18, family='Arial', weight='bold')),
                tickfont=dict(size=14, family='Arial', weight='bold'),
                tickangle=45,
                showticklabels=True
            ),
            yaxis=dict(
                title=dict(text='Anno di inizio digitalizzazione', font=dict(size=18, family='Arial', weight='bold')),
                tickfont=dict(size=14, family='Arial', weight='bold'),
                showticklabels=True
            ),
            title={'text': '  ', 'x': 0.5},
            template='plotly_white',
            font=dict(size=14),
            width=1500,
            height=900,
            margin=dict(l=200, r=200, t=150, b=30)
        )

        # Mostriamo il grafico in Streamlit
        st.plotly_chart(fig, use_container_width=True)

#################################################################################################### MATURITA E LEADER ####################################################################################################
    def analizza_maturita_leader(self):
        """
        Crea una heatmap che mostra la relazione tra il livello di maturità digitale 
        e il coinvolgimento del leader nell'azienda.
        
        Args:
            df (pd.DataFrame): DataFrame contenente le colonne 'coinvolgimento_leader' e 'maturita_digitale'.
        """
        
        # Verifica che le colonne esistano
        if 'coinvolgimento_leader' not in self.df.columns or 'maturita_digitale' not in self.df.columns:
            st.error("Le colonne 'coinvolgimento_leader' e 'maturita_digitale' non sono presenti nel dataset.")
            return

        # Verifica e correggi i valori di 'coinvolgimento_leader'
        self.df['coinvolgimento_leader'] = pd.to_numeric(self.df['coinvolgimento_leader'], errors='coerce')  
        self.df['coinvolgimento_leader'] = self.df['coinvolgimento_leader'].fillna(0)  
        self.df['coinvolgimento_leader'] = self.df['coinvolgimento_leader'].apply(lambda x: x if 0 <= x <= 5 else 0)  
        
        # Definiamo l'ordine delle categorie numeriche
        ordine_coinvolgimento_leader = [0, 1, 2, 3, 4, 5]

        # Creiamo una mappatura per l'asse Y con frasi descrittive
        etichette_coinvolgimento = {
            0: "Non coinvolto",
            1: "Minimamente coinvolto",
            2: "Coinvolto moderatamente",
            3: "Coinvolto",
            4: "Molto coinvolto",
            5: "Completamente coinvolto"
        }

        ordine_maturita = [
            "Non digitalizzato",
            "Qualche progetto interrotto",
            "Qualche progetto avviato",
            "Relativamente digitale",
            "Totalmente Digital Oriented"
        ]
        
        # Creiamo la tabella di contingenza con aggregazione
        tabella_contingenza = (self.df.groupby(["coinvolgimento_leader", "maturita_digitale"])
                            .size()
                            .reset_index(name="conteggio"))
        
        # Aggiungi un controllo per verificare se la tabella di contingenza è corretta
        if tabella_contingenza.empty:
            st.warning("La tabella di contingenza è vuota. Verifica i dati di input.")
            return

        # Ordiniamo le categorie
        tabella_contingenza["coinvolgimento_leader"] = pd.Categorical(
            tabella_contingenza["coinvolgimento_leader"], 
            categories=ordine_coinvolgimento_leader, 
            ordered=True
        )
        tabella_contingenza["maturita_digitale"] = pd.Categorical(
            tabella_contingenza["maturita_digitale"], 
            categories=ordine_maturita, 
            ordered=True
        )

        # Creiamo la matrice pivot usando pivot_table per gestire i duplicati
        matrice_heatmap = (tabella_contingenza.pivot_table(
            index="coinvolgimento_leader",
            columns="maturita_digitale",
            values="conteggio",
            aggfunc='sum'
        )
        .reindex(index=ordine_coinvolgimento_leader, columns=ordine_maturita)
        .fillna(0))

        # Verifica la matrice heatmap
        if matrice_heatmap.isnull().values.any():
            st.warning("La matrice heatmap contiene valori nulli. Assicurati che i dati siano completi.")

        # Creiamo la heatmap con gli assi invertiti
        fig = px.imshow(
            matrice_heatmap.values,
            labels=dict(x="Maturità Digitale", y="Coinvolgimento del Leader", color="Numero di Aziende"),
            text_auto=True,
            x=ordine_maturita,
            y=[etichette_coinvolgimento[x] for x in ordine_coinvolgimento_leader],
            color_continuous_scale=['#FAD02E', '#F28D35', '#D83367', '#1F4068', '#5B84B1']
        )

        # Personalizziamo il layout
        fig.update_layout(
            xaxis=dict(
                title=dict(text='Maturità Digitale', font=dict(size=18, family='Arial', weight='bold'))
            ),
            yaxis=dict(
                title=dict(text='Coinvolgimento del Leader', font=dict(size=18, family='Arial', weight='bold'))
            ),
            title={'text': '  ', 'x': 0.5},
            template='plotly_white',
            font=dict(size=14),
            width=1500,
            height=900,
            margin=dict(l=200, r=200, t=150, b=30),
            coloraxis_colorbar=dict(title="Numero di Aziende")
        )

        # Mostriamo il grafico in Streamlit
        st.plotly_chart(fig, use_container_width=True)
