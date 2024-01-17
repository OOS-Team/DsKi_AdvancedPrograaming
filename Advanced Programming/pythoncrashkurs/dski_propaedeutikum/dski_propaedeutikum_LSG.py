#tw, 15.3.2023
#-------------

#                          =======================================================
#                          =======================================================
#                                    DSKI-PROPÄDEUTIKUM - Lösungen zu den Aufgaben
#                          =======================================================
#                          =======================================================
#
#
#   

###Struktur von Komponenten
# List Comprehension
# [expression for element in iterable if condition]

# Lambda Funktion
# lambda parameters: expression


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
# +++

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


# Der One-Liner listet alle Angestellte auf die über 100000 Euro im Jahr verdienen. 
# Die List Comprehension erstellt eine neue Liste mit den werten k und v.
# Sie enthält eine for schleife für die iteratoren k und v. Durch die Funktion .items() 
# werden die key (k) und value (v) Werte aus dem Dictionary herausgeholt.
# Die if Bedingung filtert die (k,v) Tupel heraus wo der Value wert über 100000 ist.


#########################################################################################
#########################################################################################
# 2-2 Using List Comprehension to Find Words with High Information Value
#########################################################################################
#+++

# split() teilt in Zeilen oder Wörter

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


# For line in text.split('\n') extrahiert aus dem String text die einzelnen Zeilen heraus.
# die innere ListComprehension x for in line.split() extrahiert aus Zeilen einzelne Wörter.
# die if Bedingung filtert Wörter heraus die weniger als drei Buchstaben haben.
#  (Länge des wortes > 3)

#########################################################################################
#########################################################################################
# 2-3 Reading a File
#########################################################################################
#+++

# Bemerkung
# strip() kürzt Strings zB Absatz und leerzeichen

# One-Liner
print([line.strip() for line in open("one_liner_2-3.py")])
# Output: <This file content>

# Der One-Liner enthält eine Listcomprehension welche dann in der Konsole ausgegeben
# wird. In die liste werden gestutze Zeilen eingefügt welche aus dem file one_liner_2-3
# über die openfunktion extrahiert werden. Gestutz bedeutet dass Leerzeichen vor und hinter 
# dem geschriebenen ausgeschnitten werden.



#########################################################################################
#########################################################################################
# 2-4 Using Lambda and Map Functions
#########################################################################################
#+
# map(funktion, iterable) 


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



# DIe Lambda Funktion hat den Parameter s welcher für einen String steht. In der expression 
# wird definiert, dass ein Tupel bestehend aus Boolean und dem String zurückgegeben wird. 
# Durch die Bedingung in der Lambda Funktion wird der String s überprüft ober das Wort
# anonymous enthält. Trifft das zu ist der Boolean True ansonsten False. Die map Funktion 
# wendet die Lambda Funktion auf jeden String in dem Array txt an.


#########################################################################################
#########################################################################################
# 2-5 Using Slicing to Extract Matching Substring Environments
#########################################################################################

#find() gibt den niedrigsten Index des (Anfangszeichen) Teilstringszurück 

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


# Die Lambda Fuktion enthält zwei Parameter x(String --> letters_amazon) und q(Wort --> SQL).
# In der Expression der Lambda Funktion wird der Index von dem Anfangsbuchstaben des zu
#  suchenden Wortes über die Funktion find() gesucht. Anschließend wird auf der Linken Seite 
# des Slicing der Index minus 18 gerechnet und auf der rechten Seite des Sclicing Operators 
# plus 18 gerechnet. somit werden 18 Zeichen vor dem Gesuchten Wort und 18 Zeichen nach dem Anfangsbuchstaben
# des gesuchten Wortes für das Slicing definiert. 

#########################################################################################
#########################################################################################
# 2-6 Combining List Comprehension and Slicing
#########################################################################################
#+++

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

# Die List Comprehension befüllt die neue Liste mit jedem zweiten Wert einer Zeile
# duch den Slicing Operator ::2. Die for Schleife nimmt sich jedes Element(line) aus dem 
# mehrdimensionalem Array(also ein Array) heraus. Das neue mehrdimensionale Array wird
# der variable sample zugeschrieben



#########################################################################################
#########################################################################################
# 2-7 Using Slice Assignment to Correct Corrupted Lists
#########################################################################################
#+++

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


# Durch den Slicing Operator visitors[::2] wird - angefangen bei dem ersten Element der Liste
# - jeder zweite Wert abgegriffen. Der Slicing Operator [1::2] Nimmt jeden zweiten Wert ab 
# dem zweiten Element. Durch die zuweisung werden in der Liste visitors jeder zweite Wert ab
# dem zweiten Element mit jedem zweiten Wert ab dem ersten Element ersetzt. (Bsp corrupted --> Firefox)


#########################################################################################
#########################################################################################
# 2-8 Analyzing Cardiac Health Data with List Concatenation
#########################################################################################
#+++

# Dependencies
import matplotlib.pyplot as plt

# Data
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

# One-Liner
expected_cycles = cardiac_cycle[1:-2] * 10

## Result
plt.plot(expected_cycles)
plt.show()

# Die Slicing Operationcardic_cycle[1:-2] wählt ab dem zweiten Element bis zum 
# vor vorletzten Element aus. Das Erste das letze und vorletze Element von cardiac_cycle
# werden durch die Operation ausgeschnitten. Durch die Multiplikation *10 wird
# die Länge der Liste extrahierter Werte verzehnfacht.  

#########################################################################################
#########################################################################################
# 2-9 Using Generator Expressions to Find Companies That Pay Below Minimum Wage
#########################################################################################
#++

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

# In der Bedingung der Listcomprehenshion werden mit einer Schleife (for y in companies[x].values)
# die Value Werte der Dictionaries herausgelesen. Die value Werte werden mit einem Vergleichsoperator
# mit kleiner 12 verglichen. Die any() funktion überprüft ob es irgendwelche True Werte aus dem Vergleich gibt.
# Wenn ein True Wert gefunden wurde wird der Name des gesamten Dictionary in die Liste
# miteingetragen. 

#########################################################################################
#########################################################################################
# 2-10 Formatting Databases with the zip() Function
#########################################################################################
#+

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

# In der List Comprehenshion wird mit einer for Schleife durch db_rows iteriert 
# um auf einzelne Zeilen zuzugreifen(row). In der Expression der List Comprehension 
# wird mit der zip() funktion jedem Wert in der Zeile row (value) ein Wert von
# column_names (Key) zugewiesen. Die Funktion dict() erstellt aus einer zeile row ein 
# Dictionary.

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
#++

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

# salaries * taxation multipliziert die werte der beiden np arrays und errechnet die 
# höhe der abzugebenden Steuern. Salaries - das Produkt aus dem vorherigen Schritt 
# subtrahiert die beiden np arrays. Es ergibt sich das Gehalt nach Steuern. Mit der
# Funktion max() wird das höchste nettogehalt gefunden. Anschließend wird das höchste Gehalt
# der Variable max_income zugewiesen.


#########################################################################################
#########################################################################################
# 3-2 Working with NumPy Arrays: Slicing, Broadcasting, and Array Types
#########################################################################################
#++


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

# Mit employees[0,::2] wird nur auf den ersten Wert und jeder zweite aus der ersten Zeile
# zugegriffen(0,). Die ausgewählten Werte werden dann mit 1,1 multipliziert.

employees * 4
np_dataScientist = np.array(dataScientist)

dataScientist * 4

dataScientist * 1.1

np_dataScientist * 1.1

np_dataScientist * 4


#########################################################################################
#########################################################################################
# 3-3 Conditional Array Search, Filtering, and Broadcasting to Detect Outliers
#########################################################################################
#+

# nonzero() Indizes der Nicht-Null-Elemente eines Arrays zu ermitteln
# gibt zwei Listen zurück mit Indizes der True und False Werte

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

# Mit X > np.average(X) wird der Durchschnitt von X mit allen Werten von X über
# broadcasting miteinander verglichen. Die Funktion nonzero() teilt True Werte und False
# Werte auf. Somit werden mit [0] auf alle Werte == True zugegriffen. Diese Indizes
# werden verwendet um die Namen der Städte abzugreifen. Die Funktion stellt sicher,
# dass es keine Duplikate mehr gibt also jeder Name nur einmal vorkommt. Die einzigartigen
# Namen der Städte werden der Variable polluted zugewiesen.


#########################################################################################
#########################################################################################
# 3-4 Boolean Indexing to Filter Two-Dimensional Arrays
#########################################################################################
#++
# astype(float) ändert den Datentypen

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

# Mit inst[:,0] wird auf die erste gesamte Spalte von inst zugegriffen. Die Funktion
# astype(float) ändert den Datentyp der Werte in Gleitkommazahlen um. Duch den Vergleichoperator
# und broadcasting werden alle Werte der erstenspalte mit dem Wert 100 verglichen.
# Sind die Werte über 100 ist das Ergebnis der Operation True, womit der Wert der zweiten Spalte
# (Name) superstars zugewießen wird. 



#########################################################################################
#########################################################################################
# 3-5 Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element
#########################################################################################
#+++
# Array Formatieren(Umstrukturiere+n)

## Sensor data (Mo, Tu, We, Th, Fr, Sa, Su)
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

## One-liner
tmp[6::7] = np.average(tmp.reshape((7,-1)), axis=0)

## Result
print(tmp)
#[1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]

# Die Funktion reshape((7,-1)) formatiert das np.array tmp um sodass das neue Array sieben 
# Zeilen(7) und drei spalten(-1= automatisch) hat. Die Funktion np.average() berechnet für jede 
# spalte einen duchschnitt(axis=0). Dieser durchschnitt wird in die siebte Spalte jeder Zeile
# eingefügt ([6::7]--> siebte spalte::jeder siebte wert) 


#########################################################################################
#########################################################################################
# 3-6 When to Use the sort() Function and When to Use the argsort() Function in NumPy
#########################################################################################
#++

#

## Data: SAT scores for different students
sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])

## One-liner
top_3 = students[np.argsort(sat_scores)][:-4:-1]

#students[np.argsort(sat_scores)][:-4:1]

## Result
print(top_3)
#['Alice' 'Frank' 'Carl']

# Die Funktion argsort() gibt die Indizes von sat_score zurück in absteigender 
# Reihenfolge der Werte. Der Slicing Operator [:-4:-1] kehrt einmal die
# Reihenfolge um und gibt alle werte zurück bis auf die letzten Vier. 



#########################################################################################
#########################################################################################
# 3-7 How to Use Lambda Functions and Boolean Indexing to Filter Arrays
#########################################################################################
#++


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

# Die Lambda Funktion hat zwei Parameter namens x(books) und y(3,9). Mit x[:,1] wird 
# auf die zweite Spalte von books zugegriffen. Die enthaltende Werte der zweiten 
# Spalte werden mittels der astype(float) Funktion in Gleitkommazahlen umgewandelt
# und anschließend mit dem gesetzten y Wert verglichen. Liegt der Wert aus books über 
# dem LimitWert (3,9) so wird die Zeile der Variable pred_bestsell zugewiesen  

#########################################################################################
#########################################################################################
# 3-8 How to Create Advanced Array Filters with Statistics, Math, and Logic
##########################################################
###############################
# +

# axis=0 --> Zeilen (Vertikal)
# np.abs() -->  absoluter Wert (die Betragsfunktion)
# Der Operator * wird hier verwendet, 
# um eine elementweise logische UND-Operation durchzuführen.

# Datenpunkte in allen drei Dimensionen (Spalten)
# des Arrays a gleichzeitig als Ausreißer betrachtet werden
 


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

# a[:,0] wält die erste Spalte aus von a. (sinngemäß dann auch für spalte 2 und Spalte 3)
# Die Werte der ausgewählten Spalte werden mittels Broadcasting mit dem Median 
# subtrahiert. Die funktion np.abs berechnet dann den Absoluten Wert der Differenz. 
# Der Betrag wird anschließend mit der Standardabweichung der Spalte verglichen. Duch
# den * Operator (And) werden die Drei Spalten Berechnungen mit einander logisch,
# sodass alle drei werte einer Zeile True sein müssen damit sie als Ausreißer in 
# outlieres zugewiesen werden. 



#########################################################################################
#########################################################################################
# 3-9 Simple Association Analysis: People Who Bought X Also Bought Y
#########################################################################################
#++

'''
np.all
gibt True zurück, wenn alle Elemente in diesem iterierbaren Objekt als wahr bewertet werden
'''

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

# Es werden sich die beiden letzten Spalten angesehen mit basket[:,2:0] und 
# entlang der Spalten(axis=1)die Werte der Zeilen zusammengefasst. DIe Funktion all()
# gibt True Werte zurück wenn in beiden Spalten die werte einer Zeile beide 1 (also True) sind.a
# mit np.sum() wird dann die Summe der (1,1) paare berechnet. Diese Summe wird dannn durch
# die gesamte Anzahl an Zeilen dividiert
# 

#########################################################################################
# 3-10 Intermediate Association Analysis to Find Bestseller Bundles
#########################################################################################
#+

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

# in der Listcomprehension sind zwei in einander verschachtelte for Schleifen mit zwei iterable 
#  range(4) (0,1,2,3) und range(i+1,4) (0+i,1+i, 2+i, 3+i). Die expression der Listcomprehension 
# hat ein Tupel bestehend aus den zwei Elementen der for Schleifen und der Summe von Zeilen die beide  
# den Wert 1 haben. Hier findet Braodcasting statt damit Werte von Zwei Spalten miteinander addiert werden.


for i in range(4):
    for j in range(1+i,4):
        print(f'i Wert {i}')
        print(f'j Wert {j}')
        print("==============")


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################





#                                    4 - Machine Learning mit scikit-learn
#                                    =====================================





#########################################################################################
#########################################################################################
# 4.1 Linear Regression
#########################################################################################

'''
np.arange(n): Erstellt ein Array mit aufeinanderfolgenden Zahlen von 0 bis n-1 
(in diesem Fall [0, 1, 2]). Diese Zahlen repräsentieren die Zeit oder eine andere 
unabhängige Variable in der linearen Regression.
.reshape((n,1)): Ändert die Form des Arrays in eine zweidimensionale Struktur,
was erforderlich ist, da scikit-learn Modelle Eingabedaten in diesem Format erwarten.
'''

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

# Aus sklear wurde eine Klasse Linearregression importiert aus welche dann ein Objekt erstellt wird
# (LinearRegression()). Dieses Objekt wird mit der funktion fit() trainiert. In der
# Trainingsfunktion, werden zu einen die X-Werte(1,2,3) und Y-Werte (stock prices) eingegeben.a
# X und y werte wenn man es sich wie in einem Koordinatensystem vorstellt. Trainings und Zielvariable
# sind damit nicht gemeint. 


#########################################################################################

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#FINIS














