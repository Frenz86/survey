import streamlit as st

def main():
###############################################

   # Puoi usare le colonne di Streamlit per centrare contenuti
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Conclusione")
        text= """
L'Osservatorio sulla Maturità Digitale ha rivelato un tessuto imprenditoriale in chiara evoluzione digitale, ma con significative opportunità di miglioramento. La trasformazione digitale nelle imprese analizzate richiede un salto di qualità: dall'approccio tattico a quello strategico, dall'ottimizzazione all'innovazione, dalla tecnologia come strumento alla tecnologia come abilitatore di nuovi modelli di business.

Il percorso di maturazione digitale è iniziato per quasi tutte le aziende (93,8%), ma la vera sfida consiste ora nel passare dalla semplice adozione tecnologica a una trasformazione profonda dei processi e dei modelli di business. La ricerca ha evidenziato che anche investimenti relativamente contenuti (5-10% del budget) possono generare significativi miglioramenti, suggerendo che non è tanto la quantità di risorse investite quanto la loro allocazione strategica a fare la differenza.

Un elemento cruciale emerso dall'analisi è la necessità di bilanciare gli investimenti in tecnologia con lo sviluppo delle competenze necessarie per sfruttarla. Le aziende più mature mostrano non solo una maggiore adozione tecnologica, ma anche un approccio integrato che valorizza competenze analitiche, innovative e data-driven.

## L'approccio ecosistemico come chiave del successo

L'Osservatorio evidenzia come il successo della trasformazione digitale non dipenda esclusivamente dalle singole organizzazioni, ma dalla loro capacità di interagire efficacemente con un ecosistema complesso di attori interconnessi: fornitori di tecnologia, sistema formativo, centri di ricerca, istituzioni pubbliche, investitori, startup digitali, e altri.RiprovaClaude può commettere errori. Verifica sempre le risposte con attenzione.
"""
        st.markdown(text)






###############################################

if __name__ == "__main__":
   main()