import streamlit as st

def main():
###############################################

   # Puoi usare le colonne di Streamlit per centrare contenuti
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Trasformazione Digitale: Dalla Tecnologia all'Ecosistema")
        st.image("./img/ecosistemi.jpg")
        text= """
      ## Rapporto Finale dell'Osservatorio sulla Maturità Digitale 2024  

      ### Prefazione
      Il presente rapporto è stato realizzato grazie al contributo essenziale della Fondazione Cassa dei
      Risparmi di Forlì, che ha reso possibile la ricerca e la messa a disposizione dei risultati all'intera
      comunità imprenditoriale e istituzionale del territorio. Attraverso questo sostegno, la Fondazione
      conferma il proprio impegno nel promuovere lo sviluppo economico e l'innovazione locale,
      contribuendo a costruire un ecosistema digitale territoriale più competitivo e resiliente.
      L'Osservatorio sulla Maturità Digitale rappresenta uno strumento strategico per comprendere lo
      stato attuale della trasformazione digitale e orientare azioni concrete per il futuro.

      # Indice

      1. **Executive Summary**
      2. **Metodologia e Campione**
      3. **Risultati dell'Analisi Descrittiva**
         - Maturità digitale e investimenti
         - Competenze e capitale umano
         - Infrastrutture e tecnologie
         - Processi di trasformazione
         - Impatti e soddisfazione
      4. **Risultati dell'Analisi Dimensionale**
         - Principali correlazioni identificate
         - Evoluzione temporale e contesto storico
      5. **Risultati dell'Analisi Economico-Finanziaria**
         - Correlazioni fondamentali
         - Stabilità e prevedibilità nei risultati
      6. **I Tre Livelli di Maturità Digitale**
         - Impresa Digitalmente Matura
         - Impresa in Fase di Transizione
         - Impresa Digitalmente Immatura
      7. **Pattern Emergenti dai Dati**
      8. **Conclusioni**
      9. **L'Approccio Ecosistemico come Chiave del Successo**
      10. **Raccomandazioni per le Imprese**
         - Breve periodo (0-12 mesi)
         - Medio periodo (1-3 anni)
         - Lungo periodo (3-5 anni)
      11. **Raccomandazioni per le Istituzioni**
         - Breve periodo (0-12 mesi)
         - Medio periodo (1-3 anni)
         - Lungo periodo (3-5 anni)
      12. **Considerazioni Finali**


## Executive Summary

L'Osservatorio sulla Maturità Digitale ha coinvolto 74 imprese, prevalentemente manifatturiere e di servizi dell'area forlivese, rivelando un tessuto imprenditoriale in evoluzione digitale, con il 93,8% delle aziende che dichiara di aver avviato un processo di trasformazione digitale. Con un indice medio di soddisfazione di 3,43 su 5, l'analisi evidenzia un approccio alla digitalizzazione ancora in fase di sviluppo, caratterizzato da elementi di complessità e alcune contraddizioni significative.

I principali risultati evidenziano che il 39,2% delle aziende ha iniziato il percorso di digitalizzazione solo dal 2020, probabilmente accelerato dalla pandemia COVID-19. La maggioranza adotta un approccio pragmatico e graduale, focalizzato principalmente sull'efficienza operativa e sulla riduzione dei costi, con investimenti contenuti: il 29,3% investe meno del 5% del budget, il 24,1% tra il 5% e il 10%, mentre solo il 5,1% destina più del 20% alle iniziative digitali.

Emerge un chiaro gap tra l'adozione di infrastrutture tecnologiche (hardware 82,2%, sicurezza informatica 79,4%) e la loro effettiva integrazione nei processi (digitalizzazione processi 37%, piattaforme collaborative 39,2%). La ricerca ha identificato tre livelli di maturità digitale:

* **Imprese digitalmente mature (circa 15% del campione)**: mostrano performance finanziarie superiori (EBITDA/Vendite mediano >20%)
* **Imprese in fase di transizione (circa 50% del campione)**: digitalizzazione ancora parziale, principalmente nei processi amministrativi
* **Imprese digitalmente immature (circa 35% del campione)**: approccio frammentario e investimenti minimi

La ricerca evidenzia come il successo della trasformazione digitale non dipenda esclusivamente dalle singole organizzazioni, ma dalla loro capacità di interagire efficacemente con un ecosistema complesso di attori interconnessi. Le organizzazioni che adottano un approccio ecosistemico alla trasformazione digitale mostrano maggiore capacità di ottimizzare investimenti, ridurre rischi e accelerare l'innovazione.

## Risultati dell'Analisi Descrittiva

### Maturità digitale e investimenti

* **Difficoltà autovalutativa**: La maggioranza delle aziende (74,3%) non risponde alla domanda sul livello di maturità digitale, riflettendo una sostanziale difficoltà nel comprendere e analizzare il complesso mondo della digital transformation. Questo fenomeno non è riconducibile a semplice reticenza strategica, ma evidenzia una più profonda incertezza nella comprensione dei paradigmi e delle implicazioni organizzative della trasformazione digitale. Le aziende sembrano mancare di parametri chiari e framework condivisi per autovalutare oggettivamente il proprio posizionamento nel percorso di digitalizzazione.
* **Approccio pragmatico**: Le aziende mostrano una significativa maggiore facilità nel riconoscere e descrivere azioni specifiche e progetti concreti rispetto a valutare uno stato complessivo di maturità digitale. Questo orientamento al "fare" piuttosto che al "pianificare strategicamente" riflette un approccio incrementale alla trasformazione, dove l'adozione di singole soluzioni tecnologiche prevale sulla definizione di una visione integrata. Tale comportamento potrebbe limitare la capacità di sfruttare appieno le sinergie tra diverse iniziative digitali.
         """
        st.markdown(text)
###############################################

if __name__ == "__main__":
   main()