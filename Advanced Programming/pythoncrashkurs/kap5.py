#tw, 24.8.22  



#                         STRUKTURIERTE TYPEN UND MUTABILITÄT (VERÄNDERBARKEIT)





#Die Programme, die wir uns bisher angesehen haben, haben sich mit drei Arten von
#Objekten beschäftigt: int, float und str. Die numerischen Typen int und float sind
#skalare Typen. Das heißt, Objekte dieser Typen haben keine zugängliche interne Struktur. 
#Im Gegensatz dazu kann str als ein strukturierter Typ betrachtet werden. 
#Wir können Indizierungen (Indexing) verwenden, um einzelne Zeichen aus einer Zeichenkette 
#zu extrahieren und Zerlegungen (Slicing), um Teilstrings zu extrahieren.
#In diesem Kapitel stellen wir vier weitere strukturierte Typen vor.
#Einer von ihnen, tuple, ist eine einfache Verallgemeinerung von str. 
#Die anderen drei - list, range und dict - sind interessanter. 
#Wir kommen auch auf das Thema der Programmierung höherer Ordnung (higher order programming) 
#mit einigen Beispielen zu sprechen, die zeigen, wie nützlich es ist, Funktionen 
#auf die gleiche Weise zu behandeln wie andere Arten von Objekten.
#Im Profi-Jargon: functions are first-class citizens - functions are values !



#------------------------------------------------------------------------------------
#                             5.1 Tupel
#------------------------------------------------------------------------------------

#Wie Zeichenketten (strings) sind Tupel unveränderliche geordnete Folgen von Elementen.
#Der Unterschied besteht darin, dass die Elemente eines Tupels keine Zeichen (characters) 
#sein müssen. Die einzelnen Elemente können von beliebigem Typ sein und müssen nicht vom
#gleichen Typ zu sein.
#Literale vom Typ Tupel werden geschrieben, indem eine durch Kommata getrennte Liste von 
#Elementen in runden Klammern gesetzt wird. Zum Beispiel kann man schreiben

t1 = ()
t2 = (1, 'zwei', 3)
print(t1)
print(t2)

#Es überrascht nicht, dass die obigen print-Anweisungen die folgende Ausgabe erzeugen
#         ()
#         (1, 'zwei', 3)

#Wenn man sich dieses Beispiel ansieht, könnte man meinen, dass das Tupel, das den 
#Einzelwert 1 enthält, als (1) ausgegeben wird. Aber das wäre falsch. Literale vom
#Typ Tupel verwenden Klammern nur, um Ausdrücke zu gruppieren- d.h. (1) ist lediglich 
#ein umständlicher Weg, die ganze Zahl 1 zu schreiben. 
#Um das Singleton-Tupel zu bezeichnen, das diesen Wert enthält, schreiben wir (1,). 

(1)       #1
(1,)      #(1,)

#Fast jeder, der Python benutzt, hat schon einmal das eine oder andere Mal versehentlich 
#das lästige Komma weggelassen.

#Wiederholungen (Repetitions) können auf Tupel angewendet werden. 
#Zum Beispiel wird der Ausdruck 

3*('a', 2) 

#als ('a', 2, 'a', 2, 'a', 2) ausgewertet.

#Wie Zeichenketten können Tupel verkettet (concatenated), indiziert (indexed), 
#zerlegt (sliced) und wiederholt (repeated) werden. Betrachten Sie

t1 = (1, 'zwei', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2))           #Concatenation
print((t1 + t2)[3])        #Indexing
print((t1 + t2)[2:5])      #Slicing
print(3 * t1)              #Repetition

#Die zweite Zuweisungsanweisung bindet den Namen t2 an ein Tupel, das das Tupel t1 
#und die Fließkommazahl Zahl 3.25 enthält. Dies ist möglich, weil ein Tupel, 
#wie alles andere in Python ein Objekt ist, so dass Tupel weitere Tupel enthalten 
#können. Daher erzeugt die erste print-Anweisung die Ausgabe
#         ((1, 'zwei', 3), 3.25)
#Die zweite print-Anweisung gibt den Wert aus, der durch Konkatenation der an 
#t1 und t2 gebundenen Werte erzeugt wird, also ein Tupel mit fünf Elementen. 
#Sie erzeugt die Ausgabe
#        (1, 'zwei', 3, (1, 'zwei', 3), 3.25)
#Die dritte print-Anweisung selektiert und druckt das vierte Element des verketteten 
#Tupels (wie immer in Python beginnt die Indizierung bei 0) 
#        (1, 'zwei', 3)
#und die vierte print-Anweisung erzeugt und druckt ein Slice dieses Tupels
#        (3, (1, 'zwei', 3), 3.25)
#und die fünfte print-Anweisung erzeugt ein neues Tupel mit dem dreimaligen Inhalt
#von t1
#       (1, 'zwei', 3, 1, 'zwei', 3, 1, 'zwei', 3)

#Eine for-Anweisung kann verwendet werden, um über die Elemente eines Tupels zu
#iterieren. Und der in-Operator kann verwendet werden, um zu prüfen, ob ein Tupel 
#einen bestimmten Wert enthält. Siehe folgenden Code

def intersect(t1, t2):
    """Assumes t1 and t2 are tuples
       Returns a tuple containing elements that are in
       both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

print(intersect((1, 'a', 2), ('b', 2, 'a')))      #('a', 2).



#                     5.1.1 Mehrfachzuweisung (Multiple Assignment)
#------------------------------------------------------------------------------------

#Wenn Sie die Länge einer Sequenz (z. B. eines Tupels oder einer Zeichenkette) kennen, 
#kann es praktisch sein, Pythons Anweisung zur Mehrfachzuweisung zu verwenden, um
#die einzelnen Elemente zu extrahieren. Zum Beispiel bindet die Anweisung 

x, y = (3, 4) 
print(x, y)

#x an 3 und y an 4. 
#Ähnlich wird die Anweisung 

a, b, c = 'xyz'
print(a, b, c) 

#a an 'x', b an 'y' und c an 'z' binden.
#Dieser Mechanismus ist besonders praktisch bei der Verwendung mit Funktionen, 
#die mehrere Werte zurückgeben. Betrachten Sie dazu folgende Funktionsdefinition

def find_extreme_divisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
       Returns a tuple containing the smallest common
       divisor > 1 and 
       the largest common divisor of n1 & n2. If no
       common divisor,
       other than 1, returns (None, None)"""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
                max_val = i
    return min_val, max_val     #<-- mehrfache Returnwerte !!

#Die Mehrfachzuweisung

min_divisor, max_divisor = find_extreme_divisors(100, 200)
print(min_divisor, max_divisor)          #2 2

#wird min_divisor an 2 und max_divisor an 2 binden.
#Statt mehrerer, einzelner Variablen kann man auch ein Tupel verwenden

ergebnis_tupel = ()
ergebnis_tupel = find_extreme_divisors(100, 200)
print(ergebnis_tupel)       #(2, 2)



#------------------------------------------------------------------------------------
#                   5.2 Bereiche und Iterablen (Ranges and Iterables)
#------------------------------------------------------------------------------------

#Die Funktion range erzeugt ein Objekt vom Typ range. Wie Strings und Tupel sind 
#Objekte vom Typ range unveränderlich (immutable). Alle Operationen, die für Tupel 
#gelten, stehen auch für ranges zur Verfügung, mit Ausnahme von Verkettung und Wiederholung. 
#Zum Beispiel

#range
range(10)[2:6][2]     #4 

#ergibt 4. 
#Wenn der Operator == verwendet wird, um Objekte vom Typ range zu vergleichen, 
#gibt er True zurück, wenn beide Bereiche die gleiche Folge von Ganzzahlen darstellen. 
#Zum Beispiel

range(0, 7, 2) == range(0, 8, 2)         #True 

#ergibt True. Dagegen ergibt 

range(0, 7, 2) == range(6, -1, -2)       #False 

#ergibt jedoch Falsch, denn obwohl die beiden Bereiche zwar dieselben ganzen Zahlen 
#enthalten, treten diese aber in unterschiedlicher Reihenfolge auf.
#Diese Bedeutung der Reihenfolge gilt ebenfalls für Tupel:

(3,2,1) == (1,2,3)         #False

#auch dies ergibt False.

#Im Gegensatz zu Objekten des Typs Tuple ist der Platz, den ein Objekt vom Typ range 
#beansprucht, nicht proportional zu seiner Länge. Da ein range vollständig durch seine 
#Start-, Stopp- und Schrittweite definiert ist, benötigt er nur wenig Speicherplatz.

#Die häufigste Verwendung von range ist in for-Schleifen, aber Objekte vom Typ range 
#können überall dort verwendet werden, wo eine Folge von Ganzzahlen benötigt wird.
#In Python 3 ist range ein Spezialfall eines iterierbaren (iterable) Objekts. 
#Alle iterierbaren Typen haben eine Methode, __iter__, die ein Objekt vom Typ Iterator 
#zurückgibt. Der Iterator kann dann in einer for-Schleife verwendet werden, um eine
#Sequenz von Objekten zurückgeben, eines nach dem anderen. 
#Zum Beispiel sind Tupel iterabel, und die folgende for-Anweisung

for elem in (1, 'a', 2, (3, 4)):
    pass

#erzeugt einen Iterator, der die Elemente des Tupels einzeln zurückgibt. 
#Python hat viele eingebaute iterable-Typen, darunter Strings, Listen, und Dictionaries.
#Viele nützliche, eingebaute Funktionen arbeiten mit Iterablen. Zu den nützlichsten 
#gehören sum, min und max. Die Funktion sum kann auf Iterablen von Zahlen angewendet 
#werden. Sie gibt die Summe der Elemente zurück. Die Funktionen max und min können auf 
#Iterablen angewandt werden, für die es eine wohldefinierte Ordnung der Elemente gibt.


###############
#Aufgabe 5.2.a:
############### 
#Schreiben Sie einen Ausdruck, der den Mittelwert von Tupeln von Zahlen ergibt. 
#Verwenden Sie die Funktion sum.
###############
len((1,2,3))         #3

def mittelwert_v2(t):
    """t ist ein Tupel, das Zahlen enthaelt"""
    summe = 0
    for e in t:
        summe += e
    return summe / len(t)

mittelwert_v2((1,2,3,4,5,6,7,8,9))     #5.0


#------------------------------------------------------------------------------------
#                           5.3 Listen und Mutabilität
#------------------------------------------------------------------------------------

#Wie ein Tupel ist auch eine Liste eine geordnete Folge von Werten, wobei jeder Wert
#durch einen Index gekennzeichnet ist. Die Syntax für den Ausdruck von Literalen des Typs
#list ist ähnlich wie bei Tupeln; der Unterschied besteht darin, dass wir
#eckige Klammern anstelle von runden Klammern verwenden. Die leere Liste wird 
#als [] geschrieben, und Singleton-Listen werden ohne das (ach so leicht zu vergessende)
#Komma vor der schließenden Klammer geschrieben.

#Da Listen iterierbar sind, können wir eine for-Anweisung verwenden, um über
#die Elemente der Liste zu iterieren. So könnte zum Beispiel der Code

L = ['I did it all', 4, 'Love']
for e in L:
    print(e)

#die Ausgabe,
#               I did it all
#               4
#               Love
#erzeugen.

#Wir können auch in Listen indexieren und Listen zerschneiden (slicing), 
#genau wie bei Tupeln. Zum Beispiel, der Code

L1 = [1, 2, 3]
L2 = L1[-1::-1]
for i in range(len(L1)):
    print(L1[i]*L2[i])

#druckt
#          3
#          4
#          3

#Die Verwendung eckiger Klammern für drei verschiedene Zwecke (Literale vom
#Typ Liste, Indizierung in Iterablen und Slicing von Iterablen), kann zu
#visuellen Verwirrungen führen. Zum Beispiel verwendet der Ausdruck 

[1,2,3,4][1:3][1]

#der zu 3 ausgewertet wird, eckige Klammern auf die drei soeben genannten Arten. 
#Dies ist in der Praxis selten ein Problem, da Listen meistens inkrementell aufgebaut
#und nicht explizit als Literale im Code geschrieben werden.
#Listen unterscheiden sich von Tupeln in einem äußerst wichtigen Punkt: Listen sind
#veränderbar (mutable). Im Gegensatz dazu sind Tupel und Strings unveränderlich (immutable). 
#Viele Operatoren können verwendet werden, um Objekte unveränderlicher Typen zu erzeugen, 
#und Variablen können an Objekte dieses Typs gebunden werden. Aber Objekte von 
#unveränderlichen Typen können nach ihrer Erstellung nicht mehr geändert werden. 
#Andererseits können Objekte veränderlicher Typen nach ihrer Erstellung geändert werden.

#Der Unterschied zwischen dem Ändern eines Objekts und dem Zuweisen eines Objekts an 
#eine Variable mag auf den ersten Blick subtil erscheinen. Wenn Sie jedoch immer wieder
#das Mantra "In Python ist eine Variable lediglich ein Name, d. h. ein Etikett, 
#das an ein Objekt angehängt werden kann", wird es Ihnen Klarheit verschaffen. 
#Und vielleicht hilft Ihnen auch die folgende Reihe von Beispielen.
#Wenn die Zuweisungsanweisungen

Techs = ['MIT', 'Caltech', 'HOST'] 
Ivys = ['Harvard', 'Yale', 'Brown']

#ausgeführt werden, erstellt der Interpreter zwei neue Listen und bindet die
#entsprechenden Variablen an sie, wie in der folgenden Abbildung 5-1 dargestellt

#                           ...........................................
#                           .                                         .
#                           .                                         .
#              Techs -------------> ['MIT', 'Caltech', 'HOST']        .
#                           .                                         .
#                           .                                         .
#                           .                                         .
#              Ivys ------------> ['Harvard', 'Yale', 'Brown']        .
#                           .                                         .
#                           .                                         .
#                           .                                         .
#                           ...........................................

#Die folgenden Zuweisungs-Anweisungen erzeugen

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech', 'HOST'], ['Harvard', 'Yale', 'Brown']]

#auch neue Listen und binden Variablen an sie. Die Elemente dieser
#Listen sind selbst wieder Listen. Die drei Druckanweisungen

print('Univs =', Univs)
print('Univs1 =', Univs1)
print(Univs == Univs1)

#erzeugen folgende Ergebnisse
#       Univs = [['MIT', 'Caltech', 'HOST'], ['Harvard', 'Yale', 'Brown']]
#       Univs1 = [['MIT', 'Caltech', 'HOST'], ['Harvard', 'Yale', 'Brown']]
#       True

#Es scheint, als ob Univs und Univs1 an denselben Wert gebunden sind. 
#Aber der Schein kann trügerisch sein. Wie Abbildung 5-2 veranschaulicht, 
#sind Univs und Univs1 an ganz unterschiedliche Werte gebunden

#                           ...........................................
#                           .                                         .
#                           .                                         .
#              Techs --------------> ['MIT', 'Caltech', 'HOST']       .
#                           .       ^                                 .
#                           .      /                                  .
#              Univs ---------> [   ,   ]                             .
#                           .         \                               .
#                           .         v                               .                 
#              Ivys -----------------> ['Harvard', 'Yale', 'Brown']   .
#                           .                                         .
#                           .                                         .
#                           .        ['MIT', 'Caltech', 'HOST']        .
#                           .       ^                                 .
#                           .      /                                  .
#              Univs1 --------> [   ,   ]                             .
#                           .         \                               .
#                           .         v                               .                   
#                           .          ['Harvard', 'Yale', 'Brown']   .
#                           .                                         .
#                           ...........................................

#Dass Univs und Univs1 an verschiedene Objekte gebunden sind, lässt sich
#mit der eingebauten Python-Funktion id überprüft werden, die einen eindeutigen
#ganzzahligen Bezeichner für ein Objekt zurückgibt. Mit dieser Funktion können 
#wir auf Objektgleichheit zu testen, indem man ihre id vergleicht. 
#Eine einfachere Methode zur Prüfung auf Objektgleichheit zu testen, ist die 
#Verwendung des is-Operators. Wenn wir den folgenden Code ausführen

print(Univs == Univs1)                 #True         Wertgleichheit wurde getestet
print(id(Univs) == id(Univs1))         #False        Objektgleichheit wurde getestet
print(Univs is Univs1)                 #False        Objektgleichheit wurde getestet
print('Id of Univs =', id(Univs))      #Id of Univs = 1384415156736
print('Id of Univs1 =', id(Univs1))    #Id of Univs1 = 1384415231680

#Erwarten Sie nicht, dass Sie immer die gleichen eindeutigen Bezeichner sehen, 
#wenn Sie diesen Code ausführen. Die Semantik von Python sagt nichts darüber aus, 
#welcher Bezeichner mit jedem Objekt verbunden ist; sie verlangt lediglich, 
#dass keine zwei Objekte denselben Bezeichner haben.

#Beachten Sie, dass in Abbildung 5-2 die Elemente von Univs keine Kopien der Listen
#sind, an die Techs und Ivys gebunden sind, sondern die Listen selbst sind. 
#Die Elemente von Univs1 sind Listen, die die gleichen Elemente enthalten wie die 
#Listen in Univs, aber es sind nicht die gleichen Listen. Wir können dies sehen, 
#indem wir folgenden Code ausführen

print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1]))
print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))

#Das ergibt
#       Ids of Univs[0] and Univs[1] 1384415231552 1384415086144
#       Ids of Univs1[0] and Univs1[1] 1384415220544 1384415088576
#Sie sind alle unterschiedlich.

#Warum die große Aufregung um den Unterschied zwischen Wert- und Objekt-Gleichheit? 
#Antwort: weil Listen veränderbar (mutable) sind. Betrachten Sie folgenden Code

Techs.append('RPI')
Techs                 #['MIT', 'Caltech', 'HOST', 'RPI']

#Die eingebaute Methode append für Listen hat einen sog. Seiteneffekt (side effect).
#                                                        -------------------------- 
# Anstatt eine neue Liste zu erstellen, verändert sie die bestehende Liste Techs, 
#indem sie ein neues Element, im obigen Beispiel die Zeichenkette "RPI", an das 
#Ende der Liste angehängt. Abbildung 5-3 veranschaulicht den Zustand nach der 
#Ausführung von append.

#                           ...........................................
#                           .                                         .
#                           .                                         .
#              Techs --------------> ['MIT', 'Caltech', 'HOST', 'RPI'].
#                           .       ^                                 .
#                           .      /                                  .
#              Univs ---------> [   ,   ]                             .
#                           .         \                               .
#                           .         v                               .                 
#              Ivys -----------------> ['Harvard', 'Yale', 'Brown']   .
#                           .                                         .
#                           .                                         .
#                           .        ['MIT', 'Caltech', 'HOST']        .
#                           .       ^                                 .
#                           .      /                                  .
#              Univs1 --------> [   ,   ]                             .
#                           .         \                               .
#                           .         v                               .                   
#                           .          ['Harvard', 'Yale', 'Brown']   .
#                           .                                         .
#                           ...........................................

#Das Objekt, an das Univs gebunden ist, enthält immer noch die gleichen zwei Listen,
#aber der Inhalt einer dieser Listen hat sich geändert. Folglich werden die 
#folgenden Printanweisungen

print('Univs =', Univs)
print('Univs1 =', Univs1)

#dies ergeben:
#          Univs = [['MIT', 'Caltech', 'HOST', 'RPI'], ['Harvard', 'Yale', 'Brown']]
#          Univs1 = [['MIT', 'Caltech', 'HOST'], ['Harvard', 'Yale', 'Brown']]

#Was wir hier haben, nennt man Aliasing. Es gibt zwei verschiedene Pfade zu ein und 
#                              --------
#demselben Listenobjekt. Der eine Weg führt über die Variable Techs und der andere 
#über das erste Element des Listenobjekts, an das Univs gebunden ist. 
#Wir können das Objekt über einen der beiden Pfade mutieren (verändern), und die
#Auswirkung der Mutation wird aber über beide Pfade sichtbar sein. Das kann bequem 
#sein, aber es kann auch tückisch sein. Unbeabsichtigtes Aliasing führt zu 
#Programmierfehlern, die oft sehr schwer zu finden sind. Was glauben Sie zum 
#Beispiel, was durch folgenden Code gedruckt wird ?

print('davor: ', end=' ')
L1 = [[]]*2
print('L1 =', L1, end=' und ')
L2 = [[], []]
print('L2 = ', L2)
for i in range(len(L1)):
    L1[i].append(i)
    L2[i].append(i)
print('danach: ', end=' ')
print('L1 =', L1, 'aber', 'L2 =', L2)

#Gedruckt wird
#     davor:  L1 = [[], []] und L2 =  [[], []]
#     danach:  L1 = [[0, 1], [0, 1]] aber L2 = [[0], [1]]
#Warum? Weil die erste Zuweisungsanweisung eine Liste mit zwei Elementen erzeugt, 
#von denen jedes dasselbe Objekt ist, während die zweite Zuweisungsanweisung 
#eine Liste mit zwei verschiedenen Objekten erzeugt, von denen jedes anfangs 
#gleich einer leeren Liste ist. L1 enthält also zweimal dieselbe (Objektidentität) 
#Liste. L2 enthält zwei unterschiedliche Listen. Deshalb haben die append-
#Anweisungen in der Schleife unterschiedliche Auswirkungen auf die Elemente
#in L1 und L2.



###############
#Aufgabe 5.3.a:
############### 
#Was gibt der folgende Code aus?
#Nicht einfach ausprobieren, sondern erst austüfteln und vorhersagen:
L = [1, 2, 3]
#Ist rekuriv wiederholt sich unendlich oft
L.append(L)
# Da unendlich
print(L is L[-1])

#Hinweis: der Index -1 bzeichnet das letzte Listenelement, siehe z.B.:
[1,2,3][-1]    #3
###############



#Das Zusammenspiel von Aliasing und Veränderbarkeit bei Defaultparameterwerten
#ist etwas, auf das man achten sollte. Betrachten Sie den folgenden Code

def append_val(val, list_1 = []):
    list_1.append(val)
    print(list_1)
 
append_val(3)          #[3]
append_val(4)          #[3, 4]

#Man könnte meinen, dass der zweite Aufruf von append_val die Liste
#die Liste [4] ausgeben würde, weil er 4 an die leere Liste angehängt hätte.
#Tatsächlich wird [3, 4] gedruckt. Dies geschieht, weil bei der Funktionsdefinition
#ein neues Objekt vom Typ list als Default-Parameter erzeugt wird, dessen Anfangswert 
#die leere Liste ist. 
#Jedes Mal, wenn append_val aufgerufen wird, ohne einen Wert für den formalen Parameter 
#list_1, wird das bei der Funktionsdefinition erzeugte Objekt an list_1 gebunden, 
#mutiert und dann gedruckt. So wird beim zweiten Aufruf von append_val mutiert und eine
#Liste ausgedruckt, die bereits durch den ersten Aufruf von append_val mutiert wurde.

#Wenn wir eine Liste an eine andere anhängen, z.B. (siehe oben) Techs.append(Ivys),
#wird die ursprüngliche Struktur beibehalten. Das Ergebnis ist eine Liste, die eine
#Liste enthält. Angenommen, wir wollen diese Struktur nicht beibehalten, sondern
#die Elemente(!) einer Liste in eine andere Liste einfügen. Dann können wir das tun, 
#indem wir eine Listenverkettung (concatenation) mit dem +-Operator oder mit der 
#extend-Methode ausführen, z.B.

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

#wird folgendes ausdrucken:
#         L3 = [1, 2, 3, 4, 5, 6]
#         L1 = [1, 2, 3, 4, 5, 6]
#         L1 = [1, 2, 3, 4, 5, 6, [4, 5, 6]]

#Beachten Sie, dass der Operator + keine Seiteneffekte hat. Er erstellt eine neue
#Liste und gibt sie zurück. Im Gegensatz dazu mutieren extend und append jeweils L1.
#Es folgt eine kurze Beschreibung einiger der Methoden, die für Listen verfügbar sind. 
#Beachten Sie, dass alle diese Methoden außer count und index die Liste verändern.

#     L.append(e)        fügt das Objekt e ans Ende der Liste L ein
#     L.count(e)         returniert wie häufig e in L vorkommt
#     L.insert(i, e)     fügt e beim Index i in L ein
#     L.extend(L1)       fügt die Elemente der Liste L1 ans Ende von L ein
#     L.remove(e)        entfernt das erste Auftreten von e in L
#     L.index(e)         returniert den Index des ersten Auftretens von e in L;
#                        wirft eine Exception, wenn e nicht in L ist
#     L.pop(i)           entfernt und returniert das Element am Index i in L;
#                        wirft eine Exception, wenn L leer ist; wenn i weggelassen wird,
#                        ist der default -1, so dass das letzte Element entfernt und
#                        returniert wird
#     L.sort()           sortiert die Elemente in L aufsteigend
#     L.reverse          kehrt die Reihenfolge der Elemente in L um



#                     5.3.1 Klonen (Cloning)
#------------------------------------------------------------------------------------

#In der Regel ist es ratsam, die Mutation einer Liste zu vermeiden, über die man
#iteriert. Betrachten Sie folgenden Code

def remove_dups(L1, L2):
    """Assumes that L1 and L2 are lists.
       Removes any element from L1 that also occurs in L2"""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)


#Liste duplizieren
liste = [1,2,3,4,5]
liste_false_copy = liste
liste_copy = liste[::]
#Sie werden möglicherweise überrascht sein, dass das folgendes ausdruckt
#         L1 = [2, 3, 4]

#Während einer for-Schleife verfolgt Python, wo es sich in der Liste befindet. 
#Es verwendet dazu einen internen Zähler, der am Ende jeder Iteration inkrementiert 
#wird. Wenn der Wert des Zählers die aktuelle Länge der Liste erreicht, wird die 
#Schleife beendet. Dies funktioniert so, wie Sie es erwarten, wenn die Liste 
#innerhalb der Schleife nicht verändert wird. Es kann aber überraschende Folgen 
#haben, wenn die Liste mutiert wird. In diesem Fall beginnt der versteckte Zähler 
#bei 0, stellt fest, dass L1[0] in L2 enthalten ist, und entfernt L1[0], wodurch 
#die Länge von L1 auf 3 reduziert wird. Der Zähler wird dann auf 1 erhöht, und der 
#Code fährt fort zu prüfen, ob der Wert von L1[1] in L2 liegt. Beachten Sie, 
#dass dies nicht der ursprüngliche Wert von L1[1] (d.h. 2), sondern der aktuelle 
#Wert von L1[1] (d.h., 3). Wie Sie sehen, ist es möglich, herauszufinden, 
#was passiert, wenn die Liste innerhalb der Schleife geändert wird. Allerdings 
#ist das nicht einfach. Und was passiert, ist wahrscheinlich ungewollt, wie 
#in diesem Beispiel.

#Eine Möglichkeit, diese Art von Problem zu vermeiden, ist die Verwendung von 
#Slicing zum Klonen (d.h. Erstellen einer exakten Kopie) der Liste und über diese
#Kopie dann zu iterieren.
#Dafür reicht es
#      for e1 in L1[:]: 
#zu schreiben. Beachten Sie, dass
#      neu_L1 = L1
#      for e1 in new_L1:
#das Problem nicht lösen würde. Es würde keine Kopie von L1 erstellen, sondern
#würde lediglich einen neuen Namen für die bestehende Liste einführen.

#Slicing ist nicht die einzige Möglichkeit, Listen in Python zu klonen. 
#Der Ausdruck
#      L.copy() 
#hat den gleichen Wert wie L[:]. Sowohl Slicing als auch copy führen eine so 
#genannte flache (shallow) Kopie. Eine flache Kopie erstellt eine neue Liste
#         ----------------------
#und fügt dann die Objekte (keine Kopien der Objekte) der zu kopierenden Liste
#in die neue Liste ein. Dazu importieren Sie das Standardbibliotheksmodul copy 
#und verwenden die Funktion copy.copy, wie im folgenden dargestellt.
#Dieser Code

import copy
L = [2]
L1 = [L]
L2 = L1[:]
L2 = copy.copy(L1)      
L.append(3)
print(f'L1 = {L1}, L2 = {L2}')

#druckt L1 = [[2, 3]] L2 = [[2, 3]], da sowohl L1 als auch L2 das Objekt enthalten, 
#das in der ersten Zuweisung an L gebunden wurde. 
#Wenn die zu kopierende Liste veränderbare Objekte enthält, die Sie auch kopieren 
#wollen, importieren Sie das Standardbibliotheksmodul copy und verwenden die Funktion 
#copy.deepcopy, um eine tiefe (deep) Kopie zu erstellen. Die Methode deepcopy erstellt 
#                       ------------------
#eine neue Liste und fügt dann Kopien der Objekte der zu kopierenden Liste in die neue 
#Liste ein. 
#Wenn wir die vierte Zeile im obigen Code durch L2 = copy.deepcopy(L1) ersetzen, 
#wird L1 = [[2, 3]], L2 = [[2]] ausgedruckt, da L1 das Objekt, an das L gebunden 
#ist, nicht enthalten würde.

#Das Verständnis von copy.deepcopy ist knifflig, wenn die Elemente einer Liste
#selbst wieder Listen sind, die Listen (oder irgendeinen veränderbaren Typ) 
#enthalten. Betrachten Sie z.B. diesen Code, der

import copy
L1 = [2]
L2 = [[L1]]
L3 = copy.deepcopy(L2)
L1.append(3)
print(f'L1 = {L1}, L2 = {L2}, L3 = {L3}')

#sowas druckt: L1 = [2, 3], L2 = [[[2, 3]]], L3 = [[[2]]]. Begründung: copy.deepcopy 
#erzeugt ein neues Objekt nicht nur für die Liste [L1], sondern auch für die Liste L1. 
#D.h., es macht Kopien bis ganz nach unten - zumindest die meiste Zeit. 
#Warum "die meiste Zeit?" Z.B. der Code
#
#     L1 = [2]
#     L1.append(L1)
#
#erzeugt eine Liste, die sich selbst enthält. Ein Versuch, Kopien bis zum Ende 
#der Liste zu kopieren, würde nie enden. Um dieses Problem zu vermeiden, erzeugt
#copy.deepcopy genau eine Kopie jedes Objekts an und verwendet diese Kopie für jede 
#Instanz des Objekts. Dies ist auch dann wichtig, wenn Listen sich selbst nicht 
#enthalten. Zum Beispiel

import copy
L1 = [2]
L2 = [L1, L1]
L3 = copy.deepcopy(L2)
L3[0].append(3)
print(L3)

#druckt [[2, 3], [2, 3]], weil copy.deepcopy nur eine Kopie von L1 anfertigt und sie 
#beide Male verwendet, wenn L1 in L2 vorkommt.



#                     5.3.2 List Comprehension
#------------------------------------------------------------------------------------

#Eine List Comprehension (Listenverständnis ?? Das macht keinen Sinn - kann man 
#irgendwie nicht gut übersetzen) bietet eine prägnante Möglichkeit, eine Operation
#auf die Sequenzwerte anzuwenden, die durch Iteration über einen iterierbaren Wert 
#bereitgestellt werden. Es erstellt eine neue Liste, in der jedes Element das Ergebnis 
#der Anwendung einer gegebenen Operation auf einen Wert aus einer Iterablen (z.B. 
#die Elemente in einer anderen Liste). Es handelt sich um einen Ausdruck der Form
#
#          [expr for elem in iterable if test]
#
#Die Auswertung dieses Ausdrucks ist gleichbedeutend mit dem Aufruf der Funktion

def func_listcomprehension(expr, iterable, test = lambda x: True):
    new_list = []
    for e in iterable:
        if test(e):
            new_list.append(expr(e))
    return new_list

#Hier sind ein paar Anwendungsbeispiele der List Comprehension: 

[e**2 for e in range(6)]                            #ergibt [0, 1, 4, 9, 16, 25] 
[e**2 for e in range(8) if e%2 == 0]                #ergibt [0, 4, 16, 36]
[x**2 for x in [2, 'a', 3, 4.0] if type(x) == int]  #ergibt [4, 9]

#Und hier dieselben Beispiele unter Verwendung von func_listcomprehension:

func_listcomprehension(lambda x: x**2, range(6))                                        #[0, 1, 4, 9, 16, 25] 
func_listcomprehension(lambda x: x**2, range(8), lambda x: True if x%2 == 0 else False) #[0, 4, 16, 36]
func_listcomprehension(lambda x: x**2, [2, 'a', 3, 4.0], lambda x: True if type(x) == int else False) #[4, 9]

#Die List-Comprehension bietet eine bequeme Möglichkeit, Listen zu initialisieren.
#Zum Beispiel erzeugt [[] for _ in range(10)] eine Liste mit 10 verschiedenen leeren 
#Listen. Der Variablenname _ zeigt an dass die Werte dieser Variablen bei der Erzeugung 
#der Listenelemente nicht verwendet werden, d.h. es handelt sich lediglich um einen 
#Platzhalter. Diese Konvention ist in Python-Programmen üblich.

#Python erlaubt mehrere for-Anweisungen innerhalb einer List-Comprehension. 
#Betrachten Sie den Code

L = [(x, y) 
     for x in range(6) if x%2 == 0 
     for y in range(6) if y%3 == 0]
print(L)                             #[(0, 0), (0, 3), (2, 0), (2, 3), (4, 0), (4, 3)]

#Der Python-Interpreter beginnt mit der Auswertung des ersten for und weist x die Folge 
#der Werte 0, 2, 4 zu. Für jeden dieser drei Werte von x, wertet er das zweite for aus
#(das jedes Mal die Folge der Werte 0, 3 erzeugt). Anschließend fügt es der erzeugten 
#Liste das Tupel (x, y) hinzu. So entsteht insgesamt die obige Ergebnisliste.
#Natürlich können wir die gleiche Liste auch ohne List-Comprehension erzeugen,
#aber der Code ist dann wesentlich weniger kompakt:

L = []
for x in range(6):
    if x%2 == 0:
        for y in range(6):
            if y%3 == 0:
                L.append((x, y))
print(L)                             #[(0, 0), (0, 3), (2, 0), (2, 3), (4, 0), (4, 3)]

#Der folgende Code ist ein Beispiel für die Verschachtelung einer List-Comprehension
#innerhalb eines Listenaufrufs:

print([[(x,y) for x in range(6) if x%2 == 0] for y in range(6) if y%3 == 0])

#Das ergibt [[(0, 0), (2, 0), (4, 0)], [(0, 3), (2, 3), (4, 3)]].
#Es braucht etwas Übung, um sich mit verschachtelten Listen zurechtzufinden, 
#aber sie können sehr nützlich sein. Wir wollen nun verschachtelte List-Comprehensions
#verwenden, um eine Liste aller Primzahlen kleiner als 100 zu erstellen. Die Grundidee 
#besteht darin, mit einer Comprehension eine Liste zu erstellen mit allen in Frage 
#kommenden Zahlen (d.h. 2 bis 99), und eine zweite Comprehension, um eine Liste der 
#Reste zu erstellen, die sich aus der ganzzahligen Division eines Primzahlkandidaten 
#durch jeden potenziellen Divisor ergibt. Dabei verwenden wir die built-in Funktion 
#all, um zu prüfen, ob einer dieser Reste 0 ist:

print([x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))])   #[2, 3, 5, 7, ...]

#Das wollen wir mal analysieren. 
#Was macht die Funktion all ?
all([True,True,True])      #True
all([True, False, True])   #False
all([])                    #True
#In all wird für jede Zahl x eine Liste mit entsprechenden
#Wahrheitswerten erzeugt. In dieser Liste wird für alle Zahlen y, die kleiner 
#als x sind, überprüft, ob x und y teilerfremd sind. Falls ja, wird in die Liste ein
#True eingefügt. Nur wenn alle Elemente dieser Liste True sind, wird auch all
#ein True returnieren. Auf diese Weise werden in der List Comprehension alle
#Nicht-Primzahlen herausgefiltert.

#Die Auswertung des obigen Primzahl-Ausdrucks ist gleichbedeutend mit dem Aufruf 
#der Funktion

def gen_primes():
    primes = []
    for x in range(2, 100):
        is_prime = True
        for y in range(2, x):
            if x%y == 0:
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes
print(gen_primes())    #[2, 3, 5, 7, ...]



#################
#Aufgabe 5.3.2.a:
################# 
#Schreiben Sie eine List-Comprehension, die alle Nicht-Primzahlen 
#zwischen 2 und 100 erzeugt.
###############


print([x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))])   #[2, 3, 5, 7, ...]


#------------------------------------------------------------------------------------
#                       5.4 Operationen höherer Ordnung auf Listen
#------------------------------------------------------------------------------------

#Genauso wie man Funktionen als Argumente in Parameterlisten von anderen Funktionen,
#sog. Funktionen höherer Ordnung (higher order functions) übergeben kann, kann man
#dies auch für Listen tun. Hier ist ein Beispiel: 
# Vorlesung FUnktionen höherer art
def meinefkt(f):
    def nocheinefkt(a):
        return f(a)
    return nocheinefkt

meinefkt(5)
#Code 5.4.1 
#---Anwenden einer Funktion auf Elemente einer Liste---
def apply_to_each(L, f):
    """Assumes L is a list, f a function
       Mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
      
L = [1, -2, 3.33]
print('L =', L)                                 
print('Apply abs to each element of L.')
apply_to_each(L, abs)
print('L =', L)
print('Apply int to each element of', L)
apply_to_each(L, int)
print('L =', L)
print('Apply squaring to each element of', L)
apply_to_each(L, lambda x: x**2)
print('L =', L)
#---


#Die Funktion apply_to_each wird als Funktion höherer Ordnung bezeichnet, weil sie
#ein Argument hat, das selbst eine Funktion ist. Wenn sie zum ersten Mal aufgerufen 
#wird, verändert (mutiert) sie L, indem sie die unäre built-in Funktion abs auf 
#jedes Element der Liste anwendet. Beim zweiten Aufruf wendet sie eine 
#Typkonvertierung auf jedes Element an. Und beim dritten Aufruf wird jedes Element
#durch das Ergebnis der Anwendung einer mit Lambda definierten Funktion ersetzt. 
#Es wird insgesamt folgendes ausgedruckt:
#     L = [1, -2, 3.33]
#     Apply abs to each element of L.
#     L = [1, 2, 3.33]
#     Apply int to each element of [1, 2, 3.33]
#     L = [1, 2, 3]
#     Apply squaring to each element of [1, 2, 3]
#     L = [1, 4, 9]

#Python hat eine eingebaute Funktion höherer Ordnung, map, die ähnlich, aber 
#allgemeiner ist als die Funktion apply_to_each, die in Code 5.4.1 dargestellt ist. 
#In ihrer einfachsten Form ist das erste Argument von map eine unäre Funktion 
#(d.h. eine Funktion, die nur einen Parameter hat) und das zweite Argument ist eine 
#beliebige geordnete Sammlung von Werten, die als Argumente für das erste Argument,
#also die unäre Funktion, dienen. Die Funktion map wird häufig anstelle einer 
#List-Comprehension verwendet. Zum Beispiel ist list(map(str, range(10)))
#äquivalent zu [str(e) for e in range(10)].

#Die map-Funktion wird häufig in einer for-Schleife verwendet. Bei der Verwendung 
#in einer for-Schleife, verhält sich map wie die Funktion range, indem sie einen 
#Wert für jede Iteration der Schleife zurückgibt. map returniert also ein Iterable-
#Objekt. Seine Werte werden erzeugt, indem das erste Argument auf jedes Element des 
#zweiten Arguments angewandt wird. Z.B. wie in diesem Code

for i in map(lambda x: x**2, [2, 6, 4]):
    print(i, end=' ')

#der folgendes ausdruckt:   4  36  16
#Bei einem Iterable-Objekt muss man die Auswertung "erzwingen". Das kann man 
#(wie oben) durch eine Schleife, oder durch bestimmte Funktionen, wie z.B. list

print(map(lambda x: x**2, [2, 6, 4]))     #<map object at 0x000002970B88C430>
list(map(lambda x: x**2, [2, 6, 4]))      #[4, 36, 16]

#Allgemeiner ausgedrückt, kann das erste Argument einer map-Funktion eine Funktion 
#mit n Argumenten sein; in diesem Fall müssen ihm n geordnete Listen (jeweils mit 
#der gleichen Länge) folgen; wie in diesem Code

L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i, end=' ')

#dies ergibt:   1  28  9



###############
#Aufgabe 5.4.a:
############### 
#Implementieren Sie eine Funktion, die die folgende Spezifikation erfüllt. 
#Hinweis: Es ist zweckmäßig, lambda im Körper der Implementierung zu verwenden.
def f(L1, L2):
    """L1, L2 lists of same length of numbers
       returns the sum of raising each element in L1
       to the power of the element at the same index in L2
       For example, f([1,2], [2,3]) returns 9"""
###############



#------------------------------------------------------------------------------------
#  5.5 Zeichenketten (strings), Tupel (Tuples), Bereiche (Ranges) und Listen (Lists)
#------------------------------------------------------------------------------------

#Wir haben uns vier iterierbare Sequenztypen angesehen: str, tuple, range und list. 
#Sie sind sich insofern ähnlich, als Objekte dieser Typen verwendet werden werden 
#können, wie in der folgenden Auflistung beschrieben. Einige ihrer anderen
#Gemeinsamkeiten und Unterschiede werden in der danach folgenden Tabelle 
#zusammengefasst.

#   Gemeinsame Operationen für Sequenztypen
#   .......................................
#       seq[i]          gibt das i-te Element einer Sequenz zurück
#       len(seq)        gibt die Länge einer Sequenz seq zurück
#       seq1 + seq2     gibt die Verkettung von zwei Sequenzen zurück (funktioniert
#                       aber nicht für Ranges) 
#       n * seq         gibt eine Sequenz zurück, die n-mal aus der 
#                       Sequenz seq besteht
#       seq[start:end]  gibt einen Auschnitt (slice) einer Sequenz vom Index start
#                       bis zum Index end zurück 
#       e in seq        ist True, wenn e in der Sequenz enthalten ist, sonst False
#       e not in seq    ist True, wenn e nicht der Sequenz enthalten ist, sonst False
#       for e in seq:   interiert über die Elemente der Sequenz    


#    Vergleich der Sequenztypen
#    ..........................
#    Typ             Typ der Elemente            Literale                   mutable
#    ..............................................................................
#    str             Zeichen (Buchstaben,        '', 'a', 'abc'             nein 
#                             Ziffern, etc.)
#    tuple           jeder Typ                   (), (3,), ('abc', 4)       nein
#    range           Integers                    range(10), range(10,20,2)  nein
#    list            jeder Typ                   [], [3], ['abc', 4]        ja

#Python-Programmierer neigen dazu, Listen viel häufiger zu verwenden als Tupel.
#Da Listen veränderbar sind (mutable), können sie während einer Berechnung inkrementell 
#aufgebaut werden. Der folgende Code baut zum Beispiel inkrementell eine Liste even_elems auf, 
#die alle geraden Zahlen einer anderen Liste L enthält

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_elems = []
for e in L:
    if e%2 == 0:
        even_elems.append(e)
print(even_elems)

#Da Zeichenketten nur Zeichen (also Character) enthalten können, sind sie wesentlich
#weniger vielseitig als Tupel oder Listen. Andererseits, wenn Sie mit einer Zeichenkette 
#arbeiten, gibt es viele nützliche eingebaute Methoden. Die folgende Tabelle enthält kurze 
#Beschreibungen einiger dieser Methoden.
#Da Zeichenketten unveränderlich (immutable) sind, geben alle diese Methoden Werte zurück 
#und haben keine Seiteneffekte.

#     s.count(s1)            zählt, wie häufig String s1 im String s vorkommt.
#     s.find(s1)             returniert den Index des ersten Auftretens von Substring s1 
#                            im String s; returniert -1, wenn s1 nicht in s vorkommt.
#     s.rfind(s1)            wie find, aber startet am Ende von s; r steht für reverse.
#     s.index(s1)            wie find, aber wirft eine Exception, wenn s1 nicht in s vorkommt.
#     s.rindex(s1)           wie index, aber startet am Ende von s; r steht für reverse.    
#     s.lower()              wandelt ale Zeichen in s in Großbuchstaben um.
#     s.replace(old, new)    ersetzt jedes Vorkommen des Strings old im String s durch den
#                            String new.
#     s.rstrip()             entfernt nachziehenden Whitespace am Ende des Strings s.
#     s.split(d)             spaltet s am Trennzeichen d (delimiter) auf und returniert
#                            eine Liste der Teile. Wenn d fehlt wird Whitespace als
#                            Default-Trennzeichen verwendet.

#Eine der nützlicheren eingebauten Methoden ist split, dessen Argument ein Trennzeichen angibt.
#Als Ergebnis erhält man eine Liste von Teilstrings

print('My favorite professor–John G.–rocks'.split(' '))
print('My favorite professor–John G.–rocks'.split('–'))



#------------------------------------------------------------------------------------
#                               5.6 Mengen (sets)
#------------------------------------------------------------------------------------

#Sets sind eine weitere Art von Sammlung. Sie sind ähnlich wie der Begriff der Menge in der 
#Mathematik, da es sich um ungeordnete Sammlungen von eindeutigen Elementen sind. 
#Sie werden mit geschweiften Klammern geschrieben, z.B.

baseball_teams = {'Dodgers', 'Giants', 'Padres', 'Rockies'}
football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}

#Da die Elemente einer Menge nicht geordnet sind, erzeugt der Versuch, einen Index
#in einer Menge zu verwenden, z.B. baseball_teams[0], einen Fehler. 
#Wir können eine for-Anweisung verwenden, um über die Elemente einer Menge zu iterieren.
#Aber im Gegensatz zu den anderen Auflistungstypen, die wir schon kennengelernt haben, 
#ist die Reihenfolge, in der die Elemente erzeugt werden, undefiniert.
#Wie Listen sind auch Mengen veränderbar (mutable). Wir fügen ein einzelnes Element zu einer 
#Menge mit der Methode add hinzu. Wir fügen mehrere Elemente zu einer Menge hinzu, indem wir 
#eine Sammlung von Elementen (z. B. eine Liste) an die update-Methode übergeben, z.B.

baseball_teams.add('Yankees')
football_teams.update(['Patriots', 'Jets'])
print(baseball_teams)
print(football_teams)

#ergibt
#{'Padres', 'Rockies', 'Dodgers', 'Giants', 'Yankees'}
#{'Cardinals', 'Cowboys', 'Jets', 'Eagles', 'Giants', 'Patriots'}

#Die Reihenfolge, in der die Elemente erscheinen, ist in Python nicht weiter spezifiziert,
#so dass Sie möglicherweise eine andere Ausgabe erhalten, wenn Sie das obige Beispiel 
#ausführen.

#Elemente können mit der Methode remove aus einer Menge entfernt werden, die einen Fehler 
#auslöst, wenn das Element nicht in der Menge enthalten ist, oder mit der Methode discard,
#die keinen Fehler auslöst, wenn sich das Element nicht in der Menge befindet.

#Die Zugehörigkeit eines Elements zu einer Menge kann mit dem in-Operator geprüft werden, 
#z.B.

'Rockies' in baseball_teams            #true

#Die binären Methoden union, intersection, difference und issubset haben ihre
#üblichen mathematischen Bedeutungen (Mengenlehre):

print(baseball_teams.union({1, 2}))                         #Vereinigungsmenge
print(baseball_teams.intersection(football_teams))          #Schnittmenge
print(baseball_teams.difference(football_teams))            #Differenzmenge
print({'Padres', 'Yankees'}.issubset(baseball_teams))       #Teilmenge?

#ergibt:
#{'Padres', 'Rockies', 1, 2, 'Giants', 'Dodgers', 'Yankees'}
#{'Giants'}
#{'Padres', 'Rockies', 'Dodgers', 'Yankees'}
#True

#Einer der Vorzüge von Mengen ist, dass es für viele Methoden praktische Infix-Operatoren
#gibt, darunter | für union , & für intersect, - für difference, <= für subset 
#und >= für superset. Durch die Verwendung dieser Operatoren ist der Code leichter zu lesen. 
#Vergleichen Sie z.B.

print(baseball_teams | {1, 2})
print(baseball_teams & football_teams)
print(baseball_teams - football_teams)
print({'Padres', 'Yankees'} <= baseball_teams)

#mit dem zuvor vorgestellten Code, der die Punktnotation verwendet, um die gleichen Werte 
#auszugeben.

#Nicht alle Arten von Objekten können Elemente von Mengen (sets) sein. Alle Objekte in 
#einer Mengemüssen hashfähig (hashable) sein. Ein Objekt ist hashable, wenn es
#                  ---------
#
#    *   eine __hash__-Methode besitzt, die das Objekt auf einen int abbildet,
#        und dieser von __hash__ zurückgegebene Wert sich während der
#        Lebensdauer des Objekts nicht mehr ändert,
#    und
#    *   eine __eq__-Methode besitzt, mit der das Objekt auf Gleichheit mit anderen
#        Objekten geprüft werden kann.

#Alle Objekte von Pythons skalaren unveränderlichen Typen sind hashable, und
#kein Objekt von Pythons eingebauten veränderlichen Typen ist hashfähig. Ein Objekt eines 
#nicht skalaren unveränderlichen Typs (z.B. ein Tupel) ist hashfähig, wenn alle seine
#Elemente hashfähig sind.



#------------------------------------------------------------------------------------
#           5.7 Dictionaries (Wörterbücher, Abbildungen, Tabellenartige)
#------------------------------------------------------------------------------------

#Objekte vom Typ dict (kurz für: dictionary) sind wie Listen, nur dass wir sie mit 
#Schlüsseln (keys) und nicht mit ganzen Zahlen indizieren. Jedes hashfähige Objekt
#kann als ein solcher Schlüssel verwendet werden. Stellen Sie sich ein dictionary
#als eine Menge von Schlüssel/Wert-Paaren vor, also als Tabelle, in der jedem 
#Schlüssel (key) ein Wert (value) zugeordnet ist.

#Literale vom Typ dict werden in geschweifte Klammern eingeschlossen und jedes Element besteht
#aus einem Schlüssel, gefolgt von einem Doppelpunkt und einem Wert, z.B.

month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
                 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print(month_numbers)
print('Der dritte Monat ist ' + month_numbers[3])
dist = month_numbers['Apr'] - month_numbers['Jan']
print('Apr und Jan liegen', dist, 'Monate auseinander')

#ergibt
#   {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May'}
#   Der dritte Monat ist Mar
#   Apr und Jan liegen 3 Monate auseinander

#Das obige dictionary month_numbers können wir uns als folgende Tabelle vorstellen:
#
#       KEYS         VALUES
#    -------------------------
#       'Jan'    |    1
#       'Feb'    |    2
#       'Mar'    |    3
#       'Apr'    |    4
#       'May'    |    5
#       1        |    'Jan'
#       2        |    'Feb'
#       3        |    'Mar'
#       4        |    'Apr'
#       5        |    'May'

#Auf die Einträge in einem dictionary kann nicht über einen Index zugegriffen werden. 
#Deshalb bezieht sich month_numbers[1] eindeutig auf den Eintrag mit dem Schlüssel 1 und 
#nicht auf den zweiten Eintrag (wenn das eine Liste mit den Indizes 0, 1, 2, etc. wäre).
 
#Ob ein Schlüssel in einem dictionary definiert ist, kann mit dem in-Operator 
#getestet werden, z.B.

4 in month_numbers               #ergibt True

#Wie Listen sind auch dictionaries veränderbar. Wir können einen Eintrag hinzufügen, 
#indem wir zum Beispiel schreiben
 
month_numbers['June'] = 6
print(month_numbers) 

#oder einen Eintrag ändern, indem wir schreiben: 
 
month_numbers['May'] = 'V'
print(month_numbers)

#Dictionaries sind eine der großartigen Eigenschaften von Python. Sie verringern die 
#Schwierigkeiten beim Schreiben einer Vielzahl von Programmen erheblich. 
#Im folgenden längeren Code 5.7.1 verwenden wir beispielsweise dictionaries, um ein 
#(ziemlich schreckliches) Programm zum Übersetzen zwischen zwei Sprachen 
#(E engl. und F französ.) zu schreiben. Dieser Code 5.7.1 gibt Folgendes aus
#      Je bois "good" rouge vin, et mange pain. 
#      I drink of wine red.

#Code 5.7.1 
#---Text übersetzen (badly)---
EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
        'eat':'mange', 'drink':'bois', 'John':'Jean',
        'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
        'mange':'eat', 'bois':'drink', 'Jean':'John',
        'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translate_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word
  
def translate(phrase, dicts, direction):
    UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LC_letters = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '.,;:?'
    letters = UC_letters + LC_letters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        elif word != '':
            if c in punctuation:
                c = c + ' '
            translation = (translation +
                           translate_word(word, dictionary) + c)
            word = ''
    return f'{translation} {translate_word(word, dictionary)}'
print(translate('I drink good red wine, and eat bread.',
                dicts,'English to French'))
print(translate('Je bois du vin rouge.',
                dicts, 'French to English'))
#---

#Denken Sie daran, dass dictionaries veränderbar sind. Seien Sie also vorsichtig mit
#Seiteneffekten (also der Veränderbarkeit der dict-Elemente). Zum Beispiel

FtoE['bois'] = 'wood'
print(translate('Je bois du vin rouge.', dicts, 'French to English'))

#ergibt:
#      I wood of wine red.

#Viele Programmiersprachen enthalten keinen eingebauten Typ, der eine Abbildung von 
#Schlüsseln auf Werte bietet - also dictionaries. Stattdessen verwenden die Programmierer 
#in diesem Fall andere Typen, um eine ähnliche Funktionalität bereitzustellen. Es ist zum 
#Beispiel, relativ einfach, ein dictionary zu implementieren, indem man eine Liste 
#verwendet, in der jedes Element ein Tupel ist, das ein Schlüssel/Wert-Paar darstellt. 
#Wir können dann eine einfache Funktion key_search schreiben, die den assoziativen Abruf 
#durchführt, z.B.

def key_search(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
        return None

#Das Problem bei einer solchen Implementierung ist, dass sie rechnerisch ineffizient ist. 
#Im schlimmsten Fall muss ein Programm jedes Element der Liste untersuchen, um einen 
#einzigen Abruf durchzuführen. Im Gegensatz dazu ist die in Python integrierte dictionary-
#Implementierung schnell. Sie verwendet eine Technik - Hashing genannt -, die wir in einem
#späteren Kapitel kennenlernen werden. Beim Hashing-Verfahren ist der rechnerische Aufwand
#unabhängig von der Größe des dictionary.

#Es gibt mehrere Möglichkeiten, mit einer for-Anweisung über die Einträge in einem dictionary
#zu iterieren. Wenn d ein dictionary ist, kann eine Schleife der Form 
#    for k in d 
#die Schlüssel von d durchlaufen. Die Reihenfolge, in der die Schlüssel ausgewählt werden,
#ist dieselbe Reihenfolge, in der die Schlüssel in das Wörterbuch eingefügt wurden, z.B.

capitals = {'France': 'Paris', 'Italy': 'Rome', 'Japan': 'Kyoto'}
for key in capitals:
    print('The capital of', key, 'is', capitals[key])

#druckt
#The capital of France is Paris
#The capital of Italy is Rome
#The capital of Japan is Kyoto

#Um über die Werte (values) in einem dictionary zu iterieren, können wir die Methode values
#verwenden, z.B.

cities = []
for val in capitals.values():
    cities.append(val)
print(cities, 'is a list of capital cities')

#druckt
#     ['Paris', 'Rome', 'Kyoto'] is a list of capital cities

#Die Methode values gibt ein Objekt vom Typ dict_values zurück. Dies ist ein Beispiel 
#für ein sog. View-Objekt. Ein View-Objekt ist dynamisch, d.h. wenn sich das Objekt, 
#                              -----------
#mit dem es verknüpft ist, ändert, wird diese Änderung durch das View-Objekt sichtbar. 
#Zum Beispiel, der Code

cap_vals = capitals.values()
print(cap_vals)
capitals['Japan'] = 'Tokio'
print(cap_vals)

#druckt
#    dict_values(['Paris', 'Rom', 'Kyoto'])
#    dict_values(['Paris', 'Rom', 'Toyko'])

#In ähnlicher Weise gibt die Methode keys ein View-Objekt vom Typ dict_keys zurück,
#z.B.:

cap_keys = capitals.keys()
print(cap_keys)

#druckt
#    dict_keys(['France', 'Italy', 'Japan'])

#View-Objekte können in Listen umgewandelt werden, z.B. list(capitals.values())
#gibt eine Liste der Werte aus dem dict capitals und analog list(capitals.keys())
#gibt eine Liste der Schlüssel zurück:

print(list(capitals.values()))     #['Paris', 'Rome', 'Tokio']
print(list(capitals.keys()))       #['France', 'Italy', 'Japan']

#Um über ganze Schlüssel/Wert-Paare zu iterieren, verwenden wir die Methode items. Diese
#Methode gibt ein View-Objekt vom Typ dict_items zurück. Jedes Element eines
#Objekts vom Typ dict_items ist ein Tupel aus einem Schlüssel und dem zugehörigen Wert.
#Zum Beispiel:
 
for key, val in capitals.items():
    print(val, 'is the capital of', key)

#druckt
#    Paris is the capital of France
#    Rome is the capital of Italy
#    Tokyo is the capital of Japan



###############
#Aufgabe 5.7.a:
############### 
#Implementieren Sie eine Funktion, die folgender Spezifikation entspricht
def get_min(d):
 """d a dict mapping letters to ints returns the value in d 
    with the key that occurs first in the alphabet. 
    E.g., if d = {x = 11, b = 12}, get_min returns 12."""
###############



#Oft ist es praktisch, Tupel als Schlüssel zu verwenden. Stellen Sie sich zum Beispiel vor,
#ein Tupel der Form (flight_number, day) zu verwenden, um Flüge einer Fluggesellschaft zu
#repräsentieren. Es wäre dann einfach, solche Tupel als Schlüssel in einem dictionary zu 
#verwenden, das eine Zuordnung von Flügen zu Ankunftszeiten implementiert. Eine Liste
#hingegen kann nicht als Schlüssel verwendet werden, da Objekte vom Typ Liste nicht
#hashfähig sind.

#Wie wir gesehen haben, gibt es viele nützliche Methoden im Zusammenhang mit dictionaries, 
#darunter auch einige zum Entfernen von Elementen. Wir werden hier nicht alle aufzählen, 
#sondern werden sie in den Beispielen im weiteren Verlauf verwenden. Die folgende Tabelle
#enthält einige der nützlichsten Operationen mit dictionaries.

#     len(d)                 returniert die Anzahl der Elemente in d.
#     d.keys()               returniert ein View-Objekt der Schlüssel in d.
#     d.values()             returniert ein View-Objekt der Werte in d.
#     d.items()              returniert ein View-Objekt der (key,value)-Paare in d.
#     d.update(d1)           fügt die (key,value)-Paare aus d1 in d ein und überschreibt
#                            dabei bereits in d existierende keys.
#     k in d                 returniert True, wenn Schlüssel k in d enthalten ist.
#     d[k]                   returniert das Element in d mit dem Schlüssel k.
#     d.get(k, v)            returniert d[k], wenn k in d enthalten ist, sonst v.
#     d[k] = v               assoziiert den Wert v mit dem Schlüssel k in d.
#                            Falls bereits ein Wert mit dem Schlüssel k assoziiert ist,
#                            wird dieser Wert ersetzt.
#     del d[k]               entfernt den Schlüssel k aus d. 



#------------------------------------------------------------------------------------
#                         5.8 Dictionary Comprehension
#------------------------------------------------------------------------------------

#Die dictionary comprehension funktioniert ähnlich wie die list comprehension (s.o. Kap. 5.3.2). 
#Die allgemeine Form ist
#
#      {key: value for id1, id2 in iterable if test}
#
#Der Hauptunterschied (abgesehen von der Verwendung von geschweiften Klammern anstelle von
#eckigen Klammern) ist, dass zwei Werte verwendet werden, um jedes Element des dictionary zu
#erzeugen, und dass bei der internen Iteration zwei Werte auf einmal zurückzugeben werden. 
#Betrachten wir z.B. ein dictionary, das einige Dezimal-Ziffern auf englische Wörter 
#abbildet:

number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 10: 'ten'}

#Mit Hilfe der dictionary comprehension können wir daraus eine Abbildung von Wörtern
#zu Dezimal-Ziffern erstellen:

word_to_number = {w: d for d, w in number_to_word.items()}
print(word_to_number)

#Wenn wir entscheiden, dass wir nur einstellige Zahlen in word_to_number haben wollen, 
#können wir diese modifizierte dictionary comprehension verwenden

word_to_number = {w: d for d, w in number_to_word.items() if d < 10}
print(word_to_number)

#Nun wollen wir etwas Ehrgeizigeres versuchen. Eine Chiffre ist ein Algorithmus, 
#der einen Klartext (einen Text, der von einem Menschen leicht gelesen werden kann)
#in einen verschlüsselten (kryptischen) Text umwandelt. Die einfachsten Chiffrierungen 
#sind Substitutions-Chiffren, die jedes Zeichen im Klartext durch eine eindeutige
#     ----------------------
#Zeichenfolge ersetzen. Die Zuordnung zwischen den ursprünglichen Zeichen und den Zeichen, 
#die diese ersetzen, wird in der Kryptologie auch als "Schlüssel" bezeichnet (in Analogie 
#zu der Art von Schlüssel, die zum Öffnen eines Schlosses benötigt werden) - nicht zu 
#verwechseln mit den Schlüsseln (keys), die in Python-dictionaries verwendet werden. 
#In Python bieten dictionaries eine bequeme Möglichkeit zur Implementierung von Zuordnungen, 
#die zum Codieren und Decodieren von Text verwendet werden können.
#Eine Buch-Chiffre ist eine Chiffre, bei der der Schlüssel aus einem Buch abgeleitet wird. 
#     ------------
#So kann beispielsweise jedes Zeichen im Klartext durch den numerischen Index des ersten 
#Vorkommens dieses Zeichens im Buch (oder auf einer Seite des Buches) ersetzt werden. 
#Es wird davon ausgegangen, dass der Sender und der Empfänger der verschlüsselten Nachricht 
#sich zuvor auf ein bestimmtes Buch geeinigt haben. Aber ein Gegner, der die verschlüsselte 
#Nachricht abfängt, weiß nicht, welches Buch zur Verschlüsselung verwendet wurde.

#Die folgende Funktionsdefinition verwendet eine dictionary comprehension,
#um ein dictionary zu erstellen, das für die Verschlüsselung eines Klartextes mit
#einer Buch-Chiffre verwendet wird
 
gen_code_keys = lambda book, plain_text:{c: str(book.find(c)) for c in plain_text}
gen_code_keys("Once upon a time, in a house in a land far away,", "no is no")

#Wenn der Klartext, also plain_text, "no is no" lautet und das Buch, also book, mit 
#"Once upon a time, in a house in a land far away," beginnt, wird der Aufruf 
#gen_code_keys(book,plain_text) somit Folgendes zurückgeben
#    {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
#Beachten Sie übrigens, dass o auf sieben und nicht auf null abgebildet wird, weil o und O 
#unterschiedliche Zeichen sind. Und auch das Leerzeichen bekommt einen Code, nämlich '4'. 
#Damit haben wir ein sog. Kodierungswörterbuch, das wir für die Verschlüsselung des
#Klartexts verwenden können. Der Klartext "no is no" wird damit in "1 7 4 13 26 4 1 7" 
#verschlüsselt, wie man sich leicht (ohne ohne Programmhilfe) überlegen kann.
#Etwas weiter unten werden wir dazu aber die Funktion encoder verwenden.

#Wäre book der Text von Don Quijote, der so beginnt “In a village of La Mancha, 
#the name of which I have no desire to call to mind, there lived not long since one 
#of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, 
#and a greyhound for coursing”
#dann würde der Aufruf 

Don_Quixote = """In a village of La Mancha, the name of which I have no desire to call to mind, 
                 there lived not long since one of those gentlemen that keep a lance in the 
                 lance-rack, an old buckler, a lean hack, and a greyhound for coursing"""
gen_code_keys(Don_Quixote, "no is no")

#Folgendes Kodierungswörterbuch ergeben:
#    {'n': '1', 'o': '13', ' ': '2', 'i': '6', 's': '57'}

#Da wir nun mit obigem dictionary unser Kodierungswörterbuch haben, können wir mit Hilfe 
#der list comprehension eine Funktion encoder definieren, die ein Kodierungswörterbuch zur 
#Verschlüsselung eines einfachen Textes verwendet

encoder = lambda code_keys, plain_text:''.join(['*' + code_keys[c] for c in plain_text])[1:]

#Da Zeichen im Klartext durch mehrere Zeichen im verschlüsselten Text ersetzt werden können, 
#verwenden wir *, um die Zeichen im verschlüsselten Text (dem Chiffriertext) zu trennen. 
#Schliesslich wird der Operator .join wird verwendet, um die Liste der Zeichenketten in eine 
#einzelne Zeichenfolge zu verwandeln.

#Die Funktion encrypt verwendet dann die Funktionen gen_code_keys und encoder zur 
#Verschlüsselung eines Klartextes unter Verwendung eines Buches

encrypt = lambda book, plain_text:encoder(gen_code_keys(book, plain_text), plain_text)

#Der Aufruf 

encrypt(Don_Quixote, 'no is no') 

#liefert dann den verschlüsselten Text
#     '1*13*2*6*57*2*1*13'

#Anmerkung:
#Statt der Formulierung der Funktionen encoder und encrypt als lambda-Ausdrücke
#hätten wir natürlich auch die übliche Art der Funktionsdefinition verwenden können.
#Da sie sich aber jeweils als "Einzeiler" schreiben lassen, bieten sich hier auch 
#lambda-Ausdrücke an.

#Bevor wir diesen verschlüsselten Text wieder dekodieren können, müssen wir ein dekodierendes
#dictionary, also ein Dekodierungswörterbuch, erstellen. Das Einfachste wäre, das durch 
#die Funktion gen_code_keys erstellte Verschlüsselungswörterbuch zu invertieren, aber das 
#wäre irgendwie Betrug. Der ganze Sinn einer Buch-Chiffre besteht ja darin, dass der 
#Absender eine verschlüsselte Nachricht sendet, aber keine Informationen über die Schlüssel. 
#Das einzige, was der Empfänger braucht, um die Nachricht zu entschlüsseln, ist der Zugang 
#zu dem Buch, das der Verschlüsseler verwendet hat. 
#Die folgende Funktionsdefinition (aber wieder als Lambda-Ausdruck) verwendet eine 
#dictionary comprehension, um einen Dekodierschlüssel, also ein Dekodierungswörterbuch, 
#aus dem Buch und der verschlüsselten Nachricht cipher_text aufzubauen

gen_decode_keys = lambda book, cipher_text: {s: book[int(s)] for s in cipher_text.split('*')}

#Der Aufruf 

gen_decode_keys(Don_Quixote, '1*13*2*6*57*2*1*13')

#erzeugt dann folgenden Dekodierungssschlüssel
#    {'1': 'n', '13': 'o', '2': ' ', '6': 'i', '57': 's'}
#Damit kann man den verschlüsselten Text dann entschlüsseln (dekodieren), siehe
#Aufg. 5.8.b.

#Wenn ein Zeichen im Klartext vorkommt, aber nicht im Buch, passiert etwas Schlimmes. 
#Das von gen_code_keys erzeugte dictionary ordnet jedes solches Zeichen auf -1 ab.
#Das ist eine sinnvolle Meldung: -1 bedeutet, ich kenne dieses Zeichen nicht.
#Aber ein cipher_text der -1 enthält, wird bei der Erstellung des Dekodier-Wörterbuchs 
#mit gen_decode_keys eine -1 demjenigen Zeichen zuordnen, welches auch immer das 
#Letzte im Buch ist. Und das ist schlecht, da unsinnig. 
#Z.B.
#x kommt im Buch nicht vor:
encrypt(Don_Quixote, 'xanadu')                       #'-1*3*1*3*55*210'
#                     -                                --
#Und mit diesem cipher_text erhalten wir dann folgenden Dekodierschlüssel:
gen_decode_keys(Don_Quixote, '-1*3*1*3*55*210')      #{'-1': 'g', '3': 'a', '1': 'n', '55': 'd', '210': 'u'}
#                             --                       --------- 
#g ist das letzte Zeichen des Buchs. Es erhält den key -1. Das ist aber Quatsch,
#da g doch im Buch vorkommt. Dieses Verhalten ist unschön und Aufg. 5.8.a beschäftigt 
#sich damit, wie man dieses Probleme lösen kann.



###############
#Aufgabe 5.8.a:
############### 
#Beheben Sie das oben beschriebene Problem
#Tipp: Ein einfacher Weg, dies zu tun, besteht darin, ein neues Buch zu erstellen, 
#indem Sie etwas(?) an das ursprüngliche Buch anhängen.
###############



###############
#Aufgabe 5.8.b:
############### 
#Implementieren Sie anhand der obigen Beispiele encoder und encrypt
#die Funktionen decoder und decrypt. Benutzen Sie diese dann, um die Nachricht
# 22*13*33*155*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*155*59*11*23*11*1*57*6*209*7*11
#zu entschlüsseln, die mit der Buch-Chiffre des Anfangs von Don Quijote (s.o.) verschlüsselt 
#wurde.
###############



#------------------------------------------------------------------------------------
#                         5.9 In diesem Kapitel eingeführte Begriffe
#------------------------------------------------------------------------------------

#tuple                     Tupel
#multiple assignment       Mehrfachzuweisung
#iterable object           iterierbares Objekt
#type iterator             Iterator-Typ
#list                      Liste
#mutable type              veränderlicher Typ
#immutable type            unveränderlicher Typ
#id function               ID-Funktion
#object equality           Objekt-Gleichheit
#side effect               Seiteneffekt
#aliasing                  Aliasing
#cloning                   Klonen
#shallow copy              flache Kopie
#deep copy                 tiefe Kopie
#list comprehension        Listen comprehension
#higher-order function     Funktion höherer Ordnung
#whitespace character      Leerzeichen
#set                       Menge
#hashable type             Hashtable Typ
#dictionary                Wörterbuch
#keys                      Schlüssel
#value                     Wert
#view object               Ansichtsobjekt
#dictionary comprehension  Dictionary comprehension
#book cipher               Buch-Chiffre


#####################################################################################
#####################################################################################
#FINIS
