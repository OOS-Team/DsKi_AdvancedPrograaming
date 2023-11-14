
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
bonus = [(k, v + 500) for k, v in employees.items()]
# Result
print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]
print(bonus)

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
list=[(k, v) for k, v in employees.items() if v >= 100000]  #[('Alice', 100000), ('Carol', 122908)]
#Das ist eine superelegante, extrem komprimierte und trotzdem leicht lesbare 
#Schreibweise !!! Die Inspiration dafür stammt aus der funktionalen Programmiersprache
#Haskell, siehe https://wiki.haskell.org/List_comprehension
#Diese Sprache ist eine pure Umsetzung des sog. lambda-Kalküls, siehe
#https://de.wikipedia.org/wiki/Lambda-Kalk%C3%BCl
#Als Hommage an die Bedeutung des lambda-Kalküls wurde das Schlüsselwort für die Definition
#anonymer Funktionen in Python lambda getauft !!
list_keys = [(k,v) for k,v in employees.items() if v<=700000]
print(list_keys)




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
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

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
print(s[3:0])         # (empty string '')
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
#Dazu ein Bsp.:
l1 = [1,2,3]
l2 = [4,5,6]
l1_2 = zip(l1,l2)    
#Daher der Name zip: diese Funktion wirkt wie ein Reißverschluss. Da zip einen Generator
#returniert, müssen wir diesen in eine Liste stecken, um alle Inhalte zu sehen:
list(l1_2)           #[(1, 4), (2, 5), (3, 6)]
#Und mit Hilfe von "iterable unpacking" 
#    (siehe dazu: https://docs.python.org/3/reference/expressions.html#expression-lists 
#           und: https://stackoverflow.com/questions/50878860/python-unpack-iterator )
#und einer nochmaligen Anwendung von zip kann man die zusammengeschweißten Elemente 
#wieder auseinanderpflücken. Dazu müssen wir zuerst von l1_2 die umgebende eckige
#Klammer entfernen, d.h. die Elemente herausholen. Das machen wir mit dem unpacking 
#operator * (beachte: das funktioniert nur innerhalb von Funktionsaufrufen, 
#hier z.B. in print):
print(*l1_2)    #(1, 4) (2, 5) (3, 6)
#Nur der Vollständigkeit halber sei erwähnt, dass unpacking auch mit Generatoren funktioniert:
print(*range(4))    #1 2 3 4
#Die mit dem upacking-Operator * entpackten Elemente von l1_2 können wir wieder der
#zip-Funktion übergeben, dadurch erhalten wir wieder die beiden ursprünglichen Listen
#l1 und l2 (beachte: vorher *l1_2 nochmals auswerten, da es durchs unpacking in-place 
#verändert wird):
list(zip(*l1_2))          #[(1, 2, 3), (4, 5, 6)]
#oder (beachte: vorher *l1_2 nochmals auswerten, da es durchs unpacking in-place 
#verändert wird)
print(*zip(*l1_2))        #(1, 2, 3) (4, 5, 6)
#oder ganz ausführlich in voller Schönheit:
print(*zip(*zip(l1,l2)))  #(1, 2, 3) (4, 5, 6)
#Hieraus sieht man, dass zip in gewisser Weise seine eigene Umkehrfunktion ist.
#Einen iterable-unpacking-operator * werden wir los, wenn wir auf der linken Seite
#einer Zuweisungsanweisung das sog. "sequence unpacking" verwenden, 
#     siehe dazu: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
a,b = zip(*zip(l1,l2))
print(a, b)               #(1, 2, 3) (4, 5, 6)
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
b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
print(b.ndim)                                        # 2
c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
print(c.ndim)                                        # 3
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
#Als nächstes wollen wir auf das Konzept des "Reshaping" eingehen. Dabei wird die Shape:
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
#Dabei bezeichnen in jedem dieser Tupel, die ersten beiden Zahlen die ausgewählten Spalten
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
