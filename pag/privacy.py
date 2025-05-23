import streamlit as st

def main():
###############################################

   # Puoi usare le colonne di Streamlit per centrare contenuti
    # col1, col2, col3 = st.columns([1, 2, 1])
    # with col2:
    #     st.title("Trasformazione Digitale: Dalla Tecnologia all'Ecosistema")
    #     st.image("./img/ecosistemi.jpg")
        text= """
<div style="text-align: justify;">

# Informativa Privacy

## Chi siamo
Questo sito presenta i risultati di un'indagine sulla trasformazione digitale attraverso grafici e analisi statistiche dell'Univesrsità di Bologna

## Dati che mostriamo
- **Tutti i dati visualizzati sono aggregati e anonimi**
- Non è possibile identificare singole persone o aziende
- I dati sono presentati solo in forma statistica generale

## Dati che raccogliamo sui visitatori
**Non raccogliamo dati personali dei visitatori del sito.**

Nello specifico:
- Non usiamo cookie di tracciamento
- Non raccogliamo email, nomi o altre informazioni personali
- Non tracciamo il comportamento di navigazione

## Servizi tecnici
Il sito è ospitato su Streamlit Cloud. Questo servizio potrebbe registrare automaticamente:
- Indirizzo IP (per motivi tecnici di sicurezza)
- Data e ora di accesso
- Pagine visitate

Questi dati sono gestiti secondo le policy del provider di hosting e non sono accessibili a noi.

## I tuoi diritti
Poiché non raccogliamo dati personali sui visitatori, non ci sono dati da modificare o cancellare. Se hai domande sui dati dell'indagine visualizzati (che sono anonimi), puoi contattarci.

## Contatti
Per domande su questa informativa: riccardo.silvi@unibo.it

## Aggiornamenti
Questa informativa può essere aggiornata. La data dell'ultimo aggiornamento è: 23-05-2025

---

</div>
"""
        st.markdown(text, unsafe_allow_html=True)

###############################################

if __name__ == "__main__":
   main()