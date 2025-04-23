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
Il presente rapporto è stato realizzato grazie al contributo essenziale della Fondazione Cassa dei Risparmi di Forlì, che ha reso possibile la ricerca e la messa a disposizione dei risultati all'intera
comunità imprenditoriale e istituzionale del territorio. Attraverso questo sostegno, la Fondazione conferma il proprio impegno nel promuovere lo sviluppo economico e l'innovazione locale, contribuendo a costruire un ecosistema digitale territoriale più competitivo e resiliente.
L'Osservatorio sulla Maturità Digitale rappresenta uno strumento strategico per comprendere lo stato attuale della trasformazione digitale e orientare azioni concrete per il futuro.

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
* **Investimenti contenuti**: La maggioranza delle aziende destina meno del 10% del budget complessivo alla digitalizzazione (29,3% investe meno del 5% e 24,1% tra il 5% e il 10%), evidenziando una possibile sottovalutazione della complessità e dell'impatto potenziale della trasformazione digitale. Questo livello di investimento, sebbene consenta l'implementazione di soluzioni tattiche, risulta generalmente insufficiente per una trasformazione strategica e sistemica dei modelli di business e dei processi operativi. È significativo che il 27,6% delle aziende non sia in grado di quantificare gli investimenti effettuati, suggerendo una carenza di governance finanziaria specifica per i progetti digitali.

### Competenze e capitale umano

* **Polarizzazione delle esperienze**: Il campione evidenzia una forte presenza sia di professionisti con esperienza consolidata (oltre 20 anni) che di figure relativamente nuove (0-5 anni), con una distribuzione bimodale che riflette la natura emergente della trasformazione digitale. Questa composizione non è interpretabile come un ricambio generazionale in atto, ma piuttosto come la necessità di incorporare competenze digitali specifiche non sempre disponibili nelle aziende consolidate. Tale polarizzazione crea potenzialmente un terreno fertile per la cross-fertilization di competenze: da un lato l'esperienza di settore e la conoscenza profonda dei processi aziendali, dall'altro la familiarità con le nuove tecnologie e l'apertura all'innovazione.
* **Fiducia nelle competenze tecniche**: Le aziende mostrano una discreta fiducia nelle competenze tecniche (72,9%) e digitali di base (70,2%) del proprio personale. Questa percezione positiva riguarda principalmente capacità operative e funzionali, come l'utilizzo di software gestionali, sistemi ERP, strumenti di collaborazione e automatizzazione di base. Tale fiducia, se confrontata con i limitati investimenti in formazione, suggerisce una possibile sovrastima delle competenze effettivamente presenti o una sottovalutazione di quelle necessarie per affrontare una trasformazione digitale completa.
* **Gap nelle competenze avanzate**: Si registra una significativa carenza percepita nelle capacità strategiche, analitiche (58,1% di valutazioni positive) e innovative (63,5% di valutazioni positive) necessarie per capitalizzare strategicamente sugli investimenti tecnologici. Queste competenze avanzate - che includono la capacità di analizzare grandi quantità di dati, identificare pattern significativi, sviluppare soluzioni innovative e tradurle in vantaggio competitivo - risultano essenziali per evolvere da un approccio tattico a uno strategico nella trasformazione digitale. La difficoltà nel reperire e sviluppare tali competenze rappresenta uno dei principali ostacoli alla piena maturità digitale.
* **Approcci tradizionali al talent management**: Le strategie per attrarre e sviluppare talenti digitali si basano principalmente su metodi tradizionali come formazione (33,3%) e reclutamento (30,3%), con un utilizzo significativamente minore di metodologie innovative come hackathon e conferenze tecnologiche (5,05%) o programmi di mentoring e coaching (9,09%). Colpisce l'assenza di approcci come innovation lab, digital academy interne, reverse mentoring o collaborazioni strutturate con università. Questa predominanza di metodi convenzionali potrebbe limitare la capacità delle aziende di attrarre profili altamente specializzati in un mercato del lavoro digitale sempre più competitivo.

### Infrastrutture e tecnologie

* **Paradosso delle infrastrutture**: L'analisi rivela un significativo divario tra l'adozione di hardware tangibile (82,2%) e l'effettiva integrazione di questi strumenti nei processi aziendali (digitalizzazione processi 37%). Le aziende sembrano aver investito adeguatamente in infrastrutture fisiche e dispositivi, creando così una base tecnologica, ma mostrano lacune considerevoli nell'implementazione di soluzioni software avanzate e nell'integrazione tra diversi sistemi. Questo paradosso riflette una tendenza a concentrarsi sugli aspetti più visibili e concreti della digitalizzazione (computer, server, dispositivi mobili) piuttosto che sulle componenti architetturali e applicative che generano effettivo valore di business. Tale squilibrio può generare una "valle dell'implementazione" dove gli investimenti tecnologici non producono i ritorni attesi perché non adeguatamente integrati nei flussi di lavoro e nei processi decisionali.
* **Priorità alla sicurezza**: Gli investimenti in sicurezza informatica (79,4%) emergono come area prioritaria nell'allocazione delle risorse tecnologiche, posizionandosi subito dopo l'hardware nelle preferenze di investimento. Questa focalizzazione riflette probabilmente la crescente consapevolezza dei rischi cyber, amplificata da fattori come l'aumento degli attacchi informatici, l'evoluzione normativa (GDPR, NIS2) e la maggiore attenzione mediatica verso incidenti di sicurezza. La sicurezza sembra essere percepita come un prerequisito abilitante, una condizione necessaria per procedere con altre iniziative digitali, evidenziando un approccio prudente che antepone la protezione degli asset esistenti all'innovazione.
* **Adozione limitata del cloud**: I servizi cloud mostrano livelli di adozione significativamente inferiori rispetto ad altre tecnologie, emergendo come una delle aree di maggiore ritardo. Questa limitazione rappresenta un potenziale freno all'innovazione, alla scalabilità e alla flessibilità operativa delle aziende. La minore propensione verso soluzioni cloud potrebbe essere attribuibile a vari fattori: preoccupazioni sulla sicurezza e sovranità dei dati, resistenza culturale al cambiamento dei modelli operativi, mancanza di competenze specifiche per la gestione di ambienti cloud ibridi o multi-cloud, e difficoltà nella valutazione dei costi effettivi (passaggio da CapEx a OpEx). Questo ritardo nell'adozione del cloud rischia di ostacolare l'accesso delle aziende a tecnologie avanzate come AI, analytics distribuiti e microservizi, che si basano prevalentemente su architetture cloud-native.

## Processi di trasformazione

* **Fenomeno recente**: La trasformazione digitale strutturata emerge dall'analisi come un fenomeno significativamente recente nel panorama aziendale esaminato. Ben il 39,2% delle aziende ha avviato questo percorso solo dal 2020 in poi, evidenziando un punto di svolta temporale chiaramente identificabile. Questo timing non appare casuale ma coincide con l'inizio della pandemia COVID-19, che ha rappresentato un potente catalizzatore esterno, trasformando la digitalizzazione da opzione strategica a necessità operativa per garantire la continuità aziendale. I dati suggeriscono un "effetto compressione" nella curva di adozione: processi che in condizioni normali avrebbero richiesto anni sono stati condensati in pochi mesi, generando un'accelerazione forzata che, seppur positiva nell'immediato, potrebbe aver portato a implementazioni tattiche più che a trasformazioni strategiche pianificate.
* **Priorità all'operatività**: L'analisi della distribuzione delle tecnologie digitali nei diversi processi aziendali evidenzia una netta prevalenza dell'applicazione in aree amministrative (44 risposte) e operative come supply chain (34) e sviluppo prodotto (38), piuttosto che in funzioni più strategiche o innovative. Questo orientamento prevalentemente operativo riflette un approccio alla digitalizzazione ancora focalizzato sull'efficientamento dei processi esistenti e sulla riduzione dei costi, piuttosto che sulla creazione di nuove proposte di valore o sulla trasformazione radicale dei modelli di business. Le aree con minor penetrazione digitale risultano essere quelle relative alla sicurezza e all'ambiente (14), suggerendo una limitata attenzione agli aspetti di sostenibilità e gestione dei rischi, potenzialmente critici nel medio-lungo periodo.
* Stimoli interni: I dati rivelano che la trasformazione digitale nelle aziende analizzate è guidata principalmente da fattori interni (39 risposte per la creazione di un senso condiviso di responsabilità) e relazionali diretti (29 risposte per la promozione di un senso collettivo di responsabilità), con un'influenza significativamente minore di stimoli istituzionali o concorrenziali. Tra le motivazioni esterne, le collaborazioni con università e istituti di ricerca (18,2%) emergono come le più rilevanti, mentre gli incentivi da associazioni e canali di ricerca (3%) risultano i meno impattanti. Questa prevalenza di driver interni può essere interpretata positivamente come indice di una trasformazione guidata da convinzione e visione aziendale, ma potrebbe anche segnalare un insufficiente orientamento al mercato e una limitata percezione delle pressioni competitive emergenti nel panorama digitale globale.
* Coinvolgimento parziale della leadership: L'analisi del livello di coinvolgimento della leadership nei processi di trasformazione digitale evidenzia un quadro complesso: mentre circa il 46% dei leader risulta fortemente o completamente coinvolto, emerge un significativo 21,6% di "Per niente coinvolto" e un altro 22% solo "Parzialmente coinvolto". Questo limitato engagement di numerosi leader aziendali costituisce probabilmente uno dei principali ostacoli al pieno successo delle iniziative di trasformazione. La mancanza di sponsorship al vertice si traduce spesso in insufficiente allocazione di risorse, scarsa prioritizzazione strategica e difficoltà nel gestire efficacemente il cambiamento organizzativo e culturale necessario. Il dato suggerisce anche una polarizzazione dell'impegno dirigenziale ("tutto o niente"), riflettendo la consapevolezza che la trasformazione digitale richiede un coinvolgimento sostanziale per produrre risultati significativi.

## Impatti e soddisfazione

* Focus sull'efficienza: L'analisi dei benefici percepiti dalle iniziative di trasformazione digitale evidenzia una netta prevalenza di risultati legati all'efficienza operativa e all'ottimizzazione dei costi. Tra i principali miglioramenti segnalati emergono la riduzione dei costi diretti e indiretti (27 risposte), la riduzione del personale (26 risposte) e il miglioramento della produzione per i clienti (18 risposte). Significativamente minori risultano invece i riferimenti a benefici legati alla crescita strategica, all'espansione di mercato o all'innovazione di prodotto e servizio. Questa distribuzione conferma l'approccio prevalentemente tattico alla digitalizzazione, orientato al miglioramento incrementale dell'esistente piuttosto che alla generazione di nuove opportunità di business. Tale orientamento, sebbene comprensibile nell'immediato per il suo ROI più facilmente quantificabile, rischia di limitare il potenziale trasformativo delle tecnologie digitali, posizionando le aziende in una traiettoria di ottimizzazione piuttosto che di reinvenzione.
* Miglioramenti tangibili: Le aziende riportano miglioramenti concreti e misurabili in diverse aree operative. I benefici più frequentemente citati riguardano la maggiore disponibilità di dati (26,4%), il miglioramento della qualità del lavoro (19,5%) e la riduzione degli errori (17,8%). Seguono l'aumento della sicurezza nei processi (13,2%) e la miglior gestione dei fattori di rischio (8,05%). È interessante notare come i benefici percepiti riflettano una progressione logica: dall'accesso ai dati (disponibilità) all'utilizzo operativo degli stessi (qualità e riduzione errori) fino a impieghi più avanzati (gestione rischi). Questa distribuzione suggerisce un percorso evolutivo nell'uso dei dati aziendali, che parte dalla semplice disponibilità per arrivare gradualmente a utilizzi più sofisticati e strategici. La prevalenza della disponibilità di dati come beneficio principale indica che molte aziende si trovano ancora nelle fasi iniziali di questo percorso, con significative opportunità di evoluzione verso utilizzi più avanzati e a maggior valore aggiunto.
* Soddisfazione diffusa: Un dato particolarmente significativo emerge dall'analisi del livello di soddisfazione dei vertici aziendali rispetto ai risultati delle iniziative digitali: nonostante le limitazioni e i gap evidenziati in altre sezioni dell'analisi, ben il 67,6% dei decision maker si dichiara soddisfatto (32,4%), molto soddisfatto (28,4%) o pienamente soddisfatto (6,76%) dei risultati ottenuti. Solo l'8,11% esprime insoddisfazione. Questo elevato livello di approvazione, apparentemente in contrasto con la limitata profondità delle trasformazioni implementate, può essere interpretato attraverso diverse chiavi di lettura: potrebbe riflettere aspettative iniziali contenute, un focus prevalente sui benefici a breve termine piuttosto che sul potenziale strategico, o una limitata consapevolezza delle possibilità offerte da approcci più avanzati alla trasformazione digitale. È interessante notare che la soddisfazione risulta trasversale anche rispetto al grado di coinvolgimento diretto della leadership, suggerendo che anche i dirigenti meno attivamente impegnati riconoscono comunque il valore dei risultati ottenuti.

## Risultati dell'Analisi Dimensionale

### Principali correlazioni identificate

* Maturità digitale e soddisfazione: Le aziende con progetti digitali avviati riportano livelli di soddisfazione significativamente più elevati rispetto a quelle non digitalizzate o con progetti interrotti.
* Ecosistema della trasformazione digitale: La maturità digitale emerge come un ecosistema complesso composto da diversi attori (leadership, professionisti IT, utenti finali), ruoli complementari e collaborativi, e competenze interdisciplinari che devono interagire efficacemente per valorizzare il processo di trasformazione.
* Investimenti differenziati: Le aziende con progetti avviati mostrano investimenti significativamente più elevati in tutte le aree infrastrutturali (hardware, software, cloud e sicurezza) rispetto a quelle non digitalizzate.
* Paradosso delle competenze: Emerge una dinamica controintuitiva: le aziende con progetti interrotti presentano professionisti con competenze di livello eccellente nelle aree strategiche, ma mancano di contesti applicativi e collaborativi per valorizzarle.
* Leadership e innovazione: La leadership emerge come catalizzatore fondamentale, ma si evidenzia anche la possibilità di innovazione bottom-up attraverso manager intermedi visionari o pressioni competitive.

### Evoluzione temporale e contesto storico

* Accelerazione post-2020: Si registra una netta concentrazione di iniziative digitali avviate dopo il 2020, evidenziando il ruolo catalizzatore della pandemia COVID-19.
* Effetto compressione: Processi che in condizioni normali avrebbero richiesto anni sono stati condensati in pochi mesi, generando un'accelerazione significativa nell'adozione di soluzioni digitali.


"""
        st.markdown(text)
###############################################

if __name__ == "__main__":
   main()