#tw, 14.11.2023
#--------------

#                          =======================================
#                          =======================================
#                                    DSKI-PROPÄDEUTIKUM
#                          =======================================
#                          =======================================
#
#
#    Fortgeschrittene Programmiertechniken in Python für Data Science und Machine Learning




#Hinweis: Lösungen zu den in den einzelnen Kapiteln verstreuten Aufgaben
#         findet man in der Datei -- dski_propaedeutikum_LSG.py -- 




#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                       1 - Intro
#                                  ===================



#    Infoquellen, Bücher, etc.: 
#    ..........................
#         - Michael Mayer "Python One-Liners" (dpunkt 2021)
#                         https://pythononeliners.com/
#         - Bernd Klein "Numerisches Python" (Hanser 2019)
#                       https://www.python-kurs.eu/numbuch/
#         - Christian Hill "Learning Scientific Programming with Python, 2nd ed." (Cambridge Univ. Press 2020)
#                          https://scipython.com/book2/
#         - Nicholas Rougier "From Python to Numpy" (2017, DOI: 10.5281/zenodo.225783), 
#                            https://www.labri.fr/perso/nrougier/from-python-to-numpy/
#         - TW - Adaptionen aus obigen Quellen und viele eigene Erweiterungen/Ergänzungen


#    Grundlagen der Python-Programmierung (Voraussetzung für dieses DSKI-Propädeutikum !):
#    ..................................................................................... 
#         - mein Python-Crashkurs (ausführlich, umfassend)
#           
#         - Philip Klein "Coding the Matrix"  (sehr kurz, das allernötigste)
#                 Kap. 0.5 - Introduction to Python - sets, lists, dictionaries, and comprehensions:
#                               http://codingthematrix.com/python_and_inverse_index_labs.pdf 
#                 und das Tutorial - From loop to comprehension in Python:
#                              http://codingthematrix.com/from-loop-to-comprehension.pdf       
#           


##########################################################################################
#Nur um zum Testen, ob die Infrastruktur (anaconda + vscode + python-extensions) funktioniert:

import numpy as np
import matplotlib.pyplot as plt
# evenly distributed data between 0 and 1
x = np.arange(0., 1., 0.1)
# xkcd-styled plot
plt.xkcd()
# linear, quadratic, and cubic plots
plt.plot(x, x, 'v-', x, x**2, 'x-', x, x**3, 'o-')
plt.show()
##########################################################################################


#                         _                                  
#                      (`  ).                   _           
#                     (     ).              .:(`  )`.       
#        )           _(       '`.          :(   .    )      
#                .=(`(      .   )     .--  `.  (    ) )      
#               ((    (..__.:'-'   .+(   )   ` _`  ) )                 
#        `.     `(       ) )       (   .  )     (   )  ._   
#          )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
#        )  )  ( )       --'       `- __.'         :(      )) 
#        .-'  (_.'          .')                    `(    )  ))
#                          (_  )                     ` __.:'          
#                        o    .  o  .  o .  o  .  o  .  o
#                    .
#                  .        ___
#                 _n_n_n____i_i ________ ______________ 
#                (____________I I______I I____________I 
#                /ooOOOO OOOOoo  oo oooo oo         oo 
#    -----------------------------------------------------------------                                         





#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                    2 - Python-Tricks
#                                    =================


#########################################################################################
#########################################################################################
# 2-1 Using List Comprehension to Find Top Earners
#########################################################################################

# Data
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}

# One-Liner
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]

# Result
print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Python dictionary view objects
employees.items()
employees.keys()
employees.values()
#Diese View-Objekte sind eigene Datentypen:
type(employees.items())    #dict_items
type(employees.values())   #dict_values
type(employees.keys())     #dict_keys
#Aber sie erfüllen auch das Generator-Protokoll, denn sie besitzen eine __iter__-Methode:
dir(employees.items())
#Aus Generatoren kann man immer Listen erzeugen:
list(employees.items())       #[('Alice', 100000),
                              # ('Bob', 99817),
                              # ('Carol', 122908),
                              # ('Frank', 88123),
                              # ('Eve', 93121)]
#Die Tupel aus dem View-Objekt können in einem loop sukzessive herausgeholt werden:
for (k, v) in employees.items():
    print(k,v)
#Durch Kommata getrennte Variablen oder Werte bilden letztlich immer ein Tupel:
1,2,3,4    #(1,2,3,4)
#Also können wir das auch so schreiben:
for k, v in employees.items():
    print(k,v)
#Und statt in einer Schleife können wir das auch als generator expression in einer
#list comprehension verwenden:
[(k, v) for k, v in employees.items()]
#Was eigentlich dasselbe ist wie dies:
list(employees.items()) 
#Wenn wir mit einzelnen Tupeln irgendwas (z.B. bestimmte auswählen) machen wollen, 
#bevor sie in die Liste gesteckt werden, könnte man das so schreiben:
liste = []
for k, v in employees.items():
    if v >= 100000:
        liste.append((k,v))
print(liste)  #[('Alice', 100000), ('Carol', 122908)]
#Aber mit der list comprehension kann man das alles in einer Zeile ausdrücken:
[(k, v) for k, v in employees.items() if v >= 100000]  #[('Alice', 100000), ('Carol', 122908)]
#Das ist eine superelegante, extrem komprimierte und trotzdem leicht lesbare 
#Schreibweise !!! Die Inspiration dafür stammt aus der funktionalen Programmiersprache
#Haskell, siehe https://wiki.haskell.org/List_comprehension
#Diese Sprache ist eine pure Umsetzung des sog. lambda-Kalküls, siehe
#https://de.wikipedia.org/wiki/Lambda-Kalk%C3%BCl
#Als Hommage an die Bedeutung des lambda-Kalküls wurde das Schlüsselwort für die Definition
#anonymer Funktionen in Python lambda getauft !!





#########################################################################################
#########################################################################################
# 2-2 Using List Comprehension to Find Words with High Information Value
#########################################################################################

# Data
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

# One-Liner
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

# Result
print(w)
#[[], ['Call', 'Ishmael.', 'Some', 'years', 'never', 'mind', 'long', 'precisely', 'having'], 
#['little', 'money', 'purse,', 'nothing', 'particular', 'interest'], 
#['shore,', 'thought', 'would', 'sail', 'about', 'little', 'watery', 'part'], 
#['world.', 'have', 'driving', 'spleen,', 'regulating'], ['circulation.', 'Moby', 'Dick']]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Gegeben ist ein ...
text
#... das ist der Anfang von "Moby Dick".
#Unsere Heuristik besteht darin, dass wir annehmen, dass alle Worte, die länger
#als drei Buchstaben sind, irgendwie wichtig sind. Die wollen wir rausfischen.
#Das soll aber zeilenweise geschehen. Also müssen wir den Text in seine Zeilen
#aufspalten:
text.split('\n')   #damit erhalten wir eine Liste von Zeilenstrings
#Und die Worte innerhalb dieser Zeilenstrings holen wir wieder mit split raus:
for line in text.split('\n'):
    print(line.split())
#Aber wir wollen sie nicht nur ausdrucken, sondern die Worte jeweils einer Zeile
#in eine Liste packen und die Wortlisten der jeweiligen Zeilen dann in eine
#übergeordnete Gesamtliste einfügen:
[[wort for wort in line.split()] for line in text.split('\n')]
#Da die einzelnen Zeilen ja im Prinzip auch etwas anderes als Worte enthalten könnten,
#ändern wir wort in x:
[[x for x in line.split()] for line in text.split('\n')]
#Das ist im Grunde immer noch der vollständige Text, nur eben in eine Liste von
#Zeilenlisten von einzelnen Zeichenketten x umgewandelt.
#Aber aufgrund dieser Datenstruktur können wir nun jede einzelne Zeichenkette x
#für sich genommen in strukturierter Weise betrachten und gemäß unserer 
#Heuristik (Länge 3) filtern. Und da wir zeilenweise vorgehen, wissen wir auch,
#wo ungefähr ein wichtiges Wort im Gesamttext vorkommt:
[[x for x in line.split() if len(x) > 3] for line in text.split('\n')]





#########################################################################################
#########################################################################################
# 2-3 Reading a File
#########################################################################################

# One-Liner
print([line.strip() for line in open("one_liner_2-3.py")])
# Output: <This file content>


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Der herkömmliche Weg, eine Datei zu öffnen und ihre Inhalte zeilenweise
#in eine Liste zu packen, sähe so aus:
filename = "one_liner_2-3.py" 
f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())    #strip schneidet Leerzeichen weg
f.close()
print(lines)
#oder mit dem with-Konstrukt, das sich automatisch ums Schließen der
#Datei kümmert:
lines = []
with open("one_liner_2-3.py") as file:
    for line in file:
         lines.append(line.strip())
print(lines)
#oder kürzer:
with open("one_liner_2-3.py") as file:
    lines = [line.strip() for line in file]
print(lines)
#oder am kürzesten:
print([line.strip() for line in open("one_liner_2-3.py")])
#Da wir zeilenweise durch die gesamte Datei laufen, ist die Referenz am Ende leer
#und die Datei wird automatisch geschlossen. Daher können wir uns hier sogar
#das with-Konstrukt sparen. 





#########################################################################################
#########################################################################################
# 2-4 Using Lambda and Map Functions
#########################################################################################

#Unser nächster Einzeiler erzeugt aus einer Liste von Zeichenketten eine neue Liste von Tupeln, 
#die jeweils aus einem booleschen Wert und der ursprünglichen Zeichenkette bestehen. 
#Der boolesche Wert gibt an, ob die Zeichenkette 'anonymous' in der ursprünglichen Zeichenkette 
#vorkommt! Wir nennen die resultierende Liste mark, weil die booleschen Werte die Zeichenketten-
#elemente in der Liste markieren, die die Zeichenkette "anonymous" enthalten.

# Data
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

# One-Liner
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt) #Map Funktion map(funktion,iterables)

# Result
print(list(mark))
#[(True, 'lambda functions are anonymous functions.'),
#(True, 'anonymous functions dont have a name.'),
#(False, 'functions are objects in Python.')]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Um die map-Funktion zu verstehen, wollen wir sie erstmal an einem simplen
#Beispiel erproben.
def quadriere(x):
    return x*x
#map nimmt die obige quadriere-Funktion und wendet sie schrittweise auf die Elemente
#der Liste [1,2,3,4,5] an:
map(quadriere, [1,2,3,4,5])   #<map at 0x1ce55be3640>
#map returniert einen Generator. Wenn man seinen gesamten Inhalt erzeugen und sehen
#will, muss man ihn in einen Liste packen:
list(map(quadriere, [1,2,3,4,5]))    #[1, 4, 9, 16, 25]
#also: 
quadriere(1), quadriere(2), quadriere(3), quadriere(4), quadriere(5)     #(1, 4, 9, 16, 25)
#Für unser eigentliches Problem brauchen wir aber die folgende Funktion:
def erzeuge_aus_einem_string_ein_tupel_bestehend_aus_true_und_dem_string_wenn_anonymous_enthalten_ist(s):
    if 'anonymous' in s:
        return (True,s)
    else: 
        return (False,s)
#oder kürzer unter Verwendung einer ternären if-Expression (ternary conditional operator):
def erzeuge_aus_einem_string_ein_tupel_bestehend_aus_true_und_dem_string_wenn_anonymous_enthalten_ist(s):
    return (True,s) if 'anonymous' in s else (False,s)
#Diese Funktion ist sehr, sehr speziell (wie ihr Name schon andeutet); und man wird
#sie höchstwahrscheinlich nirgendwo anders wiederverwenden können.
#Wir mappen sie jetzt auf unseren txt:
list(map(erzeuge_aus_einem_string_ein_tupel_bestehend_aus_true_und_dem_string_wenn_anonymous_enthalten_ist, txt))
#das ergibt:   [(True, 'lambda functions are anonymous functions.'),
#               (True, 'anonymous functions dont have a name.'),
#               (False, 'functions are objects in Python.')]
#Da die Funktion erzeuge_aus_... nur in map benötigt wird, verwenden wir an ihrer Stelle in map
#eine anonyme (da sie nicht wiederverwendet werden soll, braucht sie auch keinen Namen) Funktion. 
#Das Schlüsselwort zur Definition anonymer Funktionen ist lambda:
lambda s: (True,s) if 'anonymous' in s else (False,s)   #<function __main__.<lambda>(s)>
#Das ist unser function-Object. 
#Wenn wir es anwenden, sieht das z.B. so aus:
(lambda s: (True,s) if 'anonymous' in s else (False,s))('lambda functions are anonymous functions.')
#das ergibt: (True, 'lambda functions are anonymous functions.')
#Und jetzt verwenden wir diese anonyme Funktion als erstes Argument der map-Funktion und bearbeiten
#damit txt:
list(map(lambda s: (True,s) if 'anonymous' in s else (False,s), txt))
#das ergibt:  [(True, 'lambda functions are anonymous functions.'),
#              (True, 'anonymous functions dont have a name.'),
#              (False, 'functions are objects in Python.')]


#~~~~~~~~
#Aufgabe:
#~~~~~~~~
#Verwenden Sie eine list comprehension anstelle der Funktion map(), 
#um das gleiche Ergebnis zu erzielen. 
#~~~~~~~~





#########################################################################################
#########################################################################################
# 2-5 Using Slicing to Extract Matching Substring Environments
#########################################################################################

#Unser Ziel ist es, eine bestimmte Textabfrage innerhalb einer mehrzeiligen Zeichenkette 
#zu finden. Sie wollen die Abfrage im Text finden und ihre unmittelbare Umgebung zurückgeben, 
#bis zu 18 Positionen um die gefundene Abfrage herum. Das Extrahieren der Umgebung und der 
#Abfrage, ist nützlich, um den Textkontext der gefundenen Zeichenfolge zu sehen - so wie 
#so wie Google Textschnipsel um ein gesuchtes Schlüsselwort herum präsentiert.

# Data
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''

# One-Liner
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1

# Result
print(find(letters_amazon, 'SQL'))
#a fully-managed MySQL and PostgreSQL


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Erstmal ein paar Beispiele zum intuiven Verständnis der slicing-Operation:
s = 'Eat more fruits!'
print(s[0:3])         # Eat
print(s[3:0])         # (empty string '') weil unlogisch
print(s[:5])          # Eat m
print(s[5:])          # ore fruits!
print(s[:100])        # Eat more fruits!
print(s[4:8:2])       # mr 
print(s[::3])         # E rfi!
print(s[::-1])        # !stiurf erom taE
print(s[:1:-1])       # !stiurf erom t    (Die Indizierung zählt immer vorwärts !
                      #                    Es gibt ein stop-Argument 1, also laufen wir
                      #                    rückwärts bis zum a von Eat, aber das a selbst
                      #                    ist exkludiert)
print(s[6:1:-1])      # rom t             (Wir laufen rückwärts beginnend beim r von more,
                      #                    da es vorwärtsgezählt den Index 6 hat bis vor das
                      #                    a (Index 1) von Eat, d.h. das t ist noch enthalten)
#Diese Beispiele des grundlegenden [start:stop:step]-Musters des Python-Slicing 
#heben die vielen interessanten Eigenschaften der Technik hervor.
#Folgende Regeln gelten:
#     - start, stop und step sind optional, der default für step ist 1
#     - [::] bzw. [:] erzeugt eine vollständige Kopie der Liste 
#     - Wenn start >= stop und step > 0, ist das Slice leer
#     - Wenn das stop-Argument größer als die Sequenzlänge ist, wird Python 
#       die gesamte Sequenz bis einschließlich des äußersten rechten Elements 
#       herausschneiden
#     - Wenn step > 0 ist, ist der Standardstart das äußerste linke Element, und 
#       der Standardstopp ist das äußerste rechte Element (einschließlich)
#     - Wenn die Schrittweite negativ ist (step < 0), durchläuft das Slice 
#       die Sequenz in umgekehrter Reihenfolge. Bei leeren start- und stop-Argumenten 
#       wird das Slice dann vom ganz rechten Element (inklusiv) zum ganz linken 
#       Element (inklusiv) verlaufen. Wenn hingegen das Argument stop angegeben wird, 
#       wird die entsprechende Position vom Slice ausgeschlossen.
#-----
#Jetzt kommen wir zu unserer Anwendung ...
#Einen Substring in einem großen String finden, wobei der Anfangsindex im
#großen Strung returniert wird, an dem der Substring erstmals auftritt: 
treffer = letters_amazon.find('SQL')   #91
#Um den Treffer herum jeweils 18 Zeichen aus dem großen Strung herausschneiden:
letters_amazon[treffer-18:treffer+18]           #'a fully-managed MySQL and PostgreSQL'
#Und sicherheitshalber in einen ternären if-Ausdruck verpackt, um zuallererst zu
#prüfen, ob sich der Substring überhaupt im großen String befindet. 
#Dazu verwenden wir den Allzweck Operator in: 
'SQL' in letters_amazon          #True
#Und jetzt alles zusammen (wobei der Code -1 signalisieren soll, dass der Substring
#ggf. nicht gefunden werden konnte): 
letters_amazon[treffer-18:treffer+18] if 'SQL' in letters_amazon else -1
#Nun verpacken wir das in eine Funktion find:
def find(x, q):
    treffer = x.find(q)
    return x[treffer-18:treffer+18] if q in x else -1
find(letters_amazon, 'SQL')         #'a fully-managed MySQL and PostgreSQL'
#Und wenn es unbedingt ein Einzeiler sein soll:
print((lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1)(letters_amazon,'SQL'))   #'a fully-managed MySQL and PostgreSQL'





#########################################################################################
#########################################################################################
# 2-6 Combining List Comprehension and Slicing
#########################################################################################

#Unser Ziel ist es, eine kleinere, aber repräsentative Stichprobe von Daten aus 
#einem großen Datensatz zu ziehen. Jeder zweite Wert würde auch reichen.
#Wir reduzieren also den Datensatz um die Hälfte, indem wir jeden zweiten Aktienkursdatenpunkt 
#ausschließen. Wir erwarten nicht, dass diese Änderung die Genauigkeit des Modells wesentlich 
#verringert - es wird nur vergröbert.

# Data (daily stock prices ($))
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

# One-Liner
sample = [line[::2] for line in price]

# Result
print(sample)
#[[9.9, 9.8, 9.5],
# [9.5, 9.4, 9.2],
# [8.4, 7.9, 8.0],
# [7.1, 4.8, 4.7]]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Für die erste Liste in price sähe das so aus:
price[0][::2]      #[9.9, 9.8, 9.5]
#und für alle Listen in price:
[line[::2] for line in price]





#########################################################################################
#########################################################################################
# 2-7 Using Slice Assignment to Correct Corrupted Lists
#########################################################################################

#Aufgrund eines Fehlers ist jede zweite Zeichenfolge beschädigt (hier angezeigt durch den 
#String 'corrupted') und muss durch die richtige Zeichenfolge (im Beispiel sei das einfach
#der Vorgängerstring) ersetzt werden. 

# Data
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

# One-Liner
visitors[1::2] = visitors[::2]

# Result
print(visitors)
#['Firefox', 'Firefox', 'Chrome', 'Chrome', 'Safari', 'Safari',
#'Safari', 'Safari', 'Chrome', 'Chrome', 'Firefox', 'Firefox']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Durch Verwendung auf der linken Seite einer Zuweisungsanweisung kann der Slice-Operator
#dazu dienen, Teile einer Liste zu modifizieren.
#In der ursprünglichen visitors-Liste ist jedes zweite Element 'corrupted'.
#Diese fehlerhaften Elemente können wir so adressieren:
visitors[1::2]    #['corrupted', 'corrupted', 'corrupted', 'corrupted', 'corrupted', 'corrupted']
#Das start-Argument muss 1 sein, weil das erste 'corrupted' den Index 1 hat und von das aus
#gehen wir in 2-er-Schritten weiter.
#Genau diese Elemente wollen wir ersetzen durch ihre jeweiligen Vorgänger-Elemente, also:
visitors[::2]    #['Firefox', 'Chrome', 'Safari', 'Safari', 'Chrome', 'Firefox']
#Wobei hier nun das start-Argument gleich 0 ist (wenn start fehlt, ist der default-Wert 0)
#und dann wieder in 2-er-Schritten weitergegangen wird.
#Und jetzt kommt endlich das slice-Assignment: jedes zweite Element beginnend beim Index 1
#wird durch jedes zweite Element beginnend beim Index 0 ersetzt. Die zu ersetzenden Elemente
#werden durch den Slice-Operator genau adressiert und sie stehen auf der linken Seiten
#der Zuweisung:
visitors[1::2] = visitors[::2]
visitors     #['Firefox',
#              'Firefox',
#              'Chrome',
#              'Chrome',
#              'Safari',
#              'Safari',
#              'Safari',
#              'Safari',
#              'Chrome',
#              'Chrome',
#              'Firefox',
#              'Firefox']
#Natürlich könnten man die betreffenden Elemente auch durch die Werte irgendeiner 6-elementigen
#Liste ersetzen, so z.B.
visitors[1::2] = [1,2,3,4,5,6]
visitors     #['Firefox',
#              1,
#              'Chrome',
#              2,
#              'Safari',
#              3,
#              'Safari',
#              4,
#              'Chrome',
#              5,
#              'Firefox',
#              6]





#########################################################################################
#########################################################################################
# 2-8 Analyzing Cardiac Health Data with List Concatenation
#########################################################################################

#In diesem Beispiel sollen Sie die Herzrythmen von Patienten überwachen und visualisieren. 
#Für einer Reihe von Messungen, die in der Liste [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62] 
#für einen einzelnen(!) Herzzyklus gespeichert sind, möchten Sie eine Visualisierung
#erzeugen, in der dieser eine Herzzyklus 10-mal wiederholt (also kopiert) wird, um ein
#suggestiveres Bild des schlagenden Herzens zu erzeugen.
#Das Problem ist, dass der erste und die beiden letzten Werte redundant sind. Es sind einfach
#Artefakte des Messgeräts, um zu signalisieren, dass ein voller Zyklus erreicht wurde.
#für die repertierende Darstellung der Daten ist das natürlich störend.

# Dependencies
import matplotlib.pyplot as plt

# Data
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

# One-Liner
expected_cycles = cardiac_cycle[1:-2] * 10

## Result
plt.plot(expected_cycles)
plt.show()


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wenn wir die Rohdaten, also cardiac_cycle, 10-mal aneinanderhängen und das
#ganze dann plotten, sieht das so aus:
plt.plot(cardiac_cycle * 10)
plt.show()
#Die oben erwähnten Überlapp-Artefakte führen zu einem fälschlichen, kleinen "Hickser"
#zwischen den goßen Peaks. Die diesem "Hickser" zugrundeliegenden Daten müssen wir 
#entfernen:
cardiac_cycle[1:-2]               #:-2 bedeutet bis zum vorletzten Element (inkl.)
#Und dann 10-mal wiederholen:
cardiac_cycle[1:-2] * 10
#Und das ganze dann plotten:
plt.plot(cardiac_cycle[1:-2] * 10)
plt.show()





#########################################################################################
#########################################################################################
# 2-9 Using Generator Expressions to Find Companies That Pay Below Minimum Wage
#########################################################################################

#Wir wollen diejenigen Firmen rausfischen, die gegen das Mindestlohngebot (12€) verstoßen 
#haben.

# Data
companies = {
    'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
    'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
    'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}
    }

companies['CoolCompany']
for x in companies:
    print(x)
    print(companies[x])
    print(list(companies[x].values()))

# One-Liner
illegal = [x for x in companies if any(y<12 for y in companies[x].values())]

# Result
print(illegal)
#['CheapCompany', 'SosoCompany']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wir überprüfen mal nur für die Coolcompany, ob sie sich gesetzestreu verhält, also
#immer mehr als den Mindestlohn zahlt:
wagelist = list(companies['CoolCompany'].values())   
wagelist       #[33, 28, 29]
boollist = []
for i in list(wagelist):
    if i<12:
        boollist.append(True)
    else:
        boollist.append(False)
boollist     #[False, False, False]
#Die Funktion any prüft, ob sich in einer Liste boolescher Werte wenigstens einmal
#der Wert True befindet:
any(boollist)    #False
#Coolcompany ist wohl ein "Good Guy".
#Der gesamte obige Code ist sehr umständlich und wir müßten ihn für die beiden
#anderen Firmen auch noch ausführen.
#Das geht mit list-comprehensions bzw. generator expressions viel eleganter ...
#Erstmal wieder nur für CoolCompany:
list(y<12 for y in companies['CoolCompany'].values())    #[False, False, False]
any(y<12 for y in companies['CoolCompany'].values())     #False
#Und dann für alle:
[(x,any(y<12 for y in companies[x].values())) for x in companies]   #[('CoolCompany', False), 
                                                                    # ('CheapCompany', True), 
                                                                    # ('SosoCompany', True)]
#Und wenn wir nur die Namen der "Bad Guys" wissen wollen:
[x for x in companies if any(y<12 for y in companies[x].values())]  #['CheapCompany', 'SosoCompany']





#########################################################################################
#########################################################################################
# 2-10 Formatting Databases with the zip() Function
#########################################################################################

#Wie kann man eine aus einer Datenbank extrahierte Spalte mit zusätzlichen Informationen
#anreichern ? Z.B. sollen alle Elemente einer Zeile mit ihren entsprechenden
#Spaltenbeschriftungen versehen werden.

# Data
column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

# One-Liner
db = [dict(zip(column_names, row)) for row in db_rows]

# Result
print(db)
#[{'name': 'Alice', 'salary': 180000, 'job': 'data scientist'},
# {'name': 'Bob', 'salary': 99000, 'job': 'mid-level manager'},
# {'name': 'Frank', 'salary': 87000, 'job': 'CEO'}]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#zuerst ein paar vorbereitende Bemerkungen ...
#Wir werden nämlich die zip-Funktion benötigen. Was macht zip ?
#------zip-EXKURS------
#Dazu ein Bsp.:
l1 = [1,2,3]
l2 = [4,5,6]
l1_2 = zip(l1,l2)
l1_2    
#Daher der Name zip: diese Funktion wirkt wie ein Reißverschluss. Da zip einen Generator
#returniert, müssen wir diesen in eine Liste stecken, um alle Inhalte zu sehen:
l = list(l1_2)           
print(l)                 #[(1, 4), (2, 5), (3, 6)]
#Und mit Hilfe von "iterable unpacking" 
#    (siehe dazu: https://docs.python.org/3/reference/expressions.html#expression-lists 
#           und: https://stackoverflow.com/questions/50878860/python-unpack-iterator )
#und einer nochmaligen Anwendung von zip kann man die zusammengeschweißten Elemente 
#wieder auseinanderpflücken. Dazu müssen wir zuerst von l1_2 die umgebende eckige
#Klammer entfernen, d.h. die Elemente herausholen. Das machen wir mit dem unpacking 
#operator * (beachte: das funktioniert nur innerhalb von Funktionsaufrufen, 
#hier z.B. in print):
print(*l)                #(1, 4) (2, 5) (3, 6)
#Nur der Vollständigkeit halber sei erwähnt, dass unpacking auch mit Generatoren funktioniert:
print(*range(4))    #0 1 2 3
#Die mit dem upacking-Operator * entpackten Elemente von l1_2 können wir wieder der
#zip-Funktion übergeben, dadurch erhalten wir wieder die beiden ursprünglichen Listen
#l1 und l2 
#(Beachte: vorher l1_2 nochmal erzeugen, da es durchs unpacking in-place verändert wird!!!):
list(zip(*l1_2))          #[(1, 2, 3), (4, 5, 6)]
#oder 
#(Beachte: vorher l1_2 nochmal erzwugen, da es durchs unpacking in-place verändert wird!!!)
print(*zip(*l1_2))        #(1, 2, 3) (4, 5, 6)
#oder ganz ausführlich in voller Schönheit:
print(*zip(*zip(l1,l2)))  #(1, 2, 3) (4, 5, 6)
#Hieraus sieht man, dass zip in gewisser Weise seine eigene Umkehrfunktion ist.
#Einen iterable-unpacking-operator * werden wir los, wenn wir auf der linken Seite
#einer Zuweisungsanweisung das sog. "sequence unpacking" verwenden, 
#     siehe dazu: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
a,b = zip(*zip(l1,l2))
print(a, b)               #(1, 2, 3) (4, 5, 6)
#------zip-EXKURS-ENDE------
#So, jetzt kommen wir zu unserem eigentlichen Anwendungsproblem...
#Das sind die Spaltenbeschriftungen:
column_names = ['name', 'salary', 'job']
#Und hier sind drei Zeilen aus der DB-Tabelle:
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]
#Die Spaltenbeschriftungen und die Zeile 0 zippen wir zusammen. Und durch sequence unpacking
#zwingen wir den durch zip returnierten Generator dazu, seine Inhalte in entsprechende
#Variablen (hier: a,b,c) zu speichern:
a,b,c = zip(column_names,db_rows[0])
#Diese Variablen enthalten jeweils Tupel bestehend aus der jeweiligen Spaltenbeschriftung
#und dem zugehörigen Wert aus der Datenbankzeile:
print(a,b,c)      #('name', 'Alice') ('salary', 180000) ('job', 'data scientist')
#Statt einzelner Tupel wollen wir lieber ein gemeinsames Dictionary haben. Dazu packen
#wir die drei Tupel in eine Liste und übergeben diese dem dict-Konstruktor:
dict([a,b,c])     #{'name': 'Alice', 'salary': 180000, 'job': 'data scientist'}
#So, dasselbe müssen wir noch für die beiden anderen Datenbankzeilen machen, aber statt
#das alles zu wiederholen, machen wir das jetzt aus einen Schlag und elegant: 
[dict(zip(column_names, row)) for row in db_rows]
#ergibt:  [{'name': 'Alice', 'salary': 180000, 'job': 'data scientist'},
#          {'name': 'Bob', 'salary': 99000, 'job': 'mid-level manager'},
#          {'name': 'Frank', 'salary': 87000, 'job': 'CEO'}]





#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                    3 - Data Science mit numpy
#                                    ==========================



#########################################################################################
#########################################################################################
# 3-1 Basic Two-Dimensional Array Arithmetic
#########################################################################################

#Wir wollen das Problem der Gehaltsdaten von Alice, Bob und Tim angehen. Es scheint, dass 
#Bob in den letzten drei Jahren das höchste Gehalt bezogen zu haben. Aber bringt er 
#tatsächlich das meiste Geld nach Hause, wenn man die individuellen Steuersätze unserer 
#drei Freunde berücksichtigt ?

#Dieses eher triviale Problem nehmen wir zum Anlaß die NumPy-Bibliothek kennenzulernen.
#Siehe auch:  https://numpy.org/
#Das ist Pythons äußerst wichtige Bibliothek für numerische Berechnungen. Sie bildet die
#Grundlage aller Data Science-, Machine Learning- und Artificial Intelligence-Anwendungen
#in Python.
#Das Herzstück der NumPy-Bibliothek sind NumPy-Arrays, die die Daten enthalten, die Sie 
#manipulieren, analysieren und visualisieren möchten. Viele höherstufige Data Science 
#Bibliotheken wie Pandas (siehe: https://pandas.pydata.org/) bauen auf NumPy-Arrays auf, 
#entweder implizit oder explizit. 
#NumPy-Arrays sind ähnlich wie Python-Listen, haben aber einige zusätzliche Vorteile. 
#Erstens haben NumPy-Arrays einen geringeren Speicherbedarf und sind in den meisten Fällen 
#schneller. 
#Zweitens sind NumPy-Arrays praktischer, wenn man auf mehr als zwei Achsen zugreifen muss, 
#was als multidimensionale Daten bekannt ist (multidimensionale Python-Standard-Listen sind 
#sind schwer zu manipulieren und elementweise zu adressieren). Da ein NumPy-Array aus 
#mehr als einer Achse bestehen kann, denken wir bei NumPy-Arrays in Dimensionen: ein Array 
#mit zwei Achsen ist ein zweidimensionales Array. 
#Drittens haben NumPy-Arrays leistungsfähigere Zugriffsfunktionalitäten, wie z.B. Broadcasting, 
#über das wir gleich mehr erfahren werden.

# Dependencies
import numpy as np

# Data: yearly salary in (€1000) [2017, 2018, 2019]
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

# One-liner
max_income = np.max(salaries - salaries * taxation)

# Result
print(max_income)
#81.0


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Jetzt kommt erstmal ein allererster, schneller Durchritt durch numpy ...
#np ist das übliche Alias für numpy:
import numpy as np
#Ein 1-D Numpy-Array, das aus einer Standard Python-Liste erzeugt wird: 
a = np.array([1, 2, 3])
print(a)     #[1 2 3]
type(a)   #numpy.ndarray, a ist also vom Typ n-D Array
#Und ein 2-D Numpy-Array, das aus einer Liste von Liste erzeugt wird:
b = np.array([[1, 2], [3, 4]])
print(b)   # [[1 2]
           # [3 4]]
#Und schliesslich ein 3-D Numpy-Array, das aus einer Liste von Listen von Listen erzeugt wird:
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)   # [[[1 2]
           #   [3 4]]
           #  [[5 6]
           #   [7 8]]]
#Hinweis: die Dimensionalität erkennt man immer sofort an der Anzahl der äußeren Klammern!
#NumPy-Arrays sind leistungsfähiger als integrierte Python-Listen. Zum Beispiel, kann man 
#die grundlegenden arithmetischen Operatoren +, -, * und / auf zwei NumPy-Arrays anwenden. 
#Diese elementweisen Operationen kombinieren zwei Arrays a und b (zum Beispiel, Addition mit 
#dem Operator +), indem jedes Element von Array a mit dem entsprechenden Element von Array b 
#kombiniert wird. Mit anderen Worten, eine elementweise Operation aggregiert zwei Elemente, 
#die sich an den gleichen Positionen in den Arrays a und b befinden:
a = np.array([[1, 0, 0], [1, 1, 1], [2, 0, 0]])
b = np.array([[1, 1, 1], [1, 1, 2], [1, 1, 2]])
print(a + b)    # [[2 1 1]
                #  [2 2 3]
                #  [3 1 2]]
print(a - b)    # [[ 0 -1 -1]
                #  [ 0 0 -1]
                #  [ 1 -1 -2]]
print(a * b)    # [[1 0 0]
                #  [1 1 2]
                #  [2 0 0]]
print(a / b)    # [[1. 0. 0. ]
                #  [1. 1. 0.5]
                #  [2. 0. 0. ]]
#Hinweis: Wenn man NumPy-Operatoren auf Integer-Arrays anwenden will, versuchen sie, 
#Integer-Arrays als Ergebnisse zu erzeugen. Nur wenn man zwei Integer-Arrays mit dem 
#Divisionsoperator dividiert, a / b, wird das Ergebnis ein Float-Array sein. 
#Dies wird durch die Dezimalpunkte angezeigt: 2., 1., 0., 0.5
#NumPy bietet viele weitere Möglichkeiten zur Manipulation von Arrays, darunter die Funktion 
#np.max(), die den Maximalwert aller Werte in einem NumPy-Array berechnet. Die Funktion 
#np.min() berechnet den Minimalwert aller Werte in einem NumPy-Array. Die Funktion 
#np.average() berechnet den Durchschnittswert aller Werte in einem NumPy-Array:
a = np.array([[1, 0, 0], [1, 1, 1], [2, 0, 0]])
print(np.max(a))       # 2
print(np.min(a))       # 0
print(np.average(a))   # 0.6666666666666666
#Nun haben wir genügend Numpy-Grundlagen für unser obiges Anwendungsproblem ...
#Wir packen die Gehaltslisten der drei Mitarbeiter in eine Liste und erzeugen mit ihr
#dann ein Numpy-Array salaries:
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
print(salaries)   #[[ 99 101 103]
                  # [110 108 105]
                  # [ 90  88  85]]
type(salaries)  #numpy.ndarray
#Welches ist das größte Gehalt?
np.max(salaries)  #110
#Jede(r) der drei MitarbeiterInnen wird spezifisch besteuert, was ebenfalls durch ein
#Numpy-Array dargestellt werden kann. Die Reihenfolge der Besteuerungslisten entsprechen
#der Reihenfolge der Gehaltslisten:
taxation = np.array([[0.2, 0.25, 0.22], [0.4, 0.5, 0.5], [0.1, 0.2, 0.1]])
print(taxation)  #[[0.2  0.25 0.22]
                 # [0.4  0.5  0.5 ]
                 # [0.1  0.2  0.1 ]]
#Nun können wir echte Array-Arithmetik betreiben und die Nachsteuergehälter berechnen...
print(salaries - salaries * taxation)
#...und auch das größte Nachsteuergehalt bestimmen:
np.max(salaries - salaries * taxation)     #81.0





#########################################################################################
#########################################################################################
# 3-2 Working with NumPy Arrays: Slicing, Broadcasting, and Array Types
#########################################################################################

#Wir haben Gehaltsdaten für eine Vielzahl von Berufen, und wir wollen nur die Gehälter 
#der Datenwissenschaftler alle zwei Jahre um 10 Prozent erhöhen. 

## Dependencies
import numpy as np

## Data: yearly salary in (€1000) for years [2025, 2026, 2027]
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]
employees = np.array([dataScientist,
                      productManager,
                      designer,
                      softwareEngineer])

## One-liner
employees[0,::2] = employees[0,::2] * 1.1   #Beachte: andere Syntax als in Standard-Listen !!
                                            #         Hier kommt Numpy voll zur Geltung!
## Result
print(employees)
#[[143 132 150]    <-- nur die DatenwissenschaftlerInnen erhalten alle 2 Jahre einen 10%-Bonus
#  ---     ---
# [127 140 145]
# [118 118 127]
# [129 131 137]]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Dieser Einzeiler demonstriert die Leistungsfähigkeit von drei interessanten NumPy-
#Eigenschaften: Slicing, Broadcasting und Array-Typen. Diese werden wir nun
#ausführlich besprechen...
#Indizierung und Slicing in NumPy funktioniert ähnlich wie Indizierung und Slicing in 
#Standard-Python. Aber aufgrund der expliziten Multidimensionalität von Numpy-Arrays sind 
#die Möglichkeiten in Numpy gravierend erweitert.
#Wir können die Indizierung auch für ein mehrdimensionales Array verwenden, indem wir 
#den Index für jede Dimension unabhängig angeben und durch Kommata getrennte Indizes 
#für den Zugriff auf die verschiedenen Dimensionen verwenden. Zum Beispiel würde die 
#Indizierungsoperation y[0,1,2] auf das erste Element der ersten Achse (engl. axis), 
#das zweite Element der zweiten Achse und das dritte Element der dritten Achse zugreifen.
#Axis ist der Numpy-Begriff für eine spezifische Dimension. Beachte, dass dies eine neue
#Syntax ausschliesslich für Numpy-Arrays ist, die für mehrdimensionale Python-Listen 
#ungültig wäre.
#
#Slicing:
#--------
#Fahren wir mit dem Slicing in NumPy fort. Für den eindimensionalen Fall ist das identisch
#mit dem Standard-Slicing (siehe auch Kap 2-5):
import numpy as np
a = np.array([55, 56, 57, 58, 59, 60, 61])
print(a)          # [55 56 57 58 59 60 61]
print(a[:])       # [55 56 57 58 59 60 61]
print(a[2:])      #       [57 58 59 60 61]
print(a[1:4])     #    [56 57 58]
print(a[2:-2])    #       [57 58 59]
print(a[::2])     # [55    57    59    61]
print(a[1::2])    #    [56    58    60]
print(a[::-1])    # [61 60 59 58 57 56 55]
print(a[:1:-2])   # [61    59    57]
print(a[-1:1:-2]) # [61    59    57]
#Der nächste Schritt besteht darin, das multidimensionale Slicing in Numpy vollständig zu 
#verstehen. Ähnlich wie bei der Indizierung, wendet man das eindimensionale Slicing separat 
#für jede Achse (kommagetrennt) an, um einen Bereich von Elementen entlang dieser Achse 
#auszuwählen:
import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
print(a)   #[[ 0  1  2  3]
           # [ 4  5  6  7]
           # [ 8  9 10 11]
           # [12 13 14 15]]
#Dritte Spalte: 
print(a[:, 2])    # [ 2 6 10 14]        : bedeutet: alle Zeilen, und 2 bedeutet: nur die 3. Spalte
#Zweite Zeile:
print(a[1, :])    # [4 5 6 7]           1 bedeutet: zweite Zeile, und : bedeutet: alle Spalten
#Zweite Zeile, jedes zweite Element: 
print(a[1, ::2])  # [4 6]               1 bedeutet: zweite Zeile, und ::2 bedeutet: jede zweite Spalte
#Alle Spalten außer der letzten:
print(a[:, :-1])  #                     : bedeutet: alle Zeilen, und :-1 bedeutet: nur bis zur vorletzten Spalte                   
                  #[[ 0  1  2]          
                  # [ 4  5  6]
                  # [ 8  9 10]
                  # [12 13 14]]
#Die letzten beiden Zeilen nicht: 
print(a[:-2, :])   #[[ 0 1 2 3]         :-2 bedeutet: bis zur vorvorletzten Zeile, und : bedeutet: alle Spalten
                   # [ 4 5 6 7]]
#Obiges kürzer formuliert:                
print(a[:-2])      #[[ 0 1 2 3]         :-2 bedeutet: bis zur vorvorletzten Zeile, und da es bzgl. der
                   # [ 4 5 6 7]]                                                   zweiten Axis keine weiteren
#                                                                                  Anweisungen gibt, heisst
#                                                                                  dass: alle Spalten. 
#Fassen wir zusammen: man kann mit der Syntax a[slice1, slice2] ein zweidimensionales Slicing 
#vornehmen. Für jede weitere Dimension fügt man einfach eine weitere durch Kommata 
#getrennte Slicing-Operation (mit den Operatoren start:stop oder start:stop:step) ein. 
#Jedes Slicing wählt eine unabhängige Teilfolge der Elemente in seiner jeweiligen Dimension. 
#Wenn man diese Grundidee einmal verstanden hat, ist der Übergang vom eindimensionalen zum 
#mehrdimensionalen Slicing trivial.
#
#Broadcasting:
#-------------
#Broadcasting beschreibt den automatischen Prozess, mit dem zwei NumPy-Arrays in dieselbe Form 
#gebracht werden, damit Sie bestimmte elementweise Operationen anwenden können. Broadcasting 
#ist eng verwandt mit dem Shape-Attribut von NumPy-Arrays, das wiederum eng mit dem Konzept 
#der Dimensionalität/Achsen (axes) zusammenhängt. Sehen wir uns also als Nächstes Achsen, 
#Shapes und Broadcasting an. 
#Jedes Numpy-Array umfasst mehrere Achsen (engl: pl. axes, sg. axis), eine für jede Dimension:
import numpy as np
a = np.array([1, 2, 3, 4])
print(a.ndim)                                        # 1
print(a.shape)                                       #(4,)
b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
print(b.ndim)                                        # 2
print(b.shape)                                       #(3, 3)
c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
print(c.ndim)                                        # 3
print(c.shape)                                       #(2, 3, 3)
#Jedes Numpy-Array hat ein zugehöriges Shape-Attribut, ein Tupel das uns die Anzahl der Elemente 
#in jeder Achse angibt. Für ein zweidimensionales Array gibt es zwei Werte in dem Tupel: 
#die Anzahl der Zeilen und die Anzahl der Spalten. Bei höherdimensionalen Arrays gibt 
#der i-te Tupelwert die Anzahl der Elemente der i-ten Achse an. Die Anzahl der Tupel-Elemente 
#ist also die Dimensionalität des NumPy-Arrays. 
#Beachte: Wenn die Dimensionalität eines Numpy-Arrays erhöht wird (z.B. wenn man von 2D- zu 3D- 
#Arrays übergeht), wird die neue Achse zur Achse 0, und die i-te Achse des niedrigdimensionalen 
#Arrays wird zur (i + 1)-ten Achse des höherdimensionalen Arrays.
import numpy as np
a = np.array([1, 2, 3, 4])
print(a)                      # [1 2 3 4]
print(a.shape)                # (4,)
b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
print(b)                      # [[2 1 2]
                              #  [3 2 3]
                              #  [4 3 4]]
print(b.shape)                # (3, 3)
c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
print(c)                      # [[[1 2 3]
                              #   [2 3 4]
                              #   [3 4 5]]
                              #  [[1 2 4]
                              #   [2 3 5]
                              #   [3 4 6]]]
print(c.shape)                # (2, 3, 3)
#Die allgemeine Idee des Broadcasting besteht nun darin, zwei Numpy-Arrays in dieselbe Shape 
#zu bringen, indem man die Daten neu anordnet. Z.B. die elementweise Addition dieser
#beiden Arrays (die Zahl 7 wird hier als 0-D Array betrachtet) wird nicht funktionieren:
#
#                          /  1   2  \
#              7     *    |  3   4   |
#                         \  5   6  /
#
#Broadcasting ist also die Umwandlung eines niedrigdimensionalen Arrays in ein 
#höherdimensionales Array, um elementweise Operationen durchzuführen. Broadcasting
#bläht also die Zahl 7 so zu einem 3x2-Array auf, dass nun die elementweise
#Multiplikation mit dem anderen 3x2-Array möglich wird:
# 
#        / 7   7  \            / 1   2  \          /  7*1   7*2  \
#       |  7   7  |      *    |  3   4  |     =    |  7*3   7*4  |
#       \  7   7 /            \  5   6 /           \  7*5   7*6 /
#
import numpy as np
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)                      # [[1 2]
                              #  [3 4]
                              #  [5 6]]
print(a.shape)      # (3, 2)
print(a.ndim)       # 2
type(a)             #numpy.ndarray
b = 7 * a                                  # <----- hier wird Broadcast eingesetzt !!
print(b)                      # [[ 7 14]
                              #  [21 28]
                              #  [35 42]]
print(b.shape)      # (3, 2)
print(b.ndim)       # 2
type(b)             #numpy.ndarray
#Broadcasting passt also automatisch die evtl. unterschiedlichen Shapes zweier Arrays 
#so an, dass elementweise Operationen (z.B. Arithmetik) ausführbar werden. Das kann 
#natürlich nicht immer funktionieren. Die genauen Regeln fürs Broadcasting findet man 
#hier:     https://numpy.org/doc/stable/user/basics.broadcasting.html
#Eine weitere Eigenschaft von Numpy-Array ist der Datentyp ihrer Elemente. NumPy-Arrays 
#sind homogen, d. h. alle Werte haben den gleichen Typ. Hier ist eine nicht 
#vollständige Liste der möglichen Array-Element-Datentypen:
#               bool         -      Boolean data type in Python (1 byte)
#               int          -      integer data type in Python (default size: 4 or 8 bytes)
#               float        -      float data type in Python (default size: 8 bytes)
#               complex      -      complex data type in Python (default size: 16 bytes)
#               np.int8      -      integer data type (1 byte)
#               np.int16     -      integer data type (2 bytes)
#               np.int32     -      integer data type (4 bytes)
#               np.int64     -      integer data type (8 bytes)
#               np.float16   -      float data type (2 bytes)
#               np.float32   -      float data type (4 bytes)
#               np.float64   -      float data type (8 bytes)
#Weitere Infos dazu siehe: https://numpy.org/doc/stable/user/basics.types.html
#Die Array-Element-Datentypen lassen sich bei der Erzeugung eines Numpy-Arrays
#explizit spezifizieren:
import numpy as np
a = np.array([1, 2, 3, 4], dtype=np.int16)
print(a)                                        # [1 2 3 4]
print(a.dtype)                                  # int16
b = np.array([1, 2, 3, 4], dtype=np.float64)
print(b)                                        # [1. 2. 3. 4.]
print(b.dtype)                                  # float64
#Jetzt haben wir alles beisammen, um unser obiges Anwendungsproblem zu verstehen...
#Wir haben die Jahresgehälter (in T€) in drei aufeinanderfolgenden Jahren für unterschiedliche
#Berufsgruppen:
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]
#Daraus basteln wir ein 2-D Numpy-Array:
employees = np.array([dataScientist,
                      productManager,
                      designer,
                      softwareEngineer])
print(employees)   # [[130 132 137]
                   #  [127 140 145]
                   #  [118 118 127]
                   # [129 131 137]]
print(employees.shape)    # (4, 3)
print(employees.ndim)     # 2
#Hier ist jedes zweite Element der ersten Zeile. Wir benutzen multidimensionales Slicing:
employees[0, ::2]          #array([130, 137])
#Diese beiden Elemente sollen um 10% erhöht werden. Dazu benutzen wir Broadcasting:
employees[0, ::2] * 1.1    #array([143. , 150.7])
#Diese neu berechneten Werte sollen die entsprechenden Elemente in employees ersetzen.
#Dazu wenden wir nun Slice-Assignment (siehe Kap 2-7) an:
employees[0, ::2] = employees[0, ::2] * 1.1
print(employees)    # [[143 132 150]
                    #  [127 140 145]
                    #  [118 118 127]
                    #  [129 131 137]]
#Dabei fällt nun auf, dass alle Elemente von employees vom Typ Integer sind, obwohl die
#beiden veränderten Elemente eigentlich als Floats berechnet wurden 
#(siehe: array([143. , 150.7])). Und richtig, die Nachkommastellen sind in employees
#weggerundet worden.  
#Als wir das Numpy-Array erstellt hatten, erkannte NumPy, dass es nur Integer-Werte enthält, 
#und ging daher davon aus, dass es ein Integer-Array ist. Jede Operation, die Sie mit einem 
#Integer-Array durchführen, ändert den Datentyp nicht, und daher rundet Numpy auf 
#Integer-Werte ab. Das ist also eine Konsequenz der Homogenitätseigenschaft von Numpy-Arrays: 
print(employees.dtype)    # int32





#########################################################################################
#########################################################################################
# 3-3 Conditional Array Search, Filtering, and Broadcasting to Detect Outliers
#########################################################################################

#In diesem Problemfall untersuchen wir die Luftqualitätsdaten von Städten. Gegeben sei 
#ein zweidimensionales NumPy-Array mit Verschmutzungsmessungen (Spalten) für mehrere Städte 
#(Zeilen). Wir wollen diejenigen Städte finden, die überdurchschnittliche Verschmutzungs-
#messungen aufweisen.

## Dependencies
import numpy as np

## Data: air quality index AQI data (row = city)
X = np.array(
    [[ 42, 40, 41, 43, 44, 43 ], # Hong Kong
     [ 30, 31, 29, 29, 29, 30 ], # New York
     [ 8, 13, 31, 11, 11, 9 ], # Berlin
     [ 11, 11, 12, 13, 11, 12 ]]) # Montreal
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

## One-liner
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

## Result
print(polluted)
#{'Berlin', 'Hong Kong', 'New York'}


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wir wollen also untersuchen, wie man Numpy-Array-Elemente findet, die eine bestimmte 
#Bedingung erfüllen. NumPy bietet die Funktion nonzero(), die Indizes von Elementen in einem 
#Array findet, die ungleich Null sind:
import numpy as np
X = np.array([[1, 0, 0], [0, 2, 2], [3, 0, 0]])
print(X)   #[[1 0 0]
           # [0 2 2]
           # [3 0 0]]
print(X.shape)    # (3, 3)
print(np.nonzero(X))      #(array([0, 1, 1, 2], dtype=int64), array([0, 1, 2, 0], dtype=int64))
#Was bedeutet dieses Ergebnis ? In unserem 3x3-array X gibt es vier nonzero Elemente: 1,2,2,3.
#Die Koordinaten dieser vier Elemente stehen, aufgeteilt in axis 0 und axis 1 in den beiden
#returnierten Arrays [0,1,1,2] und [0,1,2,0]: die 1 steht also in X[0,0], die 2 in X[1,1],
#die andere 2 in X[1,2] und die 3 in X[2,0].
#Was bringt uns das in Bezug auf unser eigentliches Problem ? Dazu brauchen wir ein weiteres
#Konzept: "boolesche Array-Operationen in Verbindung mit Broadcasting". Gleich ein Beispiel:
#          ----------------------------------------------------------
import numpy as np
X = np.array([[1, 0, 0], [0, 2, 2], [3, 0, 0]])
print(X == 2)    #[[False False False]
                 # [False True True]
                 # [False False False]]
#Broadcasting wirkt in den unterschiedlichsten Kontexten - hier: X == 2
#Daraus wird nämlich...
#  / 1   0   0  \         / 2   2   2  \       /  1==2   0==2   0==2  \       / False   False  False  \
# |  0   2   2  |   ==   |  2   2   2  |   =   |  0==2   2==2   2==2  |   =   | False   True   True   |
# \  3   0   0 /         \  2   2   2 /        \  3==2   0==2   0==2 /        \ False   False  False /
#                   ^    ______________
#                   |          ^
#                   |          |____ das ist die Wirkung des Broadcasting: die einzelne 2 wird zu    
#                   |                                                      einem Array aufgebläht.
#                   |___ das ist der log. Gleichheitsoperator !!
#Wenn wir nun die nonzero-Funktion mit booleschem Array-Broadcasting verknüpfen ...
np.nonzero(X==2)      #(array([1, 1], dtype=int64), array([1, 2], dtype=int64))
#... nutzen wir den Umstand aus, dass False eigtl. gleich 0 und True eigtl. gleich 1 ist ...
False == 0     #True
True == 1      #True                   
#... und diese Information kann nun die Funktion nonzero ausnutzen. Sie nennt uns somit
#die Koordinaten der beiden True-Elemente im Array X==2: sie befinden sich bei X[1,1] und X[1,2].
#---
#Als letztes Konzept soll noch das sog. "Advanced Indexing" vorgestellt werden. Dabei kann
#                                       -------------------
#man eine Sequenz von Array-Indizes definieren, ohne dass es sich um ein kontinuierliches Slice 
#handeln muss. Auf diese kann man auf beliebige Elemente eines gegebenen NumPy-Arrays zugreifen, 
#indem man entweder eine Folge von Ganzzahlen (die auszuwählenden Indizes) oder eine Folge von 
#Booleans (um die spezifischen Indizes auszuwählen, bei denen der entsprechende Boolean-Wert 
#True ist) angibt. Diese Folgen müssen natürlich ebenfalls Numpy-Arrays sein:
Y = np.array([1, 2, 3, 4, 5, 6])
indices_int = np.array([1,4])
indices_bool = np.array([False, True, False, False, True, False])
Y[indices_int]      #array([2, 5])
Y[indices_bool]     #array([2, 5])
#---
#Jetzt können wir endlich zu unserem eigtl. Anwendungsproblem kommen...
#Wir haben die Luftverschmutzungsdaten aus mehreren Jahren für unterschiedliche Städte:
X = np.array(
    [[ 42, 40, 41, 43, 44, 43 ], # Hong Kong
     [ 30, 31, 29, 29, 29, 30 ], # New York
     [ 8, 13, 31, 11, 11, 9 ], # Berlin
     [ 11, 11, 12, 13, 11, 12 ]]) # Montreal
#Und wir haben die Städtenamen. Die Reihenfolge der Zeilen von X spiegelt sich in der
#Reihenfolge der Städtenamen in cities wieder:  
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])
#Was ist die durchschnittliche Luftverschutzung aller Daten aller Städte ?
print(np.average(X))      #24.333333333333332
#Mit Hilfe von Broadcasting können wir mit diesem Wert ein boolesches Array aufbauen,
#wobei Daten, die größer als dieser Mittelwert sind, zu einem True führen:
print(X > np.average(X))  #[[ True  True  True  True  True  True]
                          # [ True  True  True  True  True  True]
                          # [False False  True False False False]
                          # [False False False False False False]]
#Diese boolesche Array übergeben wir nun nonzero:
print(np.nonzero(X > np.average(X)))   #(array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2], dtype=int64), 
                                       # array([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 2], dtype=int64))
#Damit haben wir die Koordinaten der Elemente mit True-Werten im booleschen Array.
#Da wir nur die Städtenamen identifizieren wollen, die zu True-Werten gehören, reicht das 
#erste Array, das von nonzero returniert wurde. Es zeigt ja diejenigen Zeilen, in denen
#True-Werte vorgekommen sind: wir sehen, dass nur die Indizes der ersten drei Zeilen
#vorkommen, also: 0, 1, und 2. Hier ist dieses erste Array:
print(np.nonzero(X > np.average(X))[0])    #[0 0 0 0 0 0 1 1 1 1 1 1 2]
#Nun verwenden wir Advanced Slicing (s.o.), um mit dieser Folge von Indizes aus dem
#cities-Array die zugehörigen Elemente herauszufischen:
print(cities[np.nonzero(X > np.average(X))[0]])   #['Hong Kong' 'Hong Kong' 'Hong Kong' 'Hong Kong' 
                                                  # 'Hong Kong' 'Hong Kong' 'New York' 'New York' 
                                                  # 'New York' 'New York' 'New York' 'New York' 'Berlin']
#Um die Dubletten zu entfernen, verwenden wir dieses Array, um daraus einen Set (also 
#eine Menge) zu erzeugen. Mengen haben die Eigenschaft, dass in ihnen Elemente nur einmal
#vorkommen können:
print(set(cities[np.nonzero(X > np.average(X))[0]]))    #{'Berlin', 'Hong Kong', 'New York'}


#~~~~~~~~
#Aufgabe:
#~~~~~~~~
#Gehen Sie zurück zum Kap 3-1 "Basic Two-Dimensional Array Arithmetic" und ziehen Sie den 
#Namen der Person mit dem höchsten Gehalt aus der Matrix heraus, indem Sie die Idee der 
#selektiven booleschen Indizierung (boolesche Array-Operationen in Verbindung mit Broadcasting) 
#anwenden, die sie hier im Kap 3-3 kennengelernt haben. 
#Rekapitulieren Sie das Problem: Wie findet man die Person mit dem höchsten Einkommen nach 
#Steuern in einer Gruppe von Personen unter Berücksichtigung ihres Jahresgehalts und ihrer 
#Steuersätze?
#~~~~~~~~



#~~~~~~~~
#Aufgabe:
#~~~~~~~~
#Sehen Sie sich Kap 2-6 "Combining List Comprehension and Slicing" noch einmal an und 
#entwerfen Sie eine prägnantere Einzeiler-Lösung unter Verwendung der NumPy-Bibliothek. 
#Tipp: Verwenden Sie NumPy's leistungsfähigere Slicing-Fähigkeiten.
#~~~~~~~~





#########################################################################################
#########################################################################################
# 3-4 Boolean Indexing to Filter Two-Dimensional Arrays
#########################################################################################

#Gegeben sei ein zweidimensionales Array von Influencern (Zeilen), mit einer ersten Spalte, 
#die den Namen des Influencers als String definiert und einer zweiten Spalte, die die Anzahl 
#der Follower des Influencers definiert. Wir wollen daraus alle Influencer-Namen mit mehr als 
#100 Millionen Followern finden.

## Dependencies
import numpy as np

## Data: popular Instagram accounts (millions followers)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

## One-liner
superstars = inst[inst[:,0].astype(float) > 100, 1]

## Results
print(superstars)
#['@instagram' '@selenagomez' '@cristiano' '@beyonce']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Dazu müssen wir verstehen, wie "Boolean Indexing (boolesches Indizieren)" funktioniert.
#                                ----------------
#Wir hatten das bereits in Kap 3-3 unter dem allg. Oberbegriff "Advanced Indexing" 
#kennengelernt. Man kann ein Boolean-Array für einen feinkörnigen Zugriff auf ein 
#entsprechendes Daten-Array verwenden, so dass nur diejenigen Elemente des Datenarrays 
#übrig bleiben, für die das Boolean-Array an seinen entsprechenden Array-Positionen 
#True-Elemente enthält: 
import numpy as np
#Datenarray
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
#Boolean Array
indices = np.array([[False, False, True],
                    [False, False, False],
                    [True, True, False]])
print(a[indices]) # [3 7 8]
#Kommen wir nun zum eigtl. Anwendungsproblem ...
#Die erste Spalte von inst können wir so herausschneiden:
inst[:,0]    #array(['232', '133', '59', '120', '111', '76'], dtype='<U16')
#Da inst aus unterschiedlichen Datentypen erzeugt wurde (Strings und Zahlen),
#hat es insgesamt einen String-Datentyp, da dieser in diesem Fall am flexibelsten ist,
#denn nur damit lassen sich Ziffernfolgen und Texte gleichermaßen darstellen:
print(inst.dtype)    #<U16
#Infolgedessen sind die Zahlen nun Strings. So machen wir aus ihnen wieder Zahlen, ...
inst[:,0].astype(float)    #array([232., 133.,  59., 120., 111.,  76.])
#...um dann damit ein boolesches Array zu erzeugen (wie immer via Broadcasting), das uns
#diejenigen Elemente von inst rauspickt (und mit True markiert), die mehr als 100Mio 
#Follower haben:
inst[:,0].astype(float) > 100    #array([ True,  True, False,  True,  True, False])
#Mit diesem booleschen Array wenden wir nun "boolesches Indizieren" auf inst an, um die
#zugehörigen Instagram-Namen zu identifizieren:
inst[inst[:,0].astype(float) > 100, 1]   #array(['@instagram', '@selenagomez', '@cristiano', '@beyonce'], dtype='<U16')





#########################################################################################
#########################################################################################
# 3-5 Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element
#########################################################################################

#Angenommen, wir haben im Garten einen Temperatursensor installiert, der über mehrere Wochen 
#hinweg Temperaturdaten misst. Jeden Sonntag holen wir den Temperatursensor aus dem Garten, 
#um die Sensorwerte zu digitalisieren. Zwangsläufig sind die dabei gemessenen Werte 
#fehlerhaft, weil für einen Teil des Tages die Temperatur in der Wohnung 
#und nicht draußen gemessen wird. Wir wollen diese Daten nun bereinigen, indem wir jeden 
#Sonntags-Sensorwert durch den durchschnittlichen Sensorwert der vorangegangenen sieben Tage
#ersetzen.

## Dependencies
import numpy as np

## Sensor data (Mo, Tu, We, Th, Fr, Sa, Su)
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

## One-liner
tmp[6::7] = np.average(tmp.reshape((-1,7)), axis=1)

## Result
print(tmp)
#[1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Erstmal eine kurze Wdh. zum Slicing assignment (siehe auch Kap 3-2):
#                            -------
import numpy as np
a = np.array([4] * 16)
print(a)     # [4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4]
#Nun sollen ab dem zweiten Element alle 4-Werte durch 42-Werte ersetzt werden, indem
#der Slice-Operator nun auf der linken Seite der Zuweisung vorkommt und genau spezifiziert,
#was ersetzt werden soll:
a[1::] = [42] * 15
print(a)     # [ 4 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42]
#Als nächstes wollen wir auf das Konzept des "Reshaping" eingehen. Dabei wird die Shape
#                                            -----------
#eines multidimensionalen Numpy-Arrays verändert, z.B.:
a = np.array([1, 2, 3, 4, 5, 6])    #1 Zeile 6 Spalten
print(a.shape)            #(6,)
print(a.reshape((2, 3)))    # [[1 2 3]
                            #  [4 5 6]]
#Aus einem 1-D-Array ist nun ein 2-D-Array (2 Zeilen 3 Spalten) geworden.
#Das können wir auch so schreiben:
print(a.reshape((2, -1)))   # [[1 2 3]
                            #  [4 5 6]]
#Dabei reicht die Spezifikation der Anzahl der Elemente in der Zeilen-Achse (also 2)
#aus, um die vorgegebenen 6 Elemente des ursprünglichen 1-D-Arrays richtig zuverteilen.
#Dass sich Numpy selbst darum soll, wird dabei durch die -1  in reshape signalisiert.
#Als letztes müssen wir noch verstehen, was das sog. "Axis-Argument" macht. Dazu wieder...
#                                                    ---------------
#...ein Beispiel dazu:
#Angenommen, wir wollen den durchschnittlichen Aktienkurs von solar_x am Morgen, mittags und 
#abends berechnen. Grob gesagt, wir wollen alle Werte in jeder Spalte zusammenfassen, indem
#wir sie mitteln. Mit anderen Worten, wir berechnen den Durchschnitt entlang der Achse 0,
#also entlang aller Zeilen. Genau das bewirkt das Schlüsselwortargument axis=0. 
#Aktienkurse von solar_x [morgens, mittags, abends]
solar_x = np.array(
     [[1, 2, 3],  # heute
      [2, 2, 5]]) # gestern
#Aktienkurse [morgens, mittags, abends] gemittelt über die beide Tage:
print(np.average(solar_x, axis=0))     #[1.5 2. 4.]
#D.h. wir mitteln bzgl. der Zeilen (also axis=0) und zwar für jede Spalte. 
#Das Axis-Argument gibt also eine Richtung an, in der im multidimensionalen Array etwas 
#berechnet werden soll (im obigen Beispiel: der Mittelwert).  
#Nun kommen wir zum eigtl. Problem ...
#Hier sind unsere Sensordaten:
#              (Mo, Di, Mi, Do, Fr, Sa, So)
tmp = np.array([1,  2,  3,  4,  3,  4,  4,
                5,  3,  3,  4,  3,  4,  6,
                6,  5,  5,  5,  4,  5,  5])
#                                      ---
#                                       diese Spaltewerte (Sonntagsdaten) wollen wir jeweils 
#                                       durch die Mittelwerte (inkl. ebenjener Sonntagsdaten) 
#                                       ihrer zugehörigen Wochen ersetzen
#Zuerst müssen wir das 1-D-Array in ein entsprechendes 2-D-Array reshapen, damit wir eine
#Richtung via dem Axis-Argument angeben können, in der dann gemittelt wird. Wir reshapen so,
#dass wir ein 2-D-Array bekommen, das aus 3 Zeilen bestehen soll, dass können wir so
tmp.reshape((3,-1))    #array([[1, 2, 3, 4, 3, 4, 3],
                       #       [5, 3, 3, 4, 3, 4, 4],
                       #       [6, 5, 5, 5, 4, 5, 5]])
#oder so
tmp.reshape((-1,7))    #array([[1, 2, 3, 4, 3, 4, 3],
                       #       [5, 3, 3, 4, 3, 4, 4],
                       #       [6, 5, 5, 5, 4, 5, 5]])
#oder so schreiben:
tmp.reshape((3,7))     #array([[1, 2, 3, 4, 3, 4, 3],
                       #       [5, 3, 3, 4, 3, 4, 4],
                       #       [6, 5, 5, 5, 4, 5, 5]])
#Nun wollen wir den Mittelwert für jede Zeile berechnen:
np.average(tmp.reshape((-1,7)), axis=1)     #array([3., 4., 5.])
#Diese drei Mittelwerte sollen jetzt im Datenarray die Messdaten der Sonntage ersetzen.
#Dazu verwenden wir Slicing Assignment, also diese drei Werte
tmp[6::7]    #array([3, 4, 5])   d.h. wir gehen durch tmp ab dem Element mit Index 6 in 7er-Schritten
#sollen ersetzt werden:
tmp[6::7] = np.average(tmp.reshape((-1,7)), axis=1)
print(tmp)   #[1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]
             #             -             -             -    <-- diese drei Elemente sind 
             #                                                  ausgetauscht worden.
#Es fällt auf, dass die drei ausgetauschten Elemente (die ja eigtl. floats waren) nun
#als ints in tmp auftauchen wurden. Das ist automatisch passiert,
#da tmp bei seiner Erzeugung nur ints verwendete und aufgrund der der Homogenität von
#Numpy-Arrays der Datentyp ihrer Elemente nicht mehr geändert wird:
tmp.dtype     #dtype('int32')
#Wenn wir diesen Informationsverlust (mögliche Abrundung der Dezimalstellen der Mittelwerte) 
#vermeiden wollen (im obigen Beispiel haben wir zufälligerweise keine derartigen Abrundungs-
#fehler, da die Mittelwerte effektiv keine Dezimalstellen haben), müssen wir ein geeignetes, 
#neues Numpy-Array erzeugen, dessen Elemente vom Typ float sind (siehe Kap 3-2). Dazu 
#erzeugen wir tmp nochmal und spezifizieren dabei explizit den Elementtyp float64:
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5], dtype = np.float64)
tmp   #array([1., 2., 3., 4., 3., 4., 4., 5., 3., 3., 4., 3., 4., 6., 6., 5., 5., 5., 4., 5., 5.])
tmp.dtype    #dtype('float64')
#Oder wir benutzen das ursprüngliche Datenarray, dessen Elementtyp automatisch int32 ist,
#da die Elemente der zugrundeliegenden Python-Liste ints sind ...
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])
tmp.dtype    #dtype('int32')        
#... und das benutzen wir dann, um ein neues Array mit dem gewünschten Elementtyp float64
#zu erzeugen
tmp_neu = np.array(tmp, dtype = np.float64)
tmp_neu.dtype   #dtype('float64')
print(tmp_neu)  #[1. 2. 3. 4. 3. 4. 4. 5. 3. 3. 4. 3. 4. 6. 6. 5. 5. 5. 4. 5. 5.]
#Und darin wechseln wir nun die Sonntagswerte durch die Wochenmittelwerte aus:
tmp_neu[6::7] = np.average(tmp_neu.reshape((-1,7)), axis=1)
print(tmp_neu)  #[1. 2. 3. 4. 3. 4. 3. 5. 3. 3. 4. 3. 4. 4. 6. 5. 5. 5. 4. 5. 5.]
#                                   -                    -                    -
#                        Das _ sind die Mittelwerte der jeweils vorangegangenen Woche





#########################################################################################
#########################################################################################
# 3-6 When to Use the sort() Function and When to Use the argsort() Function in NumPy
#########################################################################################

#In diesem Anwendungsproblem sollen die Namen derjenigen drei Schüler mit den höchsten 
#SAT-Ergebnissen (siehe https://de.wikipedia.org/wiki/SAT_(Test) ) gefunden werden. 
#Beachte: es wird nach den Namen der Schüler gefragt und nicht nach den sortierten 
#SAT-Punktzahlen.

## Dependencies
import numpy as np

## Data: SAT scores for different students
sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])

## One-liner
top_3 = students[np.argsort(sat_scores)][:-4:-1]

## Result
print(top_3)
#['Alice' 'Frank' 'Carl']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wir benötigen wieder einige Grundlagen, um die Lösung des obigen Problems zu verstehen.
#Für das Sorting (Sortieren) bietet Numpy zwei nützliche Funktionen - sort und argsort:
#  
#                                                                       SORT
#       
#                                                                        ▲
#                                                                        │
#       
#        unsortiertes Array                                     sortiertes Array
#                                      ┌───────────┐
#         10│6│8│2│5│4│9│1             │ Sortier-  │              1│2│4│5│6│8│9│10
#       ────┼─┼─┼─┼─┼─┼─┼────   ───►   │Algorithmus│   ───►    ────┼─┼─┼─┼─┼─┼─┼────
#          0│1│2│3│4│5│6│7             │           │              7│3│5│4│1│2│6│0
#                                      └───────────┘
#        Indizes des unsortierten                         Indizes, die die Elemente des
#                    Arrays                               sortierten Arrays im unsortierten
#                                                         Array hatten
#       
#                                                                        │
#                                                                        ▼
#       
#                                                                    ARGSORT
#Codebeispiel zur obigen Abbildung:      
import numpy as np
a = np.array([10, 6, 8, 2, 5, 4, 9, 1])
print(np.sort(a))    # [ 1 2 4 5 6 8 9 10]
print(np.argsort(a)) # [ 7 3 5 4 1 2 6 0]
#Wir erstellen hier ein unsortiertes Array a, sortieren es mit np.sort(a) und erhalten die 
#ursprünglichen Indizes in ihrer neuen sortierten Reihenfolge mit np.argsort(a).
#Die sort()-Funktion von NumPy unterscheidet sich von der sort()-Funktion von Standard-Python 
#darin, dass sie auch mehrdimensionale Arrays sortieren kann, indem man die entsprechende
#Axis angibt, in deren Richtung sortiert werden soll:
#
#                                                 1 0 1
#                        Axis 1
#                        ──────►     ┌──────┐     5 1 1
#                                    │Axis 0│►
#                         1 6 2      └──────┘     8 6 2
#                  A  │
#                  x  │   5 1 1        SORT
#                  i  │
#                  s  ▼   8 0 1      ┌──────┐     1 2 6
#                                    │Axis 1│►
#                  0                 └──────┘     1 1 5
#                  
#                                                 0 1 8
#Codebeispiel zur obigen Abbildung:
import numpy as np
a = np.array([[1, 6, 2],
              [5, 1, 1],
              [8, 0, 1]])
print(np.sort(a, axis=0))     # [[1 0 1]
                              #  [5 1 1]
                              #  [8 6 2]]
print(np.sort(a, axis=1))     # [[1 2 6]
                              #  [1 1 5]
                              #  [0 1 8]]
#Jetzt können wir unser Anwendungproblem besprechen...
#Unsere Ausgangsdaten bestehen aus den SAT-Ergebnissen der Studenten als eindimensionales 
#Array und einem weiteren Array mit den entsprechenden Namen der Schüler:
sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])
#D.h. Carl hat 1343 Punkte. Wir wollen die Namen der drei besten Schüler mit den meisten
#Punkten wissen. Dazu müssen wir zuerst die Indizes der sortierten Elemente rauskriegen:
print(np.argsort(sat_scores))         #[4 3 0 1 6 5 2]
#Und hier in umgekehrter Reihenfolge:
print(np.argsort(sat_scores)[::-1])   #[2 5 6 1 0 3 4]
#Aber wir brauchen nur die ersten drei:
print(np.argsort(sat_scores)[:-4:-1]) #[2 5 6]
#Das könnten wir aber auch so schreiben:
print(np.argsort(sat_scores)[::-1][:3])
#Unter Verwendung von Numpy's "Advanced Indexing" nehmen wir dieses Array mit diesen drei 
#Indizes und erhalten damit die entsprechenden Namen der besten Schüler:
print(students[np.argsort(sat_scores)[:-4:-1]])    #['Alice' 'Frank' 'Carl']





#########################################################################################
#########################################################################################
# 3-7 How to Use Lambda Functions and Boolean Indexing to Filter Arrays
#########################################################################################

#Jetzt geht es um folgendes Anwendungsproblem: es soll eine Filter-Funktion erstellt werden, 
#die eine Liste von Büchern x und eine Mindestbewertung y annimmt und eine Liste potenzieller 
#Bestseller zurückgibt, die eine höhere Bewertung y' als die Mindestbewertung y haben: y'>y .

## Dependencies
import numpy as np

## Data (row = [title, rating])
books = np.array([['Coffee Break NumPy', 4.6],
                  ['Lord of the Rings', 5.0],
                  ['Harry Potter', 4.3],
                  ['Winnie-the-Pooh', 3.9],
                  ['The Clown of God', 2.2],
                  ['Coffee Break Python', 4.7]])

## One-liner
predict_bestseller = lambda x, y : x[x[:,1].astype(float) > y]

## Results
print(predict_bestseller(books, 3.9))
#[['Coffee Break NumPy' '4.6']
# ['Lord of the Rings' '5.0']
# ['Harry Potter' '4.3']
# ['Coffee Break Python' '4.7']]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Lambda-Funktionen haben wir bereits in den Kap 2-4 und Kap 2-5 kennengelernt.
#Man definiert dazu eine durch Komma getrennte Liste von Argumenten, die als Eingaben 
#dienen. Die Lambda-Funktion wertet dann den Ausdruck aus und gibt das Ergebnis zurück.
#Hier wollen wir untersuchen, wie wir unser Problem lösen können, indem wir eine 
#Filterfunktion unter Verwendung der Lambda-Funktionsdefinition erstellen.
#Anmerkung: wir hätten das Problem statt mit einer Lambda-Funktion auch mit einer
#ganz normalen benannten Funktion lösen können.
#Die Daten bestehen aus einem zweidimensionalen NumPy-Array, in dem jede Zeile
#den Namen des Buchtitels und die durchschnittliche Benutzerbewertung (eine Fließkommazahl 
#zwischen 0.0 und 5.0) enthält. Es gibt sechs Bücher im bewerteten Datensatz books. 
#Aufgrund der Homogenität von Numpy-Arrays werden die Zahlen der zweiten Spalte wieder
#als Strings dargestellt. Um Größenvergleiche anstellen zu können, müssen sie wieder
#in Floats umgewandelt werden: 
books[:,1].astype(float)     #array([4.6, 5. , 4.3, 3.9, 2.2, 4.7])
#Mittels Broadcasting können wir aus der Zahlenspalte dann ein boolesches Array machen:
books[:,1].astype(float) > 3.9  #array([ True,  True,  True, False, False,  True])
#Dieses boolesche Array dient dann der booleschen Indizierung, um diejenigen Buchtitel
#zu erhalten, die zu den True-werten des booleschen Arrays gehören:
books[books[:,1].astype(float) > 3.9]   #array([['Coffee Break NumPy', '4.6'],
                                        #       ['Lord of the Rings', '5.0'],
                                        #       ['Harry Potter', '4.3'],
                                        #       ['Coffee Break Python', '4.7']], dtype='<U32')
#Jetzt müssen wir das nur noch in eine Lambda-Funktion packen, die als Parameter ein
#Datenarray x (wie books) und eine Mindestbewertung y (wie 3.9) erwartet:
(lambda x,y: x[x[:,1].astype(float) > y])(books, 3.9)      #array([['Coffee Break NumPy', '4.6'],
                                                           #       ['Lord of the Rings', '5.0'],
                                                           #       ['Harry Potter', '4.3'],
                                                           #       ['Coffee Break Python', '4.7']], dtype='<U32')





#########################################################################################
#########################################################################################
# 3-8 How to Create Advanced Array Filters with Statistics, Math, and Logic
#########################################################################################

#In diesem Anwendungsproblem wird der grundlegendste Algorithmus zur Erkennung von Ausreißern 
#vorgestellt: Wenn ein Beobachtungswert um mehr als eine Standardabweichung vom Mittelwert 
#abweicht, wird er als Ausreißer betrachtet. Uns liegt hier nun ein Beispiel für die Analyse 
#von Website-Daten vor. In diesen Daten wird die Anzahl der aktiven Nutzer, die Absprungrate 
#(bounce rate) und die durchschnittliche Sitzungsdauer in Sekunden dargestellt. 
#(Die Absprungrate ist der Prozentsatz der Besucher, die nach dem Besuch nur einer Webseite 
#sofort wieder gehen. Eine hohe Absprungrate ist ein schlechtes Zeichen: Sie könnte darauf 
#hindeuten, dass eine Website langweilig oder irrelevant ist.) 
#Wir wollen uns die Daten ansehen und etwaige Ausreißer ermitteln. 

## Dependencies
import numpy as np

## Website analytics data:
## (row = day), (col = users, bounce, duration)
a = np.array([[815, 70, 115],
              [767, 80, 50],
              [912, 74, 77],
              [554, 88, 70],
              [1008, 65, 128]])
mean, stdev = np.mean(a, axis=0), np.std(a, axis=0)
print(mean, stdev)       # [811.2 76.4 88. ], [152.97764543 6.85857128 29.04479299]

## One-liner
outliers = ((np.abs(a[:,0] - mean[0]) > stdev[0])
            * (np.abs(a[:,1] - mean[1]) > stdev[1])
            * (np.abs(a[:,2] - mean[2]) > stdev[2]))

## Result
print(a[outliers])
#[[1008   65  128]]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Zuerst benötigen wir wieder etwas Grundlagen-KnowHow bzgl Mittelwert und Standardabweichung.
#Und um das konkret zu machen, brauchen wir ein paar Daten. Wir benutzen die normal-Funktion
#aus Numpy's random-Modul:
import numpy as np
sequence = np.random.normal(10.0, 1.0, 500)
print(sequence)    #[ 9.88445046  9.27531172  9.19053462 11.75036549 11.72833971 10.94635214
                   #  8.78070353  9.15631879 11.28754491 11.34652973 10.00020814  9.24923221
                   #  8.61919319  8.29573909  9.9175258  ...]  
#Das 1-D-Array sequence enthält 500 normalverteilte Zahlen mit Mittelwert mu = 10 und Standard-
#abweichung sigma = 1. Daraus können wir ein Histogramm (im xkcd-Stil, siehe: https://xkcd.com) 
#machen:
import matplotlib.pyplot as plt
plt.xkcd()
plt.hist(sequence)
plt.annotate(r"$\omega_1=9$", (9, 70))
plt.annotate(r"$\omega_2=11$", (11, 70))
plt.annotate(r"$\mu=10$", (10, 90))
plt.show()
#omega-1 = mu-sigma und omega-2 = mu + sigma, also omega-1 = 9 und omega-2 = 11.
#Alle Zahlen, die kleiner als 9 oder größer als 11 sind (also außerhalb des Intervalls 
#[omega-1, omega-2]), betrachten wir (sehr simpel!) als Ausreißer.
#Wenn die Zahlen wirklich normalverteilt sind, liegen 68.2% von ihnen innerhalb einer
#Standardabweichung sigma um den Mittelwert mu.
#Für das weitere ist auch die Bestimmung des Absolutbetrags mit Hilfe der abs-Funktion 
#hilfreich:
import numpy as np
a = np.array([1, -1, 2, -2])
print(a)   # [ 1 -1 2 -2]
print(np.abs(a))  # [1 1 2 2]
#Als letztes müssen wir uns ansehen, wie Numpy logische Operatoren (wie z.B. and oder or)
#                                              -----------------------------------------
#elementweise auf Array-Elemente anwendet und als Ergebnis boolesche Arrays zurückgibt:
import numpy as np
a = np.array([True, True, True, False])
b = np.array([False, True, True, False])
print(np.logical_and(a, b))   # [False True True False]
print(np.logical_or(a, b))    # [ True  True  True False]
#Auf diese Weise können wir boolesche Filter-Arrays (boolean filter arrays) für die Anwendung
#der booleschen Indizierung mittels boolescher Operatoren kombinieren.
#Beachte: wenn man zwei boolesche Arrays a und b multipliziert, entspricht diese Operation 
#np.logical_and(a, b). Denn Python stellt einen True-Wert als ganzzahligen Wert 1 (oder 
#wirklich jeden von 0 verschiedenen ganzzahligen Wert) und einen False-Wert als den 
#ganzzahligen Wert 0 dar. Wenn man irgendetwas mit 0 multipliziert, erhält man 0, und damit 
#False. Das bedeutet, dass man nur dann ein True-Ergebnis erhält (einen ganzzahligen Wert >1), 
#wenn alle Operanden bereits True sind:
a * b   #array([False,  True,  True, False])   -- etnspricht log. and
#Und analog gilt, dass np.logical_or(a, b) alternativ durch die Addition der beiden Arrays
#bestimmt werden kann:
a + b   #array([ True,  True,  True, False])   -- entspricht log. or
#Jetzt können wir uns das eigentliche Anwendungsproblem ansehen...
#Hier sind unsere Daten (Spalte = Benutzerzahlen, Absprungrate, Besuchsdauer):
a = np.array([[815, 70, 115],
              [767, 80, 50],
              [912, 74, 77],
              [554, 88, 70],
              [1008, 65, 128]])
#Nun berechnen wir dafür (pro Spalte genommen über alle Zeilen, also axis=0) die Mittelwerte 
#und die Standardabweichungen. Und da wir drei Spalten haben, erhalten wir also drei
#Mittelwerte und drei Standardabweichnungen:
mittelwerte, standardabweichungen = np.mean(a, axis=0), np.std(a, axis=0)
print(mittelwerte, standardabweichungen)  #[811.2  75.4  88. ] [152.97764543   7.98999374  29.04479299]
#Diese Werte benutzen wir nun, um zu prüfen, ob der Abstand eines Datenwert vom Mittelwert
#größer als eine Standardabweichung ist. Zuerst machen wir das für die erste Spalte von a, 
#also die Benutzerzahlen. Der Abstand vom Mittelwert ist einfach die Differenz (beachte: hier 
#wirkt wiedermal Broadcasting) des Datenwerts einer bestimmten Zeile in der Spalte vom
#Mittelwert: 
a[:,0] - mittelwerte[0]   #array([   3.8,  -44.2,  100.8, -257.2,  196.8])
#Und da wir die Abstände haben wollen, brauchen wir die Absolutbeträge dieser Differenzen:
np.abs(a[:,0] - mittelwerte[0])   #array([  3.8,  44.2, 100.8, 257.2, 196.8])
#Und welche dieser Abstände sind größer als eine Standardabweichung ?
np.abs(a[:,0] - mittelwerte[0]) > standardabweichungen[0]  #array([False, False, False,  True,  True])
#Wir erhalten also ein boolesches Array mit zwei True-Werten.
#Analog müssen wir für die zweite und dritte Spalte von a vorgehen:
np.abs(a[:,1] - mittelwerte[1]) > standardabweichungen[1]  #array([False, False, False,  True,  True])
np.abs(a[:,2] - mittelwerte[2]) > standardabweichungen[2]  #array([False,  True, False, False,  True])
#Eine Website (eine Zeile von a) ist dann ein Ausreißer, wenn in jedem der obigen drei 
#boolschen Arrays die Daten der betreffenden Zeile zu einem True-Wert geführt haben.
#D.h. die and-Verknüpfung der betreffenden booleschen Werte muß insgesamt ein True ergeben.
#Aus praktischen Gründen geben wir diesen drei booleschen Arrays Namen:
b1 = np.abs(a[:,0] - mittelwerte[0]) > standardabweichungen[0]
print(b1)                                                      #[False False False  True  True]
b2 = np.abs(a[:,1] - mittelwerte[1]) > standardabweichungen[1] #  |      |     |      |     |
print(b2)                                                      #[False False False  True  True]
b3 = np.abs(a[:,2] - mittelwerte[2]) > standardabweichungen[2] #  |      |     |      |     |
print(b3)                                                      #[False  True False False  True]
#Jetzt kombinieren wir sie mit Hilfe des log. and.                |      |     |      |     |
#Da die and-Funktion nur zwei Argumente hat, müssen               |      |     |      |     |
#wir sie ineinander schachteln:                                   v      v     v      v     v
print(np.logical_and(np.logical_and(b1,b2),b3))                #[False False False False  True]
#Nur die letzte Zeile hat insgesamt ein True. Sie ist daher
#ein Ausreißer.
#Statt der logical_and Funktion können wir aber auch die Multiplikation verwenden (siehe Anm.
#oben):
print(b1 * b2 * b3)   #[False False False False  True]
#Und mit diesem resultierenden booleschen Array können wir schliesslich aus dem
#Daten-Array a mittels boolescher Indizierung die Ausreißer-Zeile herausfischen:
a[b1*b2*b3]    #array([[1008,   65,  128]])   #Das ist die letzte Zeile von a,
                                              #sie beschreibt eine Website, die
                                              #unsere Ausreißer-Kriterien erfüllt.





#########################################################################################
#########################################################################################
# 3-9 Simple Association Analysis: People Who Bought X Also Bought Y
#########################################################################################

#Die Assoziationsanalyse (association analysis, collaborative filtering) basiert auf 
#historischen Kundendaten, wie z.B. "Leute, die x gekauft haben, haben auch y gekauft"-Daten 
#auf Amazon. Man nennt das auch ein "recommender system", 
#siehe: https://en.wikipedia.org/wiki/Recommender_system . 
#Diese Assoziation verschiedener Produkte ist ein leistungsfähiges Marketingkonzept, 
#denn es verbindet nicht nur verwandte, aber komplementäre Produkte miteinander, sondern 
#bietet auch ein Element des sozialen Nachweises (social proof) - zu wissen, dass andere 
#Menschen ein Produkt gekauft haben, erhöht die psychologische Sicherheit für uns, das 
#Produkt selbst zu kaufen. Das ist also ein hervorragendes Instrument für Marketing-Leute.
#Konkretes Beispiel: (Produkt-Kunden-Matrix: 4 Leute, 5 Produkte, 
#                     x: gekauft, -: nicht gekauft, ?: wird die Person das kaufen ?)
#
#                    │        │                  │          │           │
#                    │ Bücher │ Game-Controller  │ Fußball  │ Notebook  │  Kopfhörer
#           ─────────┼────────┼──────────────────┼──────────┼───────────┼─────────────
#             Alice  │   -    │        x         │    x     │     x     │      -
#           ─────────┼────────┼──────────────────┼──────────┼───────────┼─────────────
#             Bob    │   x    │        -         │    x     │     -     │      x
#           ─────────┼────────┼──────────────────┼──────────┼───────────┼─────────────
#             Louis  │   -    │        x         │    x     │     ?     │      -
#           ─────────┼────────┼──────────────────┼──────────┼───────────┼─────────────
#             Larissa│   x    │        x         │    -     │     x     │      -
#                    │        │                  │          │           │
#
#Könnte Louis an einem Notebook interessiert sein ? Sollten wir so ein Produkt empfehlen ?
#Louis zeigt ein ähnliches Kaufverhalten wie Alice. Alice hat ein Notebook gekauft.
#Die Ähnlichkeit der beiden veranlaßt das recommender system, vorherzusagen, dass eine
#gute Chance besteht, dass Louis ein Notebook kaufen wird, wenn wir ihm eine entsprechende 
#Empfehlung zukommen lassen.
#Im vorliegenden Anwendungsproblem wollen wir nun wissen, wie groß der Anteil derjenigen
#Kunden ist, die beide eBooks gekauft haben. In wievielen Zeilen kommen in der dritten und
#vierten Spalte 1sen vor ? Das ist in der vierten und achten Zeile der Fall. D.h. ein
#Viertel unserer Kunden (0.25 %) sind Leseratten.

## Dependencies
import numpy as np

## Data: row is customer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],        # <----
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])       # <----

## One-liner
copurchases = np.sum(np.all(basket[:,2:], axis = 1)) / basket.shape[0]

## Result
print(copurchases)
#0.25


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Im obigen Anwendungsbeispiel haben wir vier Produkte (Spalten) und acht Kunden (Zeilen)
#im Numpy-array basket: 0 bedeutet: nicht gekauft, 1 bedeutet: gekauft.
#Zuerst müssen wir die dritte und vierte Spalte rausschneiden:
basket[:,2:]      #array([[1, 0],
                  #       [0, 1],
                  #       [0, 0],
                  #       [1, 1],
                  #       [1, 0],
                  #       [1, 0],
                  #       [0, 1],
                  #       [1, 1]])
#Wir wollen nun für jede Zeile überprüfen, ob sie zwei Einsen enthält. Wie können dazu die 
#numpy-Funktion all einsetzen. Sie prüft, ob ein boolesches Array nur True-Werte enthält.
#Aufgrund der Äquivalenz von True/False mit 1/0 geht das aber genauso gut mit einem 
#Binär-Array:
np.all([True, True, True])      #True
np.all([True, False, True])     #False
np.all([1, 1, 1])               #True
np.all([1, 0, 1])               #False
#Wenn wir all auf die dritte und vierte Spalte von basket anwenden, müssen wird noch
#das Axis-Argument setzen: axis = 1, da all je Zeile in "Richtung der Spalten" (also auf
#beide Spalten) angewandt werden soll. D.h. die Aggregationsfunktion (hier: all) kollabiert
#bzw. faltet die spezifizierte Axis:
np.all(basket[:,2:], axis = 1)     #array([False, False, False,  True, False, False, False,  True])
#Wir sehen, dass der vierte und achte Kunde beide eBooks gekauft hat.
#Nun wollen wir den prozentualen Anteil dieser Leseratten bzgl. aller Kunden berechnen:
np.sum(np.all(basket[:,2:], axis = 1)) / basket.shape[0]    #0.25 





#########################################################################################
# 3-10 Intermediate Association Analysis to Find Bestseller Bundles
#########################################################################################

#Auch in diesem Anwendungsproblem geht es um Assoziationsanalyse mit denselben Daten wie in
#Kap 3-9. Ihr Unternehmen möchte verwandte Produkte verkaufen (einem Kunden ein zusätzliches, 
#oft verwandtes Produkt zum Kauf anbieten). Für jede Kombination von Produkten müssen wir 
#berechnen, wie oft sie von ein und demselben Kunden gekauft wurden (also in wievielen Zeilen
#von basket werden z.B. course 1 und ebook 2 gekauft ? Antw.: in den beiden letzen Zeilen). 
#Wenn wir das für jede mögliche Paarkombination machen, dann können wir rauskriegen, 
#welches Produktpaar am häufigsten zusammen gekauft wurde.

## Dependencies
import numpy as np

## Data: row is customer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

## One-liner
copurchases = [(i,j,np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)]
print(copurchases)    #[(0, 1, 4), (0, 2, 2), (0, 3, 2), (1, 2, 5), (1, 3, 3), (2, 3, 2)]

## Result
print(max(copurchases, key=lambda x:x[2]))
#(1, 2, 5)        #Erläuterung: 1,2 sind die (Spalten-(Indizes der zusammen am häufigsten gekauften
                  #Produkte; und 5 ist deren Häufigkeit


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Im Kern ist das ein kombinatorisches Problem, in dem aus einem Vierervektor alle möglichen 
#Zweier-Kombinationen von Elementen gebildet werden. Die Tupel enthalten immer die Indizes
#eines Paars von Elementen, wobei das Element-Paar (i,j) natürlich gleich dem 
#Element-Paar (j,i) sein muss. Die Reihenfolge der Elemente in einem Paar ist also irrelevant.
#Welche Möglichkeiten gibt es, zwei aus vier Elementen auszuwählen unabhängig von der 
#Reihenfolge und ohne das ausgewählte Element wieder in den Vierer-Vektor zurückzulegen ?
#Der Vierervektor bestehe aus den vier Elementen 
#                 [a, b, c, d]
#mit den Indizes   0  1  2  3
#Wir betrachten hier nun die Indizes statt der Elemente selbst.                            
#Wir machen das jetzt mal ganz explizit mit folgenden Fallunterscheidungen:
#(i)   Falls wir beim ersten Zug die 0 gezogen haben, bleiben beim zweiten Zug noch 
#      die Möglichkeiten [1, 2, 3], so daß wir insgesamt die Zweier-Tupel: (0,1) (0,2) (0,3) 
#      bekommen.
#(ii)  Falls wir beim ersten Zug die 1 gezogen haben, bleiben beim zweiten Zug noch die 
#      Möglichkeiten [2, 3]. Warum nicht [0, 2, 3] ? Antw: weil wir den Index 0 bereits in
#      Fall i) abgehandelt haben. Alle Möglichkeiten, die die 0 enthalten sind durch Fall i)
#      bereits berücksichtigt. Also erhalten wir in Fall ii) die Zweier-Tupel: (1,2) (1,3).
#      Sie stellen weitere Tupel-Kombinationen dar, die nicht schon in i) vorhanden sind.
#(iii) Falls wir beim ersten Zug die 2 gezogen haben, bleiben beim zweiten Zug noch die
#      Möglichkeit [3] (analog zur Begründung wie bei ii)). Also erhalten wir in Fall iii)
#      das Zweier-Tupel: (2,3)  
#Das sind also alle Möglichkeiten zwei unterschiedliche Indizes ohne Berücksichtigung der
#Reihenfolge zu ziehen: (0,1) (0,2) (0,3) (1,2) (1,3) (2,3)
#Insgesamt 6 Möglichkeiten.
#Was wir uns hier gerade überlegt haben, ist natürlich ein Grundmodell der Kombinatorik: 
#    https://de.wikipedia.org/wiki/Urnenmodell#Ziehen_ohne_Zur%C3%BCcklegen_ohne_Beachtung_der_Reihenfolge
#Die Anzahl der Wahlmöglichkeiten in diesem Urnenmodell sind also durch den Binomial-
#koeffizienten gegeben:
#    https://de.wikipedia.org/wiki/Binomialkoeffizient
#
#           /  n \              n! 
#          |     |    =    -------------
#          \  k /           k! * (n-k)!
#
#Auf unseren speziellen Fall übertragen heißt das:
#
#           /  4 \                4!               24 
#          |     |    =    -------------   =   --------   =   6
#          \  2 /            2! *(4-2)!          2 * 2
#
#Und so können wir diese Wahlmöglichkeiten durch Code darstellen:
[(i,j) for i in range(4) for j in range(i+1,4)]   #[(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
#Übertragen wir dies nun auf unser Anwendungsproblem...
#Die 4 Elemente unseres Vierervektors sind die Spalten von basket. Jede Spalte entspricht 
#einem Produkt. Nehmen wir z.B. mal Spalte 0 und Spalte 1. Wenn wir diese beiden Spalten 
#addieren und das für alle Zeilen tun, erhalten wir...
basket[:,0] + basket[:,1]    #array([1, 0, 2, 1, 2, 1, 2, 2])
#...d.h. wir erhalten einen Überblick, welche Kunden diese beiden Produkte zusammen gekauft 
#haben. Das sind diejenigen, bei denen eine 2 steht. Nun machen wir daraus ein boolesches 
#Array. Jede 2 soll einem True entsprechen, alles andere ist False:
basket[:,0] + basket[:,1] == 2   #array([False, False,  True, False,  True, False,  True,  True])
#Da True 1 entspricht und False 0 entspricht, führt die Summe der Elemente dieses Arrays
#zu der Anzahl der Kunden, die diese beiden Produkte zusammen gekauft haben: 
np.sum(basket[:,0] + basket[:,1] == 2)    #4
#Das machen wir nun für alle 6 kombinatorischen Spalten-Paarbildungen und damit wir den 
#Überblick behalten, protokollieren wir auch immer, welche Spaltepaare wir gerade betrachten:
[(i,j, np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)] 
#=> [(0, 1, 4), (0, 2, 2), (0, 3, 2), (1, 2, 5), (1, 3, 3), (2, 3, 2)]
#Dabei bezeichnen in jedem dieser Tupel die ersten beiden Zahlen die ausgewählten Spalten
#(also die Produktpaare) und die dritte Zahl bzeichnet die Anzahl der Kunden, die diese
#Produktpaare gekauft haben.
#Welches Produktpaar kommt am häufigsten vor ? Dazu müssen wir jeweils die dritten Zahlen
#aller Tupel betrachten und dasjenige finden, dessen dritte Zahl am größten ist.
#Versuch 1:
#..........
#So geht das jedenfalls nicht. 
max([(i,j, np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)])
#=> (2, 3, 2)     wir erhalten damit nämlich das Tupel, dessen Summe(!) am größten ist.
#                 Die größte Summe interessiert uns aber nicht. 
#Versuch 2:
#..........
#Die aufwendige Lösung mit Standard-Python-Techniken.
maximum = 0
maxidx = 0
for index,(x,y,z) in enumerate([(i,j, np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)]):
    print('Index:', index, 'Tupel:', x,y,z)
    if z > maximum:
        maximum = z
        maxidx = index
print(maxidx, maximum)      #3 5     d.h. das vierte Tupel (mit dem Index 3) 
                            #        hat als dritte Zahl die 5. Und das ist die
                            #        größte dritte Zahl bzgl. aller Tupel 
#Versuch 3:
#..........
#Sehen wir uns nochmal die max-Funktion an, siehe: https://docs.python.org/3/library/functions.html#max
#Sie erwartet nicht nur ein iterable (also eine sequentielle Datenstruktur oder einen
#Generator), sondern optional ein Funktionsobjekt, das an das key-Argument gebunden wird.
#Der default für key ist None. Die offizielle Doku ist nicht so erhellend, also
#Stackoverflow: https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression/
#Hier lernen wir, dass man eine Funktion angeben kann, mit deren Hilfe eine gewünschte
#Ordnungsrelation realisiert wird (also eine Funktion, die von max verwendet wird, um zu
#entscheiden, ob zwei Datenwerte des iterables größer oder kleiner zueinander sind).
#Wie nutzen wir das nun ?
#Unsere Liste besteht aus Dreier-Tupeln. Wir suchen das Tupel, dessen drittes Element
#unter den dritten Elementen aller Tupel am größten ist. Die Vergleichsfunktion, mit der
#max arbeiten soll, muss also aus einem Tupel das dritte Element rausholen:
def hole_drittes_element_raus(tpl):
    return tpl[2]
max([(1,2,3), (4,5,6), (6,5,4), (3,2,1)], key=hole_drittes_element_raus)    #(4, 5, 6)
#Das kann man auch kürzer mittels lambda-Funktion schreiben: 
max([(1,2,3), (4,5,6), (6,5,4), (3,2,1)], key=lambda x: x[2])               #(4, 5, 6)
#Jetzt haben wir alles beisammen:
max([(i,j, np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)], key=lambda x: x[2])
#=> (1, 2, 5)

   



#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                    4 - Machine Learning mit scikit-learn
#                                    =====================================





#Hier ist mal ein grober, unvollständiger Überblick zu Python-Bibliotheken für Numerik, 
#Datenverwaltung, Computeralgebra, ML, DL, PP, LLM bis hin zu den Model-Repositories 
#von Kaggle und Huggingface und der KI-Forschung von OpenAI, DeepMind, Google's Brain-Projekt 
#und Aleph-Alpha (in Deutschland):

#https://numpy.org/           <-----------------------|
#https://scikit-learn.org     <----------------|      |
#https://pandas.pydata.org                     |      |
#https://scipy.org                             |      |
#https://www.sympy.org                         |      |
#https://pytorch.org          <--------------- | ---- | ---------------------------|
#   https://github.com/skorch-dev/skorch   ----|      |                            |         
#https://jax.readthedocs.io                -----------| <-----------------|        |
#   https://en.wikipedia.org/wiki/Google_JAX                              |        |
#   https://www.deepmind.com/blog/using-jax-to-accelerate-our-research    |        |
#   https://github.com/google/flax                                        |        |
#https://www.pymc.io                                                      |        |
#https://pyro.ai                           ----------------------------------------|
#   https://github.com/pyro-ppl/numpyro    -------------------------------|
#https://www.kaggle.com/
#https://huggingface.co/
#https://openai.com
#   https://openai.com/research/research
#   https://openai.com/product
#   https://chat.openai.com
#   https://github.com/openai/openai-python
#https://www.deepmind.com
#   https://www.deepmind.com/blog
#https://research.google/teams/brain/
#https://www.aleph-alpha.com/

#Wir lernen in diesem Abschnitt 4 das Machine-Learning-Framework scikit-learn kennen,
#siehe: https://scikit-learn.org
#Auf dieser Website finden wir folgende Selbstbeschreibung:
#      "Scikit-learn is an open source machine learning library that supports 
#      supervised and unsupervised learning. It also provides various tools 
#      for model fitting, data preprocessing, model selection, model evaluation, 
#      and many other utilities."





#########################################################################################
#########################################################################################
# 4.1 Linear Regression
#########################################################################################

#Regression beschreibt die statistische Abhängigkeit abhängiger Größen von unabhängigen Größen.
#Wenn die abhängigen und die unabhängigen Größen kontinuierlich sind, hat die Beschreibung
#des Zusammenhangs zwischen abhängigen und unabhängigen Größen den Charakter einer
#Funktionsapproximation. 
#Die lineare Regression ist ein Algorithmus des maschinellen Lernens, den man am häufigsten 
#in Tutorials zum maschinellen Lernen für Anfänger findet. Er wird üblicherweise verwendet bei 
#Problemen, bei denen das Modell fehlende Datenwerte durch Verwendung vorhandener Werte 
#ermitelt. Ein großer Vorteil der linearen Regression, ist ihre Einfachheit. Das heißt aber 
#nicht, dass sie keine echten Probleme lösen kann! Die lineare Regression hat viele praktische 
#Anwendungsfälle in verschiedenen Bereichen wie Marktforschung, Astronomie und Biologie etc.,
#siehe auch: https://de.wikipedia.org/wiki/Lineare_Regression
#Wie kann man mit Hilfe der linearen Regression die Aktienkurse an einem bestimmten Tag 
#vorhersagen? In unserem Aktienkursbeispiel sind unsere Trainingsdaten die Indizes von 
#diesen drei Tagen [0, 1, 2], an denen die Aktienkursen diese Werte haben [155, 156, 157].
#Um die Linie zu finden, die die Daten am besten beschreibt, und somit ein lineares 
#Regressionsmodell zu erstellen, müssen wir die Koeffizienten bestimmen. Hier kommt das 
#maschinelle Lernen ins Spiel. Es gibt zwei Hauptmethoden zur Bestimmung der Modellparameter 
#für die lineare Regression. 
#Erstens kann man die Linie der besten Anpassung analytisch berechnen, die zwischen diesen 
#Punkten verläuft (die Standardmethode für lineare Regression). 
#Zweitens können wir verschiedene Modelle ausprobieren, indem man jedes anhand der 
#beschrifteten Beispieldaten testet und sich schließlich für das beste Modell entscheidet. 
#In jedem Fall wird das "beste" Modell durch einen Prozess ermittelt, der als Fehlerminimierung 
#(error minimization) bezeichnet wird. Dabei minimiert das Modell die quadratische Differenz 
#(oder wählt die Koeffizienten aus, die zu einer minimalen quadratischen Differenz führen) 
#zwischen den vorhergesagten Modell Werten und der idealen Ausgabe und wählt so das Modell 
#mit dem geringsten Fehler aus.
#Für unsere Daten ergeben sich Koeffizienten von b = 155.0 und m = 1.0, wobei b der
#y-Achsenabschnitt und m die Steigung der Geraden ist:  
#
#         y = f(x) = x + 155
#
#Die Trainingsdaten und die Regressionsgerade können wir plotten:
import matplotlib.pyplot as plt
plt.xkcd()
plt.plot([155, 156, 157],'-')
plt.annotate(r"Punkt 0", (0, 155))
plt.annotate(r"Punkt 1", (1, 156))
plt.annotate(r"Punkt 2", (2, 157))
plt.show()
#Wie man dem Plot entnimmt: perfekte Passung! Der quadratische Abstand zwischen der Linie 
#(Modellvorhersage) und den Trainingsdaten ist Null - wir haben also das Modell gefunden, 
#das den Fehler minimiert. Mit diesem Modell können wir nun den Aktienkurs für jeden 
#beliebigen Wert von x vorhersagen. Nehmen wir an, wir möchten den Aktienkurs für den Tag 
#x = 4 vorhersagen. Um dies zu erreichen, berechnen wir mit Hilfe des Modells einfach 
#f(x) = 155.0 + 1.0 ×  = 159.0. Der vorhergesagte Aktienkurs am Tag 4 beträgt 159 $. 
#Ob diese Vorhersage die Realität widerspiegelt, ist natürlich eine ganz andere Frage.
#Und etwas Analoges macht unser folgendes Anwendungsbeispiel. Für die neuen x-Werte
#3 und 4 soll das Modell Aktienkursdaten (also y-Werte) vorhersagen:

## Dependencies
from sklearn.linear_model import LinearRegression
import numpy as np

## Data (Stock prices)
stock = np.array([155, 156, 157])
n = len(stock)

## One-liner
model = LinearRegression().fit(np.arange(n).reshape((n,1)), stock)

## Result
print(model.predict([[3],[4]]))
#[158. 159.]

#Die Trainingspunkte und die durch die lineare Regression bestimmten Vorhersagepunkte
#können wir nun zusammen plotten:
import matplotlib.pyplot as plt
plt.xkcd()
plt.plot([155, 156, 157, 158, 159],'-')
plt.annotate(r"Trainingspunkt 0", (0, 155))
plt.annotate(r"Trainingspunkt 1", (1, 156))
plt.annotate(r"Trainingspunkt 2", (2, 157))
plt.annotate(r"Vorhersagepunkt 3", (3, 158))
plt.annotate(r"Vorhersagepunkt 4", (4, 159))
plt.show()


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Da dem ganzen die Klasse LinearRegression von sklearn zugrundeliegt, ist es sicher sinnvoll,
#dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#Zuerst haben wir ein Numpy-Array mit den drei Trainingsdaten erstellt und auch die
#Länge des Datensatzes in der Variablen n gespeichert:
stock = np.array([155, 156, 157])
n = len(stock)
#Diese Daten stellen drei Aktienkurswerte an drei aufeinanderfolgenden Tagen dar.
#Um das Regressionsmodell aufzubauen, brauchen wir aus sklearn das Modul linear_model
#und daraus die Klasse LinearRegression, die wir mit dem Aufruf des Konstruktors
#instanzieren: LinearRegression().
#Um damit dann das Modell zu trainieren, brauchen wir die fit-Funktion (fit, engl. anpassen). 
#fit hat zwei Argumente: den input-Teil der Trainingsdaten und den output der Trainingsdaten,
#also die realen Aktienkurswerte in unserem Beispiel. Aber für das input-Argument von fit
#wird ein Array folgender Form benötigt:
#  
#      [<training_data_1>,
#       <training_data_2>,
#       ...
#       <training_data_n>]
#
#      wobei jedes dieser Elemente diese Form hat:
#           <training_data> = [feature_1, feature_2, ..., feature_k]
#
#Übertragen auf unser Beispiel heißt das, dass der input nur aus einem feature x besteht,
#nämlich dem jeweiligen Tag. Der input hat also diese seltsame Form:
#
#            [[0],
#             [1],
#             [2]]
#
#Das ist eine 2-D-Matrix, die nur aus einer einzigen Spalte besteht.
#Auch in Numpy gibt es das Analogon zur range-Funktion von Standard-Python. Es heißt: arange.
#Damit erzeugen wir ein Numpy-Array bestehend aus Integer-Elementen im Bereich 0 bis 2:
np.arange(n)     #array([0, 1, 2])
#Dieses Array hat aber für die Verwendung in fit noch nicht die richtige Shape. Wir müssen
#daraus mit Hilfe von reshape (siehe dazu Kap 3-5) ein 2D-Matrix mit einer Spalte machen:
np.arange(n).reshape((n,1))    #array([[0],
                               #       [1],
                               #       [2]])
#Insgesamt wird unser Regressionsmodell so erzeugt:
model = LinearRegression().fit(np.arange(n).reshape((n,1)), stock)
#                              --------------------------   -----
#                                        ^                    ^
#                                        |                    |
#                                     input                output
#
#Jetzt können wir das trainierte Modell für Vorhersagen (predictions) nutzen:
model.predict([[3],[4]])    #array([158., 159.])
#Die predict-Funktion von LinearRegression hat dieselben Anforderungen an ihr
#einziges Argument wie die beim input-Argument der fit-Funktion: deshalb die 
#seltsame Form: [[3],
#                [4]]
#Das ist wieder eine 2-D-Matrix mit nur einer einzigen Spalte. Wir wollen vom Modell für 
#beiden neuen Inputwerte (also die Tage 3 und 4) wissen, welche Aktienkurswerte zu erwarten 
#sind. Da unsere Fehlerminimierung gleich Null war, erhalten wir perfekt lineare Outputs 
#von 158 und 159. Dies passt perfekt zur Regressionslinie im obigen Plot (Vorhersagepunkte 
#3 und 4). 
#Aber es ist oft nicht möglich, ein perfekt passendes einzelnes lineares Modell zu finden. 
#Wenn unsere Aktienkurse zum Beispiel [157, 156, 159] sind, und man wenn man mit diesen Daten
#wieder eine Regressionsmodell trainiert und damit dann für die Tage 3 und 4 Vorhersagen
#berechnet, sieht das so aus:
from sklearn.linear_model import LinearRegression
import numpy as np
stock = np.array([157, 156, 159])
n = len(stock)
model = LinearRegression().fit(np.arange(n).reshape((n,1)), stock)
print(model.predict([[3],[4]]))     #[159.33333333 160.33333333]
#Plotten der obigen Trainingsdaten und der Vorhersagen:
import matplotlib.pyplot as plt
plt.xkcd()
plt.plot([157, 156, 159, 159.3, 160.3],'*')
plt.annotate(r"Trainingspunkt 0", (0, 157))
plt.annotate(r"Trainingspunkt 1", (1, 156))
plt.annotate(r"Trainingspunkt 2", (2, 159))
plt.annotate(r"Vorhersagepunkt 3", (3, 159.3))
plt.annotate(r"Vorhersagepunkt 4", (4, 160.3))
plt.plot([0,3,4],[model.predict([[0]]),159.3, 160.3],'-')  #ein Hack, um die Linie plotten zu können
plt.show()
#In diesem Fall findet die Funktion fit() auch eine Lineare Funktion, die den quadratischen 
#Fehler zwischen den Trainingsdaten minimiert. Aber im Gegensatz zum vorigen Beispiel ist
#der quadratische Fehler nicht 0 (die Trainingspunkte liegen nicht auf der Regressions-
#geraden (orange)).





#########################################################################################
#########################################################################################
# 4.2 Logistic Regression in One Line
#########################################################################################

#Die logistische Regression wird in der Regel für Klassifizierungsprobleme verwendet, 
#bei denen man vorhersagen will, ob eine Stichprobe zu einer bestimmten Kategorie (oder 
#Klasse) gehört. Wikipedia ist dazu leider nur bedingt erhellend, dennoch sei darauf verwiesen:
#               https://de.wikipedia.org/wiki/Logistische_Regression 
#
#Dies ist anders als bei (linearen) Regressionsproblemen (z.B. Kap 4.1), bei denen man 
#eine Stichprobe erhält und dazu dann einen numerischen Output-Wert vorhersagen kann, 
#der in einen kontinuierlichen Bereich fällt.
#Was aber macht man, wenn der Output nicht kontinuierlich, sondern kategorisch ist und zu 
#einer begrenzten Anzahl von Gruppen oder Kategorien gehört? Nehmen wir zum Beispiel an, wir 
#wollen die Wahrscheinlichkeit von Lungenkrebs vorhersagen in Abhängigkeit von der Anzahl 
#der Zigaretten, die ein Patient täglich raucht. Jeder Patient kann entweder Lungenkrebs 
#haben oder nicht. Im Gegensatz zur Vorhersage der linearen Regression (Kap 4-1) haben wir 
#hier nur diese beiden möglichen Ergebnisse. D.h. für eine (mehr oder weniger) kontinuierliche 
#Input-Größe (z.B. Zigarettenanzahl) wollen wir eine binäre Vorhersage erzwingen (Lungenkrebs 
#ja oder nein). So könnten typische Daten (x = Patient hat Lungenkrebs, o = Patient ist 
#krebsfrei) für unser Lungenkrebsbeispiel aussehen:
#
#                             ▲
#                             │
#                             │
#                             │
#                x Lungenkrebs│    x             x       x  x xxxxxxxxxx           --> "1"
#                             │                         ------------------
#                             │                       ---
#                             │                     ---
#                             │                   --    Sigmoide Fkt.
#                             │                 --
#                             │              ----
#                             │   ------------
#                 o kein Krebs│ oooooooooooo  o      o        o                    --> "0"
#                             │
#                             │
#                             └──────────────────────────────────────────►
#                                               Anzahl tgl. Zigaretten
#
#Wie kann man diese Daten beschreiben ? Antw.: Man versucht, eine S-förmige Funktion (s.o. ---)
#anzupassen. Während die lineare Regression (s. Kap 4-1) eine Linie an die Trainingsdaten 
#anpasst, passt die logistische Regression eine S-förmige Kurve, die so genannte Sigmoid-
#funktion oder auch Logistische Funktion an, siehe:  
#              https://de.wikipedia.org/wiki/Logistische_Funktion
#Mit einer solchen Sigmoide läßt sich z.B. das Sättigungsverhalten von biologischen oder 
#chemischen Prozessen beschreiben.
#Die S-förmige Kurve hilft, binäre Entscheidungen zu treffen (z. B. ja/nein). Für die meisten 
#Eingabewerte gibt die Sigmoid-Funktion einen Wert zurück, der entweder sehr nahe bei "0" 
#(das entspricht einer Kategorie) oder sehr nahe bei "1" (das entspricht der anderen Kategorie) 
#liegt. 
#                             ▲ P(Krebs)
#                             │
#                             │
#                             │
#                             │                          
#          P(Krebs)=1.0  ─────┼─                        ------------------
#                             │                       ---
#          P(Krebs)=0.8  ─────┼─                    ---
#                             │                   --  
#                             │                 --    
#                             │              ----     
#          P(Krebs)=0.0  ─────┼─  ------------        
#                             │                       
#                             │                       
#                             │                       
#                             └───────────────────────────────────────────►
#                                         Anzahl tgl. Zigaretten
#
#Die sigmoide Funktion in der obigen Abbildung approximiert die Wahrscheinlichkeit, dass
#ein Patient an Lungenkrebs erkrankt, wenn er die übliche Anzahl seiner Zigaretten raucht. 
#Diese Wahrscheinlichkeit hilft uns, eine robuste Entscheidung zu treffen, wenn die einzige
#Information, die wir haben, die Anzahl der Zigaretten ist, die der Patient raucht: Hat er
#Lungenkrebs oder nicht ?
#Die Hauptfrage bei der logistischen Regression ist, wie man die richtige Sigmoid-Funktion 
#auswählt, die am besten zu den Trainingsdaten passt. Die Antwort liegt in der sog. 
#likelihood des gewählten Modells (also der Sigmoide): diese likelihood beschreibt 
#die Wahrscheinlichkeit, dass das gewählte Modell die beobachteten Trainingsdaten erzeugen 
#würde. Und wir möchten dasjenige Modell finden, das mit der größten Wahrscheinlichkeit die 
#Daten erzeugt. Dazu wird die sog. Maximum-Likelihood-Methode eingesetzt, siehe dazu:
#          https://de.wikipedia.org/wiki/Maximum-Likelihood-Methode  (Methode der größten Plausibilität)
#          https://de.wikipedia.org/wiki/Likelihood-Funktion (Plausibilitätsfunktion)
#Auch dies ist wieder nicht sehr erhellend für unbedarfte LeserInnen, daher folgt hier nun
#ein ...                   ____________________________
#                          ____________________________
#                          ...EXKURS zur Likelihood und 
#                         zur Maximum-Likelihodd-Methode     
#                          ____________________________
#          beruhend auf Ben Lambert's Lehrbuch "A Student's Guide to Bayesian Statistics" 
#          und das Material auf seiner Webseite https://ben-lambert.com/
#          sowie einige ausgewählte (zum likelihood-Thema passende) Video-Tutorials 
#          auf seinem YT-Kanal https://www.youtube.com/@SpartacanUsuals/playlists
#          und zwar:
#                   "Why is a likelihood not a probability distribution?"
#                   https://www.youtube.com/watch?v=IhoEwC9R8pA&list=PLwJRxp3blEvZ8AKMXOy0fc0cqT61GsKCG&index=17
#                   "Maximum Likelihood estimation - an introduction part 1"
#                   https://www.youtube.com/watch?v=I_dhPETvll8
#                   "Maximum Likelihood estimation - an introduction part 2"      
#                   https://www.youtube.com/watch?v=Z582V53dfr8
#                   "Maximum Likelihood estimation - an introduction part 3"
#                   https://www.youtube.com/watch?v=jpHreXjtw1Q                   
#                          ____________________________
#                          ____________________________
#                               ENDE DES EXKURSES
#                          ____________________________
#Man versucht also bei der logistischen Regression, die Parameter der Sigmoid-Funktion (s.o.) 
#so durch numerische Verfahren anzupassen, dass sie sich möglichst gut an die gegebenen
#Daten anpaßt - um all das kümmert sich sklearn automatisch.
#Wenn mehr als zwei binäre Alternativen klassifiziert werden sollen, also beim Übergang von
#der binomialen zur multinomialen Klassifikation, verwendet man eine höher-dimensionale 
#Verallgemeinerung der logistischen Funktion, die sog. Softmax-Funktion, siehe:          
#               https://de.wikipedia.org/wiki/Softmax-Funktion
#Das obige Beispiel "Anzahl Zigaretten -> Lungenkrebswahrscheinlichkeit" wollen wir nun mit
#einem Toy-Datensatz mal ausprobieren...

## Dependencies
from sklearn.linear_model import LogisticRegression
import numpy as np

## Data (#cigarettes, cancer)
X = np.array([[0, "No"],
              [10, "No"],
              [60, "Yes"],
              [90, "Yes"]])

## One-liner
model = LogisticRegression().fit(X[:,0].reshape(-1,1), X[:,1])

## Result & puzzle
print(model.predict([[2],[12],[13],[40],[90]]))   #['No' 'No' 'No' 'Yes' 'Yes']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Da dem ganzen die Klasse LogisticRegression von sklearn zugrundeliegt, ist es sicher sinnvoll,
#dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#Die Trainingsdaten X bestehen aus vier Patientendatensätzen (den Zeilen) mit jeweils zwei 
#Spalten. Die erste Spalte enthält die Anzahl der Zigaretten, die die Patienten rauchen 
#(Input-Merkmal), und die zweite Spalte enthält die Klassenlabels, die besagen, ob sie 
#letztendlich an Lungenkrebs erkrankt sind.
#Wir erstellen das Modell durch den Aufruf des Konstruktors LogisticRegression() und rufen
#die fit()-Methode für dieses Modell auf; fit() benötigt zwei Argumente, nämlich die Eingabe 
#(Zigarettenkonsum) und die jeweils zugehörigen Klassenetiketten (Krebs, ja oder nein) als 
#Output. 
#Die Methode fit() erwartet ein zweidimensionales Eingabe-Array-Format mit einer Zeile pro 
#Trainingsdatenprobe und jeweils einer Spalte pro Merkmal dieser Trainingsdaten. In unserem
#Beispiel haben wir nur ein Merkmal, das ist die erste Spalte von X:
print(X[:,0])                  #['0' '10' '60' '90']
#Aufgrund der Homogenität von Numpy-Arrays werden die Zahlen der ersten Spalte wieder
#als Strings dargestellt, da die zweite Spalte ebenfalls aus Strings besteht. Wir müssen daher
#die erste Spalte wieder in numerische Werte umwandeln:
print(X[:,0].astype(float))    #[ 0. 10. 60. 90.]
#In der Doku zu LogisticRegression steht allerdings, dass diese Typkonversion auch automatisch
#von LogisticRegression vorgenommen wird.
#Da wir nur ein Merkmal haben, müssen wir dies für die Verwendung in fit in ein 2-D-Array mit 
#nur einer Spalte umwandeln, siehe dazu auch Kap.3-5 (zur Funktion reshape):
print(X[:,0].astype(float).reshape(-1,1))      #[[ 0.]
                                               # [10.]
                                               # [60.]
                                               # [90.]]
#Die -1 besagt, dass reshape sich die Zeilenzahl selbst überlegen soll. Wir können diese
#natürlich auch explizit angeben:
print(X[:,0].astype(float).reshape(4,1))       #[[ 0.]
                                               # [10.]
                                               # [60.]
                                               # [90.]]
#Die Output-Klassenetiketten stehen in der zweiten Spalte von X. Sie sind das zweite Argument
#der fit-Methode:                                               
print(X[:,1])       #['No' 'No' 'Yes' 'Yes']  
#Nun setzen wir beide Argumente in fit ein und das Modell wird berechnet:                                         
model = LogisticRegression().fit(X[:,0].astype(float).reshape(-1,1), X[:,1])
#Als Nächstes wollen wir mit Hilfe des Modells voraussagen, ob ein Patient an Lungenkrebs 
#erkrankt ist, wenn eine bestimmte Anzahl Zigaretten gegeben ist, die er raucht. D.h. wir geben 
#2, 12, 13, 40, 90 Zigaretten in das Modell hinein und es soll uns mit "Krebs, ja oder nein"
#antworten (beachte, die Eingabe ist wieder ein 2D-Array mit einer Spalte):
print(model.predict([[2],[12],[13],[40],[90]]))     #['No' 'No' 'No' 'Yes' 'Yes']
#Das Modell sagt voraus (predict), dass die ersten drei Patienten Lungenkrebs-negativ sind,
#während die letzten beiden Patienten Lungenkrebs-positiv sind.
#Schauen wir uns die Wahrscheinlichkeiten, die die Sigmoidfunktion liefert, im Detail an.
#Dazu führen wir einfach den folgenden Codeschnipsel aus. Mit der Methode predict_proba 
#können wir die berechnete Sigmoide abtasten:
for i in range(100):
    print("x=" + str(i) + " --> " + str(model.predict_proba([[i]])))   #x=0 --> [[9.99568507e-01 4.31492826e-04]]
                                                                       #x=1 --> [[9.99462453e-01 5.37546844e-04]]
                                                                       #x=2 --> [[9.99330350e-01 6.69649778e-04]]
                                                                       #...
                                                #Kippbereich   \__     #x=35 --> [[0.51308165 0.48691835]]
                                                #der Sigmoide  /       #x=36 --> [[0.45821454 0.54178546]]
                                                                       #...
                                                                       #x=98 --> [[1.01609505e-06 9.99998984e-01]]
                                                                       #x=99 --> [[8.15540636e-07 9.99999184e-01]]
#                                                                                                 ______________
#                                                                                                     ^
#                                                                                                     |
#                                                                                              weiter unten werden
#                                                                                              wir dann nur diese
#                                                                                              zweite Spalte zum Plotten
#                                                                                              der Sigmoide verwenden (*)
#Angezeigt wird dadurch für jeden x-Wert ein 2D-Array mit einer Zeile und zwei Spalten.
#In der ersten Spalte steht die Wahrscheinlichkeit für Lungenkrebs "No" und in der zweiten 
#Spalte die Wahrscheinlichkeit für Lungenkrebs "Yes". Bis x=35 ist "No" wahrscheinlicher
#und ab x=36 ist "Yes" wahrscheinlicher. In diesem Bereich liegt also gerade der Kippbereich
#der Sigmoide. Wenn ein Patient mehr als 35 Zigaretten geraucht hat, stuft der Algorithmus 
#ihn als lungenkrebspositiv ein.
#Nun wollen wir die im Modell berechnete Sigmoide und die Eingabedaten, für die wir soeben 
#Lungenkrebsvorhersagen mit Hilfe des Modells gemacht haben, plotten, wobei "No" als y-Wert 0
#und "Yes" als y-Wert 1 dargestellt wird. Und für die Darstellung der Sigmoide können wir die 
#obige Abtastatung der Sigmoide mittels predict_proba verwenden, wobei wir nur die Wahrschein-
#lichkeiten für Lungenkrebs "Yes" verwenden und diese Daten in eine Liste schreiben:
[model.predict_proba([[i]])[0,1] for i in range(100)]   #[0.00043149282579138575,
                                                        # 0.0005375468444284601,
                                                        # 0.0006696497776482076,
                                                        # ...
                                                        # 0.9999989839049465,
                                                        # 0.9999991844593635]                                                        
#Da predict_proba für jeden Punkt ein 2D-Array mit nur einer Zeile und zwei Spalten returniert,
#holen wir das zweite Element dieser einen Zeile mit der Slicing-Operation [0,1] heraus, siehe dazu
#auch (*).
#Und hier ist nun endlich der gesamte Plot:
import matplotlib.pyplot as plt
plt.xkcd()
plt.plot(range(100),[model.predict_proba([[i]])[0,1] for i in range(100)])
plt.annotate(r"P1", (2, 0))      #"No"
plt.annotate(r"P2", (12, 0))     #"No"
plt.annotate(r"P3", (13, 0))     #"No"
plt.annotate(r"Kipppunkt", xy=(35, 0.5), xytext=(8,0.8), arrowprops=dict(facecolor='red', shrink=1.5))
plt.annotate(r"P4", (40, 1))     #"Yes"
plt.annotate(r"P5", (90, 1))     #"Yes"
plt.show()
#Die Punkte P2 und P3 liegen aufgrund der Skalierung fast übereinander. Man sieht aber
#deutlich, wie die Sigmoide die Punkte P1, P2 und P3 der Klassifikation "No" zuordnet,
#und die Punkte P4 und P5 der Klassifikation "Yes".
#Der Rote Pfeil zeigt auf den Kipppunkt bei (35, 0.5).





#########################################################################################
#########################################################################################
# 4.3 K-Means Clustering in One Line
#########################################################################################

#In den vorherigen Abschnitten wurde das überwachte Lernen behandelt, bei dem die Trainings-
#daten beschriftet (Labeled) sind. Mit anderen Worten: wir kennen den Ausgabewert für jeden 
#Eingabewert in den Trainingsdaten. In der Praxis ist dies jedoch nicht immer der Fall. 
#Häufig ist man mit unbeschrifteten Daten konfrontiert - vor allem in vielen Datenanalyse-
#anwendungen -, bei denen nicht klar ist, was "die optimale Ausgabe" sein soll. In diesen 
#Situationen ist eine Vorhersage nicht möglich (weil es keine Ausgabedaten gibt), aber wir 
#können dennoch nützliches Wissen aus diesen unbeschrifteten Datensätzen destillieren (z.B. 
#können wir Cluster von ähnlichen unbeschrifteten Daten finden). Modelle, die unbeschriftete 
#Daten verwenden, fallen unter die Kategorie des unsupervised Learning.
#
#Nehmen wir an, Sie arbeiten in einem Startup, das verschiedene Zielmärkte mit verschiedenen 
#Einkommensstufen und Altersgruppen bedient. Sie sollen nun eine bestimmte Anzahl von 
#Zielpersonas zu finden, die am besten zu Ihren Zielmärkten passen. Sie können Clustering-
#Methoden verwenden, um die durchschnittlichen Kunden-Personas zu identifizieren, die Ihr 
#Unternehmen bedient, z.B.:
#                      ┌──────────────────────────────────────────────────────────────┐
#                     ─┤                                                              │
#                      │      x = Kunden                                              │
#                  65 ─┤      o = Personas                                            │
#                      │                                                              │
#                  60 ─┤                                                           x  │
#                      │                                                       x      │
#                  55 ─┤                                                          xxx │
#                      │                                                        xxoxx │
#                  50 ─┤                                                              │
#                      │                                                        x  x  │
#                  45 ─┤                                                              │
#                      │                                                              │
#          Alter   40 ─┤                                                              │
#                      │                                                              │
#                  35 ─┤                                                              │
#                      │                               x  x                           │
#                  30 ─┤                                     x                        │
#                      │                                x xoxxx                       │
#                  25 ─┤        x   x  x                 x                            │
#                      │     x    xxo                  x    x                         │
#                  20 ─┤        x xx                                                  │
#                      │              x                                               │
#                  15 ─┤           x                                                  │
#                      │                                                              │
#                      └──────────┬────────────┬───────────┬────────────┬──────────┬──┘
#                                 │            │           │            │          │
#                               2000         2500        3000         3500        4000
#          
#                                                     Einkommen in €
#
#Im obigen diagramm können wir leicht drei Arten von Personas mit unterschiedlichen
#Einkommen und Alter identifizieren. Aber wie findet man diese algorithmisch? Dies ist
#die Domäne von Clustering-Algorithmen wie dem weit verbreiteten K-Means-Algorithmus, siehe
#dazu     https://de.wikipedia.org/wiki/K-Means-Algorithmus
#Ausgehend von einem gegebenen Datensatz (in der obigen Abb. mit "x" markiert) und einer 
#ganzen Zahl k findet der K-Means-Algorithmus k Datencluster so, dass die Differenz zwischen 
#dem Zentrum eines Clusters (genannt Zentroid) und den Daten im Cluster minimal ist. Mit 
#anderen Worten: wir können die verschiedenen Personas (in der obigen Abb. mit "o" markiert) 
#finden, indem wir den K-Means-Algorithmus auf den Datensatz anwenden.
#Die Clusterzentren ("o") gehören zu den unterschiedlich geclusterten Kundendaten ("x").
#Jedes Clusterzentrum kann als eine Kundenpersona betrachtet werden. Wir haben also
#drei idealisierte Personas: ein 23-Jähriger, der €2000 verdient, ein 27-Jähriger, der
#der 3000€ verdient, und ein 53-Jähriger, der 4000€ verdient. Und das Tolle daran ist, 
#dass der K-Means-Algorithmus diese Clusterzentren sogar in hochdimensionalen Räumen 
#(in denen es für Menschen schwierig wäre, die Personas visuell zu finden) identifiziert.
#Der K-Means-Algorithmus benötigt "die Anzahl der Clusterzentren k" als Eingabe. In diesem 
#Fall schaut man sich die Daten an und bestimmt "auf magische Weise" k = 3. Fortgeschrittenere 
#Algorithmen können die Anzahl der Clusterzentren automatisch ermitteln.
#Wie funktioniert nun der K-Means-Algorithmus? Kurz gesagt, er führt folgendes Verfahren 
#durch:
#
#PSEUDOCODE
#        Initialisiere zufällige Clusterzentren (Zentroide).
#        Wiederhole bis zur Konvergenz:
#                 Weise jeden Datenpunkt dem nächstgelegenen Clusterzentrum zu.
#        Berechne jedes Clusterzentrum als Schwerpunkt aller ihm zugewiesenen Datenpunkte neu.
#
#Betrachten wir nun das folgende Problem: Gegeben seien zweidimensionale Gehaltsdaten
#(geleistete Arbeitsstunden (Work), verdientes Gehalt (Salary)). Wir wollen in dem gegebenen 
#Datensatz zwei Cluster von Angestellten finden, die eine ähnliche Anzahl von Stunden arbeiten 
#und ein ähnliches Gehalt verdienen...

## Dependencies
from sklearn.cluster import KMeans
import numpy as np

## Data (Work (h) / Salary (€))
X = np.array([[35, 7000], [45, 6900], [70, 7100],
              [20, 2000], [25, 2200], [15, 1800]])

## One-liner
kmeans = KMeans(n_clusters=2).fit(X)      #zusätzliches Argument: n_init='auto'  ?

## Result & puzzle
cc = kmeans.cluster_centers_
print(cc)     #[[  20. 2000.]
              # [  50. 7000.]]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Da dem ganzen die Klasse KMeans von sklearn zugrundeliegt, ist es sicher sinnvoll,
#dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#In den ersten Zeilen importieren wir das KMeans-Modul aus dem sklearn.cluster package. 
#Dieses Modul kümmert sich um das Clustering selbst. Wir müssen auch NumPy importieren, 
#da das KMeans-Modul mit NumPy-Arrays arbeitet.
#Unsere Daten sind zweidimensional. Sie korrelieren die Anzahl der Arbeitsstunden mit dem 
#Gehalt einiger Mitarbeiter. Wir wollen die Daten mal in einem Plot darstellen, siehe dazu:
#          https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
import matplotlib.pyplot as plt
x = X[:,0]
y = X[:,1]
color = 'green'
area = 30  
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.show()
#Ziel ist es, die beiden Clusterzentren zu finden, die am besten zu diesen Daten passen:
kmeans = KMeans(n_clusters=2).fit(X)      #zusätzliches Argument: n_init='auto'  ?
#Im obigen Einzeiler erstellen wir ein neues KMeans-Objekt, das alles für uns übernimmt. 
#Beim Erstellen legen wir die Anzahl der Clusterzentren mit dem Argument n_clusters fest. 
#Mit dem Argument n_init kann man festlegen, wie häufig der Algorithmus mit unterschiedlichen
#Centroid-Anfangswerten gestartet werden soll. Dann rufen wir einfach die Instanzmethode 
#fit(X) auf, um den K-Means-Algorithmus auf die Eingabedaten X anzuwenden. Das KMeans-Objekt 
#enthält nun alle Ergebnisse. Alles, was noch übrig ist, ist das Abrufen der Ergebnisse mit 
#Hilfe entsprechender Attribute von KMeans:
cc = kmeans.cluster_centers_
print(cc)   #[[  50. 7000.]
            # [  20. 2000.]]
#Diese beiden Clusterzentren wollen wir auch noch in unseren Scatterplot eintragen:
import matplotlib.pyplot as plt
x = X[:,0]
y = X[:,1]
color = 'green'
area = 30  
plt.scatter(x, y, c=color, s=area, alpha=0.5)
xc = cc[:,0]
yc = cc[:,1]
color = 'red'
area = 130
plt.scatter(xc, yc, c=color, s=area, alpha=0.3)
plt.show()
#Beachte, dass es im sklearn-Paket die Konvention gibt, einen nachgestellten Unterstrich 
#für einige Attributnamen (z.B. cluster_centers_) zu verwenden, um anzuzeigen, dass diese 
#Attribute dynamisch während der Trainingsphase (der fit()-Funktion) erzeugt wurden.
#Wir können sehen, dass die beiden Clusterzentren (20, 2000) und (50, 7000) sind.
#Dies ist auch das Ergebnis des Python-Einzeilers. Diese Cluster entsprechen zwei 
#idealisierten Mitarbeiter-Personas: Die erste Persona arbeitet 20 Stunden pro Woche und 
#verdient €2000 pro Monat, während die zweite Persona 50 Stunden pro Woche arbeitet und 
#€7000 verdient. 





#########################################################################################
#########################################################################################
# 4.4 K-Nearest Neighbors in One Line
#########################################################################################

#Der beliebte K-Nearest Neighbors-Algorithmus (KNN) wird für Regression und Klassifizierung in 
#vielen Anwendungen wie Empfehlungssystemen, Bildklassifizierung, Vorhersage von Finanzdaten 
#u.v.a. eingesetzt. Er ist die Grundlage für viele fortgeschrittene Techniken des maschinellen 
#Lernens (z.B. beim Information Retrieval).
#Er ist einfach zu implementieren und dennoch eine wettbewerbsfähige und schnelle Technik des 
#maschinellen Lernens. Alle anderen Modelle für maschinelles Lernen, die wir bislang erörtert 
#haben, verwenden die Trainingsdaten zur Berechnung einer Repräsentation der Originaldaten. 
#Mit dieser Darstellung kann man dann neue Daten vorhersagen, klassifizieren oder clustern.
#Die Algorithmen der linearen und logistischen Regression definieren zum Beispiel Lern-
#parameter, während der Clustering-Algorithmus auf Basis der Trainingsdaten Cluster berechnet. 
#Der KNN-Algorithmus ist jedoch anders.
#Im Gegensatz zu den anderen Ansätzen berechnet er nicht ein abstrahierendes Modell (oder eine
#Repräsentation), sondern verwendet den gesamten(!) Datensatz als "Modell".
#Das so erstellte "Modell" ist nichts weiter als ein Satz von Beobachtungen. Jede einzelne 
#Instanz unserer Trainingsdaten ist somit Teil dieses "Modells". 
#Das hat Vor- und Nachteile. 
#Ein Nachteil ist, dass das Modell schnell aufgebläht werden kann, wenn die Trainingsdaten 
#wachsen, was dann eine Stichprobenziehung oder Filterung als Vorverarbeitungsschritt 
#erfordert. 
#Ein großer Vorteil ist jedoch die Einfachheit der Trainingsphase (einfach die neuen Daten-
#werte zum Modell hinzufügen). Außerdem können wir den KNN-Algorithmus für Vorhersage 
#(in sklearn: KNeighborsRegressor) oder Klassifizierung (in sklearn: KNeighborsClassifier)
#verwenden. 
#Man führt dabei die folgende Strategie aus:
#
#         Gegeben sei der Eingabevektor x:
#                   1. Finde die k nächsten Nachbarn von x (gemäß einer vordefinierten 
#                      Abstandsmetrik).
#                   2. Aggregiere die k nächsten Nachbarn zu einem einzelne Vorhersage- oder
#                      Klassifikationswert. Dabei kann eine beliebige Aggregatorfunktion 
#                      verwendet werden, z.B. Durchschnitt, Mittelwert, Maximum oder Minimum.
#
#Lassen Sie uns ein konkretes Beispiel durchgehen. 
#Ihr Unternehmen verkauft Häuser für Kunden. Es hat dazu eine große Datenbank mit Kunden und 
#Hauspreisen erworben (siehe folgende Abb.):
#  
#                     ▲
#                     │
#                     │
#                     │                                           x
#                     │
#                     │                      │               x
#                     │                      │         x           x
#                     │                      │             x
#                     │             x        │                  x
#                     │                      │
#                  H  │                      │              x
#                  a  │            ┌─────────┴────────┐
#                  u  │            │       x(A)       │
#                  s  │            │               x(B)         │ A: (50m^2, €34000)
#                  p  │            │ x(C)             │        ◄│ B: (55m^2, €33500)
#                  r  │            │                  │         │ C: (45m^2, €32000)
#                  e  │            └─────────┬────────┘
#                  i  │                      │        3NN        ───────────────────
#                  s  │                      │                    D: (52m^2, €99500/3)
#                  e  │                      │                       = (52m^2, €33167)
#                 (€) │                      │
#                     │                      │
#                     │                      │
#                     │                      │
#                     │                      │D: (52m^2, ?)
#                     └──────────────────────┼────────────────────────────►
#                                            │       Hausgroessen (m^2)

#Eines Tages fragt Ihr Kunde, wie viel er für ein Haus mit 52 Quadratmetern zu zahlen hat
#Wir fragen Ihr KNN-Modell ab, und es gibt uns sofort die Antwort €33167. Und tatsächlich, 
#unser Kunde findet ein Haus für €33489 in derselben Woche. Wie kam das KNN-System zu dieser 
#erstaunlich genauen Vorhersage? Zunächst einmal berechnet das KNN-System einfach die k = 3 
#nächsten Nachbarn zu der Anfrage D = 52 Quadratmeter unter Verwendung der euklidischen 
#Distanz sqrt((x2-x1)**2 + (y2-y1)**2). Die drei nächstgelegenen Nachbarn sind A, B und C 
#mit den jeweiligen Preisen €34000, €33500 und €32000. Anschließend werden die drei nächsten 
#Nachbarn zusammengefasst, indem der einfache Durchschnitt ihrer Werte berechnet wird. 
#Da in diesem Beispiel k = 3 ist, können wir das KNN-Modell als 3NN bezeichnen. Natürlich 
#können wir den Parameter k und die Aggregationsmethode variieren (statt Mittelwert irgendwas
#anderes), um anspruchsvollere Vorhersagemodelle zu entwickeln. 
#Ein weiterer Vorteil von KNN ist, dass es leicht angepasst werden kann, wenn neue 
#Beobachtungen gemacht werden. Dies ist bei Modellen des maschinellen Lernens im Allgemeinen 
#nicht der Fall. Eine offensichtlicher Schwachpunkt in dieser Hinsicht ist, dass die Suche 
#nach den k nächsten Nachbarn immer schwieriger wird, je mehr Punkte man hinzufügt. 
#Um dies auszugleichen, kann man kontinuierlich veraltete Werte aus dem Modell entfernen.
#Wie bereits erwähnt, kanen man KNN auch für Klassifizierungsprobleme verwenden. Anstatt 
#über die k nächsten Nachbarn zu mitteln, kann man dazu einen Abstimmungsmechanismus 
#verwenden: Jeder nächste Nachbar stimmt für seine Klasse ab, und die Klasse mit den 
#meisten Stimmen gewinnt.
#Unser Code greift das obige Beispiel mit der Hausgrößen und -preisen auf...

## Dependencies
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

## Data (House Size (square meters) / House Price (€))
X = np.array([[35, 30000], [45, 45000], [40, 50000],
              [35, 35000], [25, 32500], [40, 40000]])

## One-liner
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1,1), X[:,1])

## Result & puzzle
res = KNN.predict([[30]])
print(res)                  #[32500.]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Da dem ganzen die Klasse KNeighborsRegressor von sklearn zugrundeliegt, ist es sicher 
#sinnvoll, dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#Um uns das Ergebnis zu verdeutlichen, plotten wir die Wohnungsdaten aus dem obigen Code... 
import matplotlib.pyplot as plt
x = X[:,0]
y = X[:,1]
color = 'green'
area = 30  
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.show()
#Man kann den allgemeinen Trend erkennen? Mit zunehmender Größe eines Hauses, ist ein 
#linearer Anstieg des Marktpreises erwarten. Verdoppelt man die Quadrat-Meter, wird sich der 
#Preis ebenfalls verdoppeln. 
#Im One-Liner-Code bittet der Kunde um unsere Preisprognose für ein Haus mit 30 Quadratmetern. 
#Was sagt KNN mit k = 3 (kurz: 3NN) vorher? Werfen wir einen Blick auf den folgenden Plot... 
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
x = X[:,0]
y = X[:,1]
fig, ax = plt.subplots()
color = 'green'
area = 30  
ax.scatter(x, y, c=color, s=area, alpha=0.5)
X3 = np.array([elt for elt in X if elt[0] <= 35])     #(*)
x3 = X3[:,0]
y3 = X3[:,1]
x_average = np.average(x3)                            #(**)
y_average = np.average(y3)                            #(**)
color = 'red'
area = 130
ax.scatter(x_average, y_average, c=color, s=area, alpha=0.3)
ellipse = Ellipse(xy=(x_average, y_average), width=15, height=8000, edgecolor='r', facecolor='none')
ax.add_patch(ellipse)
ellipse_label = "3NN"
label_x, label_y = 32, 37000
ax.text(label_x, label_y, ellipse_label, fontsize=12, color='r', ha='center')
ax.set_xlim(24, 50)
ax.set_ylim(29000, 51000)
plt.show()
#Schön, nicht wahr? Für den obigen Plot haben wir die drei nächsten Nachbarn per Hand aus den
#Daten gefischt (siehe Markierung (*) im obigen Plot-Code) und auch den Mittelwert selbst 
#bestimmt (siehe Markierungen (**) im obigen Plot-Code).
#Der KNN-Algorithmus hingegen findet die drei am nächsten liegenden Häuser in Bezug auf die 
#Hausgröße selbst und bildet den Durchschnitt des vorhergesagten Hauspreises als Durchschnitt
#der k=3 nächstgelegenen Nachbarn. Das Ergebnis ist also €32500.
#Sehen wir uns den Einzeiler im Detail an:
#Zunächst erstellen wir ein neues Modell für maschinelles Lernen namens KNeighborsRegressor,
#das 3-Nachbarn berücksichtigt:
KNN = KNeighborsRegressor(n_neighbors=3) 
#Wenn wir KNN für die Klassifizierung verwenden wollten, würden wir stattdessen
#KNeighborsClassifier verwenden. 
#Dann trainieren wir das Modell mit Hilfe der Funktion fit() mit zwei Parametern. Der erste 
#Parameter definiert die Eingabe (die Hausgröße), und der zweite Parameter definiert die 
#Ausgabe (den Hauspreis). Die Form der beiden Parameter muss eine array-ähnliche Datenstruktur 
#sein. Um zum Beispiel 30 als Eingabe zu verwenden, müssen wir sie als [30] übergeben. 
#Der Grund dafür ist, dass im Allgemeinen die Eingabe nicht eindimensional, sondern 
#mehrdimensional sein kann. Deshalb, müssen wir die Eingabe halt umgestalten, d.h. aus...
print(X[:,0])      #[35 45 40 35 25 40]
#machen wir:
print(X[:,0].reshape(-1,1))     #[[35]
                                # [45]
                                # [40]
                                # [35]
                                # [25]
                                # [40]]
#Beachte, dass, wenn wir dieses 1D NumPy-Array als Eingabe verwenden würden, die fit-Methode
#nicht funktionieren würde, da sie ein Array von (Array-ähnlichen) Beobachtungen erwartet, 
#und nicht ein Array mit ganzen Zahlen. Der Ausgabe-Parameter kann ein 1d Numpy-Array 
#bleiben: 
KNN.fit(X[:,0].reshape(-1,1), X[:,1])
#       -------------------   ------
#               |                |
#           Eingabe            Ausgabe
#Das KNN-Objekt wurde somit trainiert und kann nun für Regressionsvorhersagen verwendet 
#werden, wobei als Eingabe wieder ein Array von Arrays erwartet wird:
KNN.predict([[30]])         #array([32500.])
#Zusammenfassend lässt sich sagen, dass wir in diesem Einzeiler gelernt haben, wie man einen 
#KNN-Regressor in einer einzigen Code-Zeile erstellt. Wenn man eine Menge sich ändernder 
#Daten hat, ist KNN unser bester Freund!





#########################################################################################
#########################################################################################
# 4.5 Neural Network Analysis in One Line
#########################################################################################

#Neuronale Netze haben in den letzten Jahren stark an Popularität gewonnen. Dies liegt zum 
#Teil daran, dass sich die Algorithmen und Lerntechniken auf diesem Gebiet verbessert haben, 
#und zum andern Teil an der verbesserten Hardware und dem Aufkommen der Allzweck-GPU-
#Technologie (GPGPU). In diesem Abschnitt lernen wir das mehrschichtige Perzeptron (MLP,
#multilayer perceptron) kennen, das eine der beliebtesten neuronalen Netzwerk-Strukturen ist. 
#Nach der Lektüre dieses Abschnitts werden wir in der Lage sein, unser eigenes neuronales 
#Netzwerk in einer einzigen Zeile Python-Code zu schreiben.
#
#Für diesen Einzeiler wurde ein spezieller Trainingsdatensatz vorbereitet. Das Ziel war es, 
#einen nachvollziehbar-realistischen Datensatz aus der realen Welt zu erstellen. 
#Dazu wurden E-Mail-Abonnenten gebeten, sich an einem Experiment zur Datengenerierung zu 
#beteiligen. Den E-Mail-Abonnenten wurden sechs anonymisierte Fragen zu ihren Python-
#Kenntnissen und ihrem Einkommen gestellt. Die Antworten auf diese Fragen dienen als 
#Trainingsdaten für das einfache Beispiel eines neuronalen Netzwerks (als Python-Einzeiler). 
#Die Trainingsdaten basieren auf den Antworten auf die folgenden sechs Fragen:
#
#    1- Wie viele Stunden haben Sie sich in den letzten sieben Tagen mit Python-Code 
#       befasst?
#    2- Vor wie vielen Jahren haben Sie begonnen, sich mit Informatik zu beschäftigen?
#    3- Wie viele Programmierbücher stehen in Ihrem Regal?
#    4- Wie viel Prozent Ihrer Python-Zeit verbringen Sie mit der Arbeit an realen 
#       Projekten?
#    5- Wie viel verdienen Sie pro Monat (auf €1000 aufrunden) mit dem "Verkauf Ihres 
#       technischen KnowHows (im weitesten Sinne)?
#    6- Wie lautet Ihre ungefähre Stackoverflow-Bewertung (Reputation), gerundet auf 
#       100 Punkte?
#
#Die ersten fünf Fragen sind der Input, und die sechste Frage ist der Output für die 
#Analyse des neuronalen Netzes. Mit anderen Worten: wir wollen mit Hilfe der neural-network-
#Regression voraussagen, welchen numerischen Wert die Python-Fähigkeiten einer Person 
#(ausgedrückt durch eine hypothetische Stackoverflow-Bewertung in Bezug auf die Beantwortung
#von Python-bezogenen Problemen, 6-) haben auf der Grundlage anderer numerischer 
#Eingangsmerkmale (1- bis 5-). 
#Diese sechste Frage (6-) ist eine mögliche quantitative Beschreibung des Fähigkeitsniveaus 
#eines Python-Programmierers. 
#Wir beginnen damit, zu visualisieren, wie jede Frage (1- bis 5-) das Ergebnis (die mehr oder 
#weniger objektive Bewertung der Fähigkeiten eines Python-Entwicklers, 6-) beeinflusst.
#Unser Trainings-Datensatz X umfaßt 18 Python-Programmierer, die die sechs Fragen beantwortet
#haben:
import numpy as np
X = np.array(
    [[20, 11, 20, 30, 4000, 3000],
     [12, 4, 0, 0, 1000, 1500],
     [2, 0, 1, 10, 0, 1400],
     [35, 5, 10, 70, 6000, 3800],
     [30, 1, 4, 65, 0, 3900],
     [35, 1, 0, 0, 0, 100],
     [15, 1, 2, 25, 0, 3700],
     [40, 3, -1, 60, 1000, 2000],
     [40, 1, 2, 95, 0, 1000],
     [10, 0, 0, 0, 0, 1400],
     [30, 1, 0, 50, 0, 1700],
     [1, 0, 0, 45, 0, 1762],
     [10, 32, 10, 5, 0, 2400],
     [5, 35, 4, 0, 13000, 3900],
     [8, 9, 40, 30, 1000, 2625],
     [1, 0, 1, 0, 0, 1900],
     [1, 30, 10, 0, 1000, 1900],
     [7, 16, 5, 0, 0, 3000]]) 
print(len(X))                     #18
#X ist offensichtlich ein 2D-Array. Wir wollen nun fünf Streudiagramme erstellen, in denen
#die ersten fünf Spalten jeweils als x-Werte und die sechste Spalte immer als y-Werte dienen:
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,20) 
area = 30
plt.subplot(5,1,1)
x = X[:,0]
y = X[:,5]
color = 'green'  
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.xlabel('Hours (per week)')
plt.ylabel('Rating')
plt.grid()
plt.subplot(5,1,2)
x = X[:,1]
y = X[:,5]
color = 'orange'
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.xlabel('Learned CS (years)')
plt.ylabel('Rating')
plt.grid()
plt.subplot(5,1,3)
x = X[:,2]
y = X[:,5]
color = 'blue'
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.xlabel('Coding books (no.)')
plt.ylabel('Rating')
plt.grid()
plt.subplot(5,1,4)
x = X[:,3]
y = X[:,5]
color = 'red'
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.xlabel('Ratio real projects (%)')
plt.ylabel('Rating')
plt.grid()
plt.subplot(5,1,5)
x = X[:,4]
y = X[:,5]
color = 'violet'
plt.scatter(x, y, c=color, s=area, alpha=0.5)
plt.xlabel('Monthly income (€)')
plt.ylabel('Rating')
plt.grid()
plt.show()
#Beachten Sie, dass diese Streu-Diagramme nur zeigen, wie jedes einzelne Merkmal (Frage 1- 
#bis 5-) sich auf die endgültige Stackoverflow-Bewertung auswirkt, aber sie sagen nichts über 
#die Auswirkungen einer Kombination von zwei oder mehr Merkmalen. Beachten Sie auch, dass 
#einige Pythonistas nicht alle sechs Fragen beantwortet haben; in diesen Fällen wurde dann 
#der Dummy-Wert -1 verwendet.
#
#Was ist ein künstliches neuronales Netz (artificial neural network)?
#Die Idee, ein theoretisches Modell des menschlichen Gehirns (das biologische neuronale Netz) 
#zu schaffen, wurde in den letzten Jahrzehnten ausgiebig untersucht. Aber die Grundlagen für 
#künstliche neuronale Netze wurden bereits in den 1940er und 50er Jahren vorgeschlagen! 
#Seitdem wurde das Konzept der künstlichen neuronalen Netze verfeinert und kontinuierlich 
#verbessert.
#Die Grundidee besteht darin, die große Aufgabe des Lernens und Schlussfolgerns in mehrere 
#Mikro-Aufgaben aufzuteilen. Diese Mikroaufgaben sind nicht unabhängig, sondern voneinander 
#abhängig. Das Gehirn besteht aus Milliarden von Neuronen, die mit Billionen von Synapsen 
#verbunden sind. In dem vereinfachten Modell besteht das Lernen lediglich in der Anpassung 
#der Stärke der Synapsen (in künstlichen neuronalen Netzen auch Gewichte oder Parameter 
#genannt) 
#Wie wird also eine neue Synapse in dem Modell "angelegt"? Ganz einfach - man erhöht ihre 
#Gewichtung von Null auf einen Wert ungleich Null. Die folgende Prinzip-Abbildung zeigt 
#ein grundlegendes neuronales Netz mit drei Schichten: Eingabe-Schicht (input layer), 
#versteckte Schicht (hidden layer), Ausgabe-Schicht (output layer). Jede Schicht besteht 
#aus mehreren Neuronen, die von der Eingabeschicht über die versteckte Schicht mit der 
#Ausgabeschicht verbunden sind:
#
#                             input layer           hidden layer        output layer
#                                
#                                                       ┌──┐
#                                                       │  │
#                                         ┌──────────►  │  │  ──────┐
#                                         │             │  │        │
#                                 ┌──┐   ─┼───────────► │  │        │
#                                 │  │    │             │  │        │
#                                 │  │    │             │  │        │
#                                 │  │   ─┼───────┐     └──┘        │
#                                 │  │    │       │      .          │
#                                 │  │   ─┼──┐    │      .          │       .
#                         / ──►   │  │    │  │    │     ┌──┐        │       .
#                       /   .     └──┘    │  │    │     │  │        │     ┌──┐
#              \\     /     .             │  │    └──►  │  │        └─►   │  │
#              (o>          .       .     │  │          │  │              │  │
#           \\_//)    - - - ──►     .     │  │          │  │   ────────►  │  │    "Bird"
#            \_/_)          .       .     │  │          │  │              │  │
#             _|_     \     .             │  │          │  │              │  │
#                      \    .             │  │   ┌───►  │  │       ┌───►  │  │
#                       \ ──►      ┌──┐   │  │   │      └──┘       │      │  │
#                                  │  │ ──┘  │   │        .        │      └──┘
#                                  │  │      │   │        .        │        .
#                                  │  │      │   │      ┌──┐       │        .
#                                  │  │      └───┼────► │  │       │
#                                  │  │          │      │  │       │
#                                  │  │          │      │  │       │
#                                  │  │  ────────┘      │  │       │
#                                  └──┘                 │  │  ─────┘
#                                                       │  │
#                                     │                 │  │
#                                     └─────────────►   │  │
#                                                       └──┘
#
#In diesem Beispiel wird das neuronale Netz darauf trainiert, Tiere in Bildern zu erkennen. 
#In der Praxis würde man ein Eingangsneuron pro Pixel des Bildes verwenden. Dies kann zu 
#Millionen von Eingangsneuronen führen, die mit Aber-Millionen von versteckten Neuronen 
#verbunden sind. Oft ist jedes Ausgangsneuron für ein Bit der Gesamtausgabe verantwortlich. 
#Um z. B. zwei verschiedene Tiere (z. B. Katzen und Hunde) zu erkennen, verwenden Sie nur 
#ein einziges Neuron in der Ausgabeschicht, das zwei verschiedene Zustände modellieren kann 
#(0=Katze, 1=Hund). Die Idee ist, dass jedes Neuron aktiviert oder "abgefeuert" werden kann, 
#wenn ein bestimmter Eingangsimpuls am Neuron eintrifft. Jedes Neuron entscheidet unabhängig, 
#basierend auf der Stärke des Eingangsimpulses, ob es feuert oder nicht. Auf diese Weise 
#simulieren wir das menschliche Gehirn, in dem sich Neuronen gegenseitig durch Impulse 
#aktivieren. Die Aktivierung der Eingangsneuronen pflanzt sich durch das Netzwerk, bis die 
#Ausgangsneuronen erreicht sind. Einige Ausgangsneuronen werden aktiviert, andere nicht. 
#Das spezifische Muster der feuernden Ausgangsneuronen bildet die endgültige Ausgabe (oder 
#Vorhersage) des künstlichen neuronalen Netzes. In unserem Modell könnte ein feuerndes 
#Ausgangsneuron eine 1 kodieren, und ein nicht feuerndes Neuron eine 0. Auf diese Weise können 
#wir unser neuronales Netz so trainieren, dass es alles vorhersagen kann, was als Folge von 0 
#und 1 kodiert werden kann (also alles, was ein Computer darstellen kann). 
#Wir werfen in der folgenden Abb. einen detaillierten Blick darauf, wie Neuronen mathematisch 
#funktionieren:
#
#              x1=1
#               ┌──┐                w1=0.5
#               │  │   ─────────────────┐
#               └──┘                    │
#                                       │
#                                       │
#                                       │
#                                       └────────┐
#               x2=0                             ▼     x4 = w1*x1 + w2*x2 + w3*x3 = 0.7
#                ┌──┐         w2=0.1            ┌──┐                                       ┌───┐
#                │  │   ─────────────────────►  │x4│  ─────────────────────────────────►   │   │
#                └──┘                           └──┘        w4=...                         └───┘
#                                                 ▲
#                                       ┌─────────┘
#                                       │
#              x3=1                     │
#               ┌──┐                    │
#               │  │   ─────────────────┘
#               └──┘            w3=0.2
#
#Jedes Neuron ist mit anderen Neuronen verbunden, aber nicht alle Verbindungen sind gleich. 
#Stattdessen hat jede Verbindung ein bestimmtes Gewicht. Formal gesehen, gibt ein feuerndes 
#Neuron einen Impuls von 1 an die ausgehenden Nachbarn weiter, während ein nicht feuerndes 
#Neuron einen Impuls von 0 weiterleitet. Das Gewicht bestimmt dann wie viel des Impulses des 
#feuernden Eingangsneurons über die Verbindung an das Neuron weitergeleitet wird. 
#Mathematisch gesehen, multipliziert man den Impuls mit dem Gewicht der Verbindung, um den 
#Input für das nächste Neuron zu berechnen. 
#In unserem Beispiel summiert das Neuron einfach über alle Eingaben, um seine eigene Ausgabe
#zu bestimmen. Dies ist die Aktivierungsfunktion, die beschreibt, wie genau die Eingaben eines 
#Neurons eine Ausgabe erzeugen. In unserem Beispiel feuert ein Neuron mit höherer Wahrschein-
#lichkeit, wenn seine relevanten Eingangsneuronen ebenfalls feuern. So pflanzen sich die 
#Impulse durch das neuronale Netz weiter.
#Was macht der Lernalgorithmus? Er verwendet die Trainingsdaten, um die Gewichte w des 
#neuronalen Netzes so zu modifizieren, dass irgendwann das geünschte Ergebnis herauskommt. 
#Bei einem Trainingseingangswert x führen unterschiedliche Gewichte w zu unterschiedlichen 
#Ausgaben. Daher ändert der Lernalgorithmus schrittweise die Gewichte w - in vielen 
#Iterationen - bis die Ausgabeschicht ähnliche Ergebnisse liefert wie die Trainingsdaten. 
#Mit anderen Worten: Der Lernalgorithmus reduziert schrittweise den Fehler bei der korrekten 
#Vorhersage der Trainingsdaten.
#Es gibt viele Arten von Netzwerkstrukturen, Trainingsalgorithmen und Aktivierungsfunktionen. 
#In diesem Kap4-5 haben wir einen praktischen Ansatz zur Verwendung des neuronalen Netzes 
#in einer einzigen Code-Zeile gezeigt. Wenn Sie mehr wissen wollen, ist Wikipedia ein
#guter erster Einstieg: https://de.wikipedia.org/wiki/Neuronales_Netz
#                       https://de.wikipedia.org/wiki/Neuroinformatik
#
#In unserem konkreten Anwendungsproblem besteht das Ziel darin, ein neuronales Netzwerk zu 
#erstellen, das das Python-Kenntnisniveau (repräsentiert durch die Stackoverflow-Reputation,
#siehe auch: https://stackoverflow.com/help/whats-reputation) anhand der fünf Eingangsmerkmale 
#(Antworten auf die Fragen) vorhersagt:
#   - WOCHE      Wie viele Stunden haben Sie in den letzten sieben Tagen mit Python-Code 
#                zu tun gehabt? 
#   - JAHRE      Vor wie vielen Jahren haben Sie begonnen, sich mit Informatik zu beschäftigen?
#   - BÜCHER     Wie viele Programmierbücher befinden sich in Ihrem Regal?
#   - PROJEKTE   Wie viel Prozent Ihrer Python-Zeit verbringen Sie mit der Umsetzung realer 
#                Projekte?
#   - VERDIENST  Wie viel verdienen Sie pro Monat (auf €1000 aufrunden) mit dem "Verkauf" 
#                Ihrer technischen Fähigkeiten (im weitesten Sinne, also angestellt oder
#                freiberuflich)?
#Wiederum wollen wir uns auf die Schultern von Giganten stellen und die scikit-learn (sklearn) 
#Bibliothek für neuronale Netzwerkregression verwenden...

## Dependencies
from sklearn.neural_network import MLPRegressor
import numpy as np

## Questionaire data (WEEK, YEARS, BOOKS, PROJECTS, EARN, RATING)
X = np.array(
    [[20, 11, 20, 30, 4000, 3000],
     [12, 4, 0, 0, 1000, 1500],
     [2, 0, 1, 10, 0, 1400],
     [35, 5, 10, 70, 6000, 3800],
     [30, 1, 4, 65, 0, 3900],
     [35, 1, 0, 0, 0, 100],
     [15, 1, 2, 25, 0, 3700],
     [40, 3, -1, 60, 1000, 2000],
     [40, 1, 2, 95, 0, 1000],
     [10, 0, 0, 0, 0, 1400],
     [30, 1, 0, 50, 0, 1700],
     [1, 0, 0, 45, 0, 1762],
     [10, 32, 10, 5, 0, 2400],
     [5, 35, 4, 0, 13000, 3900],
     [8, 9, 40, 30, 1000, 2625],
     [1, 0, 1, 0, 0, 1900],
     [1, 30, 10, 0, 1000, 1900],
     [7, 16, 5, 0, 0, 3000]])

## One-liner
neural_net = MLPRegressor(max_iter=10000).fit(X[:,:-1], X[:,-1])

## Result
res = neural_net.predict([[0, 0, 0, 0, 0]])
print(res)      #[1365.71238915]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Da dem ganzen die Klasse MLPRegressor von sklearn zugrundeliegt, ist es sicher 
#sinnvoll, dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#In den ersten paar Zeilen erstellen wir den Datensatz. Die Algorithmen für maschinelles 
#Lernen in der Bibliothek scikit-learn verwenden ein ähnliches Eingabeformat. Jede Zeile ist 
#eine einzelne Beobachtung mit mehreren Merkmalen. Je mehr Zeilen, desto mehr Trainingsdaten 
#sind vorhanden; je mehr Spalten, desto mehr Merkmale für jede Beobachtung. In diesem Fall 
#haben wir fünf Merkmale für die Eingabe und ein Merkmal für den Ausgabe-Wert der einzelnen 
#Trainingsdaten.
#Der Einzeiler erstellt ein neuronales Netz, indem er den Konstruktor der Klasse MLPRegressor. 
#Wir haben max_iter=10000 als Argument übergeben, weil das Training nicht konvergiert, wenn 
#man die Standardanzahl von Iterationen verwendet (max_iter=200):
neural_net = MLPRegressor(max_iter=10000) 
#Danach rufen wir die Funktion fit() auf, die die Parameter des neuronalen Netzes bestimmt. 
#Input sind die ersten 5 Spalten von X:
print(X[:,:-1])     #[[   20    11    20    30  4000]
                    # [   12     4     0     0  1000]
                    # [    2     0     1    10     0]
                    # [   35     5    10    70  6000]
                    # [   30     1     4    65     0]
                    # [   35     1     0     0     0]
                    # [   15     1     2    25     0]
                    # [   40     3    -1    60  1000]
                    # [   40     1     2    95     0]
                    # [   10     0     0     0     0]
                    # [   30     1     0    50     0]
                    # [    1     0     0    45     0]
                    # [   10    32    10     5     0]
                    # [    5    35     4     0 13000]
                    # [    8     9    40    30  1000]
                    # [    1     0     1     0     0]
                    # [    1    30    10     0  1000]
                    # [    7    16     5     0     0]]
#Output ist die 6. Spalte von X:
print(X[:,-1])      #[3000 
                    #1500 
                    #1400 
                    #3800 
                    #3900  
                    #100 
                    #3700 
                    #2000 
                    #1000 
                    #1400 
                    #1700 
                    #1762 
                    #2400 
                    #3900
                    #2625 
                    #1900 
                    #1900 
                    #3000]
#Input und Output sind unsere Trainingsdaten.
#Nach dem Aufruf von fit() ist das neuronale Netz erfolgreich trainiert worden. Die Funktion 
#fit() nimmt ein mehrdimensionales Eingabefeld (eine Beobachtung pro Zeile, ein Merkmal pro 
#Spalte) und ein eindimensionales Ausgabe-Array (Größe = Anzahl der Beobachtungen):
neural_net.fit(X[:,:-1], X[:,-1]) 
#Nun kann die Funktion predict für neue Eingabewerte (die nicht zum Trainingsdatensatz) 
#aufgerufen werden:
neural_net.predict([[0, 0, 0, 0, 0]])          #array([1007.90509136])
#Beachten, dass die tatsächliche Ausgabe aufgrund der nicht-deterministischen Natur der 
#Funktion und des unterschiedlichen Konvergenzverhaltens leicht variieren kann.
#Im Klartext: Wenn ... 
#   - ... Sie in der letzten Woche 0 Stunden programmiert haben,
#   - ... Sie Ihr Informatikstudium vor 0 Jahren begonnen haben,
#   - ... Sie 0 Programmierbücher in Ihrem Regal stehen haben,
#   - ... Sie 0 Prozent Ihrer Zeit mit der Implementierung echter Python-Projekte verbringen, 
#   - ... Sie 0 Euro mit dem Verkauf Ihrer Programmierkenntnisse verdienen,
#schätzt das neuronale Netz, dass Ihr Kenntnisstand relativ niedrig ist. Allerdings scheint mir
#eine Bewertung so um die 1000 immer noch viel zu hoch zu sein.
#Und wenn wir in der letzten Woche 20 Stunden Python programmiert haben ?
neural_net.predict([[20, 0, 0, 0, 0]])        #array([736.7785529])
#Ups - das macht keinen Sinn. Unsere Reputation ist nun kleiner, als wenn wir nix gemacht 
#hätten. Das ist Quatsch.
#Und was passiert, wenn wir nich 10 Bücher anschaffen ?
neural_net.predict([[20, 0, 10, 0, 0]])       #array([3434.86592874])
#Wow ! Das hilft sehr.
#Und wenn wir uns seit einem Jahr damit beschäftigen und 50% unserer Projekte aus Python 
#bestehen?
neural_net.predict([[20, 1, 10, 50, 0]])      #array([3893.88048528])
# Hier traue ich dem neuronalen Netz nicht allzu sehr. Das zeigt aber auch, dass das 
#neuronale Netz nur so gut sein kann wie seine Trainingsdaten. Wir haben nur sehr begrenzte 
#Daten, und das neuronale Netz kann diese Einschränkung nicht wirklich überwinden: Es gibt 
#einfach zu wenig Wissen in einer Handvoll von Datenpunkten. 
#Zusammenfassend lässt sich sagen, dass wir hier die Grundlagen von neuronalen Netzen 
#kennengelernt haben und wissen wie man sie in einer einzigen Zeile Python-Code verwendet.
#Entscheidend sind allerdings die Trainingsdaten - ihre Qualität und ihre Menge !!
#Interessanterweise zeigen die Daten des Fragebogens, dass es für den Lernerfolg wichtig ist, 





#########################################################################################
#########################################################################################
# 4.6 Decision-Tree Learning in One Line
#########################################################################################

#Entscheidungsbäume sind leistungsstarke und intuitive Werkzeuge in unserer Toolbox für 
#maschinelles Lernen. Ein großer Vorteil von Entscheidungsbäumen ist, dass sie im Gegensatz 
#zu vielen anderen Techniken des maschinellen Lernens, für den Menschen lesbar sind. 
#Wir können problemlos einen Entscheidungsbaum trainieren und ihn Anderen zeigen, die nichts 
#über maschinelles Lernen wissen müssen, um zu verstehen, was Ihr Modell ist. 
#Dies ist besonders für Datenwissenschaftler von Vorteil, die ihre Ergebnisse oft vor unter-
#schiedlichen Entscheidungsträgern verteidigen und präsentieren müssen. 
#Im Gegensatz zu vielen Algorithmen des maschinellen Lernens sind die Ideen hinter Entschei-
#dungsbäumen aus unserer eigenen Erfahrung vertraut. Sie stellen eine strukturierten Weg dar, 
#Entscheidungen zu treffen. Jede Entscheidung eröffnet neue Zweige. Durch die Beantwortung 
#einer Reihe von Fragen landen Sie schließlich bei dem empfohlenen Ergebnis. Die folgende
#Abbildung zeigt ein Beispiel:

#               ┌───────────────────┐
#               │                   │
#               │ Do you like math? ├──────┐
#               │                   │      │
#               └──┬────────────────┘      │
#                  │                       │ No
#                  │                       │
#                  │ Yes                   │
#                  │                       ▼
#                  │                 ┌──────────────────┐
#                  │                 │                  │
#         Study ◄──┘                 │Do you like       ├──────┐
#         Computer Science           │      language?   │      │
#                                    └───┬──────────────┘      │
#                                        │                     │  No
#                                        │                     │
#                                        │ Yes                 │
#                                        │                     ▼
#                                        │                ┌─────────────────┐
#                               Study ◄──┘                │                 │
#                               Linguistics               │ Do you like     ├────┐
#                                                         │     painting?   │    │
#                                                         └──┬──────────────┘    │
#                                                            │                   │
#                                                            │                   │
#                                                            │ Yes               │ No
#                                                            │                   │
#                                                  Study  ◄──┘                   │
#                                                  Art                           │
#                                                                                │
#                                                                                ▼
#                                                                            Study
#                                                                            History
#
#Entscheidungsbäume werden für Klassifizierungsprobleme wie "Welches Fach soll ich studieren, 
#wenn ich mich dafür interessiere?" Man beginnt ganz oben. Dann beantwortet man wiederholt 
#Fragen und wählt die Optionen aus, die die eigenen Eigenschaften am besten beschreiben. 
#Schließlich erreicht man einen Blattknoten des Baums, also einen Knoten ohne Kinder. 
#Dieser Knoten ist dann die empfohlene Klasse auf der Grundlage der jeweiligen Merkmalsauswahl.
#Das Lernen mit Entscheidungsbäumen hat viele Nuancen. Im vorangegangenen Beispiel, hat die 
#erste Frage mehr Gewicht als die letzte Frage (die Reihenfolge der Fragen ist relevant). 
#Wenn wir Mathe mögen, wird der Entscheidungsbaum niemals Kunst oder Linguistik empfehlen. 
#Dies ist nützlich, weil einige Merkmale für die Klassifizierungsentscheidung viel wichtiger 
#sein können als andere. Ein Klassifizierungssystem, das unseren aktuellen Gesundheitszustand 
#vorhersagt, kann zum Beispiel, kann unser Geschlecht (Merkmal) verwenden, um viele Krankheiten 
#(Klassen) auszuschließen.
#Daher bietet sich die Reihenfolge der Entscheidungsknoten für Leistungsoptimierungen an: 
#Man stellt dazu diejenigen Merkmale an den Anfang, die einen großen Einfluss auf die endgültige 
#Klassifizierung haben. Beim Entscheidungsbaum-Lernen werden wir dann die Fragen aggregieren, 
#die einen geringem Einfluss auf die endgültige Klassifizierung besitzen, wie in der nächsten
#Abbildung gezeigt:

#                     ┌──────┐                                  ┌───────┐
#                     │      │                              ┌───┤       ├───┐
#           Yes ┌──── │ Math?│ ───────┐  No                 │   │ Math? │   │
#               │     └──────┘        │                     │   └───────┘   │ No
#               │                     │                     │               │
#               ▼                     ▼           ─────►    │Yes            ▼
#         ||                                     Pruning    │          ┌────────┐
#           |||──────┐          ┌────────┐        ─────►    │          │        │
#            │ |||   │          │        │                  │          │Language?
#            │Language?         │Language?                  ▼          │        │
#            │      |||         │        │                 CS          └─┬────┬─┘
#            └┬─────┬─|||       └─┬─────┬┘                               │    │
#             │     │    ||       │     │                            Yes │    │ No
#        Yes  │     │  No     Yes │     │ No                             │    │
#             │     │             │     │                                ▼    ▼
#             ▼     ▼             ▼     ▼
#                                                                    Ling.    Hist.
#           CS     CS           Ling.   Hist.

#Angenommen, der vollständige Entscheidungsbaum sieht wie der Baum auf der linken Seite aus. 
#Für jede Kombination von Merkmalen gibt es ein separates Klassifizierungsergebnis (die Baum-
#Blätter). Einige Merkmale liefern jedoch möglicherweise keine zusätzlichen Informationen
#in Bezug auf das Klassifizierungsproblem (z. B. der erste (linke) Entscheidungsknoten 
#"Language?" im obigen Beispiel). Entscheidungsbaum-Lernen würde diese Knoten aus Gründen 
#der Effizienz beseitigen -  dieser "Bereinigungs"-Prozess wird als "Pruning" bezeichnet.
#Das obige Entscheidungsproblem wird im folgenden Code umgesetzt...

## Dependencies
from sklearn import tree
import numpy as np

## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
              [1, 8, 1, "linguistics"],
              [5, 7, 9, "art"]])

## One-liner
Tree = tree.DecisionTreeClassifier().fit(X[:,:-1], X[:,-1])

## Result & puzzle
student_0 = Tree.predict([[8, 6, 5]])
print(student_0)

student_1 = Tree.predict([[5, 7, 9]])
print(student_1)                       #['computer science']
                                       #['art']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Da dem ganzen die Klasse MLPRegressor von sklearn zugrundeliegt, ist es sicher 
#sinnvoll, dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/tree.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#Die Daten in diesem Code beschreiben drei Studenten mit ihren geschätzten Fähigkeiten
#(dargestellt durch eine Punktzahl von 1-10) in den drei Bereichen Mathematik, Sprache und 
#Kreativität. Wir kennen auch die Studienfächer dieser Studenten. Im obigen Beispiel:
#Der erste Schüler ist sehr gut in Mathe und studiert Informatik.
#Der zweite Schüler ist in der Sprache viel besser als in den anderen beiden Fähigkeiten 
#und studiert Linguistik. 
#Der dritte Schüler ist kreativ begabt und studiert Kunst.
#Das sind unsere Trainingsdaten:
X = np.array([[9, 5, 6, "computer science"],
              [1, 8, 1, "linguistics"],
              [5, 7, 9, "art"]])
#Der darauffolgende Einzeiler erstellt ein neues Entscheidungsbaumobjekt und trainiert 
#das Modell mit Hilfe der Funktion fit() auf den beschrifteten (labeled) Trainingsdaten 
#(die letzte Spalte ist die Bezeichnung). Intern werden drei Knoten erstellt, einer für 
#jedes Merkmal: Mathe, Sprache und Kreativität. 
Tree = tree.DecisionTreeClassifier().fit(X[:,:-1], X[:,-1])
#                                        ________  _______
#                                          /            \
#                                 alle Zeilen           nur die
#                             ohne die letzte            letzte 
#                                      Spalte            Spalte
#                                     (input)          (output)
#
#Bei der Vorhersage der Klasse von Student_0 (Mathe = 8, Sprache = 6, Kreativität = 5), 
#liefert der Entscheidungsbaum "computer science".
print(Tree.predict([[8, 6, 5]]))     #['computer science']
#Er hat gelernt, dass dieses Merkmalsmuster (hoch, mittel, mittel) ein Indikator für die erste 
#Klasse ist. Andererseits, wenn nach (5, 7, 9) gefragt wird, sagt der Entscheidungsbaum "art" 
#voraus, weil er gelernt hat, dass die Punktzahl (niedrig, mittel, hoch) auf die dritte Klasse 
#hinweist.
print(Tree.predict([[5, 7, 9]]))     #['art']
#Beachte, dass der Algorithmus nicht deterministisch ist. Mit anderen Worten, wenn derselbe 
#Code zweimal ausgeführt wird, können sich unterschiedliche Ergebnisse ergeben. Dies ist 
#üblich für Algorithmen des maschinellen Lernens, die mit Zufallsgeneratoren arbeiten. 
#In diesem Fall ist die Reihenfolge der Merkmale zufällig organisiert, so dass der 
#endgültige Entscheidungsbaum eine andere Reihenfolge der Merkmale aufweisen kann.
#Zusammenfassend lässt sich sagen, dass Entscheidungsbäume eine intuitive Methode zur 
#Erstellung von durch Menschen lesbare Modelle darstellen. Jeder Zweig repräsentiert eine 
#Wahl auf der Grundlage eines einzelnen Merkmals einer neuen Probe (Anfrage). Die Blätter 
#des Baums stellen die endgültige Vorhersage (Klassifizierung oder Regression) dar.





#########################################################################################
#########################################################################################
# 4.7 Get Row with Minimal Variance in One Line
#########################################################################################

#Wir verlassen jetzt mal konkrete Algorithmen des maschinellen Lernens für einen Moment und 
#betrachten ein wichtiges Konzept beim maschinellen Lernen: die Varianz.
#Sie haben vielleicht schon von den fünf Vs in Big Data gelesen: Volume, Velocity, Variety, 
#Veracity und Value (Volumen, Geschwindigkeit, Vielfalt, Wahrhaftigkeit und Wert).
#Die Varianz (ihre Wurzel heißt "Standardabweichung") ist ein weiteres wichtiges V: Sie misst 
#die erwartete (quadrierte) Abweichung der Daten von ihrem Mittelwert. In der Praxis ist die 
#Varianz ein wichtiges Maß mit relevanten Anwendungsbereichen in der Finanzdienstleistung, 
#Wettervorhersage und Bildverarbeitung u.v.a.
#Siehe dazu auch: https://de.wikipedia.org/wiki/Varianz_(Stochastik)
#Die Varianz misst, wie stark die Daten um ihren Mittelwert im ein- oder mehrdimensionalen 
#Raum streuen. Wir werden gleich ein grafisches Beispiel sehen. Tatsächlich ist die Varianz 
#eine der wichtigsten Eigenschaften beim maschinellen Lernens. Sie erfasst die Muster der 
#Daten auf eine verallgemeinerte Weise - und beim maschinellen Lernen geht es vor allem um 
#Mustererkennung (pattern recognition).
#Viele Algorithmen für maschinelles Lernen stützen sich in der einen oder anderen Form auf 
#Varianz. Der Kompromiss zwischen Bias (Verzerrung) und Varianz, das sog. "Bias-Varianz-
#Dilemma", ist zum Beispiel ein bekanntes Problem beim maschinellen Lernen, siehe dazu:
#https://de.wikipedia.org/wiki/Verzerrung-Varianz-Dilemma
#Bei anspruchsvollen maschinellen Lernmodellen besteht die Gefahr der Überanpassung an die 
#Daten (hohe Varianz); Sie repräsentieren aber die Trainingsdaten sehr genau (geringe 
#Verzerrung). Auf der anderen Seite verallgemeinern einfache Modelle oft gut (geringe 
#Varianz), bilden die Daten aber nicht genau ab (hohe Verzerrung).
#Was genau ist also Varianz? 
#Es handelt sich um eine einfache statistische Eigenschaft, die angibt, wie stark der 
#Datensatz von seinem Mittelwert abweicht. Die folgende Abbildung zeigt ein Beispiel,
#in dem zwei Datensätze dargestellt sind: einer mit geringer Varianz und einer mit hoher 
#Varianz:

#           ▲
#           │
#           │
#           │
#           │                       Food Company
#           │                       (low variance)    +        #2        (Strecke #1-#2
#       A   │                              +     +          +             = Mittelwert)
#       k   │                        +
#       t   │
#       i   │                  +
#       e   │       +     +                        
#       n   │  #1                                  *
#       k   │                                              *
#       u   │
#       r   │                        *                         #4        (Strecke #3-#4
#       s   │                                                             = Mittelwert)
#           │             *                 *
#           │
#           │                                           *
#           │  #3               *        Tech Startup
#           │       *                    (High Variance)
#           │
#           └───────────────────────────────────────────────────────────────►
#                                          Zeit

#Dieses Beispiel zeigt die Aktienkurse von zwei Unternehmen. Der Aktienkurs des Tech-Startups 
#schwankt stark um seinen Durchschnitt. Der Aktienkurs des Lebensmittelunternehmens ist recht 
#stabil und schwankt nur geringfügig um den Durchschnitt. Mit anderen Worten: Das Tech-Startup 
#hat eine hohe Varianz, und das Lebensmittelunternehmen hat eine geringe Varianz in der
#Kursentwicklung .
#Mathematisch gesehen kann man die Varianz var(X) einer Menge X von numerischen Werten mit 
#Hilfe der folgenden Formel berechnen:     
#                          ----
#                          \           _  2
#             var(X)   =    >    ( x - x )
#                          /
#                          ----
#                          x aus X
#         _
#Der Wert x ist der Durchschnittswert der Daten in X:
#                          ----
#             _         1  \          
#             x     =  --   >    x 
#                     |X|  /
#                         ----
#                         x aus X
#
#|X| ist die Mächtigkeit der Menge X, also die Anzahl ihrer Elemente.
#
#Mit zunehmendem Alter möchten viele Anleger das Gesamtrisiko ihres Anlageportfolios 
#reduzieren. Die vorherrschende Anlagephilosophie besagt, man Aktien mit geringerer Varianz 
#als weniger riskante Anlageform betrachten kann. Grob gesagt, kann man weniger Geld 
#verlieren, wenn man in ein stabiles, vorhersehbares und großes Unternehmen investiert 
#als bei einem kleinen Startup-Unternehmen aus der Technologiebranche.
#Das Ziel des folgenden Einzeilers ist es, diejenige Aktie in Ihrem Portfolio zu 
#identifizieren, die die kleinste Varianz besitzt. Wenn man mehr Geld in diese Aktie 
#investiert, kann man eine geringere Gesamtstreuung des Portfolios erwarten.
#Wir suchen also diejenige Datenreihe in unserem Gesamtdatensatz X mit der geringsten
#Varianz...

## Dependencies
import numpy as np

## Data (rows: stocks / cols: stock prices)
X = np.array([[25,27,29,30],
              [1,5,3,2],
              [12,11,8,3],
              [1,1,2,2],
              [2,6,2,2]])

## One-liner: Find the stock with smallest variance
min_row = min([(i,np.var(X[i,:])) for i in range(len(X))], key=lambda x: x[1])

## Result & puzzle
print("Row with minimum variance: " + str(min_row[0]))    #Row with minimum variance: 3
print("Variance: " + str(min_row[1]))                     #Variance: 0.25


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wie üblich definieren wir zunächst die Daten, auf die wir den Einzeiler dann anwenden wollen 
#(siehe oben im Listing). Das NumPy-Array X enthält fünf Zeilen (eine Zeile pro Aktie in 
#unserem Portfolio) mit vier Werten pro Zeile (Aktienkurse):
X = np.array([[25,27,29,30],
              [1,5,3,2],
              [12,11,8,3],
              [1,1,2,2],
              [2,6,2,2]])
#Das Ziel ist es, die ID und die Varianz der Aktie mit minimaler Varianz zu finden.
#Daher ist die äußerste Funktion des Einzeilers die min()-Funktion.
#Wir führen die Funktion min() auf einer Liste von Tupeln (a,b) aus, wobei der erste
#Tupelwert a der Zeilenindex (also die jeweilige Aktie) ist und der zweite Tupelwert b 
#die Varianz dieser Zeile ist.
#Wir wollen das erstmal "händisch" zusammenbauen:
(0, np.var(X[0,:]))      #(0, 3.6875)
(1, np.var(X[1,:]))      #(1, 2.1875)
(2, np.var(X[2,:]))      #(2, 12.25)
(3, np.var(X[3,:]))      #(3, 0.25)       <------- diese Zeile hat die geringste Varianz
(4, np.var(X[4,:]))      #(4, 3.0)
#          ------
#            \
#           Das sind die einzelnen Aktienkurse aus X
#Die 5 Tupel packen wir in eine Liste (jetzt aber nicht mehr "händisch"):
[(i, np.var(X[i,:])) for i in range(len(X))]    #[(0, 3.6875), (1, 2.1875), (2, 12.25), (3, 0.25), (4, 3.0)]
#Wir suchen nun dasjenige Tupel, dessen zweiter Wert der kleinste unter den zweiten Werten 
#aller fünf Tupel ist.
#wenn wir naiver Weise folgendes versuchen...
min([(i, np.var(X[i,:])) for i in range(len(X))])     #(0, 3.6875)
#...erhalten wir nicht das, was wir suchen, sondern es wird defaultmäßig offensichtlich das
#Tupel, dessen erster Wert am kleinsten ist, gefunden. 
#Wir müssen die Minimmal-Suche vor ihrer Verwendung genauer definieren. Zu diesem Zweck
#verwenden das key-Argument der Funktion min(). Das key-Argument erwartet eine Funktion,
#die eine für den jeweiligen Anwendungszweck geeignete benutzer-orientierte Ordnungsrelation 
#über den Tupeln implementiert. In vorliegenden Fall soll also nicht bzgl. des ersten
#Tupel-Elements das Minimum bestimmt werden, sondern bzgl. des zweiten Elements.
#Die eine solche Ordnungsrelation definierende Funktion könnte man z.B. so schreiben:
def zweitesElement(tpl):
    return tpl[1]
#Diese Funktion benutzen wir nun in min:
min([(i, np.var(X[i,:])) for i in range(len(X))], key=zweitesElement)   #(3, 0.25)
#Die Funktion zweitesElement können wir natürlich auch als lambda-Funktion direkt im min-
#Aufruf schreiben:
min([(i,np.var(X[i,:])) for i in range(len(X))], key=lambda x: x[1])    #(3, 0.25)
#
#
#Es sei noch hinzugefügt, dass es einen alternativen Weg gibt, dieses Problem zu lösen.
#                                       ----------------
#Wenn wir unsere sportliche Ambition, alles mit Python-Einzeiler lösen zu wollen, kurz mal 
#fallenlassen, könnte man auch folgendes schreiben:
res_var = np.var(X, axis=1)      
res_var     #array([ 3.6875,  2.1875, 12.25  ,  0.25  ,  3.    ])
#Wir nutzen dabei aus, dass die die Varianz-Funktion in Numpy broadcasting-fähig ist.
#Siehe zur Widerholung nochmal den Abschnitt 3-5. Wenn wir ein axis-Argument angeben,
#können wir damit spezifizieren, in welcher Richtung des mehrdimensionalen Arrays wir die
#Varianzen berechnen wollen:
#
#             ------------------> axis 1
#          |   [[25,27,29,30],
#          |    [1,5,3,2],
#          |    [12,11,8,3],
#          |    [1,1,2,2],
#          v    [2,6,2,2]]
#       axis 0
#
#Das obige res_var ist wieder ein Numpy-Array:
type(res_var)     #numpy.ndarray
#Den kleinsten Wert von res_var bestimmen wir leicht:
min(res_var)      #0.25
#Wir wollen aber auch noch den Index der kleinsten Varianz haben. Wir kriegen wir
#das möglichst elegant heraus ? Natürlich via boolesches Array - siehe dazu den Abschnitt 3-3.
#Mit Hilfe des booleschen Arrays wollen wir den Ort in res_var durch ein True markieren,
#an dem sich das Minimum befindet:
res_var == min(res_var)           #array([False, False, False,  True, False])
#Und da False*Zahl immer 0 ist,z.B.:
False*5      #0
#Können wir diese Eigenschaft in folgender Weise ausnutzen:
(res_var == min(res_var))*range(len(res_var))           #array([0, 0, 0, 3, 0])
#Dass müssen wir nur noch aufsummieren, und schon haben wir den gesuchten Index:
sum((res_var == min(res_var))*range(len(res_var)))      #3
#Insgesamt können wir die Informationen, die wir suchen, also so formulieren:
(sum((res_var == min(res_var))*range(len(res_var))), min(res_var))     #(3, 0.25)
#
#Wir können den Index des Minimal-Elements aber auch noch auf eine weitere Weise berechnen. 
#Dazu gehen wir zu unserem boolschen Array zurück:
res_var == min(res_var)           #array([False, False, False,  True, False])
#Es gibt in Numpy-Arrays die Mehtode nonzero. Siehe dazu: 
#https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html
#nonzero returniert die Indizes der von 0 verschiedenen Elemente bzw. der 
#nicht-False-Elemente (im Falle unseres booleschen Arrays):
(res_var == min(res_var)).nonzero()      #(array([3], dtype=int64),)
#Wir könnten statt nonzero aber die die Numpy-Funktion where verwenden, siehe dazu:
#https://numpy.org/doc/stable/reference/generated/numpy.where.html
np.where(res_var==min(res_var))          #(array([3], dtype=int64),)
#Mit diesen beiden alternativen werkzeuge ließe sich das gewünschte Gesamtergebnis so
((res_var==min(res_var)).nonzero(), min(res_var))     #((array([3], dtype=int64),), 0.25)
#oder so
(np.where(res_var==min(res_var)), min(res_var))       #((array([3], dtype=int64),), 0.25)
#formulieren.
#Die letzten beiden Lösungen sind besser lesbar als die Einzeiler-Lösung. Es besteht also 
#eindeutig ein Kompromiss zwischen Prägnanz und Lesbarkeit. Nur weil man alles in eine 
#einzige Codezeile packen kann, heißt das nicht, dass man das auch tun sollte. Wenn alle 
#Dinge sonst gleich sind, ist es viel besser, prägnanten und lesbaren Code zu schreiben, 
#anstatt den Code mit unnötigen Definitionen, Kommentaren oder Zwischenschritten aufzublähen.
#Nachdem wir in diesem Abschnitt die Grundlagen der Varianz kennengelernt haben, sind wir 
#nun bereit zu lernen, wie man grundlegende Statistiken berechnet.





#########################################################################################
#########################################################################################
# 4.8 Basic Statistics in One Line
#########################################################################################

#Als DatenwissenschaftlerInnen und ExpertInnnen für maschinelles Lernen müssen wir über 
#grundlegende Statistik-Kenntnisse verfügen. Einige Algorithmen des maschinellen Lernens 
#beruhen vollständig auf Statistik (zum Beispiel Bayes'sche Netze).
#Das Extrahieren grundlegender statistischer Daten aus Matrizen (z.B. Durchschnitt, Varianz 
#und Standardabweichung) ist eine wichtige Komponente für die Analyse eines vielfältigen
#Anwendungsbereichs wie Finanzdaten, Gesundheitsdaten oder Daten aus sozialen Medien.
#In diesem Abschnitt wird erklärt, wie man den Durchschnitt, die Standardabweichung und 
#die Varianz entlang einer Achse eines mehrdimensionalen Numpy-Arrays berechnet. Diese 
#drei Berechnungen sind sehr ähnlich; wenn wir eine verstehen, werden wir alle verstehen.
#Folgendes konkretes Problem soll uns beschäftigen: Gegeben ist ein NumPy-Array mit 
#Aktiendaten mit Zeilen, die die verschiedenen Unternehmen angeben, und Spalten, die ihre 
#täglichen Kursentwicklungen anzeigen. Das Ziel ist es, den Durchschnitt und die Standard-
#abweichung der Aktienkurse jedes Aktienkurses der einzelnen Unternehmen zu finden. Hier 
#anhand einer prizipiellen Abbildung dargestellt:

#                                        Average along Axis 1
#              
#                                                 / 3 \
#                                                |    |
#                                                | 1  |
#                      Axis 1            ┌───►   |    |
#                    ─────────►          │       \ 2 /
#                  │                     │
#              A   │   1  3  5       ────┘
#              x   │
#              i   │   1  1  1
#              s   │                 ─────┐       / 2.66 \
#                  │   0  2  4            │      |       |
#              0   ▼                      │      | 0     |
#                                         └──►   |       |
#                                                \ 2.66 /
#              
#                                        Variance along Axis 1

#Dieses Beispiel zeigt ein zweidimensionales NumPy-Array, aber in der Praxis, kann das Array 
#eine viel höhere Dimensionalität haben.
#Angenommen, wir möchten den einfachen Durchschnitt, die Varianz oder die Standardabweichung 
#über alle Werte in einem NumPy-Array berechnen. Wir haben bereits Beispiele für den 
#Durchschnitt und die Varianzfunktion weiter oben gesehen. Die Standardabweichung ist einfach 
#die Quadratwurzel aus der Varianz. wir können dies leicht mit den folgenden Funktionen 
#erreichen:

import numpy as np

X = np.array([[1, 3, 5],
              [1, 1, 1],
              [0, 2, 4]])

print(np.average(X))         # 2.0
print(np.var(X))             # 2.4444444444444446
print(np.std(X))             # 1.5634719199411433

#Wir wenden hier diese Funktionen auf das zweidimensionale NumPy-Array X an. Aber NumPy 
#flacht das Array einfach ab und berechnet die Funktionen auf das auf eine Dimension 
#reduzierte Array. Zum Beispiel kann der einfache Durchschnitt des flattened NumPy-Array X 
#wie folgt berechnet werden:
#            (1 + 3 + 5 + 1 + 1 + 1 + 0 + 2 + 4) / 9 = 18 / 9 = 2.0
#
#Manchmal möchte man diese Funktionen jedoch entlang einer Achse (axis) berechnen. Wir können 
#dies tun, indem wir das Schlüsselwort axis als Argument für die jeweiligen Statistik-
#Funktionen angeben (siehe Abschnitt 3-5 für eine ausführliche Einführung in das axis-
#Argument). Hier nun ein etwas größeres Beispiel mit einem 2D-Numpy-array...

## Dependencies
import numpy as np

## Stock Price Data: 5 companies
# (row=[price_day_1, price_day_2, ...])
x = np.array([[8, 9, 11, 12],
              [1, 2, 2, 1],
              [2, 8, 9, 9],
              [9, 6, 6, 3],
              [3, 3, 3, 3]])

## One-liner
avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

## Result & puzzle
print("Averages: " + str(avg))               #Averages: [10.   1.5  7.   6.   3. ]
print("Variances: " + str(var))              #Variances: [2.5  0.25 8.5  4.5  0.  ]
print("Standard Deviations: " + str(std))    #Standard Deviations: [1.58113883 
                                             #                      0.5        
                                             #                      2.91547595 
                                             #                      2.12132034 
                                             #                      0.        ]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Der obige Einzeiler verwendet das Schlüsselwort axis, um die Achse anzugeben, entlang derer
#Durchschnitt, Varianz und Standardabweichung berechnet werden. Wenn Sie zum Beispiel diese 
#drei Funktionen entlang der axis=1 ausführen, wird jede Zeile zu einem einzigen Wert 
#aggregiert. D.h. die entsprechenden Werte werden über alle Spalten der betreffenden Zeile
#genommen. Und da wir aggregieren hat das resultierende NumPy-Array eine reduzierte 
#Dimensionalität von eins.
#Wie sieht das nun bei einem noch höher-dimensionalen z.B. einem 3D-Numpy-Array aus ?

import numpy as np

x = np.array([[[1,2], [1,1]],              #ein 3D-Array...
              [[1,1], [2,1]],
              [[1,0], [0,0]]])

print(np.average(x, axis=2))       #[[1.5 1. ]       <---...wird hier entlang axis 2 flattened,
                                   # [1. 1.5]              d.h. aus [[1, 2], [1, 1]] wird also
                                   # [0.5 0. ]]            [1.5  1.] etc.

print(np.var(x, axis=2))           #[[0.25 0. ]
                                   # [0. 0.25]
                                   # [0.25 0. ]]

print(np.std(x, axis=2))           #[[0.5 0. ]
                                   # [0. 0.5]
                                   # [0.5 0. ]]

#Es gibt drei Beispiele für die Berechnung von Durchschnitt, Varianz und Standardabweichung
#entlang der axis 2. Dabei werden jeweils alle Werte der Achse 2 werden zu einem einzigen Wert 
#kombiniert (flattened), was natürlich dazu führt, dass es im resultierenden Array keine 
#axis 2 mehr gibt, d.h. die Dimension des resultierendenArrays ist um 1 vermindert. 
#Dieser Abschnitt vermittelte ein tieferes Verständnis, wie man das leistungsstarke NumPy-
#Toolset nutzen kann, um schnell und effizient grundlegende Informationen aus mehrdimen-
#sionalen Arrays extrahiert. Dies ist ein Vorverarbeitungsschritt für viele Algorithmen 
#des maschinellen Lernens





#########################################################################################
#########################################################################################
# 4.9 Classification with Support-Vector Machines in One Line
#########################################################################################

#Support-Vector-Maschines (SVMs) haben in den letzten Jahren massiv an Popularität gewonnen, 
#da sie selbst in hochdimensionalen Räumen robuste Klassifikationen hervorbrigen können.
#Siehe dazu https://de.wikipedia.org/wiki/Support_Vector_Machine
#Überraschenderweise funktionieren SVMs auch dann, wenn es mehr Dimensionen (Merkmale) als 
#Datenelemente gibt. Dies ist ungewöhnlich für Klassifizierungsalgorithmen wegen des "Fluchs 
#der Dimensionalität" (curse of dimensionality): Mit zunehmender Dimensionalität werden die Daten
#extrem spärlich, was es den Algorithmen schwer macht, Muster im Datensatz zu finden.
#Siehe dazu https://de.wikipedia.org/wiki/Fluch_der_Dimensionalit%C3%A4t 
# 
#Das Verstehen der grundlegenden Ideen von SVMs ist von fundamentaler Bedeutung.
#Wie funktionieren Klassifizierungsalgorithmen? Sie verwenden die Trainingsdaten, um eine 
#Entscheidungsgrenze zu finden, die Daten der einen Klasse von Daten der anderen Klasse 
#trennt - wie in der folgenden Abb.:
                                 
#                                           /            + = Computer Scientist
#                                           /            0 = Artist
#            ▲                          ++  /  ..
#            │       +    +    +            / ...  --
#            │                     +        //.  --
#          L │                      +      ../   -
#          o │           +      +         .. /  -
#          g │                          ..   / -
#          i │             +      +   ...    /--
#          c │      +               ...      /-
#            │                    ...       -/      0
#          S │           +       ..         -/       0
#          k │                  ..         --/           0     0
#          i │                ..           - /    0
#          l │              ..            -  /
#          l │            ...            --  //    00   0       00
#          s │          ...              -    /
#            │        ...              --     /     0  00     00
#            │       ..               --      /         0  00
#            │     ...               --       /
#            │                             
#            │   several Decision boundaries ???
#            │
#            └──────────────────────────────────────────────────────────►
#                             Creativity Skills

#Angenommen, Sie möchten ein Empfehlungssystem für angehende Studenten erstellen. 
#Die obige Abbildung veranschaulicht die Trainingsdaten, die aus Benutzern bestehen,die nach 
#ihren Fähigkeiten in zwei Bereichen klassifiziert sind: Logik und Kreativität. Einige 
#Personen haben hohe Logikfähigkeiten und relativ geringe Kreativität; andere haben hohe
#Kreativität und relativ geringe Logikfähigkeiten. Die erste Gruppe wird als Informatiker 
#bezeichnet und die zweite Gruppe wird als Künstler bezeichnet.
#Um neue Benutzer zu klassifizieren, muss das maschinelle Lernmodell eine Entscheidungsgrenze
#(decision boundary) finden, die die Informatiker von den Künstlern trennt. Grob gesagt,
#klassifizieren wir einen Benutzer danach, wo er in Bezug auf die Entscheidungsgrenze fällt. 
#Im Beispiel klassifizieren wir Benutzer, die in den linken Bereich fallen, als Informatiker, 
#und Benutzer, die in den rechten Bereich fallen, als Künstler.
#Im zweidimensionalen Raum ist die Entscheidungsgrenze entweder eine Linie oder eine Kurve 
#(höherer Ordnung). Ersteres wird als linearer Klassifikator bezeichnet, letzteres als ein 
#nichtlinearer Klassifikator. In diesem Abschnitt werden nur lineare Klassifikatoren 
#untersucht.
#Die obige Abbildung zeigt drei Entscheidungsgrenzen, die alle gültige Separatoren der Daten 
#sind. In unserem Beispiel ist es unmöglich zu quantifizieren, welche der gegebenen Entschei-
#dungsgrenzen besser ist; sie führen alle zu perfekter Genauigkeit bei der Klassifizierung 
#der gegebenen Trainingsdaten.
#Aber was ist die beste Entscheidungsgrenze?
#Support-Vektor-Maschinen bieten eine einzigartige und schöne Antwort auf diese Frage. 
#Die beste Entscheidungsgrenze bietet eine maximale Sicherheit. Mit anderen Worten: SVMs 
#maximieren den Abstand zwischen den nächstgelegenen Datenpunkten und der Entscheidungsgrenze. 
#Das Ziel ist die Minimierung des Fehlers von neuen Punkten, die nahe an der Entscheidungs-
#grenze liegen, siehe folgende Abb.:

#                                                        + = Computer Scientist
#                                                        0 = Artist
#                ▲                          ++         .
#                │       +    +    +                 ...       //
#                │    Data points      +          ....      ////
#              L │                      +      +..        ///     .
#              o │           +      +       ...        ///     ....
#              g │                      ....        ///      ...
#              i │             +      ...        ////     0 ◄──────────── one Support Vector
#              c │      +           ...        ///    ....
#                │                ...       ///    .... 0
#              S │            .+...      ////    ...     0
#              k │          ....       ///     ...           0     0
#              i │     ..+...       ///      .0       0
#              l │   ....         ///     ...
#              l │  ..         ///      ...            00   0       00 Data points
#              s │           ///      ...
#                │        ///       ...                 0  00     00
#                │     ///        ...                       0  00
#                │    //       ....
#                │Decision    ..
#                │Boundary
#                │
#                └──────────────────────────────────────────────────────────►
#                                 Creativity Skills

#Der SVM-Klassifikator findet die jeweiligen Stützvektoren (support vectors) so, dass die Zone
#zwischen den Stützvektoren möglichst dick ist. Dabei sind die Stützvektoren diejenigen 
#Datenpunkte, die auf den beiden gepunkteten Linien parallel zur Entscheidungsgrenze liegen.
#Diese Linien werden als Ränder (margins) bezeichnet. Die Entscheidungsgrenze (decision 
#boundary) ist die Linie in der Mitte mit maximalem Abstand zu den Rändern. Da dieZone 
#zwischen den Rändern und der Entscheidungsgrenze maximiert ist, ist die Fehlergrenze bei 
#der Klassifizierung neuer Datenpunkte maximal. Daraus resultiert eine hohe Klassifizie-
#rungsgenauigkeit für viele praktische Probleme.
#Das alles funktioniert natürlich nur, wenn die zu klassifizierenden Datenpunkte
#"linear separabel" sind, siehe dazu: https://de.wikipedia.org/wiki/Lineare_Separierbarkeit
#Wenn das nicht der Fall ist, muss man zum sog. "Kernel-Trick" greifen, siehe dazu:
#https://de.wikipedia.org/wiki/Kernel-Methode
#Und hier ist unser "Einzeiler"...

## Dependencies
from sklearn import svm
import numpy as np

## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
              [10, 1, 2, "computer science"],
              [1, 8, 1, "literature"],
              [4, 9, 3, "literature"],
              [0, 1, 10, "art"],
              [5, 7, 9, "art"]])

## One-liner
svm = svm.SVC().fit(X[:,:-1], X[:,-1])

## Result & puzzle
student_0 = svm.predict([[3, 3, 6]])
print(student_0)

student_1 = svm.predict([[8, 1, 1]])
print(student_1)                      #['art']
                                      #['computer science']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#
#Da dem ganzen die Klasse SVC im Modul svm von sklearn zugrundeliegt, ist es sicher 
#sinnvoll, dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/svm.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#Der Code zeigt, wie man Support-Vektor-Maschinen in Python in ihrer einfachsten Form 
#verwenden kann. Das NumPy-Array enthält die beschrifteten Trainingsdaten mit einer Zeile 
#pro Benutzer und einer Spalte pro Merkmal (Kompetenzniveau in Mathematik, Sprache und 
#Kreativität). Die letzte Spalte ist das Label (die Klasse).
#Da es sich um dreidimensionale Daten handelt, trennt die Support-Vektor-Maschine die 
#Daten mit Hilfe von zweidimensionalen Ebenen (linear separator) anstelle von 
#eindimensionalen Linien. 
#Wir sehen, dass es auch möglich ist, drei Klassen zu trennen und nicht nur zwei, wie in 
#den vorangegangenen Beispielen gezeigt. Der Einzeiler selbst ist einfach: wir erstellen 
#zunächst das Modell mit dem Konstruktor der Klasse svm.SVC (SVC steht für support-vector 
#classification). Dann rufen wir die Funktion fit() auf, um das Training auf der Grundlage
#markierten Trainingsdaten durchzuführen.
#Im Ergebnisteil des Codeschnipsels rufen wir die Funktion predict() für neue Beobachtungen 
#auf. Da die Fähigkeiten von Student_0 mit Mathe=3, Sprache=3 und Kreativität=6 angegeben 
#sind, sagt die Support-Vektor-Maschine voraus, dass das label "Kunst" zu den Fähigkeiten 
#dieses Studenten passt. Ähnlich verhält es sich bei Student_1, dessen Fähigkeiten wie 
#folgt angegeben werden Mathe=8, Sprache=1 und Kreativität=1. Daher sagt die Support-Vektor-
#Maschine voraus, dass die label "Computer Science" zu den Fähigkeiten dieses Studenten 
#passt.
#Zusammenfassend lässt sich sagen, dass SVMs auch in hochdimensionalen Räumen gut 
#funktionieren, wenn es mehr Merkmale als Trainingsdatenvektoren gibt. Die Idee der 
#Maximierung der Sicherheitsspanne ist intuitiv und führt zu einer robusten Leistung bei 
#der Klassifizierung von von Grenzfällen, d.h. von Vektoren, die innerhalb des Sicherheits-
#spielraums liegen. 





#########################################################################################
#########################################################################################
# 4.10 Classification with Random Forests in One Line
#########################################################################################

#Random Forests gehören zum Typ der sog. "Ensemle-Lernverfahren".
#In den vorangegangenen Abschnitten haben wir unterschiedliche Algorithmen für maschinelles 
#Lernen kennengelernt, die man verwenden kann, um schnelle Ergebnisse zu erzielen. Allerdings 
#haben diese verschiedene Algorithmen jedoch unterschiedliche Stärken und Schwächen. 
#Neuronale Netzwerkklassifizierer können zum Beispiel bei komplexen Problemen hervorragende 
#Ergebnisse erzielen. Sie sind jedoch auch anfällig für eine Überanpassung der Daten, da sie 
#in der Lage sind, sich detaillierte Muster in den Daten zu merken. 
#Ensemble-Lernen für Klassifizierungsprobleme überwindet teilweise das Problem, dass man oft 
#nicht im Voraus weiß, welche Technik des maschinellen Lernens am besten funktioniert.
#Wie funktioniert das? Man erstellt einen Meta-Klassifikator, der aus mehreren Typen oder 
#Instanzen von grundlegenden Algorithmen des maschinellen Lernens besteht. Mit anderen Worten,
#man trainiert mehrere Modelle. Um eine einzelne Beobachtung zu klassifizieren, fragen wir 
#alle Modelle, die neue Eingabe unabhängig voneinander zu klassifizieren. Anschließend geben 
#wir diejenige Klasse als Meta-Vorhersage zurück, die am häufigsten von den involvierten 
#Modellen gefunden wurde. Dies ist dann die endgültige Ausgabe unseres Ensemble-Lern-
#algorithmus.
#"Random Forests" sind eine besondere Art von Ensemble-Lernalgorithmen. Sie konzentrieren 
#sich auf das Lernen von Entscheidungsbäumen. Ein Wald besteht aus vielen Bäumen. In ähnlicher 
#Weise besteht ein Random Forest aus vielen Entscheidungsbäumen. Jeder Entscheidungsbaum wird 
#aufgebaut, indem Zufälligkeit in das Baumerzeugungsverfahren während der Trainingsphase 
#eingefügt wird (z.B. welcher Baumknoten zuerst ausgewählt werden soll, wird zufällig 
#festgelegt). Dies führt zu verschiedenen Entscheidungsbäumen - genau das, was wir wollen.
#Die nächste Abbildung zeigt, wie die Vorhersage für einen trainierten Random Forest 
#funktioniert anhand des folgenden Szenarios:
#Alice hat hohe Mathematik(Math)- und Sprach(Lang.)-Kenntnisse. Das Ensemble besteht aus 
#drei Entscheidungsbäumen (die einen Random Forest bilden). Um Alice zu klassifizieren, wird 
#jeder Entscheidungsbaum nach der Klassifizierung von Alice befragt. Zwei der Entscheidungs-
#bäume stufen Alice als Informatikerin ein. Da dies die Klasse mit den meisten Stimmen ist, 
#wird sie als endgültige Ausgabe für die Klassifizierung zurückgegeben.

#                            Alice (Math=Yes, Language=Yes)
#                                             /\
#    ________________________________________/  \__________________________________________________
#   /                                                                                              \
#  /                                                                                                \
#  
#        ┌────────┐                       ┌─────────┐                   ┌──────────┐
#        │ Math?  │                       │ Math?   │                   │Language? │
#  Yes┌──┤        ├────┐No        Yes┌────┤         ├────┐No      Yes┌──┤          ├──────┐No
#     │  └────────┘    │             │    └─────────┘    │           │  └──────────┘      │
#     │                │             │                   │           │                    │
#     │                │             │                   │           │                    │
#     │                │             │                   │           │                    │
#     ▼                │             ▼                   │           ▼                    │
#    CS                ▼            CS                   ▼         Ling.                  ▼
#                ┌─────────┐                         ┌─────────┐                    ┌──────────┐
#                │Language?│                  Yes┌───┤Language?├───┐No      Yes┌────┤ Math?    ├──┐No
#         Yes┌───┤         ├───┐No               │   │         │   │           │    │          │  │
#            │   └─────────┘   │                 │   └─────────┘   │           │    └──────────┘  │
#            │                 │                 │                 │           │                  │
#            │                 │                 ▼                 ▼           ▼                  ▼
#            ▼                 ▼               Ling.             Hist.        CS                 Art
#           CS               Hist.
#  
#  \     DECISION TREE 1: CS            DECISION TREE 2: CS               DECISION TREE 3: Ling.     /
#   \________________________________________    ___________________________________________________/
#                                            \  /
#                                             \/
#                                       Final Output: CS

#Bleiben wir bei diesem Beispiel der Klassifizierung des Studienfachs auf der Grundlage der
#Kompetenzniveau in drei Bereichen (Mathematik, Sprache, Kreativität). Man könnte denken, dass
#die Implementierung einer Ensemble-Lernmethode in Python kompliziert ist. Aber dank der 
#umfassenden scikit-learn Bibliothek ist das nicht der Fall...

### Dependencies
import numpy as np
from sklearn.ensemble import RandomForestClassifier

## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
              [5, 1, 5, "computer science"],
              [8, 8, 8, "computer science"],
              [1, 10, 7, "literature"],
              [1, 8, 1, "literature"],
              [5, 7, 9, "art"],
              [1, 1, 6, "art"]])

## One-liner
Forest = RandomForestClassifier(n_estimators=10).fit(X[:,:-1], X[:,-1])

## Result
students = Forest.predict([[8, 6, 5],
                           [3, 7, 9],
                           [2, 2, 1]])
print(students)     #['computer science' 
                    # 'art' 
                    # 'literature']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#
#Da dem ganzen die Klasse RandomForestClassifier im Modul ensemble von sklearn zugrundeliegt, 
#ist es sicher sinnvoll, dass wir deren Doku mal ansehen:
#       https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#Weiter unten in dieser Doku findet man auch konkrete Beispiele.
#
#Nach der Initialisierung der gelabelten Trainingsdaten im obigen Listing erstellt der Code
#einen Random forest, indem er den Konstruktor der Klasse RandomForestClassifier mit einem 
#Parameter n_estimators, der die Anzahl der Bäume im Forest definiert. Als Nächstes füllen
#und trainieren wir das Modell, das aus der vorherigen Initialisierung resultiert durch 
#Aufruf der Funktion fit().
#Dazu bestehen die Eingabedaten aus allen Daten bis auf die letzte Spalte des Arrays X, 
#während die Labels der Trainingsdaten in der letzten Spalte definiert sind. Wie in den 
#vorherigen Beispielen verwenden wir Slicing, um die entsprechenden Spalten aus dem 
#Datenfeld X zu extrahieren.
#Der Klassifizierungsteil (mit predict) ist in diesem Codeschnipsel etwas anders. 
#Hier sollte mal gezeigt werden, wie man mehrere Beobachtungen statt nur einer 
#klassifizieren kann, indem ein mehrdimensionales Array mit einer Zeile pro Beobachtung
#verwendet wird.
#Beachte, dass das Ergebnis immer noch nicht deterministisch ist (das Ergebnis kann bei
#verschiedenen Ausführungen des Codes unterschiedlich ausfallen), da der Random-Forest-
#Algorithmus auf dem Zufallszahlengenerator beruht. Man kann diesen Aufruf aber 
#deterministisch machen, indem man das integer-Argument random_state verwendet. 
#Zum Beispiel kann man random_state=1 setzen, wenn der den Konstruktor des Random Forest
#aufgerufen wird: RandomForestClassifier(n_estimators=10, random_state=1). 
#In diesem Fall wird jedes Mal, wenn man einen neuen Random-Forest-Klassifikator erstellt, 
#die gleiche Ausgabe erzeugt, da jetzt immer die gleichen Zufallszahlen erzeugt werden:
#Sie basieren alle auf der Seed-Ganzzahl 1.
#Zusammenfassend lässt sich sagen, dass in diesem Abschnitt ein Meta-Ansatz für die 
#Klassifizierung vorgestellt wurde:
#Die Verwendung der Ergebnisse verschiedener Entscheidungsbäume dient der Verringerung der 
#Varianz des Klassifizierungsfehlers. Dies ist eine Variante des Ensemble-Lernens, das
#mehrere Basismodelle zu einem einzigen Metamodell kombiniert, das ihre individuellen 
#Stärken nutzen kann.
#Beachte: Zwei unterschiedliche Entscheidungsbäume können zu einer hohen Varianz des Fehlers 
#führen: Der eine liefert gute Ergebnisse, während der andere dies nicht tut. Durch die 
#Verwendung von Random Forests kannen man diesen Effekt abmildern.
#Variationen dieser Idee sind beim maschinellen Lernen üblich - und wenn man die 
#Vorhersagegenauigkeit schnell verbessern muss, führt man einfach mehrere Modelle des 
#maschinellen Lernens aus und bewertet deren Ergebnisse, um das beste Modell zu finden.
#In gewisser Weise realisieren Ensemble das, was in der Praxis des maschinellen 
#Lernens häufig sowieso gemacht wird: Auswählen, Vergleichen, und Kombinieren der Ergebnisse 
#verschiedener maschineller Lernmodelle. Die große Stärke des Ensemble-Lernens ist, dass dies 
#für jeden Datenwert einzeln zur Laufzeit erfolgt.





#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                    5 - Regular Expressions
#                                    =====================================





#########################################################################################
#########################################################################################
# 5.1 Finding Basic Textual Patterns in Strings
#########################################################################################

#In den nächsten Kapiteln lernen wir eine unterschätzte Technik kennen, mit der die Arbeit 
#mit Textdaten effizienter wird: die Verwendung regulärer Ausdrücke. Schrittweise lernen wir, 
#reguläre Ausdrücke zu verwenden, um alltägliche Probleme mit weniger Aufwand, Zeit und 
#Energie zu lösen. Data Science (DS) und Machine Learning (ML) basieren auf Daten. ALLE Daten sind 
#letztlich "Textdaten" (more or less), die häufig (immer ?) irgendwie vorbereitet, gesäubert 
#oder sonst irgendwie bearbeitet werden müssen, bevor sie für DS oder ML verwendbar sind.
#Für diese Datenaufbereitung ist Regex perfekt geeignet. 
#Alle "großen" Programmiersprachen stellen eine Regex-Lib zur Verfügung. In Python allerdings
#ist sie besonders leicht verwendbar.
#
#Was sind "reguläre Ausdrücke" ?
#-------------------------------
#siehe dazu:
#       https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck
#       https://de.wikipedia.org/wiki/Chomsky-Hierarchie
#
#Mit dem "regex-coach (von Edi Weitz)" 
#-------------------------------------
#kann man üben, komplexe regexes ausprobieren und debuggen (die Webseite enthält auch ein 
#gutes Tutorial):
#http://www.weitz.de/regex-coach/
#
#Und die "Doku von Pythons regex-Bibliothek" brauchen wir jetzt immer wieder:
#---------------------------------------
# https://docs.python.org/3/library/re.html
#
#In diesem Abschnitt werden reguläre Ausdrücke unter Verwendung des Moduls re und seine 
#wichtige Funktion re.findall() eingeführt. Wir beginnen mit der Erläuterung einiger 
#grundlegender reguläre Ausdrücke (regular expressions, kurz: regex). Ein regulärer 
#Ausdruck beschreibt formal ein Suchmuster, das wir verwenden können, um Textabschnitte 
#abzugleichen. Das einfache Beispiel zeigt eine Suche in Shakespeares Text "Romeo und Julia".
#Siehe: https://de.wikipedia.org/wiki/Romeo_und_Julia
#und https://de.wikisource.org/wiki/Romeo_und_Julia_(%C3%9Cbersetzung_Schlegel)
#Hier ist daraus ein Textauszug (aus dem Drittem Aufzug, Dritte Szene):
txt_romeo_julia = """Romeo. Nein, Folter – Gnade nicht! Hier ist der Himmel,
                     Wo Julia lebt, und jeder Hund und Katze
                     Und kleine Maus, das schlechteste Geschöpf,
                     Lebt hier im Himmel, darf ihr Antlitz sehn;
                     Doch Romeo darf nicht. Mehr Würdigkeit,
                     Mehr Ansehn, mehr gefäll’ge Sitte lebt
                     In Fliegen, als in Romeo. Sie dürfen
                     Das Wunderwerk der weißen Hand berühren,
                     Und Himmelswonne rauben ihren Lippen,
                     Die sittsam, in Vestalenunschuld, stets
                     Erröten, gleich als wäre Sünd’ ihr Kuß.
                     Dies dürfen Fliegen thun, ich muß entfliehn;
                     Sie sind ein freies Volk, ich bin verbannt.
                     Und sagst du noch: Verbannung sei nicht Tod?
                     So hattest du kein Gift gemischt, kein Messer
                     Geschärft, kein schmählich Mittel schnellen Todes,
                     Als dies verbannt, zu töten mich? Verbannt!
                     O Mönch! Verdammte sprechen in der Hölle
                     Dies Wort mit Heulen aus: hast du das Herz,
                     Da du ein heil’ger Mann, ein Beicht’ger bist,
                     Ein Sündenlöser, mein erklärter Freund,
                     Mich zu zermalmen mit dem Wort Verbannung?
                     
                     Lorenzo. Du kindisch blöder Mann, hör’ doch ein Wort!
                     
                     Romeo. O, du willst wieder von Verbannung sprechen!
                     
                     Lorenzo. Ich will dir eine Wehr dagegen leihn,
                     Der Trübsal süße Milch, Philosophie,
                     Um dich zu trösten, bist du gleich verbannt.
                     
                     Romeo. Und noch verbannt? Hängt die Philosophie!
                     Kann sie nicht schaffen eine Julia,
                     Aufheben eines Fürsten Urteilspruch,
                     Verpflanzen eine Stadt: so hilft sie nicht,
                     So taugt sie nicht; so rede länger nicht! 
                     """
#Und wir wollen hierin nach dem Muster (pattern) "Julia" suchen:
import re
print(re.findall('Julia', txt_romeo_julia))             #['Julia', 'Julia']
#Zwei Treffer (zweite und viertletzte Zeile) !!
#
#Wir lernen hier: der einfachste reguläre Ausdruck besteht aus einem einfachen String.
#Die Zeichenkette "Julia" ist ein absolut gültiger regulärer Ausdruck. Reguläre Ausdrücke 
#sind unglaublich leistungsfähig und können viel mehr als die Suche nach regulärem Text, 
#aber sie werden mit nur einer Handvoll grundlegender Befehle zusammengesetzt. Wir lernen
#hier diese grundlegenden Befehle und werden dadurch in der Lage sein, komplexe reguläre 
#Ausdrücke zu schreiben. In diesem Abschnitt werden wir uns auf die drei wichtigsten Regex-
#Befehle konzentrieren, die die Funktionalität der trivialen Suche (siehe obiges Beispiel) 
#nach Zeichenkettenmustern in einem bestimmten Text erweitern:

#Der Punkt-Regex
#---------------
#Zunächst müssen wir wissen, wie man ein beliebiges Zeichen mit Hilfe des Punkt-Regex, 
#dem . Zeichen, beschreibt. Der Punkt-Regex passt auf jedes Zeichen (einschließlich
#Leerzeichen). Mit ihm können wir angeben, dass es Ihnen egal ist, welches Zeichen passt, 
#solange genau eines passt:
import re
text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.
'''
print(re.findall('b...k', text))           # ['block', 'block', 'block']
#Dieses Beispiel verwendet die findall()-Methode des Moduls re. Das erste Argument ist der 
#Regex selbst: wir suchen nach einem beliebigen Zeichenkettenmuster, das mit dem Zeichen 'b'
#beginnt, gefolgt von drei beliebigen Zeichen, ... , gefolgt von dem Zeichen 'k'. Dieser 
#Regex b...k passt auf das Wort 'block', aber auch auf 'boook', 'b erk' und 'bloek'. 
#Der zweite Parameter von findall() ist der Text den wir durchsuchen wollen. Die String-
#Variable text enthält drei passende Muster, wie man in der Ausgabe der print-Anweisung sehen 
#kann.

#Der Asterisk Regex
#------------------
#Angenommen, wir wollen einen Text finden, der mit dem Zeichen "y" beginnt und endet und eine 
#beliebige Anzahl von Zeichen dazwischen besitzt. Wie können wir dies bewerkstelligen?
#Mit dem Asterisk Regex, dem *-Zeichen, können wir dies erreichen. Im Gegensatz zum
#Punkt-Regex kann das Sternchen-Regex nicht für sich alleine stehen; es verändert nämlich
#die Bedeutung des ihm direkt vorausgehenden Regex. 
#Betrachten wir das folgende Beispiel:
print(re.findall('y.*y', text))       # ['yptography']
#Der Asterisk-Operator gilt für den Regex, der unmittelbar davor steht.
#In diesem Beispiel beginnt das Regex-Muster mit dem Zeichen "y", gefolgt von eine beliebigen 
#Anzahl von Zeichen, .*, gefolgt von dem Zeichen 'y'. Beliebig kann aber auch bedeuten: kein 
#Zeichen. 
#Wie wir sehen können, enthält das Wort "cryptography" eine solche Instanz dieses Musters: 
#nämlich "yptography".
#Man fragt sich jetzt natürlich , warum dieser Code nicht die lange Teilzeichenkette zwischen
#'originally' und 'cryptography' findet, die ebenfalls dem Regex-Muster y.*y entsprechen. 
#Der Grund ist einfach, dass der Punktoperator auf jedes Zeichen außer dem Zeilenumbruchs-
#zeichen passt. Die in der Variablen text gespeicherte Zeichenfolge ist aber eine mehrzeilige
#Zeichenkette mit drei neuen Zeilen (also mit Zeilenumbrüchen am Ende). Wir können den 
#Asterisk-Operator (Sternchen-Operator) auch in Kombination mit einem anderen Regex verwenden. 
#Zum Beispiel können wir den Regex abc* verwenden, um mit den Zeichenfolgen 'ab', 'abc', 
#'abcc' und 'abccdc' zu matchen.

#Der Null-oder-eins-Regex
#------------------------
#Häufig müssen wir wissen, wie man null oder ein Zeichen matchen kann. Wir machen das, indem 
#wir den Null-oder-Eins-Regex, also das ? Zeichen, verwenden. Genau wie der Stern-Operator 
#modifiziert das Fragezeichen, den direkt vorangehenden Regex, wie wir im folgenden Beispiel 
#sehen können:
print(re.findall('blocks?', text))      #['block', 'block', 'blocks']
#Der Null-oder-Eins-Regex, ?, gilt für den Regex, der unmittelbar vor ihm steht.
#Im vorliegenden Fall ist dies das Zeichen s. Der Null-oder-Eins-Regex besagt, dass der
#Regex vor ihm, den er modifiziert, optional ist.
#Es gibt noch eine weitere Verwendung des Fragezeichens im re-Paket von Python, die aber
#hat aber nichts mit dem Null-oder-Eins-Regex zu tun: Das Fragezeichen kann mit dem Asterisk-
#Operator *? kombiniert werden, um ein "non-greedy (nicht-gierig) pattern matching" zu
#                                       ------------------------- 
#ermöglichen. Wenn wir zum Beispiel den Regex .*? verwenden, sucht Python nach einer minimalen 
#Anzahl beliebiger Zeichen. Wenn wir dagegen den Sternchenoperator * ohne das Fragezeichen 
#verwenden, also .*, werden greedily (gierig) so viele Zeichen wie möglich abgeglichen.
#                           -----------------
#Schauen wir uns ein Beispiel an: 
#Bei der Suche in der HTML-Zeichenkette '<div>hello world</div>' mit dem Regex <.*>, wird 
#die ganze Zeichenkette '<div>hello world</div>' und nicht nur das Präfix '<div>' gefunden. 
#Wenn wir aber nur das Präfix '<div>' wollen, müssen wir die non-greedy Regex <.*?> 
#verwenden:
txt = '<div>hello world</div>'
print(re.findall('<.*>', txt))       # ['<div>hello world</div>']
print(re.findall('<.*?>', txt))      # ['<div>', '</div>']

#Ausgestattet mit diesen drei Werkzeugen - dem Punkt-Regex ., dem Sternchen-Regex *, 
#und dem Null-oder-Eins-Regex ? - sind wir nun in der Lage, die nächste One-Liner-Lösung 
#zu verstehen. Unsere Eingabe ist eine Zeichenkette, und unser Ziel ist es, einen 
#non-greedy Ansatz zu verwenden, um alle Muster zu finden, die mit dem Zeichen 'p' beginnen, 
#mit dem Zeichen 'r' enden und mindestens ein Vorkommen des Zeichens 'e' (und möglicherweise 
#eine beliebige Anzahl von anderen Zeichen) dazwischen haben...

## Dependencies
import re

## Data
text = 'peter piper picked a peck of pickled peppers'

## One-Liner
result = re.findall('p.*?e.*?r', text)

## Result
print(result)           #['peter', 'piper', 'picked a peck of pickled pepper']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Die Regex-Suchanfrage lautet p.*?e.*?r . Wir schlüsseln das mal auf. Wir suchen im Text nach 
#einer Phrase, die mit dem Zeichen "p" beginnt und mit dem Zeichen "r" endet. Zwischen diesen 
#beiden Zeichen benötigen wir ein Vorkommen des Zeichen 'e'. Darüber hinaus ist eine 
#beliebige Anzahl von Zeichen erlaubt (Leerzeichen oder nicht) zwischen 'p' und 'e' sowie
#zwischen 'e' und 'r'. Wir können bei diesem Zwischenbereichen die Übereinstimmung jedoch 
#auf non-greedy Weise herstellen, indem wir im Regex .*? jeweils verwenden, d.h. Python sucht 
#dann nach einer minimalen Anzahl beliebiger Zeichen. 

#Vergleichen wir diese Lösung mit der, die wir erhalten würden, wenn wir die greedy-Variante
#des Regex verwenden, also p.*e.*r:
re.findall('p.*e.*r', text)          #['peter piper picked a peck of pickled pepper']
#Jetzt wird nicht mehr nach minimalen Zwischenbereichen gesucht, sondern der erste .*
#Part umfasst nun fast den gesamten zu durchsuchenden Text als Zwischenbereich zwischen
#dem ersten p und einem e:
re.findall('p.*e', text)   #['peter piper picked a peck of pickled peppe']
#Dann belibt zwischen diesem letzten e am ende von peppe un dem darauffolgenden r
#nicht mehr übrig - aber auch das ist ja durch den zweiten .* Part abgedeckt.

#Die vier Varianten für Regexe mit greedy oder non-greedy Zwischenbereichen 
#erzeugen also folgende Treffer:
re.findall('p.*?e.*?r', text)    #['peter', 'piper', 'picked a peck of pickled pepper']
re.findall('p.*?e.*r', text)     #['peter piper picked a peck of pickled pepper']
re.findall('p.*e.*?r', text)     #['peter piper picked a peck of pickled pepper']
re.findall('p.*e.*r', text)      #['peter piper picked a peck of pickled pepper']





#########################################################################################
#########################################################################################
# 5.2 Writing Your First Web Scraper with Regular Expressions
#########################################################################################

#Angenommen, wir arbeiten als freiberufliche Softwareentwickler. Unser Kunde ist ein
#KI-Startup, das über die neuesten Entwicklungen im Bereich KI-Anwendungen benachrichtigt
#werden will. Wir werden beauftragt, einen Web Scraper zu schreiben, der regelmäßig den
#HTML-Quellcode von Nachrichten-Websites abruft und ihn nach Wörtern durchsucht, die mit
#"KI" beginnt (zum Beispiel "KI-Anwendungen", "KI-Bot", "KI-Crash" und so weiter).
#Unser erster Versuch ist der folgende Codeschnipsel (ausprobiert am 2.5.2023):
import urllib.request
search_phrase = 'KI'
with urllib.request.urlopen('https://www.heise.de/') as response:
    html = response.read().decode("utf8") # convert to string
    first_pos = html.find(search_phrase)
    print(html[first_pos-10:first_pos+10])                          #in-Apples-KI-Abteilu
with urllib.request.urlopen('https://www.golem.de/') as response:   #          --
    html = response.read().decode("utf8") # convert to string
    first_pos = html.find(search_phrase)
    print(html[first_pos-10:first_pos+10])                          #BqDRjg8O4ZKIBNAgkBjG
                                                                    #          --
#Die Methode urlopen() (aus dem Modul urllib.request) holt den HTML-Quellcode von der 
#angegebenen URL. Da es sich bei dem Ergebnis um ein Byte Array handelt, müssen wir es 
#zunächst mit der Methode decode() in einen String umwandeln.
#Dann verwenden wir die String-Methode find(), um die Position des ersten Vorkommens der 
#gesuchten Zeichenkette zurückzugeben. Mit Slicing (siehe Kapitel 2) schneiden wir eine 
#Teilzeichenkette heraus, die die unmittelbare Umgebung der Position zurückgibt.
#Das Ergebnis sind die folgende Zeichenketten (Stand 2.5.2023):
#                 "in-Apples-KI-Abteilu"
#                 "BqDRjg8O4ZKIBNAgkBjG"
#Oh. Das sieht übel aus. Wie sich herausstellt, ist die Suchphrase mehrdeutig -
#Die viele Wörter, die "KI" enthalten, haben semantisch nichts mit KI zu tun. Unser Scraper 
#erzeugt falsch positive Ergebnisse (er findet Zeichenfolgen, die wir ursprünglich nicht 
#finden wollten). Wie können wir das also beheben?
#Natürlich mit Regulären Ausdrücken! Eine Idee zur Beseitigung falsch positiver Ergebnisse 
#ist die Suche nach Vorkommen, in denen das Wort 'KI' von bis zu 30 beliebigen Zeichen 
#gefolgt wird, gefolgt von dem Wort "Bot". Grob gesagt, lautet die Suchanfrage somit
#"KI + <bis zu 30 beliebige Zeichen> + Bot". Betrachten Sie die folgenden (fingierten) 
#Beispiele (und die zu erwartenden Ergebnisse der Regex-Suche):
#
# - "KI-Bot, der mit Bitcoin handelt"                            - ja   (Treffer: richtig-positiv)
# - "Kann man mit KI auch was anderes machen als ChatBots ?"     - nein (da Zwischentext 33 Zeichen 
#                                                                        lang: richtig-negativ)
# - "KI kann Gedanken lesen"                                     - nein (der geht uns durch die 
#                                                                        Lappen: richtig-negativ)
# - "KINDERGÄRTEN in Bottrop sollen mit Tablets ausgestattet werden"  - ja (Treffer, obwohl nix 
#                                                                           mit KI: falsch-positiv) 
#
#Also wir sehen: unsere Idee ist auch nicht Narrensicher - trotzdem wollen wir es erstmal
#mit ihr probieren.
#Wie lässt sich also das Problem lösen, dass bis zu 30 beliebige Zeichen zwischen zwei 
#Zeichenfolgen zulässig sind?
#Das geht über eine einfache Zeichenketten-Suche hinaus. Man kann nicht jedes exakte Zeichen-
#kettenmuster erfassen - eine nahezu unendliche Anzahl von Übereinstimmungen ist ja erlaubt. 
#Das Suchmuster muss zum Beispiel alle der folgenden Begriffe enthalten:
#'KI ... Bot'
#Selbst wenn wir nur 26 Zeichen im Alphabet hätten, wäre die Anzahl von Zeichenfolgen, die 
#theoretisch unserer Anforderung entsprechen würden, von der Größenordnung
#  26^30 = 2813198901284745919258621029615971520741376. 
#Im Folgenden, lernen wir, wie man einen Text nach einem Regex-Muster durchsuchen kann, das 
#einer großen Anzahl möglicher Zeichenkettenmuster entspricht...

## Dependencies
import re

## Data
text_1 = "KI-Bot, der mit Bitcoin handelt"
text_2 = "Kann man mit KI auch was anderes machen als ChatBots ?"
text_3 = "KI kann Gedanken lesen"
text_4 = "KINDERGÄRTEN in Bottrop sollen mit Tablets ausgestattet werden"

## One-Liner
pattern = re.compile("KI(.{1,30})Bot")

## Result
print(pattern.match(text_1))          #<re.Match object; span=(0, 6), match='KI-Bot'>
print(pattern.match(text_2))          #None
print(pattern.match(text_3))          #None
print(pattern.match(text_4))          #<re.Match object; span=(0, 19), match='KINDERGÄRTEN in Bot'>


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wir verwenden die folgenden speziellen Regex-Zeichen und lesen Sie von oben nach unten, 
#um so die Bedeutung des Gesamt-Musters schrittweise zu verstehen:
#       - ()               passt auf jeden Regex, der darin enthalten ist.
#       - .                passt auf ein beliebiges Zeichen.
#       - {1,30}           passt auf 1 bis 30 Vorkommen des vorherigen Regex.
#       - (.{1,30})        passt auf 1 bis 30 beliebige Zeichen.
#       - KI(.{1,30})Bot   passt auf den Regex, der aus drei Teilen besteht: dem
#                          Wort "KI", einer beliebigen Sequenz mit 1 bis 30 Zeichen, 
#                          gefolgt von dem Wort "Bot".
#Wir sagen dann, dass das Muster kompiliert wird, weil Python dadurch ein Muster-Objekt 
#erstellt, das an mehreren Stellen wiederverwendet werden kann - ähnlich wie ein kompiliertes 
#Programm mehrfach hocheffizient ausgeführt werden kann. Nun rufen wir die Funktion match() 
#unseres kompilierten Musters und dem zu durchsuchenden Text auf. Dies führt dann zu den
#obigen Ergebnissen: text_1 und text_4 sind Treffer (text_4 fälschlicherweise), text_2 und 
#text_3 sind fälschlicherweise keine Treffer (text_2 hat zwar mit KI zu tun, es fehlt aber
#'Bot'; bei text_3 ist ist Zwischentext zu lang (mehr als 30 Zeichen)).
#Wir sehen an diesem Beispiel, dass Regex perfekt funktioniert - allerdings besteht
#weiterhin die prinzipielle Schwierigekeit, durch explizite Regeln eine bestimmte Situation
#vollständig zu erfassen. Regelbasierte Lösungen sind immer tricky! Aber damit sind wir 
#bereits bei den Grundlagen der KI angelangt.





#########################################################################################
#########################################################################################
# 5.3 Analyzing Hyperlinks of HTML Documents
#########################################################################################

#Je mehr reguläre Ausdrücke man kennt, desto besser kann man Probleme aus der Praxis
#schnell und prägnant lösen. Welches sind nun die wichtigsten regulären Ausdrücke?
#Studieren wir die folgende Liste sorgfältig, denn wir werden sie alle in diesem Kapitel 
#verwenden:
#
# - Punkt-Regex 
#   .                       passt auf ein beliebiges Zeichen.
#
# - Stern-Regex 
#   <Muster>*               passt auf eine beliebige Anzahl des Regex <Muster>. 
#                           Beachte, dass dies auch Nullübereinstimmungen einschließt.
#
# - Mindestens-Eins-Regex 
#   <Muster>+               kann auf eine beliebige Anzahl von <Muster> passen, muss 
#                           aber auf mindestens eine Instanz passen.
#
# - Null-oder-Eins-Regex 
#   <Muster>?               passt entweder auf null oder eine Instanz von <Muster>.
#
# - Non-Greedy Sternchen-Regex 
#   *?                      passt auf so wenige beliebige Zeichen wie möglich, die
#                           mit gesamten Regex übereinstimmen.
#
# - Regex 
#   <Muster>{m}             passt auf genau m Kopien von <Muster>.
#
# - Regex 
#   <Muster>{m,n}           passt auf m bis n Kopien von <Muster>.
#
# - Regex 
#   <Muster_1>|<Muster_2>   passt entweder auf <Muster_1> oder <Muster_2>.
#
# - Regex 
#   <Muster_1><Muster_2>    entspricht <Muster_1> und dann <Muster_2>.
#
# - Regex 
#   (<Muster>)              entspricht <Muster>. Die Klammern gruppieren reguläre Ausdrücke, 
#                           so dass Sie die Reihenfolge der Ausführung steuern können (z.B.
#                           (<Muster_1><Muster_2>)|<Muster_3> ist anders als 
#                           <Muster_1>(<Muster_2>|<Muster_3>). Der Regex in Klammern erzeugt 
#                           auch eine übereinstimmende Gruppe, wie wir später in diesem 
#                           Abschnitt noch sehen werden.

#Ein Beispiel:
#Angenommen, wir erstellen den Regex b?(.a)*. Zu welchen Mustern wird der Regex passen? 
#Er passt auf alle Muster, die mit Null oder einem b beginnen und eine beliebige Anzahl von 
#Zwei-Zeichen-Sequenzen, die mit mit dem Zeichen 'a' enden. Folglich werden die Zeichenfolgen 
#'bcacaca', 'cadaea', '' (die leere Zeichenkette) und 'aaaaaa' alle auf diesen Regex passen.
import re
pattern = re.compile("b?(.a)*")            
pattern.match('bcacaca')                   #<re.Match object; span=(0, 7), match='bcacaca'>
pattern.match('cadaea')                    #<re.Match object; span=(0, 6), match='cadaea'>
pattern.match('')                          #<re.Match object; span=(0, 0), match=''>
pattern.match('aaaaaa')                    #<re.Match object; span=(0, 6), match='aaaaaa'>

#Bevor wir uns dem nächsten Einzeiler zuwenden, sollten wir kurz besprechen, wann man
#welche Regex-Funktion verwendet. Die drei wichtigsten Regex-Funktionen sind
#   
#           re.match(), 
#           re.search(), 
#       und re.findall(). 
#
#Zwei davon haben wir bereits kennengelernt, aber in diesem Beispiel wollen wir alle drei 
#nochmal genauer untersuchen und vergleichen:
import re
text = '''
"One can never have enough socks", said Dumbledore.
"Another Christmas has come and gone and I didn't
get a single pair. People will insist on giving me books."
Christmas Quote
'''
regex = 'Christ.*'
print(re.match(regex, text))             # None
print(re.search(regex, text))            # <re.Match object; span=(62, 102), match="Christmas has come and gone and I didn't">
print(re.findall(regex, text))           # ["Christmas has come and gone and I didn't", 'Christmas Quote']
#Alle drei Funktionen nehmen den Regex und die zu durchsuchende Zeichenkette als Eingabe. 
#Die Funktionen match() und search() geben ein Match-Objekt zurück (oder None, wenn der Regex 
#keine Übereinstimmung gefunden hat). Das match-Objekt speichert die Position der 
#Übereinstimmung und weitere Meta-Informationen. 
#Die Funktion match() findet die Regex nicht in der Zeichenkette (sie gibt None zurück). 
#             -------
#Und warum? Weil die Funktion nur am Anfang der Zeichenkette nach dem Muster sucht. 
#Die Funktion search() sucht nach dem ersten Vorkommen des Regex irgendwo in der Zeichenfolge. 
#             --------
#Daher findet sie die Übereinstimmung "Christmas has come and gone and I didn't".
#Die Funktion findall() hat die intuitivste Ausgabe, aber sie ist auch die am wenigsten 
#             ---------
#nützliche für die weitere Verarbeitung. Das Ergebnis von findall() ist eine Folge von
#Strings und nicht ein Match-Objekt - es gibt uns also keine Informationen über den genauen 
#Ort der Übereinstimmung. Dennoch hat findall() seinen Nutzen: Im Gegensatz zu den Methoden 
#match() und search() liefert die Funktion findall() alle übereinstimmenden Muster, was 
#nützlich ist, wenn man feststellen will, wie oft ein Wort in einem Text vorkommt (z.B. die 
#Zeichenkette 'Jula' im Text 'Romeo und und Julia' oder die Zeichenfolge 'KI' in einem 
#Artikel über KI-Anwendungen).

#Angenommen, ein Unternehmen bittet Sie, einen kleinen Web-Bot zu erstellen, der Webseiten 
#durchsucht und prüft, ob sie Links zur Domain "finxter.com" enthalten. Das Unternehmen bittet 
#auch darum sicherzustellen, dass die Hyperlink-Beschreibungen die Zeichenfolgen 'test' oder
#'puzzle' enthalten. In HTML werden Hyperlinks in eine <a></a>-Tag-Umgebung eingeschlossen.
#Der Hyperlink selbst wird im <a>-Tag durch den Wert des href-Attributs definiert. Folgendes 
#Problem ist jetzt zu lösen: es sollen in einer Zeichenkette alle darin enthaltenen Hyperlinks 
#gefunden werden, die auf die Domain finxter.com zeigen und die die Zeichenketten 'test' oder 
#'puzzle' in der Linkbeschreibung enthalten...

## Dependencies
import re

## Data
page = '''
<!DOCTYPE html>
<html>
<body>
<h1>My Programming Links</h1>
<a href="https://app.finxter.com/">test your Python skills</a>
<a href="https://blog.finxter.com/recursion/">Learn recursion</a>
<a href="https://nostarch.com/">Great books from NoStarchPress</a>
<a href="http://finxter.com/">Solve more Python puzzles</a>
</body>
</html>
'''

## One-Liner
practice_tests = re.findall("(<a.*?finxter.*?(test|puzzle).*?>)", page)

## Result
print(practice_tests)      #[('<a href="https://app.finxter.com/">test your Python skills</a>', 'test'),
                           # ('<a href="http://finxter.com/">Solve more Python puzzles</a>', 'puzzle')]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Die Daten bestehen aus einer einfachen HTML-Webseite (gespeichert als mehrzeiliger String), 
#der eine Liste von Hyperlinks enthält (jeweils in Tag-Umgebungen <a href="">link text</a>).
#Die Einzeilerlösung verwendet die Funktion re.findall() zur Überprüfung des regulären
#Ausdrucks (<a.*?finxter.*?(test|puzzle).*?>). Auf diese Weise sucht der reguläre Ausdruck
#alle Vorkommnisse in der Tag-Umgebung <a. ...> mit den folgenden folgenden Einschränkungen:
#Nach dem öffnenden Tag "<a" definieren wir eine beliebige Anzahl von Zeichen .*? (non-greedy, 
#um zu verhindern, dass der Regex mehrere HTML-Tag-Umgebungen auf einmal "auffrisst"), 
#gefolgt von der Zeichenkette 'finxter'. Dann kommt wieder eine beliebige Anzahl von Zeichen
#wieder definiert durch *.?  (also non-greedy), gefolgt von einem Vorkommen von entweder der 
#Zeichenfolge "test" oder der Zeichenfolge "puzzle". Auch das schliessen wir wieder durch 
#eine beliebige Anzahl von Zeichen (wieder non-greedy) ab, gefolgt von der abschließenden 
#Tag Markierung ">". 
#Auf diese Weise finden wir alle Hyperlink-Tags, die die entsprechenden Zeichenfolgen 
#enthalten. Beachte, dass dieser Regex auch Tags findet, in denen die Zeichenfolgen 'test' 
#oder 'puzzle' im Link selbst vorkommen. Beachte auch, dass wir nur non-greedy Sternchen-
#operatoren '.*?' verwenden, um sicherzustellen, dass wir immer nach minimalen Übereinstim-
#mungen suchen, anstatt nach einer einzigen sehr langen Zeichenkette, die aus mehreren 
#verschachtelten Tag-Umgebungen besteht.
#
#Das erfolgreiche Treffer-Resultat (s.o.) beweist, dass unser Regex funktioniert:
#Zwei Hyperlinks entsprechen unserem regulären Ausdruck: Das Ergebnis des Einzeilers
#ist eine Liste mit zwei Elementen. Allerdings ist jedes Element ein Tupel von Zeichenketten
#und nicht eine einfache Zeichenkette. Dies ist ein Unterschied zu den Ergebnissen von 
#findall(), die wir in früheren Codeschnipseln besprochen haben. Was ist der Grund für dieses 
#Verhalten? Der Rückgabetyp von findall ist eine Liste von Tupeln - mit einem Tupelwert für 
#jede übereinstimmende Gruppe, die in () eingeschlossen ist. 
#Der Regex (test|puzzle) verwendet zum Beispiel die Klammerschreibweise, um eine passende 
#Gruppe zu erstellen. Daher werden 'test' bzw. 'puzzle' in den Trefferlisten jeweils nochmal
#angezeigt. Um dieses Konzept zu verdeutlichen, tauchen wir gleich tiefer in das Thema der 
#passenden Gruppen (matching groups) ein.





#########################################################################################
#########################################################################################
# 5.4 Extracting Dollars from a String
#########################################################################################

#Glücklicherweise haben wir dieses Regex-Tutorial, so dass wir, anstatt eine Menge Zeit 
#zu verschwenden, unseren eigenen langwierigen, fehleranfälligen Python-Parser zu schreiben, 
#entscheiden wir uns für die saubere Lösung mit regulären Ausdrücken - eine weise Entscheidung. 
#Aber bevor wir in das nächste Problem eintauchen, wollen wir uns drei weitere Regex-Konzepte 
#ansehen.
#1.) Erstens müssen wir früher oder später auch ein Sonderzeichen finden, das auch von der 
#Regex-Sprache als Befehlszeichen verwendet wird. In diesem Fall müssen wir das Präfix \ 
#verwenden, um die Bedeutung des Befehls/Sonderzeichens zu umgehen (escaping). Ein Beispiel: 
#Um das Klammerzeichen '(', das normalerweise für Regex-Gruppen verwendet wird, zu matchen, 
#müssen wir es mit dem Regex '\(' ausklammern. Auf diese Weise verliert das Regex-Zeichen 
#'(' seine besondere Bedeutung als Regex-Kontrollzeichen.
#2.) Zweitens können wir mit der eckigen Klammerumgebung [ ] einen Bereich von spezifischen 
#Zeichen definieren, die abgeglichen werden sollen. Zum Beispiel passt der Regex [0-9]
#auf eines der folgenden Zeichen: '0', '1', '2', . . . , '9'. Ein weiteres Beispiel ist 
#der Regex [a-e], der auf eines der folgenden Zeichen passt: 'a', 'b', 'c', 'd', 'e'.
#3.) Drittens, wie im vorangegangenen Abschnitt 5-3 beschrieben, zeigen die Klammern
#(<Muster>) eine Gruppe an. Jeder Regex kann eine oder mehrere Gruppen haben. Wenn wir die 
#Funktion re.findall() auf einen Regex mit Gruppen anwenden, werden nur die übereinstimmenden 
#Gruppen als Tupel von Zeichenfolgen zurückgegeben - eine für jede Gruppe - und nicht die 
#gesamte übereinstimmende Zeichenkette. Zum Beispiel, der Regex hello(world), der auf die 
#Zeichenfolge "helloworld" angewendet wird, würde auf die gesamte Zeichenfolge passen, aber 
#nur die übereinstimmende Gruppe world zurückgeben. Andererseits, wenn man zwei verschachtelte 
#Gruppen im Regex (hello(world)) hat, wäre das Ergebnis der Funktion re.findall() ein Tupel 
#aller übereinstimmenden Gruppen, also ('helloworld', 'world').
#Sehen wir uns nun den folgenden Code an, um verschachtelte Gruppen vollständig zu verstehen:
import re
string = 'helloworld'
regex_1 = 'hello(world)'
regex_2 = '(hello(world))'
res_1 = re.findall(regex_1, string)
res_2 = re.findall(regex_2, string)
print(res_1)     # ['world']
print(res_2)     # [('helloworld', 'world')]
#Jetzt wissen wir alles, um den folgenden Einzeilerzu verstehen. Zur Erinnerung: wir möchten 
#alle monetären Zahlen aus einem bestimmten Unternehmensbericht untersuchen. Unser Ziel ist es
#insbesondere, das folgende Problem zu lösen: Finde in einer Zeichenkette eine Liste aller 
#Vorkommen von Dollarbeträgen mit optionalen Dezimalwerten. Die folgenden Beispielzeichen-
#ketten sind gültige Übereinstimmungen: $10, $10., oder $10.00021. Wie können wir dies 
#effizient in einer einzigen Codezeile erreichen?

## Dependencies
import re

## Data
report = '''
If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
'''

## One-Liner
dollars = [x[0] for x in re.findall('(\$[0-9]+(\.[0-9]*)?)', report)]

## Result
print(dollars)          #['$1', '$18087791.41', '$0.25', '$4521947.8525']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Der Bericht (report) enthält vier Dollarwerte in verschiedenen Formaten. Das Ziel ist es,
#einen Regex zu entwickeln, der zu allen Werten passt. Dazu entwerfen den Regex 
# (\$[0-9]+(.[0-9]*)?), der mit den folgenden Mustern übereinstimmt. Erstens passt er auf 
#das Dollar-Zeichen $ (wir müssen es escapen, weil es ein spezielles Regex-Kontroll-Zeichen 
#ist). Zweitens haben wir eine Zahl mit einer beliebigen Anzahl von Ziffern zwischen 0 und 9 
#(aber mindestens eine Ziffer). Drittens matchen wir auf eine beliebige Anzahl von Dezimal-
#werten nach dem Punktzeichen '.' (auch hier müssen wir wieder escapen). Diese letzte Regex-
#Gruppe ist allerdings optional, wie durch den Null-oder-Eins-Regex ? angegeben.
#Darüber hinaus verwenden wir eine list-comprehension, um nur den ersten Tupelwert aller 
#drei resultierenden Matches zu extrahieren (unser Gesamt-Regex besteht ja aus drei Gruppen). 
#Auch hier ist das Standardergebnis der re.findall() Funktion eine Liste von Tupeln, mit 
#einem Tupel für jede erfolgreiche Übereinstimmung und einen Tupelwert für jede Gruppe 
#innerhalb der Übereinstimmung:
re.findall('(\$[0-9]+(\.[0-9]*)?)', report)   #[('$1',            ''),
                                              # ('$18087791.41',  '.41'),
                                              # ('$0.25',         '.25'),
                                              # ('$4521947.8525', '.8525')]
#                                                ---------------
#                                                      \
#                                                  wir wollen aber nur diesen
#                                                  Teil haben
#Es sei nochmals darauf hingewiesen, dass die Implementierung eines einfachen Parsers 
#auch ohne die mächtigen Fähigkeiten der regulären Ausdrücke schwierig und fehleranfällig ist!
#Also: warum das Rad neu erfinden, wenn es doch die regulären ausdrücke gibt ?





#########################################################################################
#########################################################################################
# 5.5 Finding Nonsecure HTTP URLs
#########################################################################################

#Der nächste Einzeiler zeigt, wie wir eines dieser kleinen, zeitintensiven Probleme lösen,
#das Webentwickler oft haben. Nehmen wir an, wir besitzen einen Programmier-Blog und haben 
#gerade unsere Website von dem unsicheren Protokoll http auf das (sicherere) Protokoll https 
#umgestellt. Unsere alten Artikel verweisen jedoch immer noch auf die alten URLs. Wie können 
#wir alle Vorkommen der alten URLs finden?
#Im vorangegangenen Abschnitt 5-4 haben wir gelernt, wie man die Notation in eckigen Klammern 
#verwendet, um einen beliebigen Bereich von Zeichen anzugeben. Zum Beispiel passt der reguläre 
#Ausdruck [0-9] auf eine einstellige Zahl mit einem Wert von 0 bis 9. Allerdings ist diese 
#Notation in eckigen Klammern jedoch noch leistungsfähiger als das. Wir können nämlich eine
#beliebige Kombination von Zeichen innerhalb der eckigen Klammern verwenden, um genau 
#festzulegen, welche Zeichen übereinstimmen und welche nicht. Zum Beispiel passt der 
#reguläre Ausdruck [0-3a-c]+ auf die Zeichenfolgen "01110" und "01c22a", aber nicht auf die
#Zeichenfolgen '443' und '00cd'. Das + Zeichen besagt: ein- oder mehrmals.
#Wir können auch einen festen Satz von Zeichen angeben, die nicht ge-matched werden sollen, 
#indem wir das Symbol ^ verwenden: Der reguläre Ausdruck [^0-3a-c]+ passt auf die Zeichen-
#folgen '4444d' und 'Python', aber nicht auf die Zeichenfolgen '001' und '01c22a'.
#Hier ist nun unsere Eingabe, eine (mehrzeilige) Zeichenkette, und unser Ziel ist es, alle 
#Vorkommen von gültigen URLs zu finden, die mit dem Präfix "http://"" beginnen. Wir berück-
#sichtigen jedoch nicht ungültige URLs ohne Top-Level-Domain (es muss mindestens ein . in
#der gefundenen URL enthalten sein) ... 

## Dependencies
import re

## Data
article = '''
The algorithm has important practical applications
http://blog.finxter.com/applications/
in many basic data structures such as sets, trees,
dictionaries, bags, bag trees, bag dictionaries,
hash sets, https://blog.finxter.com/sets-in-python/
hash tables, maps, and arrays. http://blog.finxter.com/
http://not-a-valid-url
http:/bla.ba.com
http://bo.bo.bo.bo.bo.bo/
http://bo.bo.bo.bo.bo.bo/333483--33343-/
'''

## One-Liner
stale_links = re.findall('http://[a-z0-9_\-.]+\.[a-z0-9_\-/]+', article)

## Results
print(stale_links)       #['http://blog.finxter.com/applications/', 
                         # 'http://blog.finxter.com/',
                         # 'http://bo.bo.bo.bo.bo.bo/', 
                         # 'http://bo.bo.bo.bo.bo.bo/333483--33343-/']


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Im obigen regulären Ausdruck analysieren wir eine gegebene mehrzeilige Zeichenfolge, 
#article genannt (möglicherweise ein alter Blog-Artikel), um alle URLs zu finden, 
#die mit dem String-Präfix http:// beginnen. Der reguläre Ausdruck erwartet eine positive 
#Anzahl von (klein geschriebenen) Zeichen, Zahlen, Unterstriche, Bindestriche oder Punkte 
#([a-z0-9_\-\.]+). Beachte, dass wir den Bindestrich (\-) auslassen müssen, da er normaler-
#weise einen Bereich "von-bis" innerhalb der eckigen Klammern spezifiziert. Ebenso müssen 
#wir den Punkt (\.) escapen, weil wir tatsächlich den Punkt und nicht ein beliebiges 
#Zeichen (wofür der Punkt der Regex-Kontrollzeichen ist) matchen wollen. Dies ergibt
#dann das obige Resultat.
#Es zeigt, dass vier gültige URLs möglicherweise auf das sicherere HTTPS-Protokoll umgestellt 
#werden müssen.
#Jetzt beherrschen wir bereits die wichtigsten Funktionen von regulären Ausdrücken. 
#Aber es gibt eine Ebene des tiefen Verständnisses, die wir nur durch Üben und Studieren 
#vieler Beispiele erreichen - und reguläre Ausdrücke sind da keine Ausnahme. Schauen wir 
#uns ein paar weitere praktische Beispiele dafür an, wie reguläre Ausdrücke uns das Leben 
#einfacher machen können.





#########################################################################################
#########################################################################################
# 5.6 Validating the Time Format of User Input, Part 1
#########################################################################################

#Wir wollen lernen, die Korrektheit der Formatierung von Benutzereingaben zu überprüfen. 
#Angenommen, wir schreiben eine Webanwendung, die Gesundheitsstatistiken auf der Grundlage 
#der Schlafdauer Ihrer Benutzer berechnet. Die Benutzer geben die Zeit ein, zu der sie zu 
#Bett gegangen sind und die Zeit zu sie aufwachen. Ein Beispiel für ein korrektes Zeitformat 
#ist 12:45, aber da Webbots die Benutzereingabefelder regelmäßig spammen, verursacht das 
#eine Menge "schmutziger" Daten und unnötigen Verarbeitungsaufwand auf unseren Servern. 
#Um dieses Problem zu lösen, schreiben wir ein Zeitformatprüfprogramm, das feststellt, 
#ob die Eingabe mit derer Backend-Anwendung weiterverarbeitet werden kann. Mit regulären 
#Ausdrücken, dauert das Schreiben des Codes nur ein paar Minuten.

#In den vorangegangenen Abschnitten haben wir die Funktionen re.search(), re.match(), und 
#re.findall() kennengelernt. Dies sind jedoch nicht die einzigen Regex-Funktionen. In diesem
#Abschnitt werden wir re.fullmatch(regex, string) verwenden, die prüft, ob der regex mit der 
#gesamten Zeichenkette matched.
#Außerdem werden Sie die Regex-Syntax pattern{m,n} verwenden, die zwischen m und n Instanzen 
#des jeweiligen Regex-Musters (nicht mehr und nicht weniger) matched. Beachte, dass hierbei
#versucht wird, die maximale Anzahl des Vorkommen des Musters zu matchen. 
#Hier ist ein Beispiel:
import re
print(re.findall('x{3,5}y', 'xy'))                # []
print(re.findall('x{3,5}y', 'xxxy'))              # ['xxxy']
print(re.findall('x{3,5}y', 'xxxxxy'))            # ['xxxxxy']
print(re.findall('x{3,5}y', 'xxxxxxy'))           # ['xxxxxy']
#Bei Verwendung der Klammerschreibweise matched dieser Regex nicht auf Teilstrings mit
#weniger als drei und mehr als fünf 'x'-Zeichen.
#Unser Ziel ist es, eine Funktion input_ok zu schreiben, die ein String-Argument entgegennimmt 
#und prüft, ob es das (Zeit-)Format XX:XX hat, wobei X eine Zahl von 0 bis 9 ist. Beachte, 
#dass wir im Moment noch semantisch falsche Zeitformate wie 12:86 akzeptieren, aber der 
#nächste Einzeiler-Abschnitt 5-7 wird sich dann mit diesem fortgeschrittenen Problem befassen.

## Dependencies
import re

## Data
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

## One-Liner
input_ok = lambda x: re.fullmatch('[0-9]{2}:[0-9]{2}', x) != None

## Result
for x in inputs:
    print(input_ok(x))        #True
                              #True
                              #False
                              #False
                              #False
                              #True


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Die Daten bestehen aus sechs Eingabestrings, wie sie vom Frontend unserer Webanwendung 
#empfangen werden. Sind sie korrekt formatiert? Um dies zu überprüfen, erstellen wir die
#Funktion input_ok unter Verwendung eines Lambda-Ausdrucks mit einem Eingabeargument x und 
#einer booleschen Ausgabe. Wir verwenden die Funktion fullmatch(regex, x) und versuchen,
#das Eingabeargument x mit unserem Zeitformatierungsregex zu matchen. Wenn Sie nicht 
#übereinstimmen, nimmt das Ergebnis den Wert None an und die boolesche Ausgabe wird False. 
#Andernfalls ist die boolesche Ausgabe True.
#Der Regex ist einfach: [0-9]{2}:[0-9]{2}. Dieses Muster entspricht zwei führenden Zahlen 
#von 0 bis 9, gefolgt von einem Doppelpunkt, gefolgt von zwei nachgestellten Zahlen 
#von 0 bis 9.
#Die Funktion input_ok identifiziert korrekt die richtigen Formate der Zeiteingaben. 
#Mit diesem Einzeiler haben wir gelernt, wie sehr praktische Aufgaben, die sonst mehrere 
#Codezeilen und mehr Aufwand erfordern würden, mit dem richtigen Toolset in wenigen Sekunden 
#erfolgreich erledigt werden können.





#########################################################################################
#########################################################################################
# 5.7 Validating Time Format of User Input, Part 2
#########################################################################################

#In diesem Abschnitt werden wir tiefer in die Validierung des Zeitformats von Eingaben 
#eintauchen, um das Problem des vorherigen Abschnitts zu lösen: Ungültige Zeitangaben wie
#99:99 sollten nicht als gültige Übereinstimmungen betrachtet werden.
#Eine nützliche Strategie zur Lösung von Problemen besteht darin, sie hierarchisch anzugehen. 
#Zuerst reduzieren wir das Problem auf seinen Kern und lösen die einfachere Variante. 
#Dann verfeinern wir die Lösung auf Ihr spezifisches (und komplizierteres) Problem. 
#Dieser Abschnitt verfeinert die vorherige Lösung in einem wichtigen Punkt: Er erlaubt keine
#ungültige Zeitangaben wie 99:99 oder 28:66. Das Problem ist also spezifischer (und 
#komplizierter), aber wir können Teile unserer alten Lösung wiederverwenden.
#Unser Ziel ist es, eine Funktion input_ok zu schreiben, die ein String-Argument entgegennimmt 
#und prüft, ob sie das (Zeit-)Format XX:XX hat, wobei X eine Zahl zwischen 0 und 9 ist. 
#Außerdem muss die angegebene Zeit ein gültiges Zeitformat im 24-Stunden-Zeitbereich von 
#00:00 bis 23:59 sein...

## Dependencies
import re

## Data
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

## One-Liner
input_ok = lambda x: re.fullmatch('([01][0-9]|2[0-3]):[0-5][0-9]', x) != None

## Result
for x in inputs:
    print(input_ok(x))         #True
                               #True
                               #False
                               #False
                               #False
                               #False


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wie in der Einleitung dieses Abschnitts erwähnt, können wir die Lösung des des vorigen 
#Einzeilers wiederverwenden, um dieses Problem einfach zu lösen. Der Code bleibt derselbe -
#wir haben nur den regulären Ausdruck ([01][0-9]|2[0-3]):[0-5][0-9] geändert. Der erste 
#Teil ([01][0-9]|2[0-3]) ist eine Gruppe, die auf alle möglichen Stunden des Tages passt. 
#Mit dem oder-Operator | unterscheiden wir die Stunden 00 bis 19 einerseits, und die 
#Stunden 20 bis 23 andererseits. Der zweite Teil [0-5][0-9] entspricht den Minuten des Tages 
#von 00 bis 59. Das Ergebnis lautet daher wie oben gezeigt.
#Beachte, dass die sechste Zeile der Ausgabe anzeigt, dass die Zeit 99:99 nicht mehr als 
#gültige Benutzereingabe betrachtet wird. Dieser Einzeiler zeigt, wie man reguläre Ausdrücke 
#verwendet, um zu prüfen, ob die Benutzereingabe den semantischen Anforderungen der jeweiligen 
#Anwendung entspricht.





#########################################################################################
#########################################################################################
# 5.8 Duplicate Detection in Strings
#########################################################################################

#Mit diesem Einzeiler wird eine wichtige Fähigkeit der regulären Ausdrücke eingeführt:
#Die Wiederverwendung von Teilen, die wir bereits gefunden haben, und zwar mit demselben 
#Regex. 
#Dieses leistungsstarke Feature ermöglicht es, eine Reihe neuer Probleme zu lösen, 
#einschließlich der Erkennung von Zeichenketten mit doppelten Zeichen.
#Diesmal arbeiten wir als ComputerlinguistikerInnen und analysieren, wie sich bestimmte 
#Wortverwendungen im Laufe der Zeit verändern. Wir verwenden veröffentlichte Bücher, um
#den Wortgebrauch zu klassifizieren und zu verfolgen. Wir wollen analysieren, ob es einen 
#Trend zur häufigeren Verwendung von doppelten Zeichen in Wörtern gibt. Zum Beispiel 
#enthält das Wort "Hallo" das doppelte Zeichen "l", während das Wort "Beet" das doppelte 
# Zeichen "e" enthält. Allerdings würde das Wort "mama" jedoch nicht als Wort mit dem 
#doppelten Buchstaben "a" gezählt.
#Die naive Lösung für dieses Problem ist, alle möglichen doppelten Zeichen 'aa', 'bb', 'cc', 
#'dd', . . . zz" aufzulisten und sie in einer entweder-oder-Regex zu kombinieren. Diese 
#Lösung ist mühsam und nicht leicht zu verallgemeinern. Was passiert, wenn man statt nach 
#sich wiederholenden Zeichen nun nach Zeichen-Wiederholungen mit bis zu einem Zeichen 
#dazwischen fahndet (z. B. die Zeichenfolge "mama wäre jetzt eine Übereinstimmung)?
#Kein Problem: Es gibt eine einfache, saubere und effektive Lösung, wenn man die die 
#Regex-Funktion von benannten Gruppen kennt. Wir haben bereits über Gruppen gelernt, dass
#sie in Klammern (...) eingeschlossen sind. Wie der Name schon sagt, ist eine benannte Gruppe
#                                                                             ---------------
#einfach eine Gruppe mit einem Namen. Wir können zum Beispiel um das Muster ... eine Gruppe
#mit dem Namen name definieren, indem wir die Syntax (?P<name>...) verwenden.
#Nachdem man eine derartige benannte Gruppe definiert hat, kann man sie überall 
#in einem regulären Ausdruck mit der Syntax (?P=name) verwenden. Betrachten wir dazu das 
#folgende Beispiel:
import re
pattern = '(?P<quote>[\'"]).*(?P=quote)'
text = 'She said "hi"'
print(re.search(pattern, text))       # <re.Match object; span=(9, 13), match='"hi"'>
#Im Code suchen wir nach Teilzeichenketten, die entweder in einfachen oder doppelten 
#Anführungszeichen eingeschlossen sind. Um dies zu erreichen, wird zunächst das öffnende 
#Anführungszeichen mit dem Regex ['"] ge-matched (das einfache Anführungszeichen \' wird 
#escaped, damit Python nicht fälschlicherweise annimmt, dass das einfache Anführungszeichen 
#das Ende der Zeichenkette anzeigt). Dann verwenden wir dieselbe Gruppe, um das schließende 
#Anführungszeichen mit demselben Zeichen (entweder ein einfaches oder ein doppeltes 
#Anführungszeichen) zu matchen.
#Bevor wir in den Einzeiler-Code eintauchen, sollten wir beachten, dass wir beliebige Anzahlen 
#von Leerzeichen mit dem Regex \s matchen können. Außerdem können wir Zeichen abgleichen, 
#die nicht in der Menge Y enthalten sind, indem wir die Syntax [^Y] verwenden. Das ist alles, 
#was Sie wissen müssen, um unser Problem zu lösen.
#Wir wollen nun in einem Text alle Wörter finden, die doppelte Zeichen enthalten. Ein Wort 
#ist in diesem Fall definiert als jede Reihe von Zeichen ohne Leerzeichen, die durch eine 
#beliebige Anzahl von Leerzeichen getrennt sind.

## Dependencies
import re

## Data
text = '''
It was a bright cold day in April, and the clocks were
striking thirteen. Winston Smith, his chin nuzzled into
his breast in an effort to escape the vile wind, slipped
quickly through the glass doors of Victory Mansions,
though not quickly enough to prevent a swirl of gritty
dust from entering along with him.
-- George Orwell, 1984
'''

## One-Liner
duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)

## Results
print(duplicates)     #[('thirteen.', 'e'), ('nuzzled', 'z'), ('effort', 'f'),
                      # ('slipped', 'p'), ('glass', 's'), ('doors', 'o'),
                      # ('gritty', 't'), ('--', '-'), ('Orwell,', 'l')]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Der Regex (?P<x>[^\s]) definiert eine neue Gruppe mit dem Namen x. Diese Gruppe besteht nur 
#aus einem einzigen beliebigen Zeichen, das nicht das Leerzeichen ist. Der Regex (?P=x) folgt 
#unmittelbar auf die benannte Gruppe x. Dieser findet einfach das gleiche Zeichen wie die 
#Gruppe x. D.h. hierdurch wird nach dem in der benannten Gruppe x gefundenen Zeichen nochmal
#gesucht. Falls das klappt, haben wir die doppelte Zeichen gefunden! Das Ziel ist es jedoch 
#nicht, doppelte Zeichen zu finden, sondern die Wörter mit diesem doppelten Zeichen. Also 
#matchen wir noch eine beliebige Anzahl von Nicht-Leerzeichen [^\s]* vor x und nach diesen 
#doppelten Zeichen. Das zeigt auch das Resultat des obigen Einzeilers.
#Der Regex findet alle Wörter mit doppelten Zeichen im Text. Beachte, dass der obige Regex aus 
#zwei Gruppen besteht, so dass jedes Element das von der Funktion re.findall() zurückgegeben 
#wird, aus einem Tupel von übereinstimmenden Gruppen besteht. Wir haben dieses Verhalten 
#bereits in früheren Abschnitten gesehen.
#In diesem Abschnitt haben Sie unseren Regex-Werkzeugsatz um ein leistungsfähiges Werkzeug 
#erweitert: benannte Gruppen. In Kombination mit zwei kleineren Regex-Funktionen dem 
#Abgleich beliebiger Leerzeichen mit \s und der Definition einer Gruppe von Zeichen mit dem 
#Operator [^...], die nicht abgeglichen werden, haben wir ernsthafte wichtige Erweiterungen
#unserer Python-Regex-Kenntnisse gemacht.





#########################################################################################
#########################################################################################
# 5.9 Detecting Word Repetitions
#########################################################################################

#Im vorangegangenen Abschnitt 5-8 haben wir etwas über benannte Gruppen gelernt. Das Ziel 
#dieses Abschnittes ist es nun, fortgeschrittene Möglichkeiten zur Verwendung dieser 
#leistungsstarken Funktion zu zeigen.
#Wäre es nicht nützlich, ein Werkzeug zu haben, das überprüft, ob man immer wieder dieselbe 
#Worte in einem längeren Text verwendet ?
#Wir erhalten eine Zeichenkette, die aus klein geschriebenen, durch Leerzeichen getrennten 
#Wörtern besteht, ohne Sonderzeichen. Wir suchen nun eine passende Teilzeichenkette, bei 
#der das erste und das letzte Wort gleich sind (Wiederholung) und dazwischen höchstens 
#10 Wörter liegen...

## Dependencies
import re

## Data
text = 'if you use words too often words become used'

## One-Liner
style_problems = re.search('\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s', ' ' + text + ' ')

## Results
print(style_problems)     #<re.Match object; span=(11, 34), match=' words too often words '>


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Auch hier gehen wir davon aus, dass ein bestimmter Text nur aus durch Leerzeichen getrennten 
#klein geschriebenen Wörtern besteht. Nun suchen wir den Text mit Hilfe eines regulären 
#Ausdrucks. Das sieht vielleicht auf den ersten Blick kompliziert aus, aber wir wollen das nun
#Stück für Stück aufschlüsseln:
#           '\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s'
#Sie beginnen mit einem einzelnen Leerzeichen. Dies ist wichtig, um sicherzustellen, dass wir 
#mit einem ganzen Wort beginnen (und nicht mit einem Suffix eines Wortes). Dann matchen
#wir eine benannte Gruppe x, die aus einer positiven Anzahl von Kleinbuchstaben
#von 'a' bis 'z' besteht, gefolgt von einer positiven Anzahl von Leerzeichen.
#Wir fahren dann mit 0 bis 10 Wörtern fort, wobei jedes Wort aus einer positiven Anzahl von 
#Kleinbuchstaben von "a" bis "z" gefolgt von einer positiven Anzahl von Leerzeichen besteht.
#Wir enden schliesslich mit der benannten Gruppe x gefolgt von einem Leerzeichen, um
#sicherzustellen, dass die letzte Übereinstimmung ein ganzes Wort ist (und nicht nur ein 
#Präfix eines Wortes).
#Das Resultat (s.o.) ist dann: ' words too often words '.
#Damit haben wir eine übereinstimmende Teilzeichenkette gefunden, die möglicherweise (oder 
#auch nicht) auf schlechten Schreib-Stil hinweist.
#Mit diesem Einzeiler haben wir das Problem der Suche nach doppelten Wörtern auf seinen 
#Kern reduziert und diese einfachere Variante gelöst. Beachte, dass wir in der Praxis
#kompliziertere Fälle wie Sonderzeichen, eine Mischung aus Klein- und Großbuchstaben, 
#Zahlen und so weiter antreffen. Alternativ dazu, könnte an den Text auch vorverarbeiten, 
#um ihn in die gewünschte Form zu bringen: Kleinbuchstaben, durch Leerzeichen getrennte 
#Wörter, ohne Sonderzeichen.





#########################################################################################
#########################################################################################
# 5.10 Modifying Regex Patterns in a Multiline String
#########################################################################################

#Im letzten Regex-Einzeiler lernen wir, wie man einen Text ändern kann, anstatt nur nach
#Teilen des Textes zu suchen (zu matchen). Um alle Vorkommen eines bestimmten Regex-Musters 
#durch eine neue Zeichenkette in einem bestimmten Text zu ersetzen, verwenden wir die 
#Regex-Funktion re.sub(regex, replacement, text). Auf diese Weise können wir große Text-
#bestände schnell und ohne viel manuelle Arbeit editieren.
#In den vorangegangenen Abschnitten haben wir gelernt, wie man Muster matched, die in
#einem Text vorkommen. Was aber, wenn wir ein bestimmtes Muster nicht matchen wollen, 
#wenn ein anderes Muster vorkommt? Das negative Lookahead-Regex-Muster A(?!X) matched 
#                                      -------------------------------
#mit einem Regex A , wenn der Regex X danach nicht mehr übereinstimmt. Zum Beispiel würde 
#der Regex "not (?!good)" auf die Zeichenfolge "this is not great" passen, aber nicht auf 
#die Zeichenfolge "this is not good".
#Im folgenden sind unsere Daten eine Zeichenkette und unsere Aufgabe ist es, alle Vorkommen 
#von Alice Wonderland durch 'Alice Doe' zu ersetzen, aber nicht die Vorkommen von 
#'Alice Wonderland' (eingeschlossen in einfache Anführungszeichen) zu ersetzen.

## Dependencies
import re

## Data
text = '''
Alice Wonderland married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.
'''

## One-Liner
updated_text = re.sub("Alice Wonderland(?!')", 'Alice Doe', text)

## Result
print(updated_text)     #Alice Doe married John Doe.
                        #The new name of former 'Alice Wonderland' is Alice Doe.
                        #Alice Doe replaces her old name 'Wonderland' with her new name 'Doe'.
                        #Alice's sister Jane Wonderland still keeps her old name.


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wir ersetzen alle Vorkommen von Alice Wonderland durch Alice Doe, aber nicht die Varianten
#von 'Alice Wonderland', die in einfache Anführungszeichen ' eingeschlossen sind. Dazu 
#verwenden wir einen negativen Look-Ahead. Beachte, dass wir nur prüfen, ob das schließende 
#Anführungszeichen vorhanden ist. Eine Zeichenkette mit einem öffnenden Anführungszeichen, 
#aber ohne schließendes Anführungszeichen würde übereinstimmen, und würden sie einfach 
#ersetzen. Dies mag im Allgemeinen nicht erwünscht sein, aber es führt zu dem gewünschten 
#Verhalten in unserem Beispielstring.
#Wir können sehen, dass der ursprüngliche Name "Alice Wonderland" unverändert bleibt, wenn er 
#in einfache Anführungszeichen gesetzt wird - was ja das Ziel dieses Codeausschnitts war.





#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                    6 - Algorithms
#                                    =====================================





#########################################################################################
#########################################################################################
# 6.1 Finding Anagrams with Lambda Functions and Sorting
#########################################################################################

#Zwei Wörter sind Anagramme, wenn sie aus denselben Zeichen bestehen und wenn jedes
#Zeichen des ersten Wortes genau einmal im zweiten Wort vorkommt. Dies wird in den folgenden 
#Beispielen dargestellt:
#     • “listen” → “silent”
#     • “funeral ” → “real fun”
#     • “elvis” → “lives”

## One-Liner
is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

## Results
print(is_anagram("elvis", "lives"))          #True
print(is_anagram("elvise", "livees"))        #True
print(is_anagram("elvis", "dead"))           #False


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Die Lösung ist so simpel - da gibts nix zu erklären.





#########################################################################################
#########################################################################################
# 6.2 Finding Palindromes with Lambda Functions and Negative Slicing
#########################################################################################

#Das Wichtigste zuerst: Was ist ein Palindrom? Ein Palindrom kann definiert werden als eine
#Folge von Elementen (z.B. eine Zeichenkette oder eine Liste), die sich rückwärts genauso
#wie vorwärts liest. Hier sind ein paar lustige Beispiele, die Palindrome sind, wenn man 
#die Leerzeichen weglässt:
#          • “Mr Owl ate my metal worm”
#          • “Was it a car or a cat I saw?”
#          • “Go hang a salami, I’m a lasagna hog”
#          • “Rats live on no evil star”
#          • “Hannah”
#          • “Anna”
#          • “Bob”

## One-Liner
is_palindrome = lambda phrase: phrase == phrase[::-1]

## Result
print(is_palindrome("anna"))                        #True
print(is_palindrome("kdljfasjf"))                   #False
print(is_palindrome("rats live on no evil star"))   #True


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Auch diese Lösung ist trivial - da gibts auch nix zu erklären.





#########################################################################################
#########################################################################################
# 6.3 Counting Permutations with Recursive Factorial Functions
#########################################################################################

#Die Fakultätsfunktion (!) ist so definiert:
#    n! = n * (n-1) * (n-2) * ... * 1
#bzw. in rekursiver Formulierung so:
#    0! = 1
#    1! = 1
#    n! = n * (n-1)!

## The Data
d = 5

## The One-Liner
factorial = lambda n: n * factorial(n-1) if n > 1 else 1

## The Result
print(factorial(d))          #120


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Der obige Einzeiler ist ein quasi direkte Implementierung der rekursiven
#Definition der Fakultätsfunktion.





#########################################################################################
#########################################################################################
# 6.4 Finding the Levenshtein Distance
#########################################################################################

#In diesem Abschnitt lernen wir einen wichtigen praktischen Algorithmus zur Berechnung der 
#Levenshtein-Distanz kennen, siehe https://de.wikipedia.org/wiki/Levenshtein-Distanz
#                                  https://en.wikipedia.org/wiki/Levenshtein_distance                         
#Das Verstehen dieses Algorithmus ist komplizierter als frühere Algorithmen, daher werden 
#wir dabei auch trainieren, ein Problem klar zu durchdenken.
#
#Die Levenshtein-Distanz ist eine Metrik zur Berechnung des Abstands zwischen zwei Strings; 
#mit anderen Worten, sie wird verwendet, um die Ähnlichkeit zweier Strings zu quantifizieren. 
#Ihr alternativer Name, die Editierdistanz, beschreibt genau, was sie misst: die Anzahl der 
#Zeichenänderungen (Einfügungen, Entfernungen oder Ersetzungen), die erforderlich sind,
#um eine Zeichenkette in eine andere umzuwandeln. Je kleiner die Levenshtein-Distanz ist, 
#desto ähnlicher sind die Zeichenfolgen.
#Die Levenshtein-Distanz hat wichtige Anwendungen in Bereichen wie z.B. die Autokorrekturfunktion 
#auf einem Smartphone. Wenn man "halo" im WhatsApp-Messenger eingibt, erkennt das Smartphone ein 
#Wort außerhalb seiner Bibliothek und wählt mehrere Wörter mit hoher Wahrscheinlichkeit als 
#potenzielle Ersetzungen aus, und sortiert sie dann nach dem Levenshtein-Abstand. Zum Beispiel 
#wird das Wort mit minimaler Levenshtein-Distanz und damit maximaler Ähnlichkeit beispielsweise 
#die Zeichenfolge "Hallo" sein, so dass das Telefon "halo" automatisch in "Hallo" umwandeln kann.
#
#Betrachten wir ein Beispiel mit den beiden weniger ähnlichen Zeichenfolgen "cat" und 'chello'. 
#Die Levenshtein-Distanz berechnet die minimale Anzahl von Bearbeitungen, die erforderlich sind, 
#um die zweite Zeichenfolge ausgehend von der ersten zu erreichen.
#Die folgende Tabelle zeigt die minimale Editier-Reihenfolge:

#        Current word                     Edit made
#        ------------                     ---------
#           cat                              —
#           cht                              Replace a with h
#           che                              Replace t with e
#           chel                             Insert l at position 3
#           chell                            Insert l at position 4
#           chello                           Insert o at position 5

#Es verwandelt die Zeichenkette "cat" in fünf Bearbeitungsschritten 
#in die Zeichenkette "chello", d.h. der Levenshtein-Abstand beträgt 5
#Nun wollen wir einen Python-Einzeiler schreiben, der den Levenshtein-Abstand - ls - jeweils 
#zwischen den untenstehenden Zeichenketten a und b, a und c sowie b und c berechnet... 

## The Data
a = "cat"
b = "chello"
c = "chess"

## The One-Liner
ls = lambda a, b: len(b) if not a else len(a) if not b else min(
    ls(a[1:], b[1:])+(a[0] != b[0]),
    ls(a[1:], b)+1,
    ls(a, b[1:])+1)

## The Result
print(ls(a,b))         #5
print(ls(a,c))         #4
print(ls(b,c))         #3


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Bevor wir in den Code eintauchen, wollen wir uns kurz mit einem wichtigen Python-Trick
#befassen, der in diesem Einzeiler intensiv genutzt wird. In Python hat jedes Objekt einen 
#Wahrheitswert und ist entweder True oder False. Dieses Konzept nennt man auch 
#"Truthy and Falsey". 
#Die meisten Objekte sind in der Tat True und intuitiv können wir wahrscheinlich die 
#wenigen Objekte erraten, die False sind:
#
#      - Der numerische Wert 0 ist Falsch.
#      - Die leere Zeichenkette '' ist Falsch.
#      - Die leere Liste [] ist Falsch.
#      - Die leere Menge set() ist Falsch.
#      - Das leere Dictionary {} ist False.
#
#Wir können das ja auch direkt ausprobieren:
bool(0)         #False
bool('')        #False
bool([])        #False
bool(set())     #False   
bool({})        #False
bool(len([]))   #False  - die Länge einer leeren Liste ist 0 
                #         und der Wahrheitswert von 0 ist False
#
#Als Faustregel gilt, dass Python-Objekte als False gelten, wenn sie leer oder Null sind. 
#Mit diesen Informationen ausgestattet, betrachten wir den ersten Teil der Levenshtein-
#Funktion: das ist dieser Teil
#                            lambda a, b: len(b) if not a else len(a) if not b 
#
#wir erstellen hier eine Lambda-Funktion, die zwei Strings a und b annimmt und die 
#Anzahl der Bearbeitungen zurückgibt, die erforderlich sind, um den String a in den String b
#umzuwandeln. Es gibt dabei zwei triviale Fälle: Wenn die Zeichenkette a leer ist, ist die 
#minimale Editierdistanz len(b), da man nur jedes Zeichen der Zeichenkette b einfügen müsste.
#Wenn die Zeichenkette b leer ist, ist die minimale Editierdistanz len(a). Das bedeutet,
#wenn eine der beiden Zeichenketten leer ist, können wir direkt die richtige Editier-
#distanz zurückgeben.
#
#Jetzt kommt der zweite Teil der Levenshtein-Funktion, der nicht-triviale Fall: das ist 
#dieser Teil 
#                            else min(
#                                     ls(a[1:], b[1:])+(a[0] != b[0]),
#                                     ls(a[1:], b)+1,
#                                     ls(a, b[1:])+1)
# 
#Hier nehmen wir nun an, dass beide Zeichenketten a un b nicht leer sind. 
#Wir können das Problem des nicht-trivialen Falls vereinfachen, indem wir die Levenshtein-
#Distanz kleinerer Suffixe der ursprünglichen Zeichenfolgen a und b betrachten.
#Dazu muss man zunächst die drei folgenden einfacheren Fälle betrachten. Diese sind
#formal so definiert: 
#  1.) trenne die ersten Zeichen in a und b und berechne dann den Abstand zwischen 
#      a[1:] und b[1:], das ist ls(a[1:], b[1:]). Wenn die ersten beiden Zeichen ungleich
#      sind, müssen wir editieren; wenn sie gleich sind, müssen wir nichts machen. Diese
#      beiden Fälle kann man so zusammenfassen: (a[0] != b[0]). Diesen Term müssen wir
#      zur Distanz der beiden Suffixe noch hinzuaddieren, um die Gesamtdistanz zwischen
#      a und b zu erhalten, also: ls(a[1:], b[1:]) + (a[0] != b[0])
# 
#  2.) trenne das erste Zeichen in a und betrachte das vollständige b. Berechne nun den
#      Abstand zwischen a[1:] und b, das ist ls(a[1:], b). Um den vollständigen Levenshtein-
#      Abstand zu erhalten, müssen wir aber noch das von a zuvor abgetrennte erste Zeichen 
#      behandeln. Das kostet uns in jedem Fall einen Arbeitsschritt, also ist die Gesamt-
#      distanz: ls(a[1:], b) + 1
# 
#  3.) trenne das erste Zeichen in b und betrachte das vollständige a. Berechne nun den
#      Abstand zwischen a und b[1:], das ist ls(a, b[1:]). Um den vollständigen Levenshtein-
#      Abstand zu erhalten, müssen wir aber noch das von b zuvor abgetrennte erste Zeichen 
#      behandeln. Das kostet uns in jedem Fall einen Arbeitsschritt, also ist die Gesamt-
#      distanz: ls(a, b[1:]) + 1
#
#Nun wählen wir denjenigen der drei Fälle aus, der am kleinsten ist, indem wir die min-
#Funktion verwenden. 
#Die vollständige Formulierung der Levenshtein-Funktion erhalten wir, wenn wir den 
#trivialen und den nicht-trivialen Fall kombinieren:

#                         trivialer Fall                              nicht-trivialer Fall 
#                                                                     (mit den drei weiteren 
#                                                                     Fallunterscheidungen)
#                 _________________________________________  ________________________________________
ls = lambda a, b: len(b) if not a else len(a) if not b else  min(
                                                                ls(a[1:], b[1:])+(a[0] != b[0]),  #1.)
                                                                ls(a[1:], b)+1,                   #2.)
                                                                ls(a, b[1:])+1)                   #3.)
#Da ls offensichtlich eine rekursive Funktion ist, wird sie
#sich solange durch die Teil-Zeichenketten a und b arbeiten, bis der triviale Fall erreicht 
#ist und dann in der Rücksprungphase die Teilergebnisse der rekursiven Aufrufe akkumulieren.
#
#Zum besseren Verstännis seien die Überlegungen zu den drei nicht-trivialen Fälle nochmal
#anhand des konreten Beispiels erläutert, dies wird durch die folgenden Abbildung unterstützt.
#Hier wird die Berechnung der Levenshtein-Distanz zwischen den konkreten Strings 'cat' und 
#'chello' dargestellt (detaillierte Erläuterungen dazu siehe nachfolgenden Text!!)...

#       Solve this problem...──────────────────►                        ls(cat, chello)
#       ---------------------                        ┌────────────────────────────────────────────────┐
#       ---------------------                        │                                                │
#                                                    │                   min(...) = 5                 │
#                                                    │                                                │
#                                                    └────────────────────────────────────────────────┘
#                                                    ▲                         ▲                      ▲
#                                                    │                         │                      │
#                                   _______\       5 + 0                     6 + 1                  5 + 1
#            ls(t, ello)  ______ ...       /     ls(at, hello)           ls(at, chello)           ls(cat, hello)
#                 ▲
#                 │                                        1.)                      2.)                      3.)
#  ┌──────────────┴───────────────┐                         ▲                        ▲                        ▲
#  │                              │                         │                        │                        │
#  │        min(...) = 4          │                         │                        │                        │
#  │                              │                         └────────────────────────┼────────────────────────┘
#  └──────────────────────────────┘                                                  │
#  ▲              ▲               ▲                                                  │
#  │ 3 + 1        │ 4 + 1         │  3 + 1                                           │
#ls(  , llo)    ls(  , ello)     ls(t, llo)                                          │
#Trivial case                            ▲                                          ...by solving these
#                                        │                                             three easier problems!
#                        ┌───────────────┴───────────────┐                          -------------------------
#                        │                               │                          -------------------------
#                        │         min(...) = 3          │
#                        │                               │
#                        └───────────────────────────────┘
#                        ▲               ▲               ▲
#                        │               │               │
#                      2 + 1           3 + 1           2 + 1
#                    ls(  , lo)      ls(  , llo)     ls(t, lo)

#1.) Wir berechnen den Abstand zwischen den Suffixen at und hello, denn wenn wir wissen, 
#wie man at in hello umwandelt, können wir leicht cat in chello umwandeln, indem man das 
#erste Zeichen ändert (oder das erste Zeichen beibehält, wenn beide Zeichenketten mit 
#demselben Zeichen beginnen). Unter der Annahme, dass der Abstand zwischen at und hello 
#5 beträgt (das wird allerdings erst in den tieferen Rekursionsebenen bewiesen), kann man 
#nun schließen, dass der Abstand zwischen cat und chello ebenfalls höchstens 5 ist, 
#weil man genau die Abfolge von Änderungen zwischen at und hello wiederverwenden kann 
#(beide Wörter, cat und chello beginnen mit dem Zeichen c und daher muss man dieses 
#Zeichen nicht bearbeiten).
#2.) Wir berechnen den Abstand zwischen at und chello. Unter der Annahme, dass dieser 
#Abstand 6 ist, können wir nun schließen, dass der Abstand zwischen cat und chello 
#höchstens 6 + 1 = 7 beträgt, weil man einfach das Zeichen c am Anfang des ersten Wortes 
#entfernen kann (eine zusätzliche Operation). Davon ausgehend kann man genau die gleiche 
#Lösung verwenden, um von at nach chello zu kommen. 
#3.) Wir berechnen den Abstand zwischen cat und hello. Unter der Annahme, dass dieser 
#Abstand 5 beträgt, können wir nun schließen, dass der Abstand zwischen cat und chello 
#höchstens 5 + 1 beträgt, weil das Zeichen c am Anfang des zweiten Wortes eingefügt 
#werden muss (eine zusätzliche Operation).
#
#Da dies alle möglichen Fälle sind, die man mit dem ersten Zeichen machen kann (Ersetzen, 
#Entfernen, Einfügen), ist der Levenshtein-Abstand zwischen cat und chello das 
#Minimum der drei obigen Fälle 1, 2 und 3. 
#
#Wir wollen Lassen die drei nicht-trivialen Fälle näher untersuchen.
#Zunächst berechnen wir den Editierabstand von a[1:] nach b[1:] in rekursiver Weise. 
#Wenn die führenden Zeichen a[0] und b[0] unterschiedlich sind, müssen wir dies beheben, 
#indem wir a[0] durch b[0] ersetzen, d.h. wir erhöhen den Editierabstand um eins. 
#Wenn die führenden Zeichen gleich sind, ist die Lösung des einfacheren Problems 
#ls(a[1:], b[1:]) auch eine Lösung für das komplexere Problem ls(a, b), wie man auch in der
#obigen Abbildung sieht.
#Zweitens berechnen wir den Abstand von a[1:] nach b in einer rekursiven Weise. Angenommen, 
#wir kennen das Ergebnis dieses Abstands (von a[1:] nach b)- wie kann man dann den Abstand 
#von a nach b einen Schritt weiter berechnen? Die Antwort ist, einfach das erste Zeichen a[0] 
#vom Anfang von a zu entfernen, was ine zusätzliche Operation bedeutet. Damit haben Sie das 
#kompliziertere Problem auf ein einfacheres reduziert.
#Drittens berechnen wir den Abstand von a zu b[1:] auf rekursive Weise x. Angenommen, wir 
#kennen das Ergebnis dieser Distanz (von a nach b[1:]). Wie können wir den Abstand von a 
#nach b berechnen? In diesem Fall können wir einfach einen Schritt weitergehen (von a nach 
#b[1:] nach b), indem wir das Zeichen b[0] an den am Anfang des Wortes b[1:] einfügen, 
#wodurch sich der Abstand um eins erhöht.
#
#Schließlich nehmen wir einfach den minimalen Editierabstand aller drei Fälle (wie oben 
#bereits erläutert).
#
#Wie kann man die Arbeit der Rekursion schrittweise beobachten?
#Wenn wir ls in folgenderweise modifizieren, die Arbeitsschritte während der Rekursion im
#Prinzip nachvollziehen:
ls = lambda a, b: (len(b),print(len(b)))[0] if not a else (len(a),print(len(a)))[0] if not b else  (min(
                                                                                                         ls(a[1:], b[1:])+(a[0] != b[0]),  
                                                                                                         ls(a[1:], b)+1,                   
                                                                                                         ls(a, b[1:])+1), print(min(
                                                                                                                                     ls(a[1:], b[1:])+(a[0] != b[0]),  
                                                                                                                                     ls(a[1:], b)+1,                   
                                                                                                                                     ls(a, b[1:])+1)))[0]                   
#ACHTUNG: die obigen Code-Zeilen sind sehr lang !!!
a = "cat"
b = "chello"
c = "chess"
print(ls(a,b))        
print(ls(a,c))         
print(ls(b,c))         
#
#Diese Einzeiler-Lösung zeigt einmal mehr, wie wichtig es ist, unsere Rekursionsfähigkeiten 
#zu trainieren. Rekursionsdenken ist für vielleicht nicht jedermans/fraus Sache, aber dennoch
#sehr wichtig. 

#Noch etwas Theorie und Kontextwissen und eine alternative Formulierung/Implementierung
#--------------------------------------------------------------------------------------
#Hier ist eine schöne Visualisierung der Levenshtein-Distanz von Pit Noack:
#https://www.maschinennah.de/ki-buch/
#           https://editor.p5js.org/MaschinenNah/full/QfyEWeNQa    (cat und chello eingeben)
#Die Levenshtein-Distanz, ls, mißt die Ähnlichkeit zweier Wörter bzgl. ihrer "Editierdistanz".
#Die Editierdistanz ist die minimal notwendige Anzahl von Editier-Operationen (Löschen, 
#Hinzufügen, Ersetzen), um eine Zeichekette in eine andere zu verwandeln.
#der Levenshtein-Algorithmus ist ein prominentes Beispiel für die Anwendung des Prinzips 
#der "Dynamischen Programmierung (DP)", siehe 
#           https://de.wikipedia.org/wiki/Dynamische_Programmierung
#           https://en.wikipedia.org/wiki/Dynamic_programming
#Bei DP geht es immer um die Suche nach der optimalen Lösung für ein gegebenes Problem.
#Dazu wird diese Lösung aus kleineren Teillösungen schrittweise entwickelt. Dieser Prozess
#wird rekursiv fortgesetzt bis man beim allereinfachsten Problem anlangt. Dann werden die
#Lösungen der Teilprobleme rückwärts aufgesammelt und zusammengesetzt bis man die Lösung
#des ursprünglichen Gesamtproblems hat.
#Der Levenshtein-Algorithmus gehört zu einer ganzen Klasse von Algorithmen, den sog.
#"String-Metriken", siehe https://en.wikipedia.org/wiki/String_metric 
#Diese vergleichen zwei Strings und liefern einen Wert für deren Entfernung. Alternative
#Verfahren erlauben etwa auch die Vertauschung benachbarter Zeichen. Ein anderer prominenter
#Vertreter dieser Algorithmenklasse ist die Suche nach dem längsten gemeinsamen Teilstring.
#Die Bioinformatik nutzt ein Verfahren, das an die Berechnung von Editierdistanzen angelehnt 
#ist, um die Ähnlichkeit von Gensequenzen und damit Verwandtschaftsverhältnisse von Organismen
#und Viren zu beurteilen - denn auch die Basenfolgen des genetischen Codes (DNS) sind
#letztlich Zeichenketten. Ein anderer Anwendungsfall ist die automatische Korrektur von
#Tippfehlern: der systematische Vergleich eines falsch geschriebenen Wortes mit Wörterbuch-
#einträgen liefert hierbei die naheliegendsten Korrekturvorschläge.
#Außerdem kann ein solcher Vergleich für eine "unscharfe Suche" in einem Text hilfreich
#sein. Während die normale Volltextsuche nur exakte Übereinstimmungen findet, kann eine
#unscharfe Suche auch leicht abweichende Schreibweisen aufspüren.

#Bonn und Berlin sind 4 Editier-Operationen voneinander entfernt:
#                   BONN
#                   BENN
#                    -
#                   BERN
#                     -
#                   BERLN
#                      -
#                   BERLIN
#                     -
#Mit zwei Ersetzungen (O zu E und N zu R) kommen wir von BONN nach BERN. Durch Einführung
#von L und I geht es dann von BERN nach BERLIN.
#Der kürzeste Editier-Weg von BONN nach BERLIN lässt sich schnell von Hand ermitteln.
#Wie aber sieht es aus mit der Editier-Distanz zwischenn Rhabarbermarmelade und 
#Rhododendronbusch ? Hier findet man durch bloßes Ausprobieren nicht unbedingt die beste
#(kürzeste!) Lösung ! Wir benötigen also ein automatisches Verfahren, das zuverlässig
#die küzeste Distanz zwischen zwei beliebigen Zeichenketten ermittelt. 
#Und genau das leistet der Levenshtein-Algorithmus.
#Noch ein Beispiel - ein optimaler Weg duch den "Editier-Raum", um SCHLAU in BAUCHIG
#umzuwandeln:
#              Text            Operation              Kosten
#              --------        -------------------    ------
#            > SCHLAU          S,C,H entfernen           3
#              LAU             L durch B ersetzen        1
#              BAU             B,A,U beibehalten         0
#              BAU             C,H einfügen              2       
#            < BAUCHIG                                   Summe = 6
            
#Hier ist eine schöne Visualisierung der Levenshtein-Distanz von Pit Noack:
#https://www.maschinennah.de/ki-buch/
#           https://editor.p5js.org/MaschinenNah/full/QfyEWeNQa    (cat und chello eingeben)
#Hier kann man zwei Strings eingeben, angezeigt wird dann die Editierdistanz
#und die Levenshtein-Matrix. Was hat es mit dieser Levenshtein-Matrix auf sich ?
#                                                  ------------------
#Die Matrix zeigt den Lösungsweg auf, genauer gesagt: die Berechnung der Matrix für zwei
#gegebene Strings a und b ist die Berechnung der Editierdistanz zwischen a und b.
#das Endergebnis ist immer der Wert, der in der unteren rechten Ecke der Matrix steht.
#Genauer gesagt: jede Zelle der Matrix enthält die Kosten für den Weg zwischen zwei
#Strings. Die Lenveshtein-Matrix sei im folgenden dargestellt anhand des Start-Strings
#"SCHLAUCH" und des Ziel-Strings "BAUCHIG":
#                                                Editier-Operationen:
#                                                --------------------
#                           ZIEL                 Ein Schritt nach rechts = Einfügung eines Zeichens (Kosten 1)
#                                                Ein Schritt nach unten  = Löschung eines Zeichens  (Kosten 1)
#               leer  B  A  U  C  H  I  G        Ein Schritt diagonal nach rechts unten = Ersetzung (Kosten 1) oder
#           leer   0. 1  2  3  4  5* 6  7                                                 oder Beibehaltung (Kosten 0)
#              S   1. 1  2  3  4  5  6  7                                                 eines Zeichens
#       S      C   2. 2  2  3  3  4  5  6         
#       T      H   3. 3  2  3  4  3  4  5        Der optimale Weg durch den "Editier-Raum" (wie in der obigen
#       A      L   4  4. 4  4  4  4  4  5        Tabelle dargestellt) kann in der Levenshtein-Matrix durch Punkte
#       R      A   5  5  4. 5  5  5  5  5        direkt neben den jeweils akkumulierten Kosten visualisiert werden
#       T      U   6  6  5  4.*5  6  6  6            
#              C   7  7  6  5  4. 5  6  7
#              H   8  8  7  6  5  4. 5. 6.|   <--dieser Wert ganz rechts unten ist die minimale
#                                                Editierdistanz, also die Levenshtein-Distanz zwischen
#                                                SCHLAUCH und BAUCHIG
#
#Weitere LS-Distanzen (markiert duch *), die man aus der Matrix direkt ablesen kann:
#-----------------------------------------------------------------------------------
#Levenshtein-Distanz vom Leeren String nach BAUCH = 5    (man benötigt fünf Einfügungen)
#Levenshtein-Distanz von SCHLAU nach BAU = 4             (S,C,H entfernen; L durch B ersetzen; A,U beibehalten)





#########################################################################################
#########################################################################################
# 6.5 Calculating the Powerset by Using Functional Programming
#########################################################################################

#In diesem Abschnitt erfahren wir etwas über ein wichtiges mathematisches Konzept bekannt 
#als Potenzmenge (Powerset): die Menge aller Teilmengen. Man benötigt Potenzmengen in der 
#Statistik, Mengenlehre, funktionalen Programmierung, Wahrscheinlichkeitstheorie und 
#Algorithmen-Analyse etc.

#Die Potenzmenge ist die Menge aller Teilmengen der gegebenen Menge s. Sie umfasst die 
#leere Menge {}, die ursprüngliche Menge s und alle anderen möglichen Untermengen der 
#ursprünglichen Menge. Hier sind ein paar Beispiele:

#Beispiel 1:
#   - Gegebene Menge: s = {1}
#   - Potenzmenge: P = {{},{1}}
#Beispiel 2:
#   - Gegebene Menge: s = {1, 2}
#   - Potenzmenge: P = {{},{1},{2},{1,2}}
#Beispiel 3:
#   - Gegebene Menge: s = {1, 2, 3}
#   - Potenzmenge: P = {{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

#Zuerst versuchen wir es mal gemäß einem Lehrbuch für Algorithmen-Design:
#--- Erzeugung einer Potenzmenge ---
def get_binary_rep(n, num_digits):
   """Assumes n and numDigits are non-negative ints
      Returns a str of length numDigits that is a binary
      representation of n"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > num_digits:
      raise ValueError('not enough digits')
   for i in range(num_digits - len(result)):
      result = '0' + result
   return result

def gen_powerset(L):
   """Assumes L is a list
      Returns a list of lists that contains all possible
      combinations of the elements of L. E.g., if
      L is [1, 2] it will return a list with elements
      [], [1], [2], and [1,2]."""
   powerset = []
   for i in range(0, 2**len(L)):
      bin_str = get_binary_rep(i, len(L))
      subset = []
      for j in range(len(L)):
         if bin_str[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset
#---

gen_powerset(['x','y'])      #[[], ['y'], ['x'], ['x', 'y']]

#Die Funktion gen_powerset(L) gibt eine Liste von Listen zurück, die alle möglichen 
#Kombinationen der Elemente von L enthält. Wenn L beispielsweise ['x', 'y'] ist, wird die 
#Potenzmenge von L eine Liste sein, die die Listen [], ['x'], ['y'], und ['x', 'y'] als
#Elemente enthält.

#Der Algorithmus ist ein wenig subtil (das ist nur eine freundliche Umschreibung für: 
#schwierig zu verstehen). Betrachten wir eine Liste mit n Elementen. Wir können jede 
#Kombination von Elementen durch eine Zeichenkette aus n Nullen und Einsen darstellen, 
#wobei eine 1 für das Vorhandensein eines Elements und eine 0 für dessen Abwesenheit steht. 
#Die Kombination, die keine Elemente enthält, wird dargestellt durch eine Zeichenkette, die 
#nur Nullen enthält. Und die Kombination, die alle Elemente enthält, wird wird durch eine 
#ZeichenketteFolge nur aus Einsen bestehend dargestellt. Die die Kombination, die nur
#nur das erste und letzte Element enthält, wird durch die Zeichenkette '100...001' dargestellt.

#Die Generierung aller Unterlisten einer Liste L der Länge n kann wie folgt erfolgen:
#
#         *    Erzeuge alle n-Bit-Binärzahlen. Dies sind die Zahlen von 0 bis 2^n - 1.
#
#         *    Für jede dieser 2^n Binärzahlen, b, erstelle eine Liste, indem diejenigen 
#              Elemente von L ausgewählt werden, die einen Index haben, der einer 1 in b 
#              entspricht. Wenn L zum Beispiel ['x', 'y', 'z'] und b gleich 101 ist, 
#              erzeugen die Liste ['x', 'z'].
#
#Versuchen Sie, gen_powerset auf eine Liste anzuwenden, die die ersten 10 Buchstaben
#des Alphabets enthält: 

gen_powerset('abcdefghij')

#Es wird recht schnell fertig und erzeugt eine Liste mit 1024 Elementen (denn 2^10 ist 1024). 
#Versuchen Sie als nächstes, gen_powerset mit den ersten 20 Buchstaben des Alphabets 
#aufzurufen: 

gen_powerset('abcdefghijkrstuvwxyz')

#Die Ausführung wird mehr als nur ein wenig Zeit in Anspruch nehmen und eine Liste mit etwa 
#einer Million Elementen zurückliefern (denn 2^20 ist 1048576). Wenn Sie versuchen gen_powerset 
#für alle 26 Buchstaben auszuführen, werden Sie es wahrscheinlich leid sein zu warten, es sei 
#denn, Ihrem Computer geht der Speicher aus, wenn er versucht, eine Liste mit mehreren zehn 
#Millionen Elementen zu erstellen. Denken Sie nicht einmal daran, gen_powerset auf eine Liste 
#anzuwenden, die alle Groß- und Kleinbuchstaben enthält. 
#Schritt 1 des Algorithmus erzeugt die O(2^len(L)) Binärzahlen. Der Algorithmus ist also 
#exponentiell mit der Potenz len(L).

#_______________
#Nebenbemerkung: 
#_______________
#Bei einer Liste der Länge 10, z.B. 'abcdefghij', erzeugen wir also 2^10 = 1024 Binärzahlen
#                                    __________
#                                        ||
for i in range(0, 1024):            #    V
    print(get_binary_rep(i,10))     #0000000000
                                    #0000000001
                                    #0000000010
                                    #0000000011
                                    #...
                                    #1111111110
                                    #1111111111

#Jede dieser Binärzahlen wird dann in gen_powerset in eine entsprechende Auswahlkombination 
#von Elementen aus der Liste umgewandelt, indem für eine Position in der Binärzahl, an der 
#eine '1' steht, dasjenige Element, das an derselben Position in der Liste steht, in die 
#betreffende Auswahlkombination übernommen wird. Z.B. die Binärzahl 0000000011 erzeugt die
#Auswahlkombination ['i', 'j'].  
#_______________

#Und jetzt kommt eine extrem elegante Einzeiler-Lösung, um Potenzmenge zu berechnen:
#-----------------------------------------------------------------------------------
#Die gesamte Berechnung der Potenzmenge läßt sich mit einer Kombination aus der 
#funktionalen Programmierung (FP) noch viel kürzer beschreiben!!! Mit lambda, reduce und 
#list-comprehension wird die Bestimmung des Powersets zum Einzeiler. Übrigens: comprehensions 
#sind ebenfalls eine etablierte Technik der FP, und zwar die sog. 'sequence monade'. 
from functools import reduce
#Menge s
s = {1, 2, 3}
#Und hier ist der "The One-Liner" zur Berechnung der Potenzmenge (engl. powerset):

ps = lambda s: reduce( lambda P, x: P + [subset | {x} for subset in P],  s,  [set()] ) #<---- Einzeiler !!!!!!!!!
  
#Und hier ist das Ergebnis:
print(ps(s))    #[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]

#Wie funktioniert das ?
# 1.) Initialisiere die Potenzmenge P_0 mit der leeren Menge: set(). Das ist die einzige
#     Möglichkeit in Python, die leere Menge darszustellen. Denn {} geht nicht, da {} ein
#     dict und kein set ist.
# 2.) Die Potenzmenge P_n mit n Elementen wird aus der Potenzmenge P_n-1 mit n-1 Elementen
#     erzeugt, indem aus der Menge s ein Element x entnommen wird und folgende Prozedur
#     ausgeführt wird:
# 3.) Betrachte alle Elemente p in P_n-1 (beachte: diese Elemente sind ihrerseits Mengen) und 
#     erzeuge für jedes p die Vereingung mit x, also p|x , wodurch man die temporäre Menge T 
#     dieser Vereingungsmengen erhält. Z.B.: sei P_2 = {{},{1},{2},{1,2}} und x = 3, dann 
#     erzeugen wir daraus P_3 ={{3},{1,3},{2,3},{1,2,3}}, indem wir zu jedem Element von P_2 
#     die Zahl 3 hinzufügen.
# 4.) Vereinige nun T mit P_n-1, wodurch die Potenzmenge P_n entsteht.
# 5.) Wiederhole die Schritte 3.) und 4.) bis die Menge s leer ist.
#
#Die Potenzmenge wird also schrittweise aufgebaut beginnend mit der leeren Menge. 
#Mit jedem Schritt wird ein Element aus s entnommen, das dann jedem Element der Kopie der
#Potenzmenge des vorangegangenen Schritts zugefügt wird. Die Potenzmenge des aktuellen Schritts
#besteht dann aus der Vereinigung der so modifizierten Kopie und der vorangegangenen 
#Potenzmenge. Die Potenzmenge verdoppelt sich also mit jedem Schritt, d.h. exponentielles 
#Wachstum.

#Detail-Erläuterungen:
{1,2,3} | {4,5,6}  #Addition (Vereinigung) zweier Mengen mit dem | Operator: {1, 2, 3, 4, 5, 6}
[1,2,3] + [4,5,6]  #Addition zweier Listen mit dem + Operator: [1, 2, 3, 4, 5, 6]

reduce(lambda x,y: x+y, [1,2,3,4,5])  #reduce faltet die Liste mittels Addition zusammen.
                                      #1+2 = 3
                                      #- -
                                      #      3+3 = 6
                                      #        -    
                                      #            6+4 = 10
                                      #              -
                                      #                  10+5 = 15 
                                      #                     - 
                                      #also: (((1+2)+3)+4)+5 = 15
reduce(lambda x,y: x+y, [1,2,3,4,5], 10) #Mit zusätzlicher, optionaler Initialisierung 10 
#ergibt das: 25
#Dieses "Falten" kann durch reduce mittels jeder beliebigen zweistelligen Funktion 
#<lambda x,y: x ... y> ausgeführt werden, z.B. *:
reduce(lambda x,y: x*y, [1,2,3,4,5], 10)   #((((10*1)*2)*3)*4)*5 = 1200   

#So, jetzt wissen wir, was reduce macht. Und hier ist nochmal unser Algorithmus:
ll = lambda P, x: P + [subset | {x} for subset in P]
reduce(ll,s, [set()])   #ergibt: [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
#Das sehen wir uns jetzt schrittweise an:
s = {1,2,3}
#reduce soll eine Liste der Elemente der Potenzmenge von s erzeugen.
#reduce bekommt zwei Argumente: die Menge s, aus die Potenzmenge erzeugt werden soll und
#die Initialisierung [set()]. Das ist gewissermaßen der Urzustand der zu berechenden Ergebnisliste
#der Potenzmengen-Elemente - diesen Urzustand nennen wir P0:
P0 = [set()]
#Dann wird das erste Element aus s entnommen, also die 1. Diese wird mit allen
#Elementen aus P0 zu entsprechenden Mengen vereinigt. Diese Vereinigungsmengen werden in
#eine Liste T gepackt:  
T = [subset|{1} for subset in P0]   
print(T)   #[{1}]
#Da P0 nur aus set(), also der leeren Menge, besteht, erhalten wir somit T = [{1}]
#Nun wird P0 und T zusammengefügt zur neuen Liste P1:
P1 = P0 + T 
print(P1)    #[set(), {1}]
#Nun wird das zweite Element aus s entnommen,also die 2. Diese wird mit allen
#Elementen aus P1 zu entsprechenden Mengen vereinigt. Diese Vereinigungsmengen werden in
#eine Liste T gepackt:
T = [subset|{2} for subset in P1]
print(T)   #[{2}, {1, 2}]
#P1 und T werden dann zu einer neuen Liste P2 zusammengefügt:
P2 = P1 + T
print(P2)   #[set(), {1}, {2}, {1, 2}]
#Nun wird das dritte Element aus s entnommen,also die 3. Diese wird mit allen
#Elementen aus P2 zu entsprechenden Mengen vereinigt. Diese Vereinigungsmengen werden in
#eine Liste T gepackt:
T = [subset|{3} for subset in P2]
print(T)    #[{3}, {1, 3}, {2, 3}, {1, 2, 3}]
#P2 und T werden dann zu einer neuen Liste P3 zusammengefügt:
P3 = P2 + T
print(P3)   #[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
#Und P3 ist das Endergebnis: die Potenzmenge von {1,2,3} !!!





#########################################################################################
#########################################################################################
# 6.6 Caesar’s Cipher Encryption Using Advanced Indexing and List Comprehension
#########################################################################################

#Siehe https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung

## Data
abc = "abcdefghijklmnopqrstuvwxyz"
s = "xthexrussiansxarexcoming"

## One-Liner
rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])

## Result
print(rt13(s))               #kgurkehffvnafknerkpbzvat
print(rt13(rt13(s)))         #xthexrussiansxarexcoming


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Das Alphabet wird einfach um 13 Stellen verschoben, deswegen heißt unsere obige Funktion 
#rt13 (für rot13, rotieren um 13 Stellen). Einzelne Zeichen werden damit durch ihre
#"rotierten" Zeichen ersetzt.




#########################################################################################
#########################################################################################
# 6.7 Finding Prime Numbers with the Sieve of Eratosthenes
#########################################################################################

#siehe https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes

## Dependencies
from functools import reduce

## The Data
n = 100

## The One-Liner
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))

## The Result
print(primes)     #{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~





#########################################################################################
#########################################################################################
# 6.8 Calculating the Fibonacci Series with the reduce() Function
#########################################################################################

#Die Fibonacci-Zahlen Fib(n) sind folgendermaßen rekursiv definiert, 
#wobei Fib(n) die n-te Fibonacci-Zahl ist:
#   Fib(0) = 0
#   Fib(1) = 1
#   Fib(n) = Fib(n-1) + Fib(n-2)

# Dependencies
from functools import reduce

# The Data
n = 10

# The One-Liner
fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])

# The Result
print(fibs)           #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~
#Wir verwenden hier wieder die leistungsstarke Funktion reduce(). Im Allgemeinen ist diese 
#Funktion nützlich, wenn man Zustandsinformationen aggregieren möchten, die während der 
#Laufzeit berechnet wurden; zum Beispiel, wenn wir die beiden vorherigen Fibonacci-Zahlen 
#verwenden, um die nächste Fibonacci-Zahl zu berechnen. Dies ist schwer zu erreichen mit 
#einer list-comprehension, die im Allgemeinen nicht auf Werte zugreifen kann, die durch 
#sie selbst gerade neu erzeugt worden sind.
#Wir verwenden die Funktion reduce() mit drei Argumenten, 
#reduce(function, iterable, initializer), um eine neue Fibonacci-Zahl fortlaufend zu einem 
#Aggregator-Objekt hinzuzufügt, das einen Wert nach dem anderen aus dem iterierbaren Objekt
#iterable herausholt.
#Hier verwenden wir eine einfache Liste als Aggregator-Objekt mit den beiden anfänglichen
#Fibonacci-Zahlen [0, 1]. Denke daran, dass das Aggregator-Objekt als erstes Argument an die 
#Funktion übergeben wird (in unserem Beispiel: x).
#Das zweite Argument ist das nächste Element aus dem Iterable. 
#Wir haben das iterable mit (n-2) Dummy-Werten initialisiert, um die Funktion reduce() zu 
#zwingen, die lambda-Funktion (n-2)-Mal auszuführen (das Ziel ist es, die ersten n Fibonacci-
#Zahlen zu finden - aber die ersten beiden, 0 und 1, haben wir ja bereits).
#Wir verwenden den Wegwerfparameter (throwaway-parameter) _, um anzuzeigen, dass wir nicht 
#an den Dummy-Werten des iterables interessiert sind. Stattdessen fügen wir einfach die neue
#Fibonacci-Zahl an die Aggregatorliste x an, die als Summe der beiden vorherigen Fibonacci-
#Zahlen berechnet wird.
#
#Hier ist der entscheidende Teil der Doku von reduce:
#              --- reduce(function, iterable[, initial]) -> value ---
#              Apply a function of two arguments cumulatively to the items 
#              of a sequence or iterable, from left to right, so as to reduce 
#              the iterable to a single value. For example, 
#              reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
#              calculates ((((1+2)+3)+4)+5). If initial is present, 
#              it is placed before the items of the iterable in the calculation, 
#              and serves as a default when the iterable is empty.
#Setzen wir das, was in der obigen Doku steht, einfach mal um...
#Faltung des iterables [1,2,3,4]:
reduce(lambda x,y: x+y, [1,2,3,4,5])  # 1+2 = 3
                                      # 3+3 = 6
                                      # 6+4 = 10  
                                      # 10+5 = 15    => 15
#Und jetzt mit initializer 5:
reduce(lambda x,y: x+y, [1,2,3,4], 5) # 5+1 = 6
                                      # 6+2 = 8
                                      # 8+3 = 11
                                      # 11+4 = 15    => 15
#Wenn das iterable leer ist, 
#returniert reduce einfach nur den initializer:
reduce(lambda x,y: x+y, [], 5)        #              => 5
#Jetzt wissen wir, was reduce macht!
#
#Und nun gucken wir uns den Einzeiler an...
#Für n = 0 oder n = 1 oder n = 2 gilt:
#-------------------------------------
n = 2 #oder 0 oder 1
reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])    #[0,1]
#ist dasselbe wie:
reduce(lambda x, _: x + [x[-2] + x[-1]], [], [0, 1])             #[0,1]
#Es wird einfach der initializer [0,1] returniert, da das iterable [] leer ist.
#
#Für n >= 3 gilt:
#----------------
n = 3 #(oder größer)
#also [0] * (n-2) = [0] * 1 = [0] ---->----v   d.h. das iterable ist jetzt nicht mehr leer!          
reduce(lambda x, _: x + [x[-2] + x[-1]] , [0], [0,1])   #[0,1,1]
#D.h. die lambda-Funktion wird jetzt das erste mal ausgewertet:
[0,1] + [[0,1][-2] + [0,1][-1]]                         #[0,0,1]
#OK, aber welche Aufgabe hat das iterable [0] und warum gibts das Throw-Away-Argument _ ???
reduce(lambda x: x + [x[-2] + x[-1]] , [0], [0,1])   #wenn das Throw-away-Argument fehlt,
                                                     #gibts eine Fehlermeldung. Denn: eine 
                                                     #Funktion mit nur einem Argument kann 
                                                     #nicht aggregieren !!
                                                     #reduce besteht auf einer Funktion mit
                                                     #zwei Argumenten, also...
reduce(lambda x, _: x + [x[-2] + x[-1]] , [0], [0,1])#...hier ist sie!
#Diese lambda-Funktion hat aber eine besondere Bauweise: sie konstruiert eine Liste,
#deren Elemente als Summe ihrer beiden nächsten Vorgänger-Elemente gebildet werden.
#Sie ist also im Grunde genommen eine aggregierende Funktion. Um das zu sehen, müssen wir
#das Ganze ein bißchen umbauen, eine Schleife verwenden und explizit die zu aggregierende 
#Liste mittels zweier Variablen verwalten und so innerhalb der Schleife immer wieder
#in die aggregierende Funktion einfüttern:
lmbd = lambda x: x + [x[-2] + x[-1]]
agg = [0,1]
for i in range(1,10):
    agg_ = lmbd(agg) 
    #print(agg_)   
    agg = agg_
print(agg)         #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  das sind die Fibonaccis !!
#lmbd macht also schon genau das, was wir brauchen. Und einer expliziten Schleife benötigt
#lmbd auch kein Throw-Away-Argument _.
#Da wir unbedingt einen Einzeiler schreiben wollen, müssen wir die Schleife irgendwie
#anders implementieren. Wir verwenden dazu reduce, das eine implizite, rekursive Schleife
#ausführt - und wegen reduce brauchen wir das Throw-Away-Argument _.
#Bleibt nur noch zu klären, wozu wir das iterable [0] * (n-2) benötigen:
#reduce wird nur dann ausgeführt, wenn das iterable nicht leer ist. reduce entnimmt
#schrittweise Elemente aus dem iterable und übergibt sie an das Throw-Away-Argument
#von lmbd, also _. Das können wir direkt beobachten, wenn wir lmbd etwas umbauen:
reduce(lambda x, _: (x + [x[-2] + x[-1]], print(_))[0] , [0,1,2], [0,1])  #0        \
                                                                          #1         > Throw-Away-Argument
                                                                          #2        / 
                                                                          #[0, 1, 1, 2, 3]  Endergebnis
#Wir erzeugen hier ein Tupel bestehend aus der zu aggregierenden Liste und dem
#Printen des jeweiligen Wertes des Throw-Away-Arguments. Da der Rückgabewert
#von lmbd aber von reduce beim nächsten Durchlauf weiterverwendet werden soll
#und wir letztlich dabei eine Liste aggregieren, dürfen wir nur das erste Element
#des Tupels (Index 0) returnieren.
#reduce arbeitet solange bis das letzte Element dem iterable entnommen wurde.
#Wir brauchen aber die konkreten Werte des iterables gar nicht, sondern es muss
#nur sichergestellt sein, dass das iterable eine hinreichende Länge hat,
#so dass entsprechend dieser Länge dann Schleifendurchläufe von reduce ausgeführt 
#werden. D.h. reduce in Kooperation mit dem iterable implementiert eine endliche Schleife.
#Und hier ist ein aufdiese Weise erzeugte Liste der ersten 10 Fibonaccis:
reduce(lambda x, _: x + [x[-2] + x[-1]] , [0,0,0,0,0,0,0,0], [0,1])  #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]





#########################################################################################
#########################################################################################
# 6.9 A Recursive Binary Search Algorithm
#########################################################################################

#Siehe https://de.wikipedia.org/wiki/Bin%C3%A4re_Suche

## The Data
l = [3, 6, 14, 16, 33, 55, 56, 89]
x = 33

## The One-Liner
bs = lambda l, x, lo, hi: -1 if lo>hi else(lo+hi)//2 if l[(lo+hi)//2] == x else bs(l, x, lo, (lo+hi)//2-1) if l[(lo+hi)//2] > x else bs(l, x, (lo+hi)//2+1, hi)

## The Results
print(bs(l, x, 0, len(l)-1))              #4


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~





#########################################################################################
#########################################################################################
# 6.10 A Recursive Quicksort Algorithm
#########################################################################################

#Siehe https://de.wikipedia.org/wiki/Quicksort

## The Data
unsorted = [33, 2, 3, 45, 6, 54, 33]

## The One-Liner
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

## The Result
print(q(unsorted))           #[2, 3, 6, 33, 33, 45, 54]


#~~~~~~~~~~~~~~~~
#Background infos
#~~~~~~~~~~~~~~~~





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#FINIS
