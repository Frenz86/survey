#df = pd.read_excel('cleaned_data.xlsx')
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import unicodedata
from typing import List, Dict

class Key:
    def __init__(self, df: pd.DataFrame):
        """Initialize the analyzer with a pandas DataFrame.
        
        Args:
            df (pd.DataFrame): Input DataFrame containing digital maturity data
        """
        self.df = df.copy()  # Create a copy to avoid modifying original data
        self.infrastructure_columns = ['infr_hardware', 'infr_software', 'infr_cloud', 'infr_sicurezza']
        self.maturity_order = [
            "Non digitalizzato",
            "Qualche progetto interrotto",
            "Qualche progetto avviato",
            "Relativamente digitale",
            "Totalmente Digital Oriented"
        ]
        
    def clean_maturity_data(self) -> None:
        """Clean and standardize the digital maturity column."""
        maturity_mapping = {
            'Siamo una azienda relativamente digitale; alcuni processi aziendali sono stati digitalizzati con l introduzione di tecnologie digitali': 'Relativamente digitale',
            'È stato avviato qualche progetto pilota di trasformazione digitale che al momento è ancora in corso': 'Qualche progetto avviato',
            'Siamo una azienda totalmente Digital Oriented; tutti i nostri processi sono supportati dall utilizzo di tecnologie digitali': 'Totalmente Digital Oriented',
            'Al momento non è in corso un processo di trasformazione digitale né è stato avviato e concluso in passato': 'Non digitalizzato',
            'È stato avviato qualche progetto pilota di trasformazione digitale che è stato interrotto e non portato a compimento': 'Qualche progetto interrotto'
        }
        
        # Normalize strings and apply mapping
        self.df['maturita_digitale'] = self.df['maturita_digitale'].apply(
            lambda x: unicodedata.normalize('NFKD', x) if isinstance(x, str) else x
        )
        self.df['maturita_digitale'] = self.df['maturita_digitale'].replace(maturity_mapping)
        self.df['maturita_digitale'].fillna('Nessuna risposta', inplace=True)
        
    def validate_data(self) -> Dict[str, List[str]]:
        """Validate data integrity and return any issues found.
        
        Returns:
            Dict[str, List[str]]: Dictionary containing validation issues by category
        """
        issues = {
            'infrastructure': [],
            'maturity': [],
            'missing_data': []
        }
        
        # Validate infrastructure columns
        for col in self.infrastructure_columns:
            if not self.df[col].between(0, 4).all():
                issues['infrastructure'].append(
                    f"{col} contains values outside expected range 0-4"
                )
            
        # Validate maturity categories
        invalid_categories = set(self.df['maturita_digitale'].unique()) - set(self.maturity_order)
        if invalid_categories:
            issues['maturity'].append(
                f"Found unexpected categories: {invalid_categories}"
            )
            
        # Check for missing data
        missing_data = self.df[self.infrastructure_columns + ['maturita_digitale']].isnull().sum()
        if missing_data.any():
            issues['missing_data'].extend(
                [f"{col}: {count} missing values" for col, count in missing_data.items() if count > 0]
            )
            
        return issues
        
    def prepare_infrastructure_data(self) -> None:
        """Prepare infrastructure data for analysis."""
        response_mapping = {
            'Molto D\'accordo': 4,
            'D\'accordo': 3,
            'Neutrale': 2,
            'In disaccordo': 1,
            np.nan: 0
        }
        
        for col in self.infrastructure_columns:
            # Replace 'Nessuna risposta' with np.nan first
            self.df[col] = self.df[col].replace('Nessuna risposta', np.nan)
            # Apply mapping and convert to numeric
            self.df[col] = (self.df[col]
                          .map(response_mapping)
                          .fillna(0)
                          .astype(float))
    
    def prepare_maturity_categories(self) -> None:
        """Prepare maturity categories for analysis."""
        # Remove rows with unexpected categories
        self.df = self.df[self.df['maturita_digitale'].isin(self.maturity_order)]
        
        # Convert to categorical with specified order
        self.df['maturita_digitale'] = pd.Categorical(
            self.df['maturita_digitale'],
            categories=self.maturity_order,
            ordered=True
        )
    
    def create_infrastructure_visualization(self) -> go.Figure:
        """Create the infrastructure visualization.
        
        Returns:
            go.Figure: Plotly figure object containing the visualization
        """
        # Prepare data for visualization
        medie = []
        for infr in self.infrastructure_columns:
            agg_data = (self.df.groupby('maturita_digitale', observed=True)
                       .agg({
                           infr: 'mean',
                           'maturita_digitale': 'size'
                       })
                       .reset_index(drop=False))
            agg_data['infrastruttura'] = infr
            medie.append(agg_data)
            
        df_grouped = pd.concat(medie, ignore_index=True)
        
        # Setup visualization parameters
        infrastructure_names = {
            'infr_hardware': 'Hardware',
            'infr_software': 'Software',
            'infr_cloud': 'Cloud',
            'infr_sicurezza': 'Sicurezza'
        }
        
        infrastructure_colors = {
            'infr_hardware': '#FAD02E',
            'infr_software': '#F28D35',
            'infr_cloud': '#D83367',
            'infr_sicurezza': '#1F4068'
        }
        
        # Create figure
        fig = go.Figure()
        
        # Add traces for each infrastructure type
        for infr in self.infrastructure_columns:
            df_infr = df_grouped[df_grouped['infrastruttura'] == infr]
            
            fig.add_trace(go.Bar(
                name=infrastructure_names[infr],
                x=df_infr['maturita_digitale'],
                y=df_infr[infr],
                marker_color=infrastructure_colors[infr],
                hovertemplate=(
                    f"<b>{infrastructure_names[infr]}</b><br>" +
                    "Maturità: %{x}<br>" +
                    "Media: %{y:.2f}<br>" +
                    "Numero aziende: %{customdata}<br>" +
                    "<extra></extra>"
                ),
                customdata=df_infr['maturita_digitale_size']
            ))
        
        # Update layout
        fig.update_layout(
            title={
                'text': 'Relazione tra Maturità Digitale e Infrastrutture',
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
            height=700,
            width=1200,
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
        
        return fig
    
    def visualize_maturity_infrastructure(self) -> None:
        """Main function to create and display the visualization."""
        # Prepare data
        self.clean_maturity_data()
        self.prepare_infrastructure_data()
        self.prepare_maturity_categories()
        
        # Validate data
        issues = self.validate_data()
        if any(issues.values()):
            for category, category_issues in issues.items():
                if category_issues:
                    st.warning(f"{category.title()} issues found:")
                    for issue in category_issues:
                        st.write(f"- {issue}")
        
        # Create and display visualization
        fig = self.create_infrastructure_visualization()
        st.plotly_chart(fig, use_container_width=True)



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
    def analizza_relazione_maturita_heatmap(self):
        """
        Crea una heatmap che mostra la relazione tra il livello di maturità digitale 
        e l'anno di inizio della digitalizzazione delle aziende.
        """
        # Verifica che le colonne esistano
        if 'inizio_trans' not in self.df.columns or 'maturita_digitale' not in self.df.columns:
            st.error("Le colonne 'inizio_trans' e 'maturita_digitale' non sono presenti nel dataset.")
            return

        # Definiamo l'ordine delle categorie
        ordine_inizio_trans = [
            "Prima del 2015 ",
            "Tra il 2015 e il 2019 ",
            "Dal 2020 in poi "
        ]
        
        ordine_maturita = [
            "Non digitalizzato",
            "Qualche progetto interrotto",
            "Qualche progetto avviato",
            "Relativamente digitale",
            "Totalmente Digital Oriented"
        ]
        
        # Creiamo la tabella di contingenza con aggregazione
        tabella_contingenza = (self.df.groupby(["inizio_trans", "maturita_digitale"])
                            .size()
                            .reset_index(name="conteggio"))
        
        # Aggiungi un controllo per verificare se la tabella di contingenza è corretta
        if tabella_contingenza.empty:
            st.warning("La tabella di contingenza è vuota. Verifica i dati di input.")
            return

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

        # Creiamo la matrice pivot usando pivot_table per gestire i duplicati
        matrice_heatmap = (tabella_contingenza.pivot_table(
            index="inizio_trans",
            columns="maturita_digitale",
            values="conteggio",
            aggfunc='sum'
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
            x=matrice_heatmap.columns,
            y=matrice_heatmap.index,
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
        st.plotly_chart(fig, use_container_width=True, key="heatmap_maturita_inizio")
###########################################################################################################################

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