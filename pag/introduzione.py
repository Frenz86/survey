import streamlit as st

def main():
###############################################
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

         """
   st.markdown(text)


###############################################

if __name__ == "__main__":
   main()