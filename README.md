# PYTHON CODE FOR BAYESIAN STRUCTURE LEARNING

il progetto si compone di

- cartella /render dove viene scritto l'output grafico in formato DOT/png

- sorgenti per modellizzare un grafico bayesiano : Graph.py , Visualizer.py

- sorgenti per il learning :  Learning.py , Dataset.py

- sorgenti per il testing :  Earthquake.py , Test.py

## MODELLIZZARE GRAFICO BAYESIANO

Graph.py ha come classi :

- Node : : ha una lista di nodi padri e nodi figli , tabella dei parametri , label numerica , nome
- Graph : : ha una lista di nodi e varie funzioni di Utility

    - Invert/Remove Edge SA - > aggiunge/rimuove un arco casualmente che cambia la VStructure

    - Add/Invert/Remove EDge -> dato un nodo ed un father aggiunge/inverte/rimuove arco se possibile

    - initDAG(-> connette i nodi nel graph in modo da formare un DAG casuale

    - isCyclic -> controlla se un grafico ha cicli eseguendo una DFS sul grafo

    - DFS -> chiamata in isCyclic parte da ogni sorgente e verifica che i figli scoperti non siano già stati inseriti nella lista degli ancestors scoperti fin'ora

Visualizer : : scrive una stringa di codice DOT sul file /render/graph.dot e la converte in png con una system call

## IL DATASET

Dataset.py ha come classi :

- Example : : ha una lista dei nodi e una lista dei valori assunti dai noi 

- Dataset : : ha un grafico dei nodi ed una lista di Example

ha funzioni per il conteggio :

- Nijk : : restituisce il numero di esempi che hanno il nodo i = k dato j = [ [_a combination for i.fathers ] , [ labels of i.fathers_]]

## APPRENDERE IL GRAFICO

Learning.py ha come funzioni :

- alphaijk/alphaij : : priors nel learning , le ho considerate pseudocounts unitarie ( =1 )

- make_j :: dato un nodo restituisce [ _list of cartesian product of fathers domines_ , _list of fathers's labels_ ]

- Score : : è lo scoring secondo la formula di log Cooper/Herscoviz

    scorre per ogni nodo, chiama _makej()_ per generare la lista di combinazioni di padri su cui scorrere; a questo punto incrementa lo score secondo somma/sottrazione di log( Gamma()) secondo la formula. Calcola le priors con _alphaijjk()_ e conteggia il dataset con _Nijk()_

- Learn : : si apprende secondo un Hill climbing della funzione di scoring

    inizialmente si genera in modo casuale un DAG con _initDAG()_ sui nodi del grafo , poi per ogni coppia di nodi si generano i 3 possibili grafi ottenuti da un add/invert/remove di un arco tra la coppia, a questo punto se i grafici ottenuti hanno modificato la VStructure vengono inseriti in una lista G = [].

    Dopo aver scorso tutte le coppie si controlla se tra i grafi inseriti in G alcuni hanno Score maggiore, in quel caso si aggiorna il grafico corrente e si ripete il while

    ho inserito uno step aleatorio ( San Andreas ) che chiama le funzioni remove/invert SA che modificano un arco casuale ( allo scopo di evitare minimi locali )

    la ricerca termina quando nessun grafico in G risulta migliore del corrente

- bestLearn : : ho aggiunto questa funzione per un bug

    La ricerca si fermava  quasi subito  nel Learn (!! Possibile Funzione di scoringErrata !! )

    Questa funzione chiama più volte _Learn()_ in modo da far partire più ricerche in DAG inizilizzati in modo diverso ... poi si seleziona il grafico migliore

## TESTING

in Test.py ho eseguito il test di Nijk , make_j

in Earthquake.py

- ho ricostruito il ModelloEQ secondo bnlearn  ( actualEQGraph )

- ho campionato secondo le tabelle del modello EQ ( EQSampler )

- ho appreso il grafo basandomi sul dataset campionato ( EQGraph )

.

## **<span style="color:red" >BUG RISCONTRATI</span>**

1) Lo Score del grafico appreso in Earthquake.py è migliore dello Score del Modello vero nonostante abbia una struttura diversa

2) la funzione di Learn si ferma subito trovando sempre un Massimo locale al primo Step
