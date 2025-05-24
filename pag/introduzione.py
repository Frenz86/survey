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

# Lo Stato della Trasformazione Digitale nelle Imprese del Territorio

## Sintesi dei risultati dell'Osservatorio sulla Maturità Digitale 2025

## Introduzione

L'**Osservatorio sulla Maturità Digitale 2025** nasce con l'obiettivo di comprendere lo stato di avanzamento dei processi di trasformazione digitale nelle imprese dell'area forlivese e di contribuire alla costruzione di un ecosistema digitale territoriale più consapevole, connesso e resiliente.

La realizzazione di questo lavoro è stata resa possibile grazie al sostegno della **Fondazione Cassa dei Risparmi di Forlì**.

## Obiettivi e Framework della Ricerca

L'**Osservatorio sulla Maturità Digitale** si è posto diversi obiettivi chiave:

1. **Valutare lo stato attuale di digitalizzazione delle imprese**: a che punto sono le aziende nel loro percorso di trasformazione digitale e quali livelli di maturità hanno raggiunto.
2. **Comprendere direzione e priorità**: dove è indirizzata la trasformazione digitale, quali processi vengono privilegiati e con quali obiettivi.
3. **Mappare i digital assets territoriali**: identificare e valutare le tre fondamenta su cui poggia qualsiasi trasformazione digitale efficace:
   - **Digital Talents** — le persone, con le competenze e le conoscenze necessarie per immaginare, gestire e consolidare il cambiamento digitale.
   - **Digital Infrastructure** — l'infrastruttura hardware e software, i dati, le piattaforme e gli strumenti tecnologici che abilitano l'operatività digitale.
   - **Digital Ecosystem** — l'insieme delle **relazioni con attori esterni**: scuole, enti di formazione, università e centri di ricerca, fornitori di tecnologie, istituzioni locali, sistema finanziario, incubatori, acceleratori e altri snodi dell'innovazione.
4. **Identificare difficoltà e barriere**: quali sono gli ostacoli che le imprese incontrano nel loro percorso di digitalizzazione e come possono essere superati.
5. **Analizzare risultati e impatti**: quali benefici concreti hanno ottenuto le aziende e come questi si riflettono sulle loro performance economico-finanziarie.
6. **Riconoscere modelli comportamentali**: identificare tipologie di approccio alla digitalizzazione e strategie di adozione ricorrenti tra le imprese.

L'Osservatorio intende promuovere il paradigma dei tre digital assets fondamentali, nella convinzione che senza la loro cura non sia possibile garantire **continuità, impatto e sostenibilità** ai processi di digitalizzazione.

## Sintesi dei risultati principali

Il rapporto si basa sull'analisi di **74 imprese** dell'area forlivese, prevalentemente operanti nei settori manifatturiero e dei servizi. I risultati rivelano un **tessuto imprenditoriale in movimento**, con il **93,8%** delle aziende che ha avviato percorsi di digitalizzazione, sebbene con livelli di maturità molto differenti.

Tra gli aspetti più significativi emersi:

* Un **approccio pragmatico e graduale**, con il **53,4%** delle imprese che investe **meno del 10%** del proprio budget in digitale;
* Una **focalizzazione sull'efficienza operativa e sulla riduzione dei costi**, più che sull'innovazione di modello o di prodotto;
* Una **discontinuità evidente** tra le infrastrutture adottate (hardware, sicurezza) e i processi effettivamente digitalizzati;
* Il ruolo cruciale della **leadership** e delle **competenze interne**, fattori determinanti nella qualità e coerenza del processo di trasformazione;
* Una **valorizzazione ancora insufficiente dei dati** come leva strategica;
* Solo il **15%** delle imprese può essere considerato **digitalmente maturo**.

L'analisi ha inoltre permesso di classificare le aziende in tre principali profili di maturità digitale:

* **Imprese digitalmente mature** (circa 15% del campione): caratterizzate da leadership fortemente coinvolta, investimenti bilanciati (5-10% del budget), approccio integrato alla digitalizzazione, equilibrio generazionale con un efficace mix di esperienza e innovazione, formazione continua strutturata, digitalizzazione a 360° di tutti i processi aziendali, orientamento al cliente e ai vantaggi competitivi, competenze elevate e bilanciate. Queste aziende mostrano performance finanziarie superiori, con un EBITDA/Vendite mediano che supera il 20%.
* **Imprese in fase di transizione** (circa 50% del campione): presentano "qualche progetto avviato" o investimenti tra il 5% e il 15% del budget, digitalizzazione selettiva di alcuni processi (prevalentemente amministrativi), gap significativi nell'integrazione dei sistemi e nelle competenze avanzate, approccio ancora prevalentemente tattico alla trasformazione digitale. La loro performance finanziaria è variabile, con EBITDA/Vendite che si attesta mediamente tra il 10% e il 20%.
* **Imprese digitalmente frammentate** (circa 35% del campione): mostrano una leadership distaccata dal processo di trasformazione, investimenti insufficienti (meno del 5% del budget), approccio frammentario con focus quasi esclusivamente su hardware e sicurezza di base, digitalizzazione limitata ai processi amministrativi, concentrazione sui costi come unico driver della trasformazione, competenze sbilanciate e processi decisionali basati più su impressioni che su dati. La loro performance finanziaria è instabile, con EBITDA/Vendite mediano sotto il 10%.

L'analisi dei dati ha inoltre rivelato cinque pattern emergenti che caratterizzano lo stato della trasformazione digitale nelle imprese del territorio:

1. **Pattern della Discrepanza Infrastrutturale**: Si registra un'alta adozione di hardware (82,2%) ma una bassa digitalizzazione effettiva dei processi (37%), evidenziando un divario tra investimenti in tecnologia e loro effettiva integrazione nei processi aziendali.
2. **Pattern dell'Accelerazione Pandemica**: Il 39,2% delle aziende ha iniziato il proprio percorso di digitalizzazione dal 2020 in poi, suggerendo un forte impatto della pandemia COVID-19 come catalizzatore della trasformazione digitale.
3. **Pattern dell'Efficienza Prioritaria**: Emerge una concentrazione della digitalizzazione nei processi amministrativi (44 risposte) e nella catena di approvvigionamento (34), con priorità all'efficienza operativa piuttosto che all'innovazione strategica.
4. **Pattern dell'Investimento Efficace**: I dati mostrano che anche investimenti moderati (5%-10% del budget) possono generare significativi miglioramenti dell'efficienza, suggerendo che non è tanto la quantità quanto la qualità dell'allocazione delle risorse a fare la differenza.
5. **Pattern della Maturità Settoriale**: Il settore dei servizi mostra performance superiori (EBITDA/Vendite medio del 18%) rispetto al manifatturiero (12%), evidenziando dinamiche di digitalizzazione specifiche per settore.

## Verso un ecosistema digitale territoriale

Per favorire e accelerare la transizione digitale, è possibile immaginare **diverse linee di azione**, su più livelli:

* **All'interno dell'impresa**: investire nella formazione continua, nella governance del digitale, nella digitalizzazione integrata dei processi e nella valorizzazione dei dati;
* **Tra imprese**: promuovere logiche collaborative di filiera, reti di condivisione e piattaforme comuni;
* **Tra imprese, territorio e componenti dell'ecosistema digitale**: costruire connessioni strutturate tra mondo produttivo, enti formativi, ricerca, tecnologia, istituzioni e finanza.

L'Osservatorio restituisce questa complessità attraverso una serie di sezioni dedicate all'analisi descrittiva dei dati, alla lettura per dimensioni chiave, all'approfondimento delle correlazioni, alle ricadute economico-finanziarie, alla self-analysis condotta dalle imprese stesse e alle conclusioni con raccomandazioni operative.

## Cosa troverai nell'applicazione

L'app dell'**Osservatorio sulla Maturità Digitale 2024** è pensata per offrire un'esperienza interattiva e dinamica, che consenta di **esplorare in profondità i risultati della ricerca** e di coglierne appieno il potenziale informativo e trasformativo.

All'interno troverai:

* Una **sintesi visuale** dei principali risultati emersi dalla ricerca;
* Le **analisi descrittive** aggregate sul livello di maturità digitale delle imprese del territorio;
* Le **analisi per dimensione** e tipologia aziendale (micro, piccole, medie imprese e per settore);
* L'esame delle **correlazioni** tra maturità digitale, performance economico-finanziarie e scelte gestionali;
* Un modulo dedicato alla **self-analysis**, dove ogni impresa può confrontarsi con il campione e riflettere sul proprio posizionamento digitale;
* Le **conclusioni** e un insieme di **raccomandazioni pratiche** e linee di azione utili per imprese, associazioni, enti territoriali e policy maker.


L'applicazione è uno strumento pensato per **ispirare, orientare e attivare**: uno spazio aperto per riflettere, ma anche per agire, condividere e costruire insieme un futuro digitale più solido, inclusivo e competitivo.


</div>
"""
        st.markdown(text, unsafe_allow_html=True)
###############################################

if __name__ == "__main__":
   main()