import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from .descrizione import text40


istruzioni = text40


def load_data(file_path):
    """
    Load and prepare the dataset
    """
    try:
        df = st.session_state.get('data', {}).get('spider')
        if df is None:
            df = pd.read_excel(file_path)
        df = df.fillna(0)
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def get_top_performers(df, categories, n=1):
    """
    Find top performing companies based on average score across categories
    """
    try:
        df_copy = df.copy()
        df_copy['score'] = df_copy[categories].mean(axis=1)
        top_performers = df_copy.nlargest(n, 'score')
        return top_performers
    except Exception as e:
        st.error(f"Error calculating top performers: {str(e)}")
        return None

def create_radar_chart(categories, values, labels, title):
    """
    Create a radar chart using Plotly
    """
    try:
        fig = go.Figure()
        colors = ['rgb(31, 119, 180)', 'rgb(255, 99, 71)', 
                 'rgb(60, 179, 113)', 'rgb(147, 112, 219)']
        
        for i, (value, label) in enumerate(zip(values, labels)):
            fig.add_trace(go.Scatterpolar(
                r=value + [value[0]],
                theta=categories + [categories[0]],
                name=label,
                line=dict(color=colors[i], width=2),
                fill='toself',
                fillcolor=colors[i],
                opacity=0.1
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )
            ),
            showlegend=True,
            title=dict(
                text=title,
                x=0.5,
                xanchor='center'
            ),
            height=600
        )
        return fig
    except Exception as e:
        st.error(f"Error creating radar chart: {str(e)}")
        return None

def create_difference_chart(categories, differences):
    """
    Create a bar chart showing differences from mean
    """
    try:
        fig_diff = go.Figure()
        fig_diff.add_trace(go.Bar(
            x=categories,
            y=differences,
            marker_color=['red' if x < 0 else 'green' for x in differences],
            text=[f"{x:.2f}" for x in differences],
            textposition='auto',
        ))
        
        fig_diff.update_layout(
            title="Differenze rispetto alla media del settore",
            yaxis_title="Differenza",
            showlegend=False,
            height=400
        )
        return fig_diff
    except Exception as e:
        st.error(f"Error creating difference chart: {str(e)}")
        return None

def calculate_weighted_average(comparison_df, weights=(1, 3, 3, 3, 1)):
    """
    Calcola la media pesata dei punteggi utilizzando i pesi specificati.
    
    Args:
        comparison_df (pandas.DataFrame): DataFrame contenente i dati di confronto
        weights (tuple): Pesi da applicare alle colonne in ordine di indici
        
    Returns:
        pandas.DataFrame: DataFrame originale con una colonna aggiuntiva per il punteggio finale pesato
    """
    try:
        # Verifica che il numero di pesi corrisponda al numero di colonne numeriche
        numeric_cols = comparison_df.select_dtypes(include=['number']).columns
        
        if len(weights) != len(numeric_cols):
            raise ValueError(f"Il numero di pesi ({len(weights)}) non corrisponde al numero di colonne numeriche ({len(numeric_cols)})")
        
        # Crea una copia del dataframe per non modificare l'originale
        result_df = comparison_df.copy()
        
        # Calcola la media pesata
        weighted_sum = 0
        weights_sum = sum(weights)
        
        for i, col in enumerate(numeric_cols):
            weighted_sum += comparison_df[col] * weights[i]
        
        result_df['Punteggio Finale'] = weighted_sum / weights_sum
        
        return result_df
    
    except Exception as e:
        print(f"Errore nel calcolo della media pesata: {str(e)}")
        return comparison_df


def display_detailed_data(labels,comparison_df, weights=(1, 3, 3, 3, 1)):
    """
    Display detailed comparison data with weighted average score
    """
    try:
        # Calcola il punteggio finale con media pesata
        result_df = calculate_weighted_average(comparison_df, weights)
        
        st.header("Dati di Confronto:")
        st.dataframe(result_df, hide_index=True)
        
        # Opzionalmente, evidenzia i punteggi finali
        st.subheader(f"{labels}:")
        score = result_df[['Punteggio Finale']].iloc[0,0].round(2)
        a, b = st.columns(2)

        a.metric(f"Punteggio pesato", score)

        
        
    except Exception as e:
        st.error(f"Error displaying detailed data: {str(e)}")

def display_difference_analysis(company_data, df, categories):
    """
    Display difference analysis section
    """
    try:
        st.header("Analisi delle Differenze")
        
        differences = [company_data[cat].iloc[0] - df[cat].mean() for cat in categories]
        
        fig_diff = create_difference_chart(categories, differences)
        if fig_diff:
            st.plotly_chart(fig_diff, use_container_width=True)
        
        st.subheader("Dettaglio numerico delle differenze")
        diff_from_mean = pd.DataFrame({
            'Categoria': categories,
            'Differenza dalla media': differences
        })
        st.dataframe(
            diff_from_mean.style.background_gradient(
                cmap='RdYlGn',
                subset=['Differenza dalla media']
            ),
            hide_index=True
        )
    except Exception as e:
        st.error(f"Error in difference analysis: {str(e)}")


def display_recommendations(recommendations, categories):
    """
    Display recommendations in an organized and visually appealing way
    """
    # st.write("Debug - Recommendations:", recommendations)
    # st.write("Debug - Categories for display:", categories)


    

    # Sort recommendations by priority
    sorted_cats = sorted(categories, 
                        key=lambda x: (recommendations[x]['priority'], 
                                     recommendations[x]['gap']))
    
    # Create three columns for different priority levels
    cols = st.columns(3)
    
    # Define status colors and headers
    status_sections = {
        'Da migliorare': {'color': 'red', 'description': 'Aree che richiedono interventi prioritari'},
        'Buono': {'color': 'orange', 'description': 'Aree con potenziale di miglioramento'},
        'Eccellente': {'color': 'green', 'description': 'Aree di eccellenza'}
    }
    
    # Group recommendations by status
    for idx, (status, info) in enumerate(status_sections.items()):
        with cols[idx]:
            st.subheader(status)
            st.caption(info['description'])
            for cat in sorted_cats:
                if recommendations[cat]['status'] == status:
                    with st.expander(f"{cat}"):
                        # Format gap text based on status
                        if status == 'Eccellente':
                            gap_text = f"🏆 Performance superiore alla media di {abs(recommendations[cat]['gap']):.1f} punti"
                        elif status == 'Buono':
                            gap_text = f"📈 Margine di miglioramento: {recommendations[cat]['gap']:.1f} punti"
                        else:
                            gap_text = f"⚠️ Gap da colmare: {recommendations[cat]['gap']:.1f} punti"
                        
                        st.markdown(f"### {gap_text}")
                        st.markdown("#### Piano d'azione consigliato:")
                        # Display the message, preserving formatting
                        message = recommendations[cat]['message']
                        if message != 'Analisi dettagliata non disponibile per questa categoria.':
                            # Split and format bullet points
                            for line in message.split('\n'):
                                line = line.strip()
                                if line:
                                    if line.startswith('•'):
                                        st.markdown(line)
                                    elif line.startswith('-'):
                                        st.markdown(f"&nbsp;&nbsp;{line}")
                                    else:
                                        st.markdown(line)
                        else:
                            st.warning(message)

def main():
    """
    Main application function
    """
    DATASET_PATH = '../data/spider.xlsx'
    
    # Load data
    df = load_data(DATASET_PATH)
    if df is None:
        return
    #####
    
    st.title("Sistema di Raccomandazioni per la Maturità Digitale")
    st.markdown(""" La self analysis è uno strumento visuale che permette di valutare la performance di un'organizzazione, di un progetto o di un'attività attraverso un'analisi strutturata. Ecco come interpretare e utilizzare efficacemente qualsiasi report di self analysis.
                """)
    categories = [col for col in df.columns if col != 'Azienda']
    
    # Sidebar selections
    st.sidebar.header("Seleziona Azienda e Confronto")
    selected_company = st.sidebar.selectbox(
        "Scegli l'azienda da analizzare",
        options=df['Azienda'].tolist()
    )
    comparison_type = st.sidebar.multiselect(
        "Scegli il tipo di confronto",
        options=["Media di tutte le aziende", "Azienda più virtuosa"],
        default=["Azienda più virtuosa"]
    )
    
    # Initialize data collections
    values = []
    labels = []
    comparison_df = pd.DataFrame()
    recommendations = None  # Inizializziamo recommendations a None
    
    # Add selected company data
    company_data = df[df['Azienda'] == selected_company]
    values.append([company_data[cat].iloc[0] for cat in categories])
    labels.append(selected_company)
    comparison_df = pd.concat([comparison_df, company_data[['Azienda'] + categories]])
    
    # Add sector average if selected
    if "Media di tutte le aziende" in comparison_type:
        mean_values = df[categories].mean().tolist()
        values.append(mean_values)
        labels.append("Media settore")
        mean_df = pd.DataFrame({
            'Azienda': ['Media settore'],
            **{cat: [round(df[cat].mean(), 2)] for cat in categories}
        })
        comparison_df = pd.concat([comparison_df, mean_df])
    
    # Add top performer if selected
    if "Azienda più virtuosa" in comparison_type:
        top_performer = get_top_performers(df, categories)
        if top_performer is not None:
            top_values = [top_performer[cat].iloc[0] for cat in categories]
            values.append(top_values)
            labels.append("Top performer")
            # Create anonymous top performer data
            anon_top_df = top_performer[['Azienda'] + categories].copy()
            anon_top_df['Azienda'] = 'Top performer'
            comparison_df = pd.concat([comparison_df, anon_top_df])
            
            # Generate recommendations but don't display them yet
            # recommendations = generate_recommendations(company_data, top_performer, categories)
    
    # Create and display radar chart
    fig = create_radar_chart(categories, values, labels, f"Confronto {selected_company}")
    if fig:
        st.plotly_chart(fig, use_container_width=True)
    
    # Display detailed data
    display_detailed_data(labels[0],comparison_df)
    
    # Display difference analysis if sector average is selected
    if "Media di tutte le aziende" in comparison_type:
        display_difference_analysis(company_data, df, categories)

    st.markdown(istruzioni)

    # # Display recommendations at the end if they were generated
    # # if recommendations:
    # display_recommendations(recommendations, categories)

if __name__ == "__main__":
    main()