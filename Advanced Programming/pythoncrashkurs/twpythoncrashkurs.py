# tw, 6.6.22
                ##################################
                ##################################
                ##################################
                ##################################
                #######                    #######
                #######  PYTHON-CRASHKURS  #######
                #######                    #######
                ##################################
                ##################################
                ##################################
                ##################################


# Ein Crashkurs für Python von TW.

# Hier werden nur die absoluten Basics dargestellt, damit man
# einen ersten Gesamtüberblick bekommt. Viele Details, viele komplexere
# Konzepte, die auf diesen Basics beruhen und die Möglichkeiten,
# die in der Standardbibliothek (und den unzähligen Zusatz-libs)
# stecken, werden hier nicht thematisiert !!!!

# Die ultimative Nachschlagequelle für alles rund um Python ist 
# natürlich die offizielle Doku: https://docs.python.org/3/
# Hierin herauszuheben sind ..
# .. das Tutorial
# https://docs.python.org/3/tutorial/index.html
# .. die Standardbibliothek
# https://docs.python.org/3/library/index.html
# .. die Sprachreferenz
# https://docs.python.org/3/reference/index.html
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ein besonders gutes, deutsches Tutorial stammt von Bernd Klein:
# https://www.python-kurs.eu/python3_kurs.php
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###########################################################################
##### Vorgehensweise zur schnellen Navigation zu den einzelnen Themen #####
###########################################################################
# 0.) Es gibt keine Zeilenangaben in der Inhaltsübersicht, weil das Dokument
#     laufend modifiziert wird und Zeilenangaben dadurch inkonsistent werden.
#     Stattdessen ...
# 1.) gewünschtes Thema in der Inhaltsübersicht (s.u.) markieren (z.B. PYTHON AUSFÜHREN).
#                              ----------------
# 2.) dann <strg>+<shift>+<f> drücken, dadurch öffnet sich der Search-Bar links
#     mit einer Trefferliste.
# 3.) i.d.R. genügt es, auf einen der ersten Treffer zu klicken. Das muss man
#     ein bißchen ausprobieren.Dadurch springt man an den Anfang des gewünschten Themas.
# 4.) Search-Bar wieder einklappen.
###########################################################################


#            INHALTSÜBERSICHT
#            ----------------
#    PYTHON AUSFÜHREN
#    DIE GRUNDLAGEN DER ARBEIT MIT PYTHON
#       VARIABLEN
#       AUSDRÜCKE UND ANWEISUNGEN
#       KOMMENTARE
#       EINRÜCKUNG
#    DATENTYPEN
#    OPERATOREN
#       ZUWEISUNGSOPERATOR
#       ARITHMETISCHE OPERATOREN
#       VERGLEICHSOPERATOREN
#       BOOLESCHE OPERATOREN
#       BITWEISE OPERATOREN
#       is UND in
#       DER TERNÄRE OPERATOR
#    STRINGS
#    BOOLEANS
#    ZAHLEN
#       INTEGER ZAHLEN
#       FLIESSKOMMA ZAHLEN
#       KOMPLEXE ZAHLEN
#       ARITHMETISCHE OPERATIONEN MIT ZAHLEN
#       EINGEBAUTE (BUILT-IN) FUNKTIONEN FUER ZAHLEN
#    KONSTANTEN
#    ENUMS
#    USER INPUT
#    STEUERANWEISUNGEN (CONTROL STATEMENTS)
#    LISTEN
#    TUPEL
#    DICTIONARIES
#    MENGEN (SETS)
#    BUILT-INS
#    FUNKTIONEN
#    OBJEKTE
#    SCHLEIFEN (LOOPS)
#       WHILE-SCHLEIFEN
#       FOR-SCHLEIFEN
#       BREAK UND CONTINUE
#    ITERATION
#    COMPREHENSIONS
#       LIST-COMPREHENSIONS
#       DICTIONARY-COMPREHENSIONS
#       SET-COMPREHENSIONS
#    GENERATOR EXPRESSIONS
#    GENERATOR ITERATOR
#    KLASSEN
#    POLYMORPHISMUS
#    OPERATOR OVERLOADING
#    MODULE
#       if __name__ == '__main__':
#       Module aus anderen Verzeichnissen
#       Aktuell geladenen Module und Suchpfad für Module
#    PAKETE
#    DIE PYTHON STANDARD BIBLIOTHEK
#    DER PEP8 PYTHON STYLE GUIDE
#    DEBUGGING
#    GÜLTIGKEITSBEREICHE (SCOPE) VON VARIABLEN, GLOBAL
#    AKZEPTIEREN VON ARGUMENTEN AUS DER BEFEHLSZEILE
#    LAMBDA FUNKTIONEN
#    REKURSION
#    VERSCHACHTELTE (NESTED) FUNKTIONEN, NONLOCAL
#    CLOSURES (FUNKTIONSABSCHLÜSSE)
#    DECORATORS
#    DOCSTRINGS
#    INTROSPECTION
#    ANNOTATIONS
#    EXCEPTIONS (AUSNAHMEN)
#    DIE -WITH- ANWEISUNG
#    INSTALLING 3rd PARTY PACKAGES USING PIP AND CONDA
#    VIRTUAL ENVIRONMENTS (MIT VENV UND CONDA)
#       VENV - Environments
#       CONDA - Environments
#            Saving and Sharing Virtual Environments
#       Verwendung von Environments mit dem Python-Plugin für VSCODE
#    IPYTHON, JUPYTER




# ======================================================================
# ======================================================================
# ======================================================================
#                           PYTHON AUSFÜHREN
# ======================================================================
# ======================================================================
# ======================================================================


#
1+1



# ======================================================================
# ======================================================================
# ======================================================================
#                DIE GRUNDLAGEN DER ARBEIT MIT PYTHON
# ======================================================================
# ======================================================================
# ======================================================================


# VARIABLEN
# ---------

# Wir können eine neue Python-Variable erstellen, 
# indem wir einen Wert mit dem Zuweisungsoperator = einem Label zuweisen.
# In diesem Beispiel weisen wir eine Zeichenkette mit dem Wert
# "Roger" dem Label name zu:

name = "Roger"

# Hier ist ein Beispiel mit einer Zahl:

age = 8

# Ein Variablenname kann aus Zeichen zusammengesetzt sein,
# aus Zahlen oder dem Unterstrichzeichen bestehen. Er kann nicht mit
# mit einer Zahl beginnen. Dies sind alles gültige Variablennamen:

#        name1
#        AGE
#        aGE
#        a11111
#        my_name
#        _name

# Dies sind ungültige Variablennamen:

#        123
#        test!
#        name%

# Ansonsten ist alles gültig, außer es ist ein Python-Schlüsselwort. 
# Es gibt einige Schlüsselwörter wie for , if , while , import und mehr.
# Es ist nicht nötig, sie auswendig zu lernen, denn Python wird
# Sie darauf hinweisen, wenn Sie eines davon als Variable verwenden, 
# und Sie werden sie nach und nach als Teil der Syntax der Programmier-
# sprache Python erkennen.


# AUSDRÜCKE UND ANWEISUNGEN
# -------------------------

# Wir können jede Art von Code ausdrücken, der einen Wert liefert.
# Das nennt man einen Ausdruck. 
# Zum Beispiel

1 + 1
"Roger"

# Eine Anweisung hingegen ist eine Operation, die mit einem
# Wert arbeitet, zum Beispiel sind dies zwei Anweisungen:

name = "Roger"
print(name)

# Ein Programm wird durch eine Reihe von Anweisungen gebildet. Jede
# Anweisung steht in einer eigenen Zeile, aber Sie können ein
# Semikolon verwenden, um mehr als eine Anweisung in einer einzelnen
# Zeile zu haben:

name = "Roger"; print(name)


# KOMMENTARE
# ----------

# In einem Python-Programm wird alles nach einem Rautezeichen
# ignoriert und als Kommentar betrachtet:

#this is a commented line
name = "Roger" # this is an inline comment


# EINRÜCKUNG
# ----------

# Die Einrückung in Python hat eine spezifische Bedeutung.
# Sie können nicht wahllos einrücken, wie z.B. so:

name = "Flavio"
#    print(name)      #TODO: Kommentar ganz links entfernen.
                     #      Der Language-Server meckert dann,
                     #      und meldet "Unexpected indentation".
                     #      Und wenn man nun diese beiden markiert
                     #      und zusammen auswertet, kommt ein
                     #      Indentation Error !!!!  

# Einige andere Sprachen haben keine bedeutungstragende
# Leerzeichen, aber in Python ist die Einrückung wichtig.
# Wenn Sie in diesem Fall versuchen, dieses Programm auszuführen, 
# würden Sie einen IndentationError: Unerwarteter Einrückungsfehler 
# erhalten, denn die Einrückung hat eine besondere Bedeutung.
# Alles, was eingerückt ist, gehört zu einem Block, wie eine Kontroll-
# Anweisung oder wie in einem bedingten Block, oder in einer Funktion 
# oder in einem Klassenkörper. Wir werden später mehr über diese
# Konzepte erfahren.



# ======================================================================
# ======================================================================
# ======================================================================
#                             DATENTYPEN
# ======================================================================
# ======================================================================
# ======================================================================

# Python hat mehrere eingebaute Typen.
# Wenn Sie die Variable name anlegen und ihr den Wert
# "Roger" zuweisen, repräsentiert diese Variable nun automatisch
# einen String-Datentyp.

name = "Roger"

# Sie können prüfen, welchen Typ eine Variable hat, indem Sie die Funktion
# type() verwenden und ihr die Variable name als Argument übergeben und 
# dann das Ergebnis mit str vergleichen:

name = "Roger"
type(name) == str       #True

# Oder Sie rufen type auf, um zu sehen, was herauskommt:

type(name)

# Oder sie verwenden isinstance() für den gleichen Zweck:

name = "Roger"
isinstance(name, str)   #True

# Beachten Sie, dass Sie, um den Wert True außerhalb des REPL (also des
# interaktiven IPython-Fensters) zu sehen, diesen Code in print() verpacken 
# müssen, aber aus Gründen der Übersichtlichkeit vermeide ich dies hier.

# Wir haben hier die Klasse str verwendet, aber das Gleiche funktioniert für
# andere Datentypen. Zuerst haben wir Zahlen. Ganzzahlige Zahlen werden
# durch die int-Klasse dargestellt. Fließkommazahlen (Brüche) sind vom Typ 
# float:

age = 1
type(age) == int            #True

fraction = 0.1
type(fraction) == float     #True

# Sie sehen also, dass jedes Wert-Literal einem bestimmten Typ entspricht, 
# etwa so:

name = "Flavio"
age = 20

# Python erkennt den Typ automatisch anhand des Wertes.

# Sie können eine Variable eines bestimmten Typs auch erzeugen, indem Sie
# einen entsprechenden Klassenkonstruktor verwenden. Dabei wird ein
# Wert-Literal oder ein Variablenname an den Klassenkonstruktor übergeben:

name = str("Flavio")
anotherName = str(name)

# Sie können auch von einem Typ in einen anderen konvertieren, indem Sie
# den Klassenkonstruktor verwenden. Python wird versuchen, den richtigen 
# Wert zu ermitteln, z.B. indem eine Zeichenkette als Zahl interpretiert
# wird:

age = int("20")
print(age)                     #20
fraction = 0.1
intFraction = int(fraction)
print(intFraction)             #0

# Dies wird als Casting bezeichnet. 
# Natürlich kann diese Konvertierung je nach dem übergebenen Wert 
# nicht immer funktionieren. Wenn Sie in der obigen Zeichenkette 
# "test" anstelle von "20" schreiben, erhalten Sie folgende Fehlermeldung
# - ValueError: invalid literal for int() with base 10: 'test' error -

# Das sind nur die Grundlagen der Typen. Natürlich gibt es noch viel 
# mehr Typen in Python:
#
#     complex  ---  komplexe Zahlen
#     bool     ---  boolean (logische Wahrheitswerte)
#     list     ---  Listen
#     tuple    ---  Tupel
#     range    ---  Bereich
#     dict     ---  Dictionary (Wörterbuch, assoziative Zuordnung, zweispaltige Tabelle)
#     set      ---  Menge
# u.v.a.
#
# Wir werden sie bald alle erkunden.



# ======================================================================
# ======================================================================
# ======================================================================
#                             OPERATOREN
# ======================================================================
# ======================================================================
# ======================================================================

# Python-Operatoren sind Symbole, die wir verwenden, um
# Operationen auf Werte und Variablen anzuwenden.
# Wir können Operatoren nach der Art der Operationen unterteilen,
# die sie ausführen:
#
#           - Zuweisungsoperator
#           - arithmetische Operatoren
#           - Vergleichsoperatoren
#           - logische Operatoren
#           - bitweise Operatoren
#           - sowie einige interessante Operatoren in besonderen 
#             Kontexten wie - is - und  - in -


# ZUWEISUNGSOPERATOR
# ------------------

# Der Zuweisungsoperator wird verwendet, um einer Variablen einen Wert 
# zuzuweisen:

age = 8

# Oder um einen Variablenwert einer anderen Variablen zuzuweisen:

age = 8
anotherVariable = age

# Seit Python 3.8 wird der "Walross"-Operator := verwendet, um
# einer Variablen einen Wert zuzuweisen, wenn diese Zuweisung innerhalb
# einer anderen Operation enthalten ist. Zum Beispiel innerhalb eines 
# if oder im bedingten Teil einer Schleife. Mehr dazu später.


# ARITHMETISCHE OPERATOREN
# ------------------------

# Python hat eine Reihe von arithmetischen Operatoren: + , - ,
# * , / (Division), % (Modulo, Rest nach ganzzahliger Division), 
# ** (Potenzierung), // (ganzzahlige Division):

1 + 1         #2
2 - 1         #1
2 * 2         #4
4 / 2         #2.0
4 % 3         #1
4 ** 2        #16
3.9 // 2      #1.0

# Beachten Sie, dass Sie kein Leerzeichen zwischen den
# Operanden benutzen müssen, aber es ist gut für die Lesbarkeit.

# - funktioniert auch als unärer Minus-Operator:

print(-4)     #-4

# + wird auch zur Verkettung von String-Werten verwendet:

"Roger" + " is a good dog"     #Roger is a good dog

# Wir können den Zuweisungsoperator kombinieren mit
# arithmetischen Operatoren:

#         +=
#         -=
#         *=
#         /=
#         %=
#         ..und so weiter

# Beispiel:

age = 8
age += 1        # age hat jetzt den Wert 9


# VERGLEICHSOPERATOREN
# --------------------

# Python definiert ein paar Vergleichsoperatoren.

#         ==        Gleichheit
#         !=        Ungleichheit
#         >         Größer als
#         <         Kleiner als
#         >=        Größer gleich als
#         <=        Kleiner gleich als

# Sie können diese Operatoren verwenden, um einen booleschen Wert 
# zu erhalten ( True oder False ) je nach Ergebnis der logischen 
# Auswertung:

a = 1
b = 2

a == b    #False
a != b    #True
a > b     #False
a <= b    #True


# BOOLESCHE OPERATOREN
# --------------------

# Python stellt uns die folgenden booleschen Operatoren zur Verfügung:

#         not
#         and
#         or

# Bei der Arbeit mit logischen Ausdrücken, die True oder False sein
# können, funktionieren diese wie das logische UND, ODER und NICHT 
# und werden z.B. oft in der Auswertung von if-Ausdrücken verwendet:

condition1 = True
condition2 = False
not condition1                     #False
condition1 and condition2          #False
condition1 or condition2           #True

# Achten Sie aber auf eine mögliche Quelle von
# Verwirrungen in folgender Situation:
# Wenn or in einem Ausdruck verwendet wird, gibt es den Wert des
# ersten Operanden zurück, der kein "falsey" Wert ist. Andernfalls gibt 
# es den Wert des letzten Operanden zurück.

# "falsey" sind folgende Werte: False , 0 , '' , [] 

# Beispiele:

print(0 or 1)              ## 1
print(False or 'hey')      ## 'hey'
print('hi' or 'hey')       ## 'hi'
print([] or False)         ## 'False'
print(False or [])         ## '[]'

# Die Python-Dokumentation beschreibt es (für x or y) so: 
# Wenn x falsch ist, dann y, sonst x .

# and wertet das zweite Argument nur aus, wenn das erste
# wahr ist. Wenn also das erste Argument "falsey" ist ( False ,
# 0 , '' , [] ..), gibt es dieses Argument zurück. Ansonsten wird
# das zweite Argument ausgewertet, z.B.:

print(0 and 1)             ## 0
print(1 and 0)             ## 0
print(False and 'hey')     ## False
print('hi' and 'hey')      ## 'hey'
print([] and False )       ## []
print(False and [] )       ## False

# Die Python-Dokumentation beschreibt es (für and) so: 
# Wenn x falsch ist, dann x, sonst y .


# BITWEISE OPERATOREN
# -------------------

# Einige Operatoren werden verwendet, um mit Bits und Binärzahlen 
# zu arbeiten:

#         &           führt ein binäres UND aus
#         |           führt eine binäre ODER-Verknüpfung durch
#         ^           führt eine binäre XOR-Operation durch
#         ~           führt eine binäre NOT-Operation aus
#         <<          Linksschiebe-Operation
#         >>          Rechtsschiebe-Operation

# Bitweise Operatoren werden eher selten verwendet, aber sie sollen hier auch mal
# erwähnt zu werden, z.B.:

2 & 1     #ergibt 0   , denn 2 (dezimal) -> 10 (binär)
          #                  1 (dezimal) -> 01 (binär)
          #                  2 & 1:         00 (binär) -> 0 (dezimal)  


# is UND in
# ---------

# - is - wird auch Identitätsoperator genannt. Er wird verwendet, um
# zwei Objekte zu vergleichen und gibt True zurück, wenn beide das
# dasselbe Objekt sind. Mehr zu Objekten später.

a = "A"
b = a 
a is b        #True

# - in - wird auch Zugehörigkeitsoperator genannt. Er wird verwendet, um
# festzustellen, ob ein Wert in einer Liste oder einer anderen
# Sequenz enthalten ist. Mehr zu Listen und anderen Sequenzen später.

5 in [3,6,7,4,5,2,8]     #True


# DER TERNÄRE OPERATOR
# --------------------

# Mit dem ternären Operator in Python können Sie schnell eine Bedingung 
# definieren.
# Angenommen, Sie haben eine Funktion, die eine Variable age
# mit dem Wert 18 vergleicht und je nach Ergebnis True oder False
# zurückgibt, abhängig vom Ergebnis.
# Anstatt zu schreiben:

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# Können Sie es mit dem ternären Operator auf diese Weise realisieren:

def is_adult(age):
    return True if age > 18 else False

is_adult(11)        #False

# Zuerst bestimmen Sie das Ergebnis, wenn die Bedingung wahr ist, 
# dann werten Sie die Bedingung aus, dann bestimmen Sie das Ergebnis, 
# wenn die Bedingung falsch ist. Formal:
#     <result_if_true> if <condition> else <result_if_false>



# ======================================================================
# ======================================================================
# ======================================================================
#                       STRINGS (ZEICHENKETTEN)
# ======================================================================
# ======================================================================
# ======================================================================

# Eine Zeichenkette in Python ist eine Reihe von Zeichen, die in
# in einfachen Anführungszeichen oder doppelten Anführungszeichen
# eingeschlossen sind:

"Roger"
'Roger'

# Die beiden unterschiedlichen Schreibweisen für Strings sind etwa 
# dann nützlich, wenn einfache oder doppelte Hochkommata als Zeichen 
# in einem String enthalten sein sollen:

'Er sagt "Hallo"'
"Er sagt 'Hallo'"

# Sie können einer Variablen einen String-Wert zuweisen:

name = "Roger"

# Sie können zwei Zeichenketten mit dem + Operator verketten:

phrase = "Roger" + " is a good dog"

# Mit += können Sie eine Zeichenkette an eine andere Zeichenkette 
# anhängen:

name = "Roger"
name += " is a good dog"
print(name)                #Roger is a good dog

# Sie können eine Zahl in eine Zeichenkette konvertieren, indem Sie 
# den Klassenkonstruktor str verwenden:

str(8)       #"8"

# Dies ist notwendig, wenn man eine Zahl an eine Zeichenkette 
# hängen will:

print("Roger is " + str(8) + " years old")     #Roger is 8 years old

# Eine Zeichenkette kann mehrzeilig sein, wenn sie mit einer 
# speziellen Syntax definiert wird, bei der die Zeichenkette 
# in drei Anführungszeichen eingeschlossen wird:

print("""Roger is
 8
years old
""")

# Das geht aber auch mit einfachen Anführungszeichen:

print('''
Roger is
 8
years old
''')

# Eine Zeichenkette hat eine Reihe von eingebauten Methoden, wie z.B.:
#
#   isalpha()      um zu prüfen, ob eine Zeichenkette nur 
#                  Zeichen enthält und nicht leer ist.
#   isalnum()      um zu prüfen, ob eine Zeichenkette
#                  Zeichen oder Ziffern enthält und nicht leer ist.
#   isdecimal()    um zu prüfen, ob eine Zeichenkette Ziffern enthält
#                  und nicht leer ist.
#   lower()        um eine klein geschriebene Version einer Zeichenkette 
#                  zu erhalten.
#   islower()      prüft, ob eine Zeichenkette klein geschrieben ist.
#   upper()        um eine Version einer Zeichenkette in Großbuchstaben 
#                  zu erhalten.
#   isupper()      prüft, ob eine Zeichenkette in Großbuchstaben 
#                  geschrieben ist.
#   title()        um eine großgeschriebene Version einer Zeichenkette 
#                  zu erhalten.
#   startsswith()  um zu prüfen, ob die Zeichenkette mit einer
#                  bestimmten Teilzeichenfolge startet.
#   endswith()     um zu prüfen, ob die Zeichenkette mit einer
#                  bestimmten Teilzeichenfolge endet.
#   replace()      um einen Teil einer Zeichenkette zu ersetzen.
#   split()        um eine Zeichenkette an einem bestimmten Zeichen zu 
#                  trennen.
#   strip()        zum Entfernen von Leerzeichen aus einer Zeichenkette.
#   join()         zum Anhängen neuer Buchstaben an eine Zeichenkette.
#   find()         um die Position einer Teilzeichenkette zu finden.
# etc.

# Keine dieser Methoden verändert die ursprüngliche Zeichenkette. Sie
# geben stattdessen eine neue, modifizierte Zeichenkette zurück. 
# Zum Beispiel:

name = "Roger"
print(name.lower())        #"roger"
print(name)                #"Roger"

# Sie können einige globale Funktionen verwenden, um mit
# Strings zu arbeiten. Ich denke dabei insbesondere an len() , 
# die Ihnen die Länge einer Zeichenkette liefert:

name = "Roger"
print(len(name))           #5

# Mit dem in-Operator können Sie prüfen, ob eine Zeichenkette eine
# Teilzeichenfolge enthält:

name = "Roger"
print("ger" in name)       #True

# Escaping ist eine Möglichkeit, Sonderzeichen in eine
# Zeichenfolge hinzuzufügen.
# Wie fügen Sie zum Beispiel ein doppeltes Anführungszeichen in eine
# Zeichenfolge ein, die in doppelte Anführungszeichen eingeschlossen 
# ist?

name = "Roger"

# "Ro"Ger" wird nicht funktionieren, da Python denkt, dass die 
# Zeichenkette bei "Ro" endet. Der richtige Weg ist, das doppelte 
# Anführungszeichen innerhalb der Zeichenkette mit dem 
# Backslash-Zeichen einzuleiten (Escaping):

name = "Ro\"ger"

# Dies gilt auch für einfache Anführungszeichen \' , und für spezielle
# Formatierungszeichen wie \t für Tabulator, \n für neue Zeile
# und \\ für den Backslash.
# Bei einer Zeichenkette können Sie mit dem Index in eckigen Klammern 
# ein bestimmtes Element erhalten, beginnend mit 0:

name = "Roger"
name[0]              #'R'
name[1]              #'o'
name[2]              #'g'

# Wenn Sie eine negative Zahl verwenden, beginnt die Zählung am Ende:

name = "Roger"
name[-1]             #"r"

# Sie können auch einen Index-Bereich verwenden, um einen Teilstring 
# herauszuschneiden (Slicing):

name = "Roger"
name[0:2]            #"Ro"
name[:2]             #"Ro"       :2 bedeutet: vom Anfang bis Index 2 (exkl.)
name[2:]             #"ger       2: bedeutet: vom Index 2 bis zum Ende



# ======================================================================
# ======================================================================
# ======================================================================
#                       BOOLEANS (Boolesche Werte)
# ======================================================================
# ======================================================================
# ======================================================================

# Python besitzt den Typ bool, der zwei Werte haben kann: 
# True und False (großgeschrieben).

done = False
done = True

# Booleans sind besonders nützlich bei bedingten Kontrollstrukturen
# wie if-Anweisungen:

done = True
if done:
    # run some code here
    print("dies")
else:
    # run some other code
    print("das")

# Truthy und Falsy:
# -----------------
# Bei der Auswertung eines Wertes für True oder False, wenn der
# Wert kein bool ist, haben wir einige Regeln je nach dem Typ, 
# den wir prüfen:
#
#  - Zahlen sind immer True, außer für die Zahl 0
#  - Strings sind nur False, wenn sie leer sind
#  - Listen, Tupel, Sets, Dictionaries sind nur False, wenn sie leer sind.
# -----------------

# Man kann prüfen, ob ein Wert ein Boolescher Wert ist:

done = True
type(done) == bool        #True

# Oder mit isinstance() , wobei 2 Argumente übergeben werden: die
# Variable und die Klasse bool:

done = True
isinstance(done, bool)    #True

# Die globale Funktion any() ist auch sehr nützlich bei der
# Arbeit mit Booleschen Werten, da sie True zurückgibt, wenn einer der
# Werte der als Argument übergebenen Iterablen (z.B. eine Liste) True ist:

book_1_read = True
book_2_read = False
any([book_1_read, book_2_read])             #True

# Die globale Funktion all() verhält sich ähnlich. Sie gibt aber nur
# dann True zurück, wenn alle an sie übergebenen Werte True sind:

ingredients_purchased = True
meal_cooked = False
all([ingredients_purchased, meal_cooked])   #False



# ======================================================================
# ======================================================================
# ======================================================================
#                               ZAHLEN
# ======================================================================
# ======================================================================
# ======================================================================

# Zahlen kommen in Python in 3 Typen vor: int , float und complex .


# INTEGER ZAHLEN
# --------------

# Ganzzahlige (integer) Zahlen werden mit der int Klasse dargestellt. 
# Sie können eine Ganzzahl über ein Werteliteral definieren:

age = 8

# Sie können eine Integer-Zahl auch mit dem int()-Konstruktor erzeugen:

age = int(8)

# Um zu prüfen, ob eine Variable vom Typ int ist, können Sie die 
# globale Funktion type() verwenden:

type(age) == int         #True


# FLIESSKOMMA (FLOATING POINT) ZAHLEN
# -----------------------------------

# Fließkommazahlen (Brüche) sind vom Typ float .
# Sie können ein float über ein Werteliteral definieren:

fraction = 0.1

# Oder mit dem Konstruktor float():

fraction = float(0.1)

# Um zu prüfen, ob eine Variable vom Typ float ist, können Sie
# die globale Funktion type() verwenden:

type(fraction) == float   #True


# KOMPLEXE ZAHLEN
# ---------------

# Komplexe Zahlen sind vom Typ complex .
# Sie können sie über ein Werteliteral definieren:

complexNumber = 2+3j

# oder mit dem Konstruktor complex():

complexNumber = complex(2, 3)

# Sobald Sie eine komplexe Zahl haben, können Sie ihren Real-
# und Imaginärteil bestimmen:

complexNumber.real         #2.0
complexNumber.imag         #3.0

# Um wiederum zu prüfen, ob eine Variable vom Typ komplex ist,
# können Sie die globale Funktion type() verwenden:

type(complexNumber) == complex        #True


# ARITHMETISCHE OPERATIONEN MIT ZAHLEN
# ------------------------------------

# Sie können arithmetische Operationen mit Zahlen durchführen
# mit Hilfe der arithmetischen Operatoren: + , - , * , / (Division), 
# % (Modulo, Rest nach ganzzahliger Division), ** (Potenzierung) 
# und // (Ganzzahlige Division):

1 + 1         #2
2 - 1         #1
2 * 2         #4
4 / 2         #2
4 % 3         #1
4 ** 2        #16
4.1 // 2      #2.0

# Das hatten wir weiter oben schon mal.

# Und Sie können die zusammengesetzten Zuweisungsoperatoren verwenden:

#          +=
#          -=
#          *=
#          /=
#          %=
# ..und so weiter
# um auch schnell Operationen auf Variablen durchzuführen:

age = 8
age += 1
print(age)            #9
age                   #9   (in IPython brauchen wir ja kein print)


# EINGEBAUTE (BUILT-IN) FUNKTIONEN FUER ZAHLEN
# --------------------------------------------

# Es gibt zwei eingebaute Funktionen, die im Umgang mit Zahlen helfen:
# abs() gibt den absoluten Wert einer Zahl zurück.
# round() gibt bei einer Zahl deren Wert gerundet auf
# die nächstliegende Ganzzahl:

round(0.12)          #0

# Sie können einen zweiten Parameter angeben, um die Genauigkeit 
# der Dezimalpunkte festzulegen:

round(0.12, 1)       #0.1

# Weitere mathematische Hilfsfunktionen und Konstanten werden
# von der Python-Standardbibliothek bereitgestellt:

# - Das math-Paket stellt allgemeine mathematische
#   Funktionen und Konstanten bereit.
# - Das cmath-Paket bietet Hilfsprogramme für die Arbeit mit
#   komplexen Zahlen.
# - Das decimal-Paket bietet Hilfsprogramme für die Arbeit
#   mit Dezimalzahlen und Fließkommazahlen.
# - Das Paket fractions enthält Hilfsprogramme für die Arbeit
#   mit rationalen Zahlen.

# Wir werden einige dieser Pakete später separat untersuchen.



# ======================================================================
# ======================================================================
# ======================================================================
#                              KONSTANTEN
# ======================================================================
# ======================================================================
# ======================================================================

# Python hat keine Möglichkeit, eine Variable dazu zu zwingen, eine
# Konstante zu sein.
# Am ehesten können Sie dafür ein Enum verwenden:

from enum import Enum
from typing import Iterable, Iterator

class Constants(Enum):
    WIDTH = 1024
    HEIGHT = 256

# Und zu jedem Wert gelangen Sie z. B. mit

Constants.WIDTH.value      #1024   

# Niemand kann diesen Wert nun neu zuweisen.

# Eine andere (viel einfachere) Möglichkeit bestünde darin, sich 
# einfach an Namenskonventionen zu halten: Deklarieren Sie Variablen, 
# die niemals geändert werden sollen, mit Großbuchstaben:

WIDTH = 1024


# Aber da dies nur eine Konvention ist, werden sie niemanden daran hindern, 
# diesen Wert zu überschreiben, und Python selbst wird es auch nicht verhindern.
# Aber genauso wird das Konstanten-Problem meistens umschifft -
# das ist nicht perfekt, aber pragmatisch.



# ======================================================================
# ======================================================================
# ======================================================================
#                              ENUMS
# ======================================================================
# ======================================================================
# ======================================================================

# Enums sind lesbare Namen, die an einen konstanten Wert gebunden sind.
# Um Enums zu verwenden, importieren Sie Enum aus dem enum
# Bibliotheksmodul:

from enum import Enum

# Dann können Sie ein neues Enum auf diese Weise initialisieren:

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# Sobald Sie dies getan haben, können Sie auf State.INACTIVE
# und State.ACTIVE referenzieren, und sie dienen als Konstanten.
# Wenn Sie nun z.B. versuchen, State.ACTIVE zu drucken:

print(State.ACTIVE)       #State.ACTIVE

# wird nicht 1 , sondern State.ACTIVE zurückgegeben.

# Der gleiche Wert kann durch die Nummer im Enum zugewiesen werden: 
# print(State(1)) liefert State.ACTIVE . Dasselbe gilt für die 
# Verwendung der Notation mit den eckigen Klammern: State['ACTIVE'] .
# Sie können jedoch den Wert mit State.ACTIVE.value erhalten:

print(State.ACTIVE.value)       #1

# Sie können alle möglichen Werte eines Enums auflisten:

list(State)                     #[<State.INACTIVE: 0>, <State.ACTIVE: 1>]

# Und Sie können die Werte zählen:

len(State)                      #2



# ======================================================================
# ======================================================================
# ======================================================================
#                              USER INPUT
# ======================================================================
# ======================================================================
# ======================================================================

# In einer Python-Kommandozeilenanwendung können Sie
# Informationen für den Benutzer mit der Funktion print() anzeigen:

name = "Roger"
print(name)

# Wir können auch Eingaben vom Benutzer akzeptieren, indem wir
# input() verwenden:

print('What is your age?')
age = input()    #Ein Dialogfenster erscheint, indem man was eingeben muss.
                 #In vscode/calva erscheint dieses Dialogfenster ganz oben
                 #in der Mitte - dort wo normalerweise die Kommandopalette 
                 #erscheinen würde.
print('Your age is ' + age)

# Damit erhält das Programm Eingaben zur Laufzeit, d.h. das
# Programm hält die Ausführung an und wartet, bis der Benutzer
# etwas eintippt und die Eingabetaste (return) drückt.
# Sie können auch eine komplexere Eingabeverarbeitung durchführen und
# und Eingaben zum Zeitpunkt des Programmaufrufs akzeptieren, und wir 
# werden später sehen, wie man das macht.

# So funktioniert es bei Kommandozeilenanwendungen. Andere Arten
# von Anwendungen benötigen eine andere Art der Eingabeannahme.



# ======================================================================
# ======================================================================
# ======================================================================
#                  STEUERANWEISUNGEN (CONTROL STATEMENTS)
# ======================================================================
# ======================================================================
# ======================================================================

# Das Interessante an Booleschen Ausdrücken, und Ausdrücken, die einen
# Booleschen Wert zurückgeben, ist insbesondere, dass wir Entscheidungen 
# treffen und verschiedene Wege einschlagen können abhängig vom Wert
# dieser Ausdrücke (True oder False).

# In Python tun wir dies mit der if-Anweisung:

condition = True

if condition == True:
    # do something
    print("hi")

# Wenn der Bedingungstest den Wert "True" ergibt, wie im
# obigen Fall, wird der Block ausgeführt.
# Was ist ein Block? Ein Block ist der Teil, der eine Ebene 
# (normalerweise 4 Leerzeichen) nach rechts eingerückt ist:
 
condition = True

if condition == True:
    print("The condition")
    print("was true")

# Der Block kann aus einer einzelnen Zeile, aber auch aus mehreren
# Zeilen gebildet werden, und er endet, wenn Sie zurück auf die
# vorherige Einrückungsebene gehen:

condition = True

if condition == True:
    print("The condition")
    print("was true")

print("Outside of the if")

# In Kombination mit if können Sie einen else-Block haben,
# der ausgeführt wird, wenn der Bedingungstest von if den Wert
# False hat:

condition = True

if condition == True:
    print("The condition")
    print("was True")
else:
    print("The condition")
    print("was False")

# Und Sie können verschiedene verknüpfte if-Prüfungen mit
# elif haben, die jeweils ausgeführt werden, wenn die vorherige 
# Prüfung False war:

condition = True
name = "Roger"

if condition == True:
    print("The condition")
    print("was True")
elif name == "Roger":
    print("Hello Roger")
else:
    print("The condition")
    print("was False")

# Der zweite Block wird in diesem Fall ausgeführt, wenn condition 
# False ist und name den Wert "Roger" hat.
# In einer if-Anweisung können Sie nur eine if- und
# else-Prüfung haben, aber mehrere elif-Prüfungen:

condition = True     #auch mal False ausprobieren!
name = "Roger"

if condition == True:
    print("The condition")
    print("was True")
elif name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio")
else:
    print("The condition")
    print("was False")

# if und else können auch in einem Inline-Format verwendet werden,
# wodurch wir einen Wert oder einen anderen Wert basierend auf einer
# Bedingung zurückgeben, z.B.:

a = 2
result = 2 if a == 0 else 3
print(result)                     #3



# ======================================================================
# ======================================================================
# ======================================================================
#                             LISTEN
# ======================================================================
# ======================================================================
# ======================================================================

# Listen sind eine wesentliche Datenstruktur in Python.
# Sie erlauben es Ihnen, mehrere Werte zu gruppieren und
# sie alle unter einem gemeinsamen Namen zu referenzieren.
# Zum Beispiel:

dogs = ["Roger", "Syd"]

# Eine Liste kann auch leer definiert werden:

items = []

# Eine Liste kann Werte verschiedener Typen enthalten:

items = ["Roger", 1, "Syd", True]

# Sie können mit dem in-Operator prüfen, ob ein Element in einer 
# Liste enthalten ist:

print("Roger" in items)           #True

# Sie können die Elemente in einer Liste über ihren Index referenzieren,
# beginnend bei Null:

items[0]              #"Roger"
items[1]              #1
items[3]              #True

# Mit der gleichen Notation können Sie den Wert ändern
# der an einem bestimmten Index gespeichert ist:

items[0] = "AnotherRoger"

# Sie können umgekehrt aber auch die Methode index() verwenden,
# um den Index zu einem bestimmten Wert herauszufinden:

items.index("AnotherRoger")        #0
items.index(1)                     #1
items.index("Syd")                 #2

# Wie bei Zeichenketten wird bei Verwendung eines negativen 
# Indexes die Suche vom Ende her begonnen:

items[-1]                 #True

# Sie können auch einen Teil einer Liste extrahieren, indem Sie 
# Slices verwenden:

items[0:2]                #["AnotherRoger", 1]
items[2:]                 #["Syd", True]

# Ermittelt die Anzahl der in einer Liste enthaltenen Elemente 
# mit der globalen Funktion len(), die wir auch für die Ermittlung der
# Länge einer Zeichenkette verwendet haben:

len(items)                #4

# Sie können der Liste Elemente hinzufügen, indem Sie append()
# verwenden:

items.append("Test")

# oder die Methode extend():

items.extend(["Test"])

# Sie können auch den Operator += verwenden:

items += ["Test"]

# items müsste jetzt so aussehen 
# ['Roger', 1, 'Syd', True, 'Test', 'Test', 'Test']

# Tipp: Vergessen Sie bei extend() oder += nicht die eckigen
# Klammern. Schreiben Sie nicht items += "Test" oder
# items.extend("Test"), sonst fügt Python 4
# einzelne Zeichen an die Liste an, was zu
# ['Roger', 1, 'Syd', True, 'T', 'e', 's', 't'] führen würde.

# Ein Element wird mit der Methode remove() entfernt:

items.remove("Test")

# Sie können mehrere Elemente hinzufügen, indem Sie folgendes
# schreiben:

items += ["Test1", "Test2"]

# oder sowas:

items.extend(["Test1", "Test2"])

# Diese fügen mehrere Elemente an das Ende der Liste an.

# Um ein Element in der Mitte einer Liste einzufügen, also an 
# einem bestimmten Index, verwenden Sie die Methode insert():

items.insert(2, "Test") 

# Und so (ungefähr) sieht unsere Liste nun aus:

items        #['AnotherRoger',
             # 1,
             # 'Test',        <---- das haben soeben eingefügt
             # 'Syd',
             # True, ...]

# Um mehrere Elemente an einem bestimmten Index hinzuzufügen, 
# müssen Sie Slices verwenden:

items[1:1] = ["Test1", "Test2"]

items            #['AnotherRoger',
                 # 'Test1',          <-- diese beiden haben
                 # 'Test2',          <-- wir eingefügt
                 # 1,
                 # 'Test',
                 # 'Syd',
                 # True, ...]

# Wir initialisieren die Liste nochmal neu:

items = ["abc", "Bde", "zhf", "Ueb"]

# Sortieren einer Liste mit der Methode sort():

items.sort()
print(items)        #['Bde', 'Ueb', 'abc', 'zhf']

# Tipp: sort() funktioniert nur, wenn die Liste Werte enthält, die
# verglichen werden können. Strings und Ganzzahlen zum Beispiel
# können nicht miteinander verglichen werden, und Sie erhalten dann
# den Fehler 
# TypeError: '<' not supported between instances of 'int' and 'str', 
# wenn Sie es trotzdem versuchen.

# Die sort()-Methode ordnet zuerst die Großbuchstaben,
# dann die Kleinbuchstaben. Um die Sortierregel zu ändern (z.B. alle
# unabhängig von der Schreibweise zu sortieren), kann man folgendes 
# machen:

items.sort(key=str.lower)
print(items)               #['abc', 'Bde', 'Ueb', 'zhf']

# Durch die Sortierung wird der ursprüngliche Listeninhalt verändert. 
# Um das zu vermeiden, können Sie den Listeninhalt zuerst kopieren
# und dann die Kopie sortieren:

items = ["Bde", "abc", "zhf", "Ueb"]
itemscopy = items[:]                 #Hier wird eine echte Kopie erzeugt
itemscopy.sort(key=str.lower)
print(itemscopy)
print(items)

# Oder Sie verwenden die globale Funktion sorted(),

print(sorted(items, key=str.lower))
print(items)

# die eine neue Liste (also eine Kopie) sortiert und zurückgibt, 
# anstatt die ursprüngliche Liste zu ändern.



# ======================================================================
# ======================================================================
# ======================================================================
#                             TUPEL
# ======================================================================
# ======================================================================
# ======================================================================

# Tupel sind eine weitere grundlegende Python-Datenstruktur.
# Mit ihnen können Sie unveränderliche Gruppen von Objekten erstellen.
# Das bedeutet, dass ein Tupel, sobald es erstellt wurde, nicht mehr
# geändert werden kann. Sie können keine Elemente hinzufügen oder entfernen.
# Tupel werden auf ähnliche Weise wie Listen erstellt, aber mit
# Klammern anstelle von eckigen Klammern:

names = ("Roger", "Syd")

# Ein Tupel ist geordnet, wie eine Liste, so dass Sie seine Werte 
# erhalten können, indem Sie einen Index angeben:

names[0]                      #"Roger"
names[1]                      #"Syd"

# Sie können auch die Methode index() verwenden, um den zu einem
# Wert gehörenden Index zu erhalten:

names.index('Roger')          #0
names.index('Syd')            #1

# Wie bei Strings und Listen wird bei Verwendung eines negativen 
# Index die Referenzierung vom Ende her ausgeführt:

names[-1]                     #"Syd"

# Sie können die Elemente in einem Tupel mit der Funktion len() 
# zählen:

len(names)                    #2

# Sie können mit dem in-Operator prüfen, ob ein Element in einem 
# Tupel enthalten ist:

print("Roger" in names)       #True

# Sie können auch einen Teil eines Tupels extrahieren, indem Sie 
# Slices verwenden:

names[0:2]                    #('Roger', 'Syd')
names[1:]                     #('Syd',)

# Sie können eine sortierte Version eines Tupels erzeugen, indem Sie 
# die globale Funktion sorted() verwenden:

names = ("Syd", "Roger", "Jerry")
print(sorted(names))
print(names)

# Sie können mit dem + Operator ein neues Tupel aus bestehenden 
# Tupeln erzeugen:

newTuple = names + ("Vanille", "Tina")
newTuple                            #anzeigen kann man das dann so..
print(newTuple)                     #..oder so



# ======================================================================
# ======================================================================
# ======================================================================
#                             DICTIONARIES
# ======================================================================
# ======================================================================
# ======================================================================

# Dictionaries sind eine sehr wichtige Python-Datenstruktur.
# Während Listen es Ihnen ermöglichen, Sammlungen von Werten zu 
# erstellen, erlauben Dictionaries das Erstellen von Sammlungen 
# von Schlüssel/Werte-Paaren:

dog = { 'name': 'Roger' }

# Der Schlüssel kann ein beliebiger unveränderlicher (immutable) 
# Wert sein, wie eine Zeichenkette, eine Zahl oder ein Tupel. 
# Der Wert kann alles sein, was Sie wollen.

# Ein Dictionary kann mehrere Schlüssel/Wertpaare enthalten:

dog = { 'name': 'Roger', 'age': 8 }

# Sie können auf einzelne Schlüsselwerte mit dieser Notation 
# zugreifen:

dog['name']             #'Roger'
dog['age']              #8

# Mit der gleichen Notation können Sie den Wert ändern
# der an einem bestimmten Index gespeichert ist:

dog['name'] = 'Syd'
dog                     #{'name': 'Syd', 'age': 8}

# Und eine andere Möglichkeit ist die Verwendung der Methode 
# get(), die eine Option hat, um einen Standardwert hinzuzufügen:

dog.get('name')                    #'Roger'
dog.get('test', 'default')         #'default'

# Die Methode pop() ruft den Wert eines Schlüssels ab und
# löscht anschließend das Element aus dem Wörterbuch:

dog.pop('name')                    #'Syd'
dog                                #{'age': 8}

# Die Methode popitem() holt und entfernt das zuletzt in das 
# Dictionary eingefügte Schlüssel/Wert-Paar:

dog.popitem()                      #('age', 8)
dog                                #{}          es ist nun leer!

# Sie können mit dem in-Operator prüfen, ob ein Schlüssel in einem 
# Dictionary enthalten ist:

'name' in dog                      #False

# Schlüssel von Dictionaries lassen sich mit der Funktion update mit 
# neuen Werten versehen. Als Argument wird dabei ein Dictionary erwartet,
# das die neuen Werte für die entsprechenden Schlüssel enthält:

roger = {'name': 'Roger', 'age': 8, 'type': 'dog', 'color': 'pink'}
neu = {'name': 'Jerry', 'age': 12}
roger.update(neu)
roger                   #{'name': 'Jerry', 'age': 12, 'type': 'dog', 'color': 'pink'}

# Holen Sie eine Liste mit den Schlüsseln eines Dictionary mit der
# keys()-Methode und übergeben Sie das Ergebnis an den 
# list()-Konstruktor:

dog = { 'name': 'Roger', 'age': 8 }
list(dog.keys())                       #['name', 'age']

# Holen Sie die Werte mit der Methode values(), und die
# Schlüssel/Wertpaare als Tupel mit der Methode items():

print(list(dog.values()))          #['Roger', 8]
print(list(dog.items()))           #[('name', 'Roger'), ('age', 8)]

# Ermitteln der Länge eines Wörterbuchs mit der globalen 
# Funktion len(), dieselbe, mit der wir die Länge einer
# Zeichenkette oder einer Liste bestimmt haben:

len(dog)                       #2

# Sie können dem Dictionary ein neues Schlüssel/Wert-Paar 
# auf folgende Weise hinzufügen:

dog['favorite food'] = 'Meat'
print(dog)                      #   {'name': 'Roger', 
                                #    'age': 8, 
                                #    'favorite food': 'Meat'}

# Sie können mit der Anweisung del ein Schlüssel/Wert-Paar aus 
# einem Dictionary entfernen:

del dog['favorite food']
print(dog)                      #   {'name': 'Roger', 
                                #    'age': 8,}

# Um ein Dictionary zu kopieren, verwenden Sie die Methode 
# copy():

dogCopy = dog.copy()
print(dogCopy)                  #   {'name': 'Roger', 'age': 8}



# ======================================================================
# ======================================================================
# ======================================================================
#                             MENGEN (SETS)
# ======================================================================
# ======================================================================
# ======================================================================

# Mengen sind eine weitere wichtige Python-Datenstruktur.
# Man kann sagen, dass sie wie Tupel funktionieren, aber sie sind nicht
# geordnet, und sie sind veränderbar. 
# Oder wir können sagen, dass sie funktionieren wie Dictionaries, 
# aber sie haben keine Schlüssel.

# Sie haben auch eine unveränderliche Version, genannt frozenset.

# Sie können einen Set mit dieser Syntax erstellen:

names = {"Roger", "Syd"}

# Sets verhalten sich wie mathematische Mengen.
# Sie können zwei Sets schneiden (eine Schnittmenge bilden):

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
intersect = set1 & set2    
print(intersect)                #{'Roger'}

# Sie können eine Vereinigung (Union) von zwei Sets erstellen:

set1 = {"Roger", "Syd"}
set2 = {"Luna"}
union = set1 | set2
print(union)               #{'Syd', 'Luna', 'Roger'}

# Sie können die Differenz zwischen zweier Sets erhalten:

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
difference = set1 - set2
print(difference)              #{'Syd'}

# Sie können prüfen, ob eine Menge eine Obermenge einer anderen 
# ist (und natürlich auch, ob eine Menge eine Untermenge einer 
# anderen ist):

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
isSuperset = set1 > set2
print(isSuperset)              # True

# Sie können die Elemente in einer Menge mit der globalen Funktion 
# len() zählen:

names = {"Roger", "Syd"}
len(names)                     # 2

# Sie können eine Liste aus den Elementen in einer Menge erhalten, 
# indem Sie die Menge an den list()-Konstruktor übergeben:

names = {"Roger", "Syd"}
list(names)                    #['Syd', 'Roger']

# Sie können mit dem in-Operator prüfen, ob ein Element in einer 
# Menge enthalten ist:

print("Roger" in names)        #True



# ======================================================================
# ======================================================================
# ======================================================================
#                             BUILT-ins
# ======================================================================
# ======================================================================
# ======================================================================

# Man kann in jedem Programm (ohne explizites import) eine Reihe von fest-
# eingebauten (daher: built-ins) Funktionen bzw. Objekte aufrufen, die 
# bereits einen weiten Einsatzbereich abdecken. 
# Welche es gibt, findet man in der Doku:
#
#            https://docs.python.org/3/library/functions.html
#
# Man kann sich das aber auch direkt anzeigen lassen - seltsamerweise muss man
# dazu vorher aber builtins importieren: 

import builtins
dir(builtins)

# Es folgt eine kategorisierte Kurzvorstellung  ...

# Funktionen für den REPL
# -----------------------
# dir(modul)         z.B.: dir(str)
# help(modul)        z.B.: help(str)
# exit()             #Vorsicht: nicht auswerten
# quit()             #Vorsicht: nicht auswerten

# Umwandlungsfunktionen für Container
# -----------------------------------
# list(iterable),    z.B.: list([2**x for x in range(10)])
# tuple(iterable)
# dict(iterable)
# set(iterable)
# frozenset(iterable)

# Umwandlungsfunktionen für Zahlen und Zeichenketten in Zahlen
# ------------------------------------------------------------
# int
# float
# complex
# bool

# Umwandlungsfunktionen für Zahlen in Zeichenketten
# -------------------------------------------------
# str
# hex
# oct
# bin                 z.B.: bin(1) ergibt '0b1',   int(0b1)   ergibt 1

# Umwandlungsfunktionen für beliebige Objekte in Zeichenketten
# ------------------------------------------------------------
# str
# repr
# ascii
# chr
# ord
# format

# Funktionen, die Iterables oder Sequenzen erzeugen
# -------------------------------------------------
# range
# reversed

# Mathematische Funktionen
# ------------------------
# abs
# round
# pow
# divmod

# Mengen aggregieren, zusammenfassen
# ----------------------------------
# len(sequence)             z.B.: len('Python')
# sum(iterable, start=0)
# min(iterable)
# max(iterable)
# all(iterable)
# any(iterable)

# Daten transformieren
# --------------------
# map(function, iterable, ...)
# filter(function, iterable)
# zip(*iterables)

# Spezialfunktion unterschiedlicher Gebiete
# -----------------------------------------
# aiter
# bytearray
# bytes
# breakpoint
# callable
# classmethod
# compile
# delattr
# enumerate
# exec
# eval
# getattr
# globals
# hasattr
# hash
# input
# iter
# locals
# memoryview
# next
# object
# open
# print
# property
# setattr
# slice
# sorted
# staticmethod
# super
# vars
# __import__

# Funktionen für Typen-Infos
# --------------------------
# isinstance
# issubclass
# type



# ======================================================================
# ======================================================================
# ======================================================================
#                             FUNKTIONEN
# ======================================================================
# ======================================================================
# ======================================================================

# Wenn die Built-ins (oder Funktionen aus importierten Modulen) nicht 
# ausreichen, muss man eigene Funktionen zusammenbasteln.
# Mit einer Funktion können wir einen Satz von Anweisungen erstellen, 
# die wir bei Bedarf ausführen können.
# Funktionen sind in Python und in vielen anderen Programmiersprachen 
# von essentieller Bedeutung, um sinnvolle Programme zu zu erstellen, 
# denn sie erlauben es, ein Programm in in überschaubare Teile zu 
# zerlegen, sie fördern Lesbarkeit und die Wiederverwendung von Code.

# Hier ist eine Beispielfunktion namens hello, die Folgendes ausgibt
# "Hallo!":

def hello():
    print('Hello!')

# Dies ist die Funktionsdefinition. Es gibt einen Namen ( hello ) 
# und einen Körper, die Menge der Anweisungen, mit der Teil, der auf 
# den Doppelpunkt folgt und eine Ebene nach rechts eingerückt ist.

# Um diese Funktion auszuführen, müssen wir sie aufrufen. 
# Dies ist die Syntax um die Funktion aufzurufen:

hello()            #Hello!

# Wir können diese Funktion einmal oder mehrmals ausführen.
# Der Name der Funktion, hello, ist sehr wichtig. 
# Er sollte beschreibend sein, damit sich jeder, der sie aufruft, 
# vorstellen kann, was die Funktion tut.

# Eine Funktion kann einen oder mehrere Parameter annehmen:

def hello(name):
    print('Hello ' + name + '!')

# In diesem Fall rufen wir die Funktion auf und übergeben das Argument:

hello('Roger')     #Hello Roger!

# Als Parameter bezeichnen wir die Werte, die von der Funktion 
# innerhalb der Funktionsdefinition akzeptiert werden, und als
# Argumente die Werte, die wir an die Funktion übergeben, 
# wenn wir sie aufrufen. 
# Dieser Jargon sorgt regelmäßig für Verwirrung.

# Ein Argument kann einen Standardwert haben, der angewendet wird, wenn
# das Argument nicht angegeben wird:

def hello(name='my friend'):
    print('Hello ' + name + '!')

hello()                          #Hello my friend!

# Hier sehen Sie, wie wir mehrere Parameter akzeptieren können:

def hello(name, age):
    print('Hello ' + name + ', you are ' + str(age))

# In diesem Fall rufen wir die Funktion auf und übergeben einen 
# Satz von Argumenten:

hello('Roger', 8)                #Hello Roger, you are 8

# Parameter werden per Referenz übergeben. 
#
# Dabei müssen wir nun zwei Fälle unterscheiden, und zwar
# ob die übergebenen Werte unveränderlich (Fall a) oder veränderlich
# (Fall b) sind.
# Wir erinnern uns: alle Typen in Python sind Objekte, aber einige 
# von ihnen sind unveränderlich, z.B. Integer, Booleans, Floats, 
# Strings und Tupel.
 
# Fall a) - Referenz auf unveränderliches Objekt
# -------
# Das bedeutet, wenn unveränderliche Werte als Parameter übergeben 
# werden und der Wert dieser Parameter innerhalb der Funktion geändert
# wird, wird dieser neue Wert nicht außerhalb der Funktion
# erscheinen:

val = 1

def change_a(value):
    value += 2
    print(value)

change_a(val)           #3
print(val)              #1

# Fall b) - Referenz auf veränderliches Objekt
# -------
# Wenn Sie ein Objekt an eine Funktion übergeben, das nicht 
# unveränderlich ist, und Sie eine seiner Eigenschaften ändern, 
# wird die Änderung außen widergespiegelt:

youngpeople = {'Jim': 12, 'Anna': 14}

def change_b(student):
    new = {'Sam':20, 'Steve':21}
    student.update(new)
    print(student)

change_b(youngpeople) #{'Jim': 12, 'Anna': 14, 'Sam': 20, 'Steve': 21}
print(youngpeople)    #{'Jim': 12, 'Anna': 14, 'Sam': 20, 'Steve': 21}

# Eine Funktion kann einen Wert zurückgeben, indem sie die return
# Anweisung verwenden. Im folgenden Beispiel geben wir den
# Parameter name zurück:

def hello(name):
    print('Hello ' + name + '!')
    return "Ich bin " + name

ein_name = "Jerry"
hello(ein_name)       #Hello Jerry!       <- das kommt vom print
                      #'Ich bin Jerry'    <- das ist der return-Wert

# Wenn die Funktion auf die Return-Anweisung trifft, wird die
# Funktion beendet.

# Wir können den Ausdruck hinterm return weglassen, dann gibts
# natürlich keinen Return-Wert, sondern nur noch den Seiteneffekt
# vom print:

def hello(name):
    print('Hello ' + name + '!')
    return

ein_name = "Tom"
hello(ein_name)       #Hello Tom!       

# Und wenn wir nichts returnieren, können wir eigentlich auch
# das Return weglassen:

def hello(name):
    print('Hello ' + name + '!')

ein_name = "Speedy"
hello(ein_name)       #Hello Speedy!

# Wir können die Return-Anweisung innerhalb einer Bedingung haben,
# was ein möglicher Weg ist, eine Funktion zu beenden, wenn eine 
# Ausgangsbedingung nicht erfüllt ist:

def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')

hello("")        #
hello("Tom")     #Hello Tom!

# Wenn wir die Funktion aufrufen und einen Wert übergeben, 
# der zu False auswertet, wie z. B. eine leere Zeichenkette, 
# wird die Funktion abgebrochen bevor die print()-Anweisung 
# erreicht wird.

# Sie können mehrere Werte zurückgeben, indem Sie durch Kommata
# getrennte Ausdrücke im Return angeben:

def hello(name):
    print('Hello ' + name + '!')
    return name, 'Roger', 8

hello("Syd")         #('Syd', 'Roger', 8)

# In diesem Fall ist beim Aufruf von hello('Syd') der Rückgabewert 
# ein Tupel, das diese 3 Werte enthält: ('Syd', 'Roger', 8) 



# ======================================================================
# ======================================================================
# ======================================================================
#                             OBJEKTE
# ======================================================================
# ======================================================================
# ======================================================================

# Alles in Python ist ein Objekt.
# Sogar Werte von grundlegenden primitiven Typen (Integer, String,
# float...) sind Objekte. Listen sind Objekte, Tupel, Dictionaries, 
# alles.

# Objekte haben Attribute und Methoden, auf die man mit der Punktsyntax 
# zugreifen kann.

# Versuchen Sie zum Beispiel, eine neue Variable vom Typ int zu 
# definieren:

age = 8

# age hat nun Zugriff auf die Eigenschaften und Methoden
# die für alle int-Objekte definiert sind.

# Dazu gehört z. B. der Zugriff auf den Real- und
# Imaginärteil der Zahl:

print(age.real)           #8
print(age.imag)           #0

print(age.bit_length())   #4

# Die Methode bit_length() gibt die Anzahl der Bit zurück.

# Eine Variable, die einen Listenwert enthält, hat Zugriff auf einen 
# anderen Satz von entsprechenden spezifischen Methoden:

items = [1, 2]
items.append(3)
items.pop()

# Die Methoden sind abhängig vom Typ des Wertes, also des Objekts.

# Mit der von Python bereitgestellten globalen Funktion id() 
# können Sie den Speicherort eines bestimmten Objekts ermitteln:

id(age)                  #140723093710848 (oder so ähnlich)

# Ihr Speicherort wird natürlich anders lauten, ich zeige ihn hier 
# nur als Beispiel.

# Wenn Sie der Variablen einen anderen Wert zuweisen, ändert sich 
# ihre SpeicherAdresse, weil der Inhalt der Variablen durch einen 
# anderen Wert ersetzt wurde, der an einer anderen Stelle im 
# Speicher gespeichert ist:

age = 8
print(id(age))           #140717077571584

age = 9
print(id(age))           #140717077571616

# Wenn Sie aber das Objekt mit Hilfe seiner Methoden verändern, 
# bleibt die Speicheradresse die gleiche:

items = [1, 2]
print(id(items))         #1329573312064

items.append(3)
print(items)             #[1, 2, 3]

print(id(items))         #1329573312064

# Die Adresse ändert sich nur, wenn Sie einer Variablen einen 
# anderen Wert zuweisen.

# Einige Objekte sind veränderbar, andere sind unveränderbar. Das
# hängt von dem Objekt selbst ab. Wenn das Objekt Methoden anbietet, 
# um seinen Inhalt zu ändern, dann ist es veränderbar (mutable).
# Andernfalls ist es unveränderlich (immutable). 
# Die meisten Typen, die in Python definiert sind, sind unveränderlich. 
# Zum Beispiel ist ein int-Objekt (also eine Zahl) unveränderlich. 
# Es gibt keine Methoden, um seinen Wert zu ändern: eine 5 ist ein 5.

# Wenn Sie z.B. den Wert von age inkrementieren:

age = 8
id(age)                  #140717077571584

age = age + 1
id(age)                  #140717077571616

# und Sie mit id(age) prüfen, werden Sie feststellen, dass age
# auf eine andere Speicherstelle zeigt. Der ursprüngliche Wert, 
# also 8, hat sich nicht verändert. Wir haben aber auf einen anderen 
# Wert, also 9, umgeschaltet.



# ======================================================================
# ======================================================================
# ======================================================================
#                         SCHLEIFEN (LOOPS)
# ======================================================================
# ======================================================================
# ======================================================================

# Schleifen sind ein wesentlicher Bestandteil der Programmierung.

# In Python gibt es zwei Arten von Schleifen: while-Schleifen und
# for-Schleifen.


# WHILE-SCHLEIFEN
# ---------------

# while-Schleifen werden mit dem Schlüsselwort while definiert,
# und sie wiederholen ihren Block, bis die Bedingung als False 
# ausgewertet wird:

condition = True
counter = 0

while condition == True:              
    print("The condition is True")
    counter += 1
    print(counter)
    if counter == 20:
        print("The condition is False")
        condition = False

# Das Folgende ist eine Endlosschleife. Sie endet nie.
# Sie sollten sie daher besser nicht ausführen (auswerten).
# IPython kommt sonst ziemlich durcheinander und man muss den
# Prozess abschiessen. Das ist lästig:

condition = True

while condition == True:              #lieber nicht ausführen !!!!
    print("The condition is True")

# Lassen Sie uns die Schleife gleich nach der ersten Iteration 
# anhalten:

condition = True

while condition == True:
    print("The condition is True")
    condition = False

print("After the loop")

# In diesem Fall wird die erste Iteration ausgeführt, da die 
# Bedingung zu True ausgewertet wird, und bei der zweiten Iteration
# wird der Bedingungstest zu False ausgewertet, so dass die Steuerung
# zur nächsten Anweisung nach der Schleife übergeht. 

# Es ist üblich, einen Zähler zu haben, um die Iteration nach einer 
# bestimmten Anzahl von Zyklen zu stoppen (so ein Beispiel hatten wir 
# aber bereits am Anfang dieses Abschnitts kennengelernt):

count = 0

while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")


# FOR-SCHLEIFEN
# ---------------

# Mit for-Schleifen können wir Python anweisen, einen Block für eine 
# vorher festgelegte Anzahl von Widerholungen auszuführen, also im Voraus,
# und ohne die Notwendigkeit einer separaten Variablen und einer
# Bedingung, um ihren Wert zu überprüfen.

# Zum Beispiel können wir die Elemente in einer Liste iterieren:

items = [1, 2, 3, 4]

for item in items:
    print(item)            #1  2  3  4

# Oder Sie können eine bestimmte Anzahl von Wiederholungen iterieren, indem Sie
# die Funktion range() verwenden:

for item in range(4):
    print(item)            #0  1  2  3  

# range(4) erzeugt eine Sequenz, die bei 0 beginnt und
# 4 Elemente enthält: [0, 1, 2, 3] .

# Um den Index zu erhalten, können Sie die Sequenz an
# die Funktion enumerate() übergeben. Sie erzeugt ein Iterable-Objekt,
# das von der for-Schleife benutzt wird, um sukzessive die Elemente
# der Sequenz und ihre jeweiligen Indizes zu erhalten (diese stehen
# dann in den Variablen index und item):

items = [1, 2, 3, 4]

for index, item in enumerate(items):
    print(index, item)                #0 1
                                      #1 2
                                      #2 3
                                      #3 4
                                  #index item

# BREAK UND CONTINUE
# ------------------

# Sowohl while- als auch for-Schleifen können innerhalb des Blocks 
# unterbrochen werden, und zwar mit zwei speziellen Schlüsselwörtern: 
# break und continue .

# continue hält die aktuelle Iteration an und weist Python an, die 
# nächste Iteration auszuführen.

# break hält die Schleife ganz an und fährt mit der nächsten Anweisung 
# nach dem Schleifenende fort.

# Das erste Beispiel druckt 1 aus.
# Das zweite Beispiel gibt 1, 3, 4 aus.

items = [1, 2, 3, 4]

for item in items:
    if item == 2:
        break
    print(item)                 #1

for item in items:
    if item == 2:
        continue
    print(item)                 #1   3   4



# ======================================================================
# ======================================================================
# ======================================================================
#                           ITERATION
# ======================================================================
# ======================================================================
# ======================================================================


# Listen, Tupel, Dicts, Sets, Strings, Ranges etc. dienen jeweils unterschiedlichen 
# Zwecken. Sie haben aber eine wichtige Gemeinsamkeit: Sie können sie iterieren.
# Iteration bedeutet, die Elemente eines Container-Objekts nacheinander zu 
# verarbeiten. Objekte, die Sie iterieren können, werden als iterierbar
# (engl. iterable) bezeichnet.
# Die einfachste Form der Iteration haben wir oben bei den Schleifen
# kenngelernt. Intern verwenden Schleifen einen sog. Iterator.
# Diesen Ablauf kann man auch händisch veranschaulichen. Durch die
# Built-in Funktion iter() wird ein Iterator erzeugt. next() gibt den jeweils
# nächsten Wert aus und der Iterator rückt eine Stelle weiter.
# Wenn keine Werte mehr da sind, wird eine StopIteration-Ausnahme ausgelöst.
# Der iterator ist also nur für einen Durchlauf gut, alle weiteren Aufrufe
# von next() lösen eine StopIteration aus.

#Hinweis: die folgenden Anweisungen am besten nacheinander ausführen,
#         damit die Effekte deutlich werden:
numbers = [1, 2, 3]
iterator = iter(numbers)
iterator                    # <list_iterator at 0x1ac47845de0>
next(iterator)         #1
next(iterator)         #2
next(iterator)         #3
next(iterator)         #Traceback   StopIteration

# Normalerweise kommt man mit next() und iter() nicht direkt in Berührung,
# da Python diese Funktionen automatisch im Hintergrund beim Iterieren (z.B.
# in Schleifen) ausführt.

# Es gibt verschiedene Arten von Iteratoren:
#   -- Sequenzen   (sie führen etwas immer der Reihe nach aus)
#   -- Generatoren (sie erzeugen Dinge immer erst dann, wenn sie gebraucht werden.
#                  Man nennt dieses Prinzip auch "lazy evaluation", bzw. genauer
#                  ausgedrückt "lazy instantiation". Siehe dazu:
#                  https://en.wikipedia.org/wiki/Lazy_evaluation
#                  https://en.wikipedia.org/wiki/Lazy_initialization) 

# Die Sequenz-Typen kennen Sie bereits. Es handelt sich um Listen, Tupel, Strings, etc.
# Generatoren gibt es in verschiedenen Formen, und zwar als "Comprehension", als
# "Generator expressions" und als "Generator iterator".

# Einen wichtigen Generator kennen wir bereits, nämlich die range-Funktion:

range(10)          #range(0, 10)

# Das gibt also ein range-Objekt zurück:
type(range(10))
# Das ist nur ein Generator, den man erstmal zur Auswertung, also zur
# Erzeugung von Zahlen, zwingen muss; z.B. so:

list(range(10))    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Diesen Generator braucht man ständig, weil er sehr einfach Listen mit Zahlen erzeugen
# kann. range allein allerdings tut noch nichts. Erst der Aufruf von range im 
# list-Konstruktor iteriert und packt die Ergebnisse in eine Liste.
# Das ist also ein Beispiel für "lazy instantiation", bei dem wir die Iteration
# erzwingen. Üblicherweise verwendet man range in for-Schleifen.

# Die drei Generator-Formen (Comprehensions, Generator expressions, Generator iterator) 
# werden in den drei nun folgenden Abschnitten vorgestellt. Diese Generatoren 
# werden wir in folgenden Abschnitten in Beispielen auch noch genauer kennenlernen.



# ======================================================================
# ======================================================================
# ======================================================================
#                           COMPREHENSIONS
# ======================================================================
# ======================================================================
# ======================================================================


# Eine Comprehension hat immer folgende allg. Struktur:
# 
#       [  f(number)     for number in numbers    if number % 2 == 0   ]
#          ---------     ---------------------    ------------------
#            |                   |                      |
#            V                   V                      V
#        Projektion         Iteration               Selektion
#
# Projektion: beliebiger Ausdruck f mit der Iterations-Variablen als Argument
# Iteration: Erzeugung der Elemente/Werte, die die Iterationsvariable annehmen kann
# Selektion: Auswahl bestimmter Werte der Iterationsvariablen (optional !)


# LIST-COMPREHENSIONS
# -------------------

# Da wir nun Schleifen und (weiter oben) Listen kennengelernt haben,
# lernen wir jetzt ein sehr spezielles syntaktisches Konstrukt kennen, 
# mit dem man einfach und schnell beliebige Listen (also Daten) automatisch 
# erstellen kann - die list comprehension.

# List Comprehensions sind eine Möglichkeit, Listen auf eine sehr
# prägnante Art zu erstellen.

# Angenommen, Sie haben folgende Liste:

numbers = [1, 2, 3, 4, 5]

# Sie können eine neue Liste mit Hilfe einer List Comprehension erstellen,
# bestehend aus Zweier-Potenzen der Elemente obiger Liste:

numbers_power_2 = [n**2 for n in numbers if n<5]          
print(numbers_power_2)                                  #[1, 4, 9, 16]

# List Comprehensions verwenden eine Syntax, die manchmal den üblichen
# Schleifen-Konstrukten vorgezogen wird, da sie besser lesbar ist, 
# da die ganze Operation in eine einzige Zeile geschrieben werden kann.

# Das könne wir sogar noch kürzer, ohne zusätzliche Liste numbers, so schreiben:

numbers_power_2 = [n**2 for n in range(1,5)]          
print(numbers_power_2)                                  #[1, 4, 9, 16]

# Sehen wir zum Vergleich die Formulierung mit einer for-Schleife: 

numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
print(numbers_power_2)                                  #[1, 4, 9, 16, 25]

# Und schliesslich eine Lösungsvariante desselben Problems, nun aber
# mit map und einer lambda-Funktion (die werden zwar in einem eigenen 
# Abschnitt erst weiter unten erläutert, aber dieser Vorgriff passt
# hier thematisch):

numbers_power_2 = list(map(lambda n : n**2, numbers))
print(numbers_power_2)                                  #[1, 4, 9, 16, 25]


# DICTIONARY-COMPREHENSIONS
# -------------------------

# Gegeben sei dieses Dictionary:

lexicon_de_en = {'Auto': 'car', 'Wand': 'wall', 'Boden': 'floor',}

# Wir wollen nun eine Comprehension schreiben, die die Schlüssel-Wert-Paare
# vertauscht:

lexicon_en_de = {value:key for key, value in lexicon_de_en.items()}
lexicon_en_de

# Anderes Beispiel: wir haben hier die aktiven Karrierejahre (von, bis) von Rennpferden:

race_horses = {
    'Acatango': (1993, 2005),
    'Hoof Hearted': (1973, 1978),
    'Seabiscuit': (1933, 1947),
    'Anita Hanjab': (1951, 1969),
    'Oil Beef Hooked': (1989, 1997),
    'Ben Timover': (1974, 1986),
    'Secretariat': (1972, 1989),
    'Sea the Moon': (2014, 2020)
}

# Wir wollen die Karrieredauern derjenigen Rennpferde wissen, deren Karriere
# zwischen 1970 und 1980 begonnen hat:

horse_years = {
    name: end - start 
    for name, (start, end) in race_horses.items() 
    if 1970 <= start <= 1980
}

horse_years    #{'Hoof Hearted': 5, 'Ben Timover': 12, 'Secretariat': 17}


# SET-COMPREHENSIONS
# ------------------

# Gegeben sei diese Zahlenliste:

numbers = [8, 1, 10, 2, 4, 1, 4, 4, 10, 5]

elemente_kleinerAls5 = [i for i in numbers if i < 5]
elemente_kleinerAls5                                            #[1, 2, 4, 1, 4, 4]

# Wenn man statt der eckigen Klammern nun geschweifte Klammern verwendet,
# wird aus der Liste ein Set (also eine Menge). Und Mengen können nur
# unterschiedliche Elemente enthalten, d.h. Doppelungen werden rausgeschmissen:

unterschiedliche_elemente_kleinerAls5 = { i for i in numbers if i < 5}
unterschiedliche_elemente_kleinerAls5                           #{1, 2, 4}



# ======================================================================
# ======================================================================
# ======================================================================
#                           GENERATOR EXPRESSIONS
# ======================================================================
# ======================================================================
# ======================================================================


# Comprehensions (s.o.) sind praktisch und transformieren Daten mit wenig Code.
# Allerdings werden Comprehensions an Ort und Stelle (also sofort) ausgewertet
# und so entsteht im Speicher eine komplette neue Liste (bzw. Set, Dictionary).
# Für große Datenmengen ist das ineffizient, besonders wenn Sie die Daten
# aggregieren möchten, etwa um das größte Element zu finden oder eine
# Summe zu bilden.
# Dafür gibt es Generator Expressions. Diese nutzen die gleiche Syntax wie 
# Comprehensions, schreiben aber eben nicht alles in den Speicher,
# sondern iterieren die Elemente nach und nach. 
# Generatoren sind ja lazy. Sie erzeugen Daten nur dann, wenn sie danach
# gefragt werden.


generator = (i**i for i in range(100))     #Beachte: wir verwenden hier runde Klammern,
                                           #         um den Code-Block einzufassen,
                                           #         der den Generator einfaßt.
generator                                  #<generator object <genexpr> at 0x00000179F248FF40>
sum(generator)                             #Und hier ist die Aggregation.

# Normalerweise würde man das viel kürzer so schreiben:
# Das ist eine Generator Expression !
sum(i**i for i in range(100))     #371115746176445351701210713361941528546861949073514...
                                  #542015172437236580034634746971244943788132460150776...
                                  #779198800002366059871900041784732217539059306483834...
                                  #977865973576751345853385981719448969027641921


# Wenn man hingegen eckige Klammern verwendet, ist das eine
# List-Comprehension:

lc = [i**i for i in range(100)]
lc                                #hier wird eine Liste mit der stark wachsenden
                                  #Zahlenfolge erzeugt, und zwar nicht-lazy.

sum(lc)                           #371115746176445351701210713361941528546861949073514...
                                  #542015172437236580034634746971244943788132460150776...
                                  #779198800002366059871900041784732217539059306483834...
                                  #977865973576751345853385981719448969027641921

# Das entscheidende ist der reduzierte Speicherbedarf bei Verwendung einer
# Generator Expression im Vergleich mit einer List-Comprehension.
# Den Unterschied können wir messen:
import sys
sys.getsizeof(generator)       #104
sys.getsizeof(lc)              #920



# ======================================================================
# ======================================================================
# ======================================================================
#                           GENERATOR ITERATOR
# ======================================================================
# ======================================================================
# ======================================================================


# In Python gibt es eine Besonderheit, was Funktionen angeht. Im Normalfall
# wirken sie wie in anderen Programmiersprachen - sie finden oder berechnen
# irgendeinen Wert und geben ihn mit einer return-Anweisung an den Aufrufer
# zurück. Dadurch wird die Funktion beendet.
# Es gibt aber einen Trick, um das zu verhindern. Wenn Sie statt einer
# return-Anweisung das Schlüsselwort "yield" (engl. Ertrag abwerfen, Gewinn)
# verwenden, wird ein Ergebnis erzeugt, aber die Ausführung kann danach an 
# der gleichen Stelle fortgeführt werden. Dadurch ändert sich die Semantik
# des Codes grundlegend.

def one_value():
    return 1

def two_values():
    yield 1
    yield 2

one_value()              #1
two_values()             #<generator object two_values at 0x00000267C885D8C0>

for v in two_values():
    print(v)             # 1  2

list(two_values())       #[1, 2]

# Der Aufruf von two_values() macht etwas Seltsames: er erzeugt einen
# Generator iterator. Dadurch, dass in der Funktion das Schlüsselwort "yield"
# auftaucht, verarbeitet Python die Funktion komplett anders. Der Python-Interpreter
# behandelt sie als Generator, der einen Iterator zurückgibt, der nach und nach
# Werte generiert.
# Wenn der Interpreter eine yield-Anweisung erreicht, wird die Ausführung der
# Funktion angehalten. Beim nächsten Iterationsschritt wird danach weitergemacht -
# die Funktion erzeugt also beim Aufruf einen iterierbaren Zustandsautomaten.

def count(start = 1):
    while start < 1000:
        yield start
        start += 1

for i in count():
    print(i, end=' ')        #1 2 3 ... 999

# Die Funktion count definiert einen Generator, der bis zu einer Grenze 
# (hier: 1000) hochzählt. Die for-Schleife verwendet den durch den Generator 
# erzeugten Iterator und gibt die einzelnen Werte aus.

# Diese Prinzipien haben wir bereits im vorigen Abschnitt "Generator Expressions"
# kennengelernt. Aber dort ging es vornehmlich um Ausdrücke. Diese sind gut
# geeignet, wenn sie eine flache Menge von Daten transformieren möchten, 
# allerdings ist es schwierig, damit verschachtelte Strukturen zu verarbeiten.
# Da "Generator iterators" aber im Kern Funktionen sind, können sie sich selbst
# aufrufen und eigen sich darum für rekursive (also verschachtelte) Strukturen.

def flatten(tree):
    if isinstance(tree, list):
        for branch in tree:
            yield from flatten(branch)     #yield from     sind Schlüsselworte
    else:
        yield tree

tree = [
    1, [2, 3, 4, [5, 6]], [7, 8], 9
]

for value in flatten(tree):
    print(value, end=' ')             #1 2 3 4 5 6 7 8 9

# Der Generator "flatten" betrachtet die geschachtelte Liste "tree". Jedes Element
# darin wird geprüft. Ist es eine Liste, so taucht der Iterator in diese ein, 
# indem er "flatten" erneut aufruft (besser gesagt: mit yield from als Ergebnis erzeugt). 
# Ist das Element hingegen keine Liste, so wird es einfach zurückgegeben. Durch das 
# rekursive Eintauchen in die Datenstruktur wird ein neuer Iterator erzeugt, dessen 
# Elemente wieder iteriert zurückgegeben werden müssen. Daher wird hier das Sclüsselwort 
# yield verwendet.
# Im Ergebnis wird die geschachtelte Liste - wie der Name des Generators schon
# andeutet - geplättet.



# ======================================================================
# ======================================================================
# ======================================================================
#                             KLASSEN
# ======================================================================
# ======================================================================
# ======================================================================


# Zusätzlich zur Verwendung der von Python zur Verfügung gestellten 
# Typen, können wir eigene Klassen deklarieren. Klassen definieren komplexe,
# benutzer-definierte Typen. Zu diesen komplexen Typen gehören natürlich auch
# Werte - diese nennt man Objekte. Man sagt auch: aus Klassen können 
# Objekte instanziiert (erzeugt) werden. Daher nennt man Objekte auch Instanzen
# von Klassen - genauso wie die Zahl 11 eine Instanz des Typs der Integer-Zahlen
# ist. 
# Also:
# Ein Objekt ist eine Instanz einer Klasse. Eine Klasse ist der Typ
# eines Objekts.

# Wir definieren eine Klasse auf diese Weise:
# 
#          class <class_name>:
#                # implementation

# Definieren wir zum Beispiel eine Klasse Dog mit einer Methode:

class Dog: 
    def bark(self):
        print('WOF!')

# self als Parameter der Methode zeigt auf die aktuelle Objektinstanz, 
# und muss bei der Definition einer Methode immer als erster Parameter 
# angegeben werden.

# Wir erzeugen eine Instanz einer Klasse, also ein Objekt, mit dieser
# Syntax:

roger = Dog()
roger.bark()

# Jetzt ist roger ein neues Objekt vom Typ Dog.

# Wenn Sie nach seinem Typ fragen:

print(type(roger))

# erhalten Sie <class '__main__.Dog'> .

# Ein spezieller Typ von Methode, __init__(), wird als
# Konstruktor bezeichnet. Wir können ihn verwenden, um eine 
# oder mehrere Eigenschaften zu initialisieren, wenn wir ein neues 
# Objekt von dieser Klasse erzeugen:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('WOF!')

# Wir verwenden es auf diese Weise:

roger = Dog('Roger', 8)
print(roger.name)            #'Roger'
print(roger.age)             #8
roger.bark()                 #'WOF!'

# Lokale Variablen, die mit self beginnen (z.b. self.name), sind sog. 
# Instanzvariablen oder auch Datenfelder. Sie beschreiben die Eigenschaften 
# des Objekts, das aus der Klasse instanziiert wurde. Instanzvariablen oder 
# Instanzfelder werden im Konstruktor definiert. Jede Instanz hat ihre 
# eigenen Instanzfelder (roger.name).

# Eine wichtige Eigenschaft von Klassen ist die Vererbung.

# Wir können eine Klasse Animal mit einer Methode walk() erzeugen:

class Animal:
    def walk(self):
        print('Walking..')

# und die Klasse Dog kann von Animal erben:

class Dog(Animal):
    def bark(self):
        print('WOF!')

# Wenn Sie nun ein neues Objekt der Klasse Dog erzeugen, wird 
# die walk()-Methode verfügbar sein, da diese von Animal geerbt 
# wurde:

roger = Dog()
roger.walk()                 #'Walking..'
roger.bark()                 #'WOF!'



# ======================================================================
# ======================================================================
# ======================================================================
#                          POLYMORPHISMUS
# ======================================================================
# ======================================================================
# ======================================================================


# Polymorphismus verallgemeinert eine Funktionalität, so dass sie in  
# verschiedenen Typen in gleicher Weise verwendet kann, aber ihre Wirkung
# typenabhängig in unterschiedlicher Weise (also polymorph) entfaltet. 
# Das ist ein wichtiges Abstraktionskonzept in der objektorientierten 
# Programmierung.

# D.h. wir können die gleiche Methode in verschiedenen Klassen definieren:

class Dog:
    def eat(self):
        print('Eating dog food')

class Cat:
    def eat(self):
        print('Eating cat food')

# Dann können wir Objekte erzeugen und jeweils die eat()-Methoden aufrufen, 
# unabhängig davon, zu welcher Klasse das Objekt gehört, und wir werden 
# unterschiedliche Ergebnisse erhalten:

animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()

# Wir haben eine damit verallgemeinerte Schnittstelle gebaut und müssen 
# nun nicht wissen, ob ein Tier eine Katze oder ein Hund ist. Der Typ des 
# jeweiligen Objekts entscheidet selbst, welche Implementierung der 
# eat-Methode jeweils aufgerufen wird.



# ======================================================================
# ======================================================================
# ======================================================================
#                          OPERATOR OVERLOADING
# ======================================================================
# ======================================================================
# ======================================================================


# Das Überladen (overloading) von Operatoren ist eine fortgeschrittene 
# Technik, die wir verwenden können, um Objekte, die aus Klassen erzeugt
# werden, miteinander vergleichbar zu machen und dabei die üblichen 
# Python-Operatoren verwenden zu können.

# Nehmen wir eine Klasse Dog:

class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Wir können damit zwei Dog-Objekte erstellen:

roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

# Um diese beiden Hunde bzgl. ihres Alters zu vergleichen, müßte
# man folgendes schreiben:

if roger.age > syd.age:
    print("roger is older than syd")
else:
    print("syd is older than roger")

# Wir können die aber auch Operatorüberladung verwenden, um diese 
# zwei Objekte basierend auf der Eigenschaft age miteinander zu 
# vergleichen. Dazu muss die Dog-Klasse in folgender Weise modifiziert
# werden:

class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

# Und hier sind zwei andere Hunde, die mit Hilfe dieser neuen
# Dog-Klasse erzeugt werden:

goofy = Dog('Goofy', 10)
snoopy = Dog('Snoopy', 9)

# Wenn Sie nun versuchen, print(goofy > snoopy) auszuführen, 
# erhalten Sie das Ergebnis True:

print(goofy > snoopy)              #True

# Oder etwas ausführlicher:

if goofy > snoopy:
    print("goofy is older than snoopy")
else:
    print("snoopy is older than goofy")

# Auf die gleiche Weise, wie wir __gt__() definiert haben (das bedeutet
# größer als), können wir die folgenden Methoden definieren (überladen):

#               __eq__()  um auf Gleichheit zu prüfen ( == ).
#               __lt__()  um zu prüfen, ob ein Objekt als kleiner 
#                         betrachtet werden soll als ein anderes, und 
#                         zwar unter Verwendung des < Operators.
#               __le__()  für kleiner oder gleich ( <= )
#               __ge__()  für größer oder gleich ( >= )
#               __ne__()  für nicht gleich ( != )

# Und dann haben wir noch entsprechende Methoden für die arithmetischen
# Operationen:

#              __add__()      reagiert auf den + Operator
#              __sub__()      antwortet auf den - Operator
#              __mul__()      antwortet auf den * Operator
#              __truediv__()  antwortet auf den / Operator
#              __floordiv__() antwortet auf den // Operator
#              __mod__()      antwortet auf den % Operator
#              __pow__()      antwortet auf den ** Operator
#              __rshift__()   antwortet auf den >> Operator
#              __lshift__()   antwortet auf den << Operator
#              __and__()      antwortet auf den & Operator
#              __or__()       antwortet auf den | Operator
#              __xor__()      reagiert auf den ^ Operator

# Es gibt noch ein paar weitere Methoden, um mit anderen
# Operatoren zu arbeiten, aber Sie verstehen jetzt die Idee.

# Weil diese Methoden nie direkt aufgerufen werden, sondern ihr
# Aufruf im Hintergrund durch Operatoren und Built-Ins geschieht,
# nennt man sie auch 'Magic Methods'.



# ======================================================================
# ======================================================================
# ======================================================================
#                             MODULE
# ======================================================================
# ======================================================================
# ======================================================================


# Jede Python-Datei ist ein Modul.

# Sie können ein Modul aus anderen Dateien importieren, und das 
# ist die Basis für jedes Programm mittlerer Komplexität, da es
# eine sinnvolle Organisation und die Wiederverwendung von Code 
# fördert.

# In einem typischen Python-Programm dient eine Datei als
# Einstiegspunkt. Andere Python-Dateien sind Module und stellen
# Funktionen zur Verfügung, die wir aus diesen anderen Dateien aufrufen 
# können.

# Die Datei dog.py befindet sich im Projektverzeichnis. Sie enthält u.a.
# diesen Code:

def bark(): 
    print('WOF!')

# Wir können diese Funktion aus dog.py hier importieren, indem wir
# den Befehl import verwenden, und sobald wir das getan haben, 
# können wir auf die Funktion mit der Punktschreibweise dog.bark() 
# referenzieren:

import dog

dog.bark()                    #WOF!

# Das erinnert an das, was wir oben bzgl. Klassen, Instanzen, Methoden
# kennengelernt haben, aber mit folgendem wichtigen Unterschied:
# das Modul ist keine Klasse, sondern selbst bereits eine Instanz 
# (also ein Objekt !!) und zwar die einzige Instanz. 
# Deshalb benötigt die Funktion bark auch kein self als ersten Parameter. 
# Man nennt diese direkte Manipulation einer Objekts auch 'Prototypen-basierte' 
# Programmierung. 

# Statt des Modulnamens (als des Dateinamens) kann man auch ein alias
# einführen (z.B. als Abkürzung oder als Erläuterung):

import dog as d   #Abkürzung
d.bark()

import dog as einHund   #Erläuterung
einHund.bark()

# Ein wie auch immer geartetes Alias ist immer zu präferieren,
# da so etwaige Namenskollisionen mit anderen Funktionen vermieden
# werden können und der Leser weiß, woher die jeweilige Funktion
# stammt.

# Man kann das Importieren auch noch anders schreiben:
# dazu verwenden wir die from .. import-Syntax und rufen
# die Funktion bark direkt auf:

from dog import bark

bark()                        #WOF!

# Die erste Strategie erlaubt es uns, alles zu laden, was
# in einer Datei enthalten ist - also das ganze Modul.

# Die zweite Strategie lässt uns die Dinge auswählen, die wir 
# brauchen.

# Diese Module sind spezifisch für Ihr Programm - man wählt
# diejenigen aus, die man benötigt. D.h. die Module können aus ganz
# unterschiedlichen Quellen stammen und das Importieren 
# hängt von der Position der jeweiligen Datei im Dateisystem ab.


# if __name__ == '__main__':
# --------------------------

# Ein Modul muss nicht zwingend von einem anderen Programm mit import
# eingebunden werden. Es ist nach wie vor ein echtes Python-Programm
# und kann auch direkt aufgerufen werden. D.h. ein Modul kann so geschrieben 
# werden, dass es je nach Art des Aufrufers unterschiedlich reagiert - 
# direkt als Programm oder als Modul, das in einem anderen Programm verwendet
# wird.
# Python hat dazu eine besondere Systemvariable namens __name__ (geschrieben
# mit jeweils zwei Unterstrichen auf jeder Seite). Wird das Modul intern, also
# eben als Modul, eingebunden, dann hat diese Variable als Wert den Namen
# des Moduls (also den Namen der Datei). Wird das Modul hingegen direkt als 
# Python-Programm aufgerufen (also extern), dann hat diese Systemvariable 
# den Wert __main__. 
# Dieses Verhalten kann man nun im Code des Moduls in einer entsprechenden
# if-Anweisung ausnutzen, indem man hierin spezifiziert, was bei welcher
# Verwendungsart (extern  oder intern) geschehen soll.

# Wir fügen dazu als Beispiel dem Modul dog.py (im Projektverzeichnis) folgenden
# Code hinzu:

if __name__ == '__main__':
    bark()
    print('extern')
else:
    print('intern')

# Wenn wir nun das Modul dog.py im Editor laden und starten (vscode-Hauptmenü: 
# Run->Run without debugging, oder Kontextmenü der Datei im Editor und dort dann
# Run Python File in Terminal, oder Kontextmenü der Datei im Explorer von vscode
# und dort Run Python File in Terminal, oder im Editor-Menü oben rechts das 
# Dreiecks-Symbol anklicken) wird es als externes Programm ausgeführt und es 
# erscheint: "WOF! extern"

# Wenn wir das Modul nur importieren
from dog import bark
# erscheint "intern" (aber nur beim ersten Mal)


# Module aus anderen Verzeichnissen
# ---------------------------------

# Angenommen, Sie legen dog.py in einem lib-Unterordner ab.
# In diesem Ordner müssen Sie eine leere Datei namens
# __init__.py erzeugen. Damit teilen Sie Python mit, dass der Ordner
# Module enthält. Durch die Existenz der __init__.py Datei wird aus
# dem Unterverzeichnis lib ein sog. "package". 
# Beachte: __init__.py ist leer; es ist nur eine Markierung.

# Nun können Sie wählen ...
# ... Sie können dog (insgesamt) aus lib 
# importieren:

from lib import dog

dog.bark()                     #WOF!

# Für die weiteren Experimente muss man jetzt IPython/interactive window
# wieder abschiessen !!! Mit den nächsten Anweisungen wird dann ein frischer
# Interpreter gestartet.

# ... oder Sie können aus dem Modul dog in lib spezifisch die Funktion
# bark iportieren und diese dann referenzieren:

from lib.dog import bark

bark()                         #WOF! WOF!


# Aktuell geladenen Module und Suchpfad für Module
# ------------------------------------------------

# Um eine Liste der standardmäßig eingebauten Module zu erhalten, kann
# man folgendes ausführen:

import sys
sys.builtin_module_names

# Wo auf dem lokalen Rechner wird nach Modulen gesucht ? Wir wollen also 
# den Suchpfad sehen:

import sys
for dir in sys.path:
    print(dir)

# Welche Module sind aktuell geladen ?
dir()



# ======================================================================
# ======================================================================
# ======================================================================
#                             PAKETE
# ======================================================================
# ======================================================================
# ======================================================================


# Was macht man, wenn die Anzahl der Module wächst ? 
# Wir brauchen eine Ordnungsprinzip, um die Übersicht über unsere Module 
# nicht zu verlieren. Für diesen Fall hat Python das Paketkonzept (engl. packages)
# bereitgestellt. Damit können wir mehrere Module zu einem Paket "schnüren".

# Um ein Paket in Python zu erstellen, sind nur zwei Dinge zu tun: man erzeugt
# einen Unterordner in einem Verzeichnis, in dem Python Module sucht. In diesem
# neu erzeugten Ordner muss man nun eine Datei mit Namen __init__.py anlegen.
# Diese Datei kann leer sein oder Initialisierungscode enthalten, der beim
# Einbinden des Pakets einmalig ausgeführt wird.
# Pakete können außer Modulen auch weitere Unter-Pakete enthalten.

# Im Folgenden wollen wir das an einem einfachen Beispiel vorführen.
# Unser Paket soll simple_package heißen. Dazu erzeugen wir einen Ordner
# mit diesem Namen. In diesem Ordner legen wir eine leere Datei mit dem 
# Namen __init__.py an. 
# Außerdem legen wir noch zwei einfache Module in diesem neuen Verzeichnis
# an, und zwar a.py und b.py, die folgende Inhalte haben:

#--------
#__init__.py:
     #leer
#--------
#a.py:
def f1():
    print('f1 von Modul a')
#--------
#b.py:
def foo():
    print("foo von Modul b")
#--------

# Nun können wir unser Paket simple_package benutzen - beachte: die Paket-
# Initialisierungsdatei __init__.py ist leer

from simple_package import a, b

# und wir können die in den Modulen enthaltenen Funktionen
# aufrufen:

a.f1()       #f1 von Modul a
b.foo()      #foo von Modul b

# Für die weiteren Experimente muss man jetzt IPython/interactive window
# abschiessen !!! Mit den nächsten Anweisungen wird dann ein frischer
# Interpreter gestartet.

# Wenn man nun versucht, das Paket simple_package direkt zu importieren

import simple_package

# funktioniert das zwar anscheinend, aber wenn man nun die Funktionen
# der Module aufrufen will, kommt eine Fehlermeldung:

simple_package.a.f1()   #AttributeError: module 'simple_package' 
                        #                has no attribute 'a'

# Um diesem Fehler zu begegnen, kann man die Paket-Initialisierungsdatei
# __init__.py einsetzen. Wir können in diese bisher leere Datei folgendes
# schreiben

#--------NEU
#__init__.py:
from simple_package import a, b
#--------NEU

# Für die weiteren Experimente muss man jetzt IPython/interactive window
# wieder abschiessen !!! Mit den nächsten Anweisungen wird dann ein frischer
# Interpreter gestartet.

# Wir führen die import-Anweisung im frischen Interpreter erneut aus
import simple_package

# und jetzt können wir die Funktionen der importierten Module aufrufen:
simple_package.a.f1()   #f1 von Modul a
simple_package.b.foo()  #foo von Modul b

# Natürlich geht das auch von einem anderen Python-Skript aus, z.B.
#---------
#simple_package_test.py:
import simple_package as sp
sp.a.f1()
sp.b.foo()
#---------

# In diesem Skript haben wir zur Abwechslung dem importierten Paket
# den alias-Namen sp gegeben. Wenn wir dieses Skript als ganzes ausführen,
# also mit dem Run-Button starten, erscheint im Terminal folgendes:

#    f1 von Modul a
#    foo von Modul b



# ======================================================================
# ======================================================================
# ======================================================================
#                    DIE PYTHON STANDARD BIBLIOTHEK
# ======================================================================
# ======================================================================
# ======================================================================


# Python stellt eine Menge eingebauter Funktionalität durch seine
# Standardbibliothek zur Verfügung.

# Die Standardbibliothek ist eine riesige Sammlung von allen Arten von
# Infrastrukturen, die von mathematischen Hilfsprogrammen über Debugging 
# bis hin zur Erstellung grafischer Benutzeroberflächen reicht.

# Die vollständige Liste der Module der Standardbibliothek finden Sie hier: 
# https://docs.python.org/3/library/index.html

# Einige der wichtigen Module sind:
#
# - math für mathematische Hilfsprogramme
# - re für reguläre Ausdrücke
# - json für die Arbeit mit JSON
# - datetime für die Arbeit mit Datumsangaben
# - sqlite3 für die Verwendung von SQLite
# - os für Betriebssystem-Utilities
# - random für die Erzeugung von Zufallszahlen
# - statistics für Statistik-Utilities
# - requests für die Ausführung von HTTP-Netzwerkanfragen
# - http zum Erstellen von HTTP-Servern
# - urllib für die Verwaltung von URLs
# - etc. etc.

# Wir wollen uns jetzt mal ansehen, wie man ein Modul der Standard
# Bibliothek verwendet. Sie wissen bereits, wie Sie Module verwenden können, 
# die Sie selbst erstellt haben, indem Sie sie aus anderen Dateien im 
# Programmordner importieren.

# Nun, analog ist es mit Modulen, die von der Standardbibliothek
# bereitgestellt werden:

import math

math.sqrt(4)                 #2.0

# oder

from math import sqrt

sqrt(4)                      #2.0

# Wir werden uns weiter unten ausgewählte Module einzeln ansehen, 
# um zu verstehen, was wir mit ihnen machen können.



# ======================================================================
# ======================================================================
# ======================================================================
#                    DER PEP8 PYTHON STYLE GUIDE
# ======================================================================
# ======================================================================
# ======================================================================


# Wenn Sie Code schreiben, sollten Sie sich an die Konventionen der von 
# Ihnen verwendeten Programmiersprache halten.

# Wenn Sie von Anfang an die richtigen Namensgebungs-  und Formatierung-
# Konventionen lernen, wird es einfacher, den Code, der von anderen 
# geschrieben wurde, zu lesen, und für andere wird es leichter Ihren Code 
# zu lesen.

# Python definiert seine Konventionen im PEP8 Stil Leitfaden. PEP steht 
# für Python Enhancement Proposals und es ist der Ort, an dem alle Python
# Sprachverbesserungen und Diskussionen stattfinden.
# Es gibt eine Menge PEP-Vorschläge, alle verfügbar unter
# https://www.python.org/dev/peps/ 

# PEP8 ist einer der ersten, und einer der wichtigsten PEPs
# Er definiert die Formatierung und auch einige Regeln, wie man Python 
# auf eine "pythonische" Weise schreibt.

# Sie können den gesamten Inhalt hier nachlesen:
# https://www.python.org/dev/peps/pep-0008/ 
# aber hier ist eine kurze Zusammenfassung der wichtigsten Punkte, 
# mit denen Sie beginnen können:
#
# - Einrücken mit Leerzeichen, nicht mit Tabulatoren.
# - Verwenden Sie 4 Leerzeichen zum Einrücken.
# - Python-Dateien sind in UTF-8 kodiert.
# - Verwenden Sie maximal 80 Spalten für Ihren Code.
# - Schreiben Sie jede Anweisung in eine eigene Zeile.
# - Funktionen, Variablennamen und Dateinamen sind
#   Kleinbuchstaben, mit Unterstrichen zwischen den Wörtern
#   (snake_case).
# - Klassennamen werden großgeschrieben, einzelne Wörter darin werden
#   ebenfalls mit Großbuchstaben geschrieben (CamelCase).
# - Paketnamen werden kleingeschrieben und haben keine
#   Unterstriche zwischen den Wörtern.
# - Variablen, die sich nicht ändern sollen (Konstanten), werden
#   in Großbuchstaben geschrieben.
# - Variablennamen sollten aussagekräftig sein.
# - Fügen Sie nützliche Kommentare hinzu, aber vermeiden Sie 
#   offensichtliche (triviale) Kommentare.
# - Fügen Sie Leerzeichen um Operatoren ein.
# - Verwenden Sie keine unnötigen Leerzeichen.
# - Fügen Sie eine Leerzeile vor einer Funktion ein.
# - Fügen Sie eine Leerzeile zwischen Methoden in einer Klasse ein.
# - Innerhalb von Funktionen/Methoden können Leerzeilen verwendet werden
#   um zusammenhängende Codeblöcke zu trennen, um die Lesbarkeit
#   zu erhöhen.



# ======================================================================
# ======================================================================
# ======================================================================
#                             DEBUGGING
# ======================================================================
# ======================================================================
# ======================================================================


# Fehlersuche ist eine der besten Fähigkeiten, die Sie lernen können, 
# da sie Ihnen in vielen schwierigen Situationen helfen wird.

# Jede Sprache hat ihren Debugger. Python hat pdb , der in der 
# Standardbibliothek verfügbar ist. Es gibt eine Erweiterung dazu,
# nämlich ipdb, der IPython verwendet, um den Debugger noch interaktiver
# zu machen.

# Und auch jede Entwicklungsumgebung (IDE) bietet auf diesen Debuggern
# aufbauende, zusätzliche Infrastrukturen.
# Deshalb seien hier nur die Grundlagen des Debuggens (ohne die
# Spezifika der verwendeten IDE) dargestellt.

# Seit Python 3.7 (PEP 553 - https://www.python.org/dev/peps/pep-0553/)
# gibt es die eingebaute (built-in) Funktion breakpoint().
# Diese kann man im eigenen Quellcode einfügen - sie definiert einen
# Haltepunkt (Breakpoint) für den Debugger. Wenn der Programmlauf auf diese
# Funktion trifft, wechselt er automatisch in den interaktiven Debug-Modus
# entweder mit pdb oder mit ipdb (abhängig vom Environment).
# Und natürlich hat jede IDE ihre spezifische Debugging-Funktionalität.

# Hier ist mal ein kleines Beispiel, das in der Datei debug.py steht.
# Für die Vorstellung der debug-Funktionalität arbeiten wir nun 
# ausschliesslich mit dieser Datei. Alle weiteren Infos zum Debugging
# finden sie dort !!! 

def func(x):
    c = 3
    print(c+x)

a = 2
b = 3

if(a+b == 5):
    breakpoint()         #<----- hier ist der Haltepunkt, den wir
    print('sum is 5')    #       in unseren Code eingefügt haben.
    func(a+b)            #       Bei Bedarf kann man natürlich weitere
                         #       Haltepunkt einfügen.
func(100)


# Alle Infos zum Debugging finden Sie als Kommentare in der Datei debug.py !!
#                                                                 --------



# ======================================================================
# ======================================================================
# ======================================================================
#            GÜLTIGKEITSBEREICHE VON VARIABLEN (VARIABLE SCOPE), GLOBAL
# ======================================================================
# ======================================================================
# ======================================================================


# Wenn Sie eine Variable deklarieren, ist diese Variable sichtbar in
# Teilen Ihres Programms, je nachdem, wo Sie sie deklarieren.

# Wenn Sie sie außerhalb einer Funktion deklarieren, ist die Variable
# für jeden Code sichtbar, der nach der Deklaration ausgeführt wird,
# einschließlich innerhalb von Funktionen:

age = 8

def test():
    print(age)

print(age)             #8
test()                 #8

# Wir nennen dies (also: age) eine globale Variable.

# Wenn Sie eine Variable innerhalb einer Funktion definieren, ist diese 
# Variable eine lokale Variable, die nur innerhalb dieser Funktion sichtbar ist.
# Außerhalb der Funktion ist sie nicht erreichbar:

def test():
    age_neu = 8
    print(age_neu)

test()                 #8
print(age_neu)         #NameError: name 'age_neu' is not defined

# Es stellt sich aber die Frage, was passiert, wenn wir den Wert einer Variablen 
# innerhalb einer Funktion verändern. Wird dies eine Auswirkung auf eine globale Variable 
# haben ? Wir testen dies im  folgenden kleinen Beispiel:

def f(): 
    s = "I love London!"
    print(s) 

s = "I love Paris!" 
f()                     #I love London!
print(s)                #I love Paris!

# Nein ! Hat keinen Einfluss.

# Wie sieht es aber aus, wenn wir zuerst auf s mittels print zugreifen, in der Hoffnung 
# den globalen Wert zu erhalten, und dann s einen neuen Wert zuweisen? Indem wir s einen 
# Wert zuweisen können, machen wir s zu einer lokalen Variable. Dadurch gäbe es s 
# innerhalb des Funktionsrumpfes sowohl als globale als auch als lokale Variable. 
# Python lässt diese Mehrdeutigkeit nicht zu und es kommt zu einer Fehlermeldung, 
# wie wir im folgenden Beispiel sehen können:

def f(): 
   print(s)                #<--- und hier hoffen wir, das hier die globale Variable verwendet wird
   s = "I love London!"
   print(s)
 
s = "I love Paris!"        #<--- globale Variable
f()                        #UnboundLocalError: local variable 's' referenced before assignment

# Eine Variable kann nicht sowohl lokal als auch global innerhalb des gleichen Blocks, 
# hier der Funktionsrumpf, sein. Deswegen betrachtete Python s als eine lokale Variable 
# innerhalb des Rumpfes. Da nun auf diese lokale Variable zugegriffen wird, bevor sie 
# definiert worden ist, sie also noch keinen Wert erhalten hat, erfolgt die obige Fehlermeldung.

# Man kann jedoch auf globale Variablen "schreibend" innerhalb einer Funktion zugreifen. 
# Dazu muss man sie jedoch explizit mittels des Schlüsselwortes "global" als global 
# deklarieren. Wir können dies im folgenden Beispiel sehen:

def f():
    global s
    print(s)
    s = "Zur Zeit nicht, aber Berlin ist auch toll!"
    print(s)

s = "Gibt es einen Kurs in Paris?" 
f()
print(s)

#ergibt: Gibt es einen Kurs in Paris?
#        Zur Zeit nicht, aber Berlin ist auch toll!
#        Zur Zeit nicht, aber Berlin ist auch toll!



# ======================================================================
# ======================================================================
# ======================================================================
#            AKZEPTIEREN VON ARGUMENTEN AUS DER BEFEHLSZEILE
# ======================================================================
# ======================================================================
# ======================================================================


# Python bietet mehrere Möglichkeiten, Argumente zu behandeln, die beim 
# Programmaufruf von der Kommandozeile übergeben werden.

# Bislang haben Sie Programme entweder von einem REPL (in einer IDE) 
# aus gestartet, oder mit

#          python <filename>.py

# von der Befehlszeile (Command-Shell, Powershell, bash, zsh, etc.).
# Mit Anaconda und vscode(+Python-Plugin) kann man die Command-Shell mit 
# dem Anaconda-Prompt verwenden. Dazu muss man im Panel von vscode das 
# Terminal öffnen und dort dann den Anaconda-Prompt auswählen (via
# Pulldown-Menü des +-Button ganz rechts im Panel).

# Sie können zusätzliche Argumente und Optionen übergeben, wenn 
# folgendes tun:

#          python <filename>.py <argument1>
#          python <filename>.py <argument1> <argument2>

# Eine einfache Möglichkeit, diese Argumente zu behandeln, ist die 
# Verwendung des sys-Modul aus der Standardbibliothek.

# Sie können diese Kommandozeilen-Argumente im Python-Programm 
# aufgreifen, und zwar mittels der sys.argv Liste. 
# Um das auszuprobieren, erstellen wir eine neue Datei main1.py
# in unserem aktuellen Verzeichnis (natürlich ohne die Kommentare):

#          main1.py:
#          ---------
#          import sys
#          print(len(sys.argv))
#          print(sys.argv)

# Und wenn wir diese Datei in der Kommandozeile (also im Anaconda-Prompt) 
# aufrufen und dabei auch zwei Parameter (1 und 2) übergeben:

#           ...> python main1.py 1 2
#                3
#                ['main1.py', '1', '2']

# wird das Programm die Länge der Argumentliste und
# die Argumentliste selbst ausdrucken.

# Dies ist ein einfacher Weg, aber Sie müssen eine Menge Arbeit leisten.
# Sie müssen Argumente validieren, sicherstellen, dass ihr Typ korrekt 
# ist. Sie müssen eine Rückmeldung an die Benutzer ausgeben, wenn
# sie das Programm nicht korrekt verwenden.

# Python stellt ein weiteres Paket in der Standard-Bibliothek zur 
# Verfügung, das Ihnen hilft: argparse .

# Zuerst importieren Sie argparse und rufen argparse.ArgumentParser() 
# auf, wobei Sie die Beschreibung Ihres Programms angeben:

#         main2.py:
#         ---------
#         import argparse
#
#         parser = argparse.ArgumentParser(
#              description='This program prints the name of my program' 
#         )

# Dann fahren Sie fort, Argumente hinzuzufügen, die Sie akzeptieren. 
# Sie können eine Option so einstellen, dass sie einen bestimmten Satz 
# von Werten mit vorher festgelegten Auswahlmöglichkeiten hat:
# Zum Beispiel akzeptieren wir in diesem Programm eine -c Option, 
# um eine Farbe zu übergeben, etwa so: python main2.py -c red

#         main2.py:
#         ---------
#         import argparse
#       
#         parser = argparse.ArgumentParser(
#              description='This program prints a color HEX value')
#         parser.add_argument('-c', '--color', metavar='color', 
#                             choices=['red', 'black'])
#         args = parser.parse_args()
#         print(args.color)            

# Probieren wir das mal aus:

#           ...> python main2.py -c red
#           red
#
#           ...> python main2.py -c black
#           black
#
#           ...> python main2.py -c    
#           usage: main2.py [-h] [-c color]
#           main2.py: error: argument -c/--color: expected one argument
#
#           ...> python main2.py -c blue 
#           usage: main2.py [-h] [-c color]
#           main2.py: error: argument -c/--color: invalid choice: 'blue' 
#                                          (choose from 'red', 'black')

# Es gibt noch mehr Optionen, aber das sind die Grundlagen.

# Und es gibt Community-Pakete, die weitere Funktionalitäten bieten, z.B.
# https://click.palletsprojects.com/en/8.0.x/
# https://python-prompt-toolkit.readthedocs.io/en/master/index.html




# ======================================================================
# ======================================================================
# ======================================================================
#                        LAMBDA FUNKTIONEN
# ======================================================================
# ======================================================================
# ======================================================================


# Lambda-Funktionen (auch anonyme Funktionen genannt) sind kleine 
# Funktionen, die keinen Namen und nur einen Ausdruck als Körper haben.
# In Python werden sie mit dem Schlüsselwort lambda definiert:

#           lambda <arguments> : <expression>

# Der Körper muss ein einzelner Ausdruck sein, aber keine Anweisung.
# Dieser Unterschied ist wichtig. Ein Ausdruck gibt einen Wert zurück, 
# eine Anweisung nicht.

# Ein einfaches Beispiel für eine Lambda-Funktion ist eine Funktion, 
# die den Wert einer Zahl verdoppelt:

lambda num : num * 2        #<function __main__.<lambda>(num)>

# Lambda-Funktionen können mehrere Argumente akzeptieren:

lambda a, b : a * b         #<function __main__.<lambda>(a, b)>

# Lambda-Funktionen können nicht direkt aufgerufen werden, aber Sie
# können sie Variablen zuweisen:

multiply = lambda a, b : a * b
print(multiply(2, 2))                #4

# Der Nutzen von Lambda-Funktionen ergibt sich in Kombination
# mit anderen Python-Funktionen, zum Beispiel in Kombination mit map() , 
# filter() und reduce().

# Hier ist ein Beispiel für die Verwendung einer lambda-Funktion in einer
# map-Funktion:

result = list(map(lambda a, b : a * b, [1, 2, 3, 4], [10, 100, 1000, 10000]))
print(result)         #[10, 200, 3000, 40000]



# ======================================================================
# ======================================================================
# ======================================================================
#                            REKURSION
# ======================================================================
# ======================================================================
# ======================================================================


# Eine Funktion in Python kann sich selbst aufrufen. Das ist es, was
# Rekursion bedeutet. Rekursion kann in vielen Szenarien sehr nützlich sein.

# Die übliche Art, Rekursion zu erklären, ist die der Berechnung
# der Fakultät einer Zahl.

# Die Fakultät einer Zahl n (geschrieben: !n ) ist die Zahl n multipliziert
# mit n-1 , multipliziert mit n-2 ... und so weiter, bis 1 erreicht wird:

#               3! = 3 * 2 * 1 = 6
#               4! = 4 * 3 * 2 * 1 = 24
#               5! = 5 * 4 * 3 * 2 * 1 = 120

# Mit Hilfe der Rekursion können wir eine Funktion schreiben, die die 
# Fakultät einer beliebigen Zahl berechnet:

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))                  #6
print(factorial(4))                  #24
print(factorial(5))                  #120

# Wenn Sie innerhalb der Funktion factorial() statt factorial(n-1) nun
# factorial(n) aufrufen würden, würden Sie eine unendliche Rekursion 
# verursachen. Python hält standardmäßig Rekursionen bei 1000 Aufrufen an, 
# und wenn diese Grenze erreicht ist, erhalten Sie einen RecursionError.

# Rekursion ist an vielen Stellen hilfreich, da sie unseren Code 
# vereinfacht.



# ======================================================================
# ======================================================================
# ======================================================================
#                   VERSCHACHTELTE (NESTED) FUNKTIONEN, NONLOCAL
# ======================================================================
# ======================================================================
# ======================================================================


# Funktionen in Python können in andere Funktionen verschachtelt werden.
# Eine Funktion, die innerhalb einer Funktion definiert ist, ist nur 
# sichtbar innerhalb dieser äußeren Funktion.

# Dies ist nützlich, um Hilfsprogramme zu erstellen, die für eine
# Funktion nützlich sind, aber nicht außerhalb davon.

# Sie fragen sich vielleicht: Warum sollte ich diese Funktion "verstecken", 
# wenn sie keinen Schaden anrichtet?

# Erstens, weil es immer am besten ist, Funktionalität zu verstecken, 
# die lokal zu einer Funktion ist und außerhalb davon nicht nützlich ist.
# Zum anderen, weil wir Closures verwenden können (mehr dazu dazu später).

# Hier ist ein Beispiel:

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')         #I
                                           #am
                                           #going
                                           #to
                                           #buy
                                           #the
                                           #milk

# Wenn Sie auf eine in der äußeren Funktion definierte Variable aus 
# der inneren Funktion heraus zugreifen wollen, müssen Sie sie zuerst
# als "nonlocal" deklarieren:

def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()                        #1
count()                        #1
count()                        #1

# Dies ist besonders bei Funktionsabschlüssen (closures) nützlich, wie 
# wir gleich sehen werden.



# ======================================================================
# ======================================================================
# ======================================================================
#                      CLOSURES (FUNKTIONSABSCHLÜSSE)
# ======================================================================
# ======================================================================
# ======================================================================


# Wenn Sie eine verschachtelte Funktion aus einer Funktion zurückgeben, 
# hat diese verschachtelte Funktion Zugriff auf die Variablen, die in
# der äußeren Funktion definiert wurden, auch wenn die äußere Funktion 
# nicht mehr aktiv ist.

# Hier ist ein einfaches Beispiel:

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment_func = counter()
increment_func             #<function __main__.counter.<locals>.increment()>
increment_func()           #1
increment_func()           #2
increment_func()           #3

# Mit dem return-Statement geben wir die innere Funktion increment() 
# zurück und weisen der Variablen increment_func das zugehörige function 
# object <function __main__ counter.<locals>.increment()> zu.
 
# Durch Hinzufügen der runden Klammern hinter increment_func wird dieses
# function object aufgerufen - also angewandt (das nennt man: function application).
# Das Erstaunliche ist, dass diese Funktion immer noch Zugriff auf den 
# Zustand der Variablen count hat, auch wenn die Funktion counter(),
# in der sie erzeugt wurde, bereits beendet ist und wir uns nicht 
# mehr im Kontext von counter befinden.
# D.h.: das von counter() returnierte Funktionsobjekt, das wir mit der Variablen
# increment_func halten (bzw. an diese Variable gebunden haben), hat nun einen
# Zustand. Un dieser zustand ändert sich mit jedem weiteren applikativen Aufruf
# des Funktionsobjekts !!!
# Dieses unscheinbare Konzept hat viele Anwendungen und ist die Grundlage
# vieler höherer Programmierkonzepte, wie wir gleich sehen werden.



# ======================================================================
# ======================================================================
# ======================================================================
#                         DECORATORS
# ======================================================================
# ======================================================================
# ======================================================================


# Decorators sind eine Möglichkeit, das Verhalten einer Funktion zu 
# ändern bzw. zu erweitern, ohne die Funktion selbst ändern zu müssen.

# Dies wird als Metaprogrammierung bezeichnet.

# In Python ist alles ein Objekt, auch Funktionen sind Objekte. 
# Das bedeutet, dass Funktionen sowohl als Argumente herumgereicht, 
# als auch als Ergebnisse zurückgegeben werden können. 
# Wenn Sie das zum ersten Mal sehen, mag es zunächst seltsam 
# erscheinen:

def hello():
    print("Hello!")                                                                                     

hello                         #<function __main__.hello()>
hello()                       #Hello!  
message = hello           
message                       #<function __main__.hello()>
message()                     #Hello!   

# Rufen Sie das function object entweder als message() oder als hello() 
# auf (das ist die function application) und sie haben die gleiche Ausgabe. 
# Das liegt daran, dass sich die beiden Namen/Variablen (hello und message) 
# auf das gleiche function object beziehen.

# Eine Funktion F kann eine andere Funktion A als Argument erhalten (dieses 
# Argument ist die zu dekorierende Funktion) und dann diese "dekorierte" 
# Funktion A' mit oder ohne Erweiterung zurückgeben:
#
#         A   --->   F(A)   --->   A' 
#

def hello(func):
    def inner():
        print("Hello ", end="") 
        func()
    return inner         

def name():
    print("Alice")                                                                                          

name                           #<function __main__.name()>
name()                         #Alice      
hello(name)                    #<function __main__.hello.<locals>.inner()>
hello(name)()                  #Hello Alice                                                                  
decorated_fn = hello(name)    
decorated_fn                   #<function __main__.hello.<locals>.inner()>
decorated_fn()                 #Hello Alice

# Die hello-Funktion ist nun der Decorator.
# Ein Decorator ist eine Funktion, die eine Funktion als Argument (im 
# Beispiel: func) erwartet. Diese Funktion wird dann in eine innere Funktion 
# (im Beispiel: inner) eingehüllt, die die Aufgabe ausführt, die sie erledigen 
# soll (was auch immer das ist), und diese innere Funktion wird schliesslich 
# von der Decorator-Funktion zurückgegeben. 

# Das ist natürlich nichts anderes als eine Closure (siehe vorhergehender 
# Abschnitt), wobei func nun die Rolle der Variablen einnimmt, über die 
# abgeschlossen wird.

# Die Funktionsapplikation hello(name) erzeugt also basierend auf name ein
# neues function object. Und wenn wir dieses function object aufrufen
# wollen, müssen die runden Klammern am Ende noch einmal angefügt werden,
# um die function application der Funktion inner aufzurufen.

# Wir können natürlich auch einer neuen Variablen decorated_fn das
# von hello(name) erzeugte function object zuweisen und dann mit
# decorated_fn() applizieren. 

# Fassen wir das nochmal zusammen:
# In der Anweisung

decorated_fn = hello(name)

# wird die Funktion name von der Funktion hello dekoriert, d.h.:
# hello umhüllt name mit irgendwelchen Erweiterungen.

# Python kann die Verwendung von Dekoratoren mit dem @-Symbol vereinfachen.
# In Python gibt es speziell dafür "Syntaktischen Zucker", da Decorators 
# weit verbreitet sind und durch diese spezielle Syntax vereinfacht werden 
# sollen. Sie tun zwar genau das Gleiche wie oben, aber es ist so 
# leichter lesbar und der Code ist kürzer.

# HINWEIS:
# Ich habe das auch nochmal in eine "normale" .py-Datei gesteckt, die man 
# an den Python-Interpreter schicken kann (Run-Button in vscode) !!

# Dazu ein Beispiel:

# decorated1.py:
# -------------
def display(func):
    def inner():
        print("The current user is : ", end="")
        func()
    return inner

@display
def who():
    print("Alice")

if __name__ == "__main__":
    who()                    #The current user is : Alice
# -------------

# Diese Datei kann man starten (z.B. in vscode diese Datei im
# Editor laden und mit dem grünen Dreieck ganz oben rechts 
# ausführen) und erhält dann im Terminal als Ergebnis: 
# "The current user is : Alice"

# Wenn wir den obigen Code (decorated1.py) in vscode mit IPython 
# (Interactive Window) auswerten (bis auf den if __name__...-Teil)
# und who() aufrufen:

who()    #The current user is : Alice

# erhalten dasselbe.
# Wenn wir die konventionelle(!!!) Syntax 
# verwenden, also nicht die Decorator-Syntax (sugared syntax), müssen
# wir das so schreiben (vorher muss die Funktion who nochmal frisch
# definiert werden!):

display(who)()                  #The current user is : Alice
decorated_fn = display(who)      
decorated_fn()                  #The current user is : Alice

# Parameter können mit Dekoratoren verwendet werden. 
# Wenn Sie eine Funktion haben, die die Summe a + b ausgibt, 
# etwa so

def sumab(a,b):
    summed = a + b
    print(summed)

# können Sie sie in eine Decorator-Funktion einpacken.
# Das folgende Beispiel zeigt, wie man das macht - erstmal
# als eigene Datei decorated2.py, die ausgeführt werden kann:

# decorated2.py:
# -------------
def pretty_sumab(func):
    def inner(a,b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a,b)
    return inner

@pretty_sumab
def sumab(a,b):
    summed = a + b
    print(summed)                                                                                      

if __name__ == "__main__":
    sumab(5,3)                  #5 + 3 is 8
# -------------   

# Wenn wir den obigen Code von decorated2.py hier im interactive window 
# auswerten (bis auf den if __name__...-Teil) und dann sumab(5,3)
# aufrufen

sumab(5,3)          #5 + 3 is 8

# erhalten wir das gewünschte dekorierte Ergebnis.
# Und in konventioneller Schreibweise (vorher muss die Funktion sumab
# aber nochmal frisch definiert werden !):

pretty_sumab(sumab)(5,3)        #5 + 3 is 8

# Die Funktion sumab wird von der Funktion pretty_sumab 
# umschlossen.

# Dieser Aufruf

pretty_sumab(sumab)  #<function __main__.pretty_sumab.<locals>.inner(a, b)>

# returniert das function object von inner in pretty_sumab.
# In der function application erwartet es zwei Parameter. 

# Noch ein (etwas sinnvolleres) Beispiel:

# Ein Decorator kann verwendet werden, um zu messen, wie lange die 
# Ausführung einer Funktion dauert.

# Wenn Sie eine einfache Funktion definieren, die n Sekunden schläft, 

def myFunction(n):
    time.sleep(n)  

# dann können Sie messen, wie lange es dauert, indem Sie einfach 
# die Zeile @measure_time hinzufügen - erstmal als Datei, in der
# die @-Notation verwendet wird (Hinweis: *arg ist eine variable
# Argumentliste): 

# decorated3.py:
# --------------
import time  

def myFunction(n):
    time.sleep(n)  

def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time()-t) + " seconds to run")
        return res                                                                                                          
    return wrapper

@measure_time
def myFunction(n):
    time.sleep(n)

if __name__ == "__main__":
    myFunction(2)             #Function took 2.0018045902252197 seconds to run
# --------------

# Wenn wir den obigen Code von decorated3.py hier im interactive window 
# auswerten (bis auf den if __name__...-Teil) und dann myFunction(2)
# aufrufen

myFunction(2)                 #Function took 2.0078694820404053 seconds to run

# Und hier ist nochmal die konventionelle Schreibweise (vorher muss die 
# Funktion myFunction aber nochmal frisch definiert werden !):

measure_time(myFunction)(2)   #Function took 2.0047144889831543 seconds to run

# Dadurch wird die Zeit ausgegeben, die für die Ausführung der 
# Funktion myFunction() benötigt wurde. Das Elegante daran ist, 
# dass wir durch Hinzufügen einer Codezeile @measure_time jetzt 
# ganz einfach die Programmausführungszeit messen können. 



# ======================================================================
# ======================================================================
# ======================================================================
#                         DOCSTRINGS
# ======================================================================
# ======================================================================
# ======================================================================


# Dokumentation ist immens wichtig, nicht nur um anderen Leuten zu 
# vermitteln, was das Ziel einer Funktion/Klasse/Methode/Modul ist, 
# sondern auch für Sie selbst.

# Wenn Sie in 6 oder 12 Monaten auf Ihren Code zurückkommen, erinnern 
# Sie sich vielleicht nicht mehr an all das Wissen, das Sie damals 
# in Ihrem Kopf hatten. Und wenn Sie Ihren Code lesen und verstehen wollen, 
# was er eigentlich tut, wird das ohne Doku viel schwieriger sein.

# Kommentare sind eine Möglichkeit, in dieser Situation zu helfen:

# this is a comment

num = 1      #this is another comment

# Eine andere Möglichkeit ist die Verwendung von Docstrings.

# Die Nützlichkeit von docstrings besteht darin, dass sie nur auf 
# einfachen Konventionen beruhen und als solche dann automatisch 
# verarbeitet werden können: falls ein docstring vorkommt, muss er
# die erste Anweisung in einer Definition sein. Infolgedessen muss
# er auch wie jede Anweisung eingerückt sein.
# Ein docstring soll aus einem mehrzeiligen String (""" ... """)
# bestehen. Das wars schon - mehr Regeln gibts nicht.

# So definieren Sie einen docstring für eine Funktion:

def increment(n):
    """Increment a number"""
    return n + 1

# Wenn man z.B. in vscode mit der Maus über folgenden Aufruf schwebt,
# wird automatisch der docstring eingeblendet:

increment(4)

# Man kann den docstring aber auch mit dieser Anweisung anzeigen lassen:

increment.__doc__

# Und So definieren Sie einen Docstring für eine Klasse und eine
# Methode:

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
    def bark(self):
        """Let the dog bark"""
        print('WOF!')

# Dokumentieren Sie ein Modul, indem Sie am Dateianfang einen 
# Docstring platzieren. Für dog_neu.py würde das so aussehen:

# dog_neu.py:
# -----------
"""Dog module
This module does ... bla bla bla and provides bla bla bla ...
- Dog
...
"""
class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
    def bark(self):
        """Let the dog bark"""
        print('WOF!')
# -----------

# Docstrings können sich über mehrere Zeilen erstrecken: 

def increment(n):
    """Increment
    a number
    """
    return n + 1     

# Sie können die globale Funktion help() zum Abrufen der 
# Dokumentation für eine Klasse/Methode/Funktion/Modul verwenden,
# z.B.:

help(increment)   #Help on function increment in module __main__:
                  #
                  #increment(n)
                  #    Increment
                  #    a number

# Es gibt viele verschiedene Standards docstrings zu 
# formatieren. Hier ist ein sehr bekannter Standard:
# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

# Standards ermöglichen Tools Docstrings automatisch zu
# extrahieren und so Dokumentationen für Ihren Code zu erzeugen. 



# ======================================================================
# ======================================================================
# ======================================================================
#                         INTROSPECTION
# ======================================================================
# ======================================================================
# ======================================================================


# Funktionen, Variablen und Objekte können analysiert werden, indem
# Sie Introspektion einsetzen.

# Zuerst können wir mit der globalen Funktion help() die
# Dokumentation lesen, falls diese in Form von Docstrings bereit-
# gestellt wird.

# Dann können Sie print() verwenden, um Informationen über eine
# Funktion zu erhalten ...

def increment(n):
    return n + 1
    
print(increment)   #<function increment at 0x7f420e2973a0>

# oder über ein Objekt:

class Dog():
    def bark(self):
        print('WOF!')

roger = Dog()
print(roger)        #<__main__.Dog object at 0x7f42099d3340>

# Die Funktion type() gibt uns den Typ eines Objekts:

print(type(increment))     #<class 'function'>
print(type(roger))         #<class '__main__.Dog'>
print(type(1))             #<class 'int'>
print(type('test'))        #<class 'str'>

# Mit der globalen Funktion dir() können wir alle Methoden 
# und Attribute eines Objekts herausfinden:

print(dir(roger))          #['__class__', '__delattr__', 
                           # '__dict__', '__dir__', '__doc__', 
                           # '__eq__', '__format__', '__ge__', 
                           # '__getattribute__', '__gt__', 
                           # '__hash__', '__init__', 
                           # '__init_subclass__', '__le__', 
                           # '__lt__', '__module__', '__ne__', 
                           # '__new__', '__reduce__', 
                           # '__reduce_ex__', '__repr__', 
                           # '__setattr__', '__sizeof__', 
                           # '__str__', '__subclasshook__', 
                           # '__weakref__', 'bark']

# Die globale Funktion id() zeigt uns den Standort eines 
# beliebigen Objekts im Speicher: 

print(id(roger))           #140227518093024
print(id(1))               #140227521172384

# Es kann nützlich sein zu überprüfen, ob zwei Variablen auf 
# das gleiche Objekt verweisen.

# Das Modul inspect aus der Standard-Bibliothek bietet uns mehr
# Tools, um Informationen über Objekte zu erhalten, siehe:
# https://docs.python.org/3/library/inspect.html 



# ======================================================================
# ======================================================================
# ======================================================================
#                         ANNOTATIONS
# ======================================================================
# ======================================================================
# ======================================================================


# Python ist dynamisch typisiert. Wir müssen nicht den Typ einer 
# Variablen oder eines Funktionsparameters angeben, oder den 
# Rückgabewert einer Funktion.

# Aber mit Annotations können wir dies (optional) tun.

# Dies ist eine Funktion ohne Annotations: 

def increment(n):
    return n + 1

# Dies ist die gleiche Funktion mit Annotations:

def increment(n: int) -> int:
    return n + 1

# Sie können auch Variablen mit Annotationen versehen:

count: int = 0

# Python ignoriert diese Annotationen. Ein separates Werkzeug
# namens mypy (http://mypy-lang.org/) kann eigenständig 
# ausgeführt werden oder in eine IDE, wie z.B.  VSCode oder 
# PyCharm integriert werden, um automatisch auf statische 
# Typfehler zu prüfen, während Sie programmieren, und es hilft 
# Ihnen, Typfehler zu finden, noch bevor der Code ausgeführt 
# wird.

# Eine große Hilfe, besonders wenn Ihre Software wächst und 
# Sie Ihren Code refaktorisieren müssen.



# ======================================================================
# ======================================================================
# ======================================================================
#                         EXCEPTIONS (AUSNAHMEN)
# ======================================================================
# ======================================================================
# ======================================================================


# Es ist wichtig, eine Möglichkeit zu haben, Fehler zu behandeln.
# Python bietet uns dazu die sog. Ausnahmebehandlung (exception 
# handling).

# Wenn Sie Codezeilen in einen try-Block einpacken ...

#             try:
#               # some lines of code

# ... dann macht Python Sie darauf aufmerksam, wenn ein Fehler 
# auftritt, und Sie können feststellen, welche Art von Fehler 
# aufgetreten ist, indem Sie except-Blöcke verwenden:

#             try:
#                 # some lines of code
#             except <ERROR1>:
#                 # handler <ERROR1>
#             except <ERROR2>:
#                 # handler <ERROR2>

# Um alle Ausnahmen (exceptions) abzufangen, können Sie except 
# verwenden, ohne einen Fehlertyp anzugeben:

# Der else-Block wird ausgeführt, wenn keine Ausnahmen gefunden 
# wurden, und ein finally-Block lässt Sie eine Operation in 
# jedem Fall ausführen, unabhängig davon, ob ein Fehler 
# aufgetreten ist oder nicht:

#             try:
#                 # some lines of code
#             except <ERROR1>:
#                 # handler <ERROR1>
#             except <ERROR2>:
#                 # handler <ERROR2>
#             else:
#                 # no exceptions were raised, 
#                 # the code ran successfully
#             finally:
#                 # do something in any case

# Der spezifische Fehler, der evtl. auftreten wird, hängt von der
# Operation ab, die Sie durchführen.

# Wenn Sie z. B. eine Datei lesen, erhalten Sie möglicherweise 
# einen EOFError . Wenn Sie eine Zahl durch Null dividieren, 
# erhalten Sie einen ZeroDivisionError . Wenn Sie ein 
# Typumwandlungsproblem haben, erhalten Sie möglicherweise 
# einen TypeError.

# Probieren Sie mal diesen Code aus:

result = 2 / 0       #ZeroDivisionError: division by zero

# Das Programm wird mit dem Fehler "ZeroDivisionError" 
# abgebrochen und die Codezeilen nach dem Fehler werden nicht
# ausgeführt.

# Durch das Einfügen dieses Codes in einen try-Block kann ein
# etwaiger Fehler abgefangen und das Programm fortgesetzt werden:

try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1

print(result)                 #1

# Sie können auch in Ihrem eigenen Code Exceptions auslösen, 
# indem Sie die raise-Anweisung verwenden:

#        raise Exception('An error occurred!')

# Dies löst eine allgemeine Exception aus, die Sie in folgender
# Weise abfangen können:

try:
    raise Exception('An error occurred!')
except Exception as error:
    print(error)

# Sie können auch eine eigene Exception Klasse definieren,
# die von Exception erbt:

class DogNotFoundException(Exception):
    pass

# pass bedeutet: "Anweisung, die nichts macht". Wir müssen 
# irgendeine Anweisung haben, wenn wir eine Klasse (oder eine
# Funktion) definieren.
# Wenn einem erstmal nichts zur konkreten Implementierung einfällt, 
# kann man pass benutzen, damit Python nicht meckert. Später
# kann man dies dann durch irgendwas Sinnvolles ersetzen. 

# Aber für das, was wir hier im Kontext von Exceptions erläutern
# wollen, reicht diese leere Implementierung (mit pass) für
# die Klasse DogNotFoundException aus. 
# Nun können wir unsere neue Exception-Klasse verwenden:

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')



# ======================================================================
# ======================================================================
# ======================================================================
#                         DIE -WITH- ANWEISUNG
# ======================================================================
# ======================================================================
# ======================================================================


# Die with-Anweisung ist sehr hilfreich, um die Arbeit mit dem Exception 
# Handling zu vereinfachen.

# Wenn wir zum Beispiel mit Dateien arbeiten, müssen wir jedes Mal, 
# wenn wir eine Datei öffnen, daran denken, sie irgendwann wieder zu 
# schließen. Die "with"-Anweisung macht diesen Vorgang automatisch.

# Anstatt zu schreiben:

filename = 'test.txt'

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

# Können wir auch schreiben:

filename = 'test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)

# Mit anderen Worten, wir haben eine eingebaute implizite Exception-
# Behandlung, da with close() automatisch für uns aufruft, wenn die 
# Datei nicht mehr benötigt wird.

# Die with-Anweisung ist nicht nur bei der Arbeit mit Dateien hilfreich. 
# Das obige Beispiel soll nur seine prinzipiellen Fähigkeiten konkret 
# vorstellen.



# ======================================================================
# ======================================================================
# ======================================================================
#           INSTALLING 3rd PARTY PACKAGES USING PIP AND CONDA
# ======================================================================
# ======================================================================
# ======================================================================


# Die Python-Standardbibliothek enthält eine große Anzahl von Dienst-
# programmen, die unsere Bedürfnisse bei der Python-Entwicklung 
# vereinfachen. Aber nichts kann alle Wünsche befriedigen.

# Deshalb erstellen Einzelpersonen, wissenschaftl. Arbeitsgruppen, 
# Organisationen und Firmen Software-Pakete und stellen diese 
# als Open-Source-Software für die gesamte Gemeinschaft zur Verfügung.

# Diese Module sind alle an einem einzigen Ort gesammelt, dem
# Python Package Index, verfügbar unter https://pypi.org,
# und sie können mit pip auf Ihrem System installiert werden.

# Zum Zeitpunkt des Schreibens dieses Crash-Kurses (Mai 2022) 
# sind mehr als 2.700.000 Pakete frei verfügbar.

# Sie sollten pip bereits installiert haben, wenn Sie
# meinen Python-Installationsanweisungen gefolgt sind.

# Wenn sie mit Anaconda arbeiten, müssen sie pip evtl. erst noch 
# via conda im Anaconda-Prompt installieren. Bei mir sieht das so aus:
#
#        (base) PS C:\Users\thwng> conda install pip
#
# jetzt können Sie pip auch vom Anaconda-Prompt aus verwenden.

# Wenn sie mit der Anaconda-Distribution arbeiten, können Sie statt
# pip das Anaconda-Analogon conda verwenden. Aber Sie können
# pip auch in der Anaconda-Distribution verwenden.
# Installieren Sie ein beliebiges Paket mit dem Befehl pip install:

#            pip install <package>

# Oder, wenn Sie Probleme haben, können Sie es auch so aufrufen:

#            python -m pip install <package>

# Und sobald Sie das getan haben, wird es für alle Ihre Python
# Skripte zur Verfügung stehen, da die Pakete global installiert 
# werden. Der genaue Speicherort hängt von Ihrem Betriebssystem ab.

# Aktualisieren Sie ein Paket auf seine neueste Version mit:

#            pip install –U <package>

# Installieren Sie eine bestimmte Version eines Pakets mit:

#            pip install <package>==<version>

# Deinstallieren Sie ein Paket mit:

#            pip uninstall <package>

# Lassen Sie sich die Details eines installierten Pakets anzeigen, 
# einschließlich der Version, Dokumentations-Website und 
# Autoreninformationen:

#            pip show <package>

# All dies (und noch mehr) ist analog auch mit conda möglich.
# Die entsprechende Kommandos heißen dann eben:

#            conda install <package>
#            conda update <package>
#            etc.

# Siehe auch:
# https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html
# conda (und vieles andere) ist in der Anaconda-Distribution
# enthalten (siehe: https://www.anaconda.com/).

# ------
# Der folgende Text stammt aus: 
# https://www.anaconda.com/blog/understanding-conda-and-pip

# Was ist der Unterschied zwischen pip und conda ?

# conda und pip werden oft als nahezu identisch angesehen. Obwohl sich 
# einige der Funktionen dieser beiden Werkzeuge überschneiden, wurden 
# sie für unterschiedliche Zwecke entwickelt und sollten auch für 
# unterschiedliche Zwecke verwendet werden. Pip ist das von der 
# Python Packaging Authority empfohlene Werkzeug für die Installation 
# von Paketen aus dem Python Package Index, PyPI (https://pypi.org/). 
# Pip installiert Python-Software, die als Wheels oder Quelldistributionen 
# verpackt ist. Letztere erfordern möglicherweise, dass auf dem System 
# kompatible Compiler und möglicherweise Bibliotheken installiert sind, 
# bevor pip erfolgreich aufgerufen werden kann.
# conda (https://conda.io/en/latest/) ist ein plattformübergreifender 
# package und Environment manager, der Conda-Pakete sowohl aus dem Anaconda-
# Repository (https://repo.anaconda.com/) als auch aus der Anaconda-Cloud 
# (https://anaconda.org/) installiert und verwaltet. 
# conda-Pakete sind Binärdateien. Es besteht nie die Notwendigkeit, Compiler 
# zur Verfügung zu haben, um sie zu installieren. Außerdem sind Conda-Pakete 
# nicht auf Python-Software beschränkt. Sie können auch C- oder C++-
# Bibliotheken, R-Pakete oder jede andere Software enthalten.
# Dies verdeutlicht einen wesentlichen Unterschied zwischen conda und pip. 
# pip installiert nur Python-Pakete, während conda Pakete installiert, die 
# Software enthalten können, die in einer beliebigen Sprache geschrieben 
# wurde. Bevor pip verwendet werden kann, muss z. B. ein Python-Interpreter 
# über einen Systempaketmanager oder durch Herunterladen und Ausführen 
# eines Installationsprogramms installiert werden. conda hingegen kann 
# sowohl Python-Pakete als auch den Python-Interpreter direkt installieren.
#
# Ein weiterer wichtiger Unterschied zwischen den beiden Werkzeugen ist, 
# dass conda die Möglichkeit hat, isolierte Umgebungen (sog. environments) 
# zu erstellen, die verschiedene Versionen von Python und/oder den darin 
# installierten Paketen enthalten können. Dies kann bei der Arbeit mit 
# Data-Science-Tools sehr nützlich sein, da verschiedene Tools z.T. 
# widersprüchliche Anforderungen enthalten können, die verhindern, dass 
# sie alle in einer einzigen Umgebung installiert werden können. 
# Pip hingegen hat selbst keine eingebaute Unterstützung für Umgebungen, 
# sondern ist auf andere Werkzeuge wie 
#         virtualenv (https://virtualenv.pypa.io/en/latest/) oder 
#         venv (https://docs.python.org/3/library/venv.html) 
# angewiesen, um isolierte Umgebungen zu erstellen. Werkzeuge wie 
#         pipenv (https://pipenv.pypa.io/en/latest/), 
#         poetry (https://python-poetry.org/) und 
#         hatch (https://github.com/ofek/hatch)
# umhüllen pip und virtualenv, um eine einheitliche Methode 
# für die Arbeit mit diesen Umgebungen zu bieten.
#
# pip und conda unterscheiden sich auch darin, wie Abhängigkeits-
# beziehungen (dependencies) innerhalb einer Umgebung (environment) 
# erfüllt werden. Beim Installieren von Paketen installiert pip die 
# Abhängigkeiten in einer rekursiven, seriellen Schleife. Es wird 
# nicht darauf geachtet, dass die Abhängigkeiten aller Pakete 
# gleichzeitig erfüllt werden. Dies kann zu Umgebungen führen, die 
# auf subtile Weise kaputt sind, wenn Pakete, die früher in der 
# Reihenfolge installiert werden, inkompatible Abhängigkeitsversionen 
# im Vergleich zu Paketen haben, die später in der Reihenfolge 
# installiert werden. Im Gegensatz dazu verwendet conda einen sog. 
# SAT-Solver (satisfiability solver), um zu überprüfen, ob alle 
# Anforderungen aller in einer Umgebung installierten Pakete erfüllt 
# sind. Diese Prüfung kann zusätzliche Zeit in Anspruch nehmen, 
# hilft aber, die Erstellung von fehlerhaften Umgebungen zu verhindern. 
# Solange die Paket-Metadaten über Abhängigkeiten korrekt sind, wird 
# conda vorhersehbar funktionierende Umgebungen erzeugen.
#
# Angesichts der Ähnlichkeiten zwischen conda und pip ist es nicht 
# überraschend, dass einige versuchen, diese Werkzeuge zu kombinieren, 
# um Data-Science-Umgebungen zu erstellen. Ein Hauptgrund für die 
# Kombination von pip mit conda ist, wenn ein oder mehrere Pakete nur 
# über pip zu installieren sind. Über 7.500 Pakete sind im Anaconda-
# Repository verfügbar, darunter die beliebtesten Data-Science-, 
# Machine-Learning- und KI-Frameworks. Diese, zusammen mit Tausenden 
# von zusätzlichen Paketen, die auf der Anaconda-Cloud aus Kanälen 
# wie        conda-forge (https://conda-forge.org/) 
# und        bioconda (https://bioconda.github.io/)
# verfügbar sind, können mit conda installiert werden. Trotz dieser 
# relativ großen Sammlung von Paketen ist sie immer noch sehr klein 
# im Vergleich zu den über 2.700.000 Paketen, die auf PyPI verfügbar 
# sind. 
# Gelegentlich wird ein Paket benötigt, das nicht als conda-Paket 
# verfügbar ist, aber auf PyPI vorhanden ist und mit pip installiert 
# werden kann. In diesen Fällen ist es sinnvoll, zu versuchen, 
# sowohl conda als auch pip zu verwenden.



# ======================================================================
# ======================================================================
# ======================================================================
#                   VIRTUAL ENVIRONMENTS (MIT VENV UND CONDA)
# ======================================================================
# ======================================================================
# ======================================================================


# Es ist üblich, dass Sie mehrere Python-Anwendungen auf Ihrem System 
# laufen haben.

# Wenn Anwendungen das gleiche Modul benötigen, kommt irgendwann die 
# knifflige Situation, dass eine Anwendung eine Version eines Moduls 
# benötigt, und eine andere Anwendung eine andere Version desselben 
# Moduls benötigt.

# Um dieses Dilemma zu lösen, verwenden Sie virtuelle Umgebungen 
# (environments). 
# Es gibt unterschiedliche Werkzeuge, um Environments zu erzeugen.
# Zwei diese Werkzeuge, venv und conda,  sollen jetzt vorgestellt werden.
# Um das auszuprobieren, verwenden wir ein neues Verzeichnis
# ...\testenvironments

# -------------------
# VENV - Environments
# -------------------

# Wir werden hier zuerst venv vorstellen: 
# https://docs.python.org/3/tutorial/venv.html
# Andere Werkzeuge arbeiten ähnlich, wie z.B. pipenv. 

# Wie im vorigen Abschnitt bereits erläutert,
# kann man auch conda einsetzen, um virtual environments zu erzeugen.
# Das sehen wir uns daher auch an.
 
# Wir haben z.B. ein Projekt, für das wir ein spezifisches,
# neues Environment benötigen. Ich nenne das Projektverzeichnis
# hier einfach mal "testvenv" im Verzeichnis "testenvironments".

# Zuerst gehen wir mit der Kommandozeile (im Falle von Anaconda:
# mit dem Anaconda-PowerShell prompt) in dieses Verzeichnis "testvenv", 
# in dem die Projekt liegen werden, für die das neue Environment gedacht
# ist:

#             cd ...\testvenv

# Dort erstellen wir dann eine virtuelle Umgebung in einem neuen 
# Unterverzeichnis, das wir .venv nennen:

#             python -m venv .venv

# Wir können das die virtuelle Umgebung enthaltende Unterverzeichnis
# natürlich beliebig benennen. Es ist alledings eine sinnvolle Konvention,
# dies als "verstecktes" Verzeichnis, also mit einem Punkt vorne, zu definieren,
# um deutlich zu machen, dass es sich um eine besondere Infrastruktur handelt
# und nicht um "normalen" Projektinhalt.

# Das Unterverzeichnis .venv wird jedenfalls automatisch erzeugt. 
# Darin gibt es ein Batch-Skript activate, das wir von der Kommandozeile
# (d.h. im Anaconda PowerShell Prompt) aus in folgender Weise aufrufen, 
# wobei wir weiterhin im Verzeichnis testvenv sind:

#             (base) PS ...\testvenv> .venv/Scripts/activate

# Dadurch ändert sich nun der Prompt in

#             (.venv) (base) PS ...\testvenv>

# Wenn wir pip jetzt ausführen, wird diese neue virtuelle Umgebung
# anstelle der globalen Umgebung (base) verwendet.
# Mit pip installierte Pakete (z.B. wenn man 

#              (.venv) (base) PS ...\testvenv> pip install matplotlib 

# ausführen würde) landen für dieses Environment .venv
# nun in ...\testvenv\.venv\Lib\site-packages

# Im Verzeichnis ...\testvenv\.venv\Scripts\ befinden sich weitere Tools.
# Um das Environment wieder zu deaktivieren, kann man einfach

#             (.venv) (base) PS ...\testvenv> deactivate

# ausführen. Dadurch sind wir wieder im ursprünglichen Environment base,
# was so auch im Prompt angezeigt wird:

#             (base) PS ...\testvenv>

# --------------------
# CONDA - Environments
# --------------------

# Dasselbe können wir natürlich auch mit conda machen.
# conda kann alles, was pip kann, und es kann dazu noch virtuelle
# Environments erzeugen (also das, was wir gerade mit venv 
# ausprobiert haben).

# Hier ist die offizielle Doku zu conda:
# https://docs.conda.io/projects/conda/en/latest/index.html
# https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html
# https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html      (*)
# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  (**)
# wobei (*) und insbesondere (**) detailliert auf virtuelle Environments eingehen.

# Aufgrund dieser Flexibilität und dieser Vielseitigkeit ist conda
# also ganz besonders gut geeignet für Leute, die sich mit Data Science, 
# Machine Learning und KI beschäftigen. Denn hier muss man sehr viele 
# unterschiedliche Spezialbibliotheken verwenden, die miteinander kombiniert 
# werden müssen und daher z.T. kiffligen wechselseitigen Abhängigkeiten 
# unterliegen:
#
#      -  conda erlaubt Ihnen, verschiedene Versionen desselben 
#         Pakets zu verwenden.
#      -  conda gibt Ihnen die Möglichkeit, jede Python-Version 
#         zu verwenden, die Sie wollen.
#      -  conda kompiliert Pakete vor der Veröffentlichung im 
#         Paket-Repository, damit Sie keine Compiler-Fehler 
#         erhalten.
#      -  u.v.a.
#
# conda kann das, weil es ein Paketmanager, aber auch ein 
# Umgebungsmanager ist. Es isoliert verschiedene Python und 
# Paketversionen, so dass sie sich nicht gegenseitig in die Quere kommen.

# Eine extrem konsequente Vorgehensweise könnte darin bestehen,
# JEDES Projekt mit einem EIGENEN Environment auszustatten. 
# Wir führen das hier mal exemplarisch in verschiedenen Projekten vor.

# Wir erzeugen ein neues, leeres Verzeichnis testcondaenv, 
# in dem dann später die Projekte liegen sollen:

#          ...\testenvironments\testcondaenv

# Alles, was jetzt kommt, könnten wir zwar von jedem beliebigen
# Verzeichnis aus tun, aber um die Geschichte nicht unnötig
# kompliziert zu machen, arbeiten wir mit der Anaconda-Kommandozeile 
# (also: Anaconda-PowerShell-Prompt) in diesem neuen Verzeichnis: 

#          (base) PS ... \testcondaenv>

# Am Prompt erkennen wir, dass wir aktuell im base-Environment sind,
# das standardmäßig bei der Installation der Anaconda-Distribution
# erzeugt worden ist.

# Zuerst prüfen wir mal, welche conda-Version wir aktuell benutzen:

#          (base) PS ... \testcondaenv> conda -V
#          conda 4.12.0

# Bei mir ist das die Version 4.12.0 (Stand: 9.5.2022).

# Und welche Pakete sind im base-Environment verfügbar ? Das können
# wir in folgender Weise anzeigen lassen:

#          (base) PS ... \testcondaenv> conda list

# Bei mir kommt dann folgende Auflistung (das wird bei Ihnen sicher 
# etwas anders aussehen):
#          # packages in environment at C:\Users\thwng\anaconda3:
#          #
#          # Name                    Version                   Build  Channel
#          # _anaconda_depends         2021.11                  py38_0
#          # _ipyw_jlab_nb_ext_conf    0.1.0                    py38_0
#          # alabaster                 0.7.12             pyhd3eb1b0_0
#          # anaconda                  custom                   py38_1          
# etc. etc. etc.

# Und wenn wir prüfen wollen, welche Conda-Environments wir bereits
# haben, kann man das so machen:

#          (base) PS ... \testcondaenv> conda env list

# Bei mir kommt dann diese Auflistung (wird bei Ihnen evtl. anders
# aussehen):
#          conda environments:
#          #
#          base                  *  C:\Users\thwng\anaconda3
#          py5coding                C:\Users\thwng\anaconda3\envs\py5coding
#
# Der Stern * zeigt an, in welchem Environment wir gerade sind.

# Nun wollen wir ein neues Conda-Environment erzeugen, das wir test_condaenv
# nennen wollen:

#          (base) PS ...\testcondaenv> conda create --name test_condaenv

# Conda meldet sich bei mir jetzt mit folgenden Infos:
#          Collecting package metadata (current_repodata.json): done
#          Solving environment: done
#
#          ## Package Plan ##
#
#          environment location: C:\Users\thwng\anaconda3\envs\test_condaenv
# Die nachfolgende Frage (Proceed ...) bejahen wir - und fertig.

# Im aktuellen Projektverzeichnis, in dem sich auch der Anaconda-PowerShell
# Prompt befindet, enthält nichts zu diesem neuen Environment.
# Es wird global von Conda verwaltet und (bei mir) hier gespeichert:
#    C:\Users\thwng\anaconda3\envs\test_condaenv
# Wenn man künftig mit diesem Environment arbeitet und etwaige
# Pakete installiert (z.B. mit conda install), werden diese hier
# Gespeichert.

# Wenn wir Conda jetzt nach der Liste aller Environments fragen

#          (base) PS ... \testcondaenv> conda env list

# sehen wir nun auch das neuerzeugte Environment in dieser Auflistung:
#          conda environments:
#          #
#          base                  *  C:\Users\thwng\anaconda3
#          py5coding                C:\Users\thwng\anaconda3\envs\py5coding
#          test_condaenv            C:\Users\thwng\anaconda3\envs\test_condaenv

# Um das neue Environment für die Arbeit im Anaconda-PowerShell-Prompt
# zu aktivieren, sagt man:

#          (base) PS ... \testcondaenv> conda activate test_condaenv

# Dadurch ändert sich der Prompt entsprechend:
#          (test_condaenv) PS ... \testcondaenv>

# Wenn wir in diesem aktivierten Environment nun danach fragen, welche
# Pakete hier verfügbar sind

#          (test_condaenv) PS ... \testcondaenv> conda list

# dann erhalten wir eine leere Liste:
#          # packages in environment at C:\Users\thwng\anaconda3\envs\test_condaenv:
#          #
#          # Name                    Version                   Build  Channel
# Das muss auch so sein, da wir für dieses Environment ja auch noch keine
# Pakete angefordert haben.

# Um das aktuelle Environment zu verlassen und wieder ins base-Environment
# zurückzukehren, sagt man einfach:

#          (test_condaenv) PS ...\testcondaenv> conda deactivate
# 
# Nun sind wir wieder im base-Environment:
#          (base) PS ... \testcondaenv>

# Es gibt natürlich noch viele weitere Varianten der Environment-Erzeugung
# mit Conda; z.B. kann man die gewünschte Python-Version und auch vorab
# zu installierende Pakete (inkl. Version-Spezifikation) angeben.
# Oder man kann eine YAML-Datei mit der Environment-Beschreibung dazu verwenden
# (siehe dazu: "The Python Workshop", Andrew Bird et al., S.379ff),
# oder man kann ein bereits existierendes Environment einfach klonen.
# All diese Infos findet man in der Quelle (**), s.o.

# Saving and Sharing Virtual Environments
# ---------------------------------------
# Die Environment-Erzeugung via YAML-Datei wollen wir uns aber mal
# konkret ansehen:
# Wir gehen mit dem anaconda-PowerShell-Prompt ins Verzeichnis \testenvironments ,
# so dass der Prompt nun so aussieht

#          (base) PS ...\testenvironments>

# Und offensichtlich sind wir mit dem Python-Interpreter aktuell im (base)-Environment.
# Wir wollen nun testweise ein neues Environment "example_env" erzeugen, 
# das numpy zur Verfügung stellt:

#          (base) PS ...\testenvironments> conda create -n example_env numpy

# Wir aktivieren dieses neue Environment

#          (base) PS ...\testenvironments> conda activate example_env

# was dann durch einen geänderten Prompt angezeigt wird

#          (example_env) PS ...\testenvironments> 

# Nun soll in diesem Environment auch pandas installiert werden

#          (example_env) PS ...\testenvironments> conda install pandas

# Wir können nun hier im PS-Prompt einen Python-Interpreter starten 

#          (example_env) PS ...\testenvironments> python

# Dass wir uns nun im Interpreter befinden, wird durch den Prompt >>> angezeigt.
# Hier können wir nun pandas un numpy importieren und mit exit() den Interpreter
# wieder verlassen:

#          >>> import pandas as pd
#          >>> import numpy as np
#          >>> exit()

# Das alles funktioniert also.
# Wir wollen nun eine YAML-Datei erzeugen, die die Inhalte des Environments
# beschreibt. Mit Hilfe dieser Datei können dann auch Dritte das Environment 
# erzeugen, ohne die entsprechenden Paket-Installationen im Detail selbst
# vornehmen zu müssen:

#          (example_env) PS ...\testenvironments> conda env export > example_env.yml

# Die Datei "example_env.yaml" befindet sich im Verzeichnis "testenvironments".
# Eine Liste aller Environments, die Sie bislang erzeugt haben, finden Sie
# in der Datei  C:\Users\thwng\.conda\environments.txt

# Um die obige YAML-Datei zu testen, verlassen wir nun das Environment und 
# löschen es danach sogar aus der conda-Infrastruktur:

#          (example_env) PS ...\testenvironments> conda deactivate

# Jetzt sind wir wieder im base-Environment und löschen example_env

#          (base) PS ...\testenvironments> conda env remove --name example_env

# Dass das Environment nun weg ist, können wir verfizieren, indem wir nochmal in
# C:\Users\thwng\.conda\environments.txt blicken. Dort erscheint example_env nun
# nicht mehr.
# Mit Hilfe der YAML-Datei "example_env.yml" können wir das Environment leicht
# wieder automatisiert erzeugen

#          (base) PS ...\testenvironments> conda env create -f example_env.yml

# Und es natürlich auch wieder aktivieren, um damit zu arbeiten:

#          (base) PS ...\testenvironments> conda activate example_env
#          (example_env) PS ...\testenvironments>

# Natürlich können virtuelle Environments für Python auch in IDEs
# genutzt werden. Exemplarisch sei dies im Folgenden für VSCODE 
# mit seinem offiziellen Python-Plugin besprochen ...

# ------------------------------------------------------------
# Verwendung von Environments mit dem Python-Plugin für VSCODE
# ------------------------------------------------------------

# siehe auch: https://code.visualstudio.com/docs/python/environments

# Wenn man eine Python-Datei im Editor geöffnet hat bzw. ein Python-Projekt im 
# Explorer geladen ist, wird in der Status-Zeile (ganz rechts unten)
# der aktuell verwendete Python-Interpreter angezeigt. Wenn man auf diese
# Anzeige klickt, werden die verfügbaren Interpreter (+ die virtuellen 
# Environments, in denen sie wirken) angezeigt.
# Stattdessen hätten wir auch die Kommando-Palette von vscode mit <strg+shift+p>
# öffnen können und dort dann "Python:Select Interpreter" auswählen können.

# Unser oben erzeugtes Environment test_condaenv ist aber nicht darunter.
# Warum ? In dem Environment haben noch keinen Python-Interpreter spezifiziert.
# Das hätte man auch bereits bei der Erzeugung des Environments tun können.

# Wir müssen das nun nachholen. Dazu öffnen wir den Anaconda-PowerShell-Prompt,
# gehen ins Verzeichnis testcondaenv und aktivieren das Environment test_condaenv:

#          (base) PS ... \testcondaenv> conda activate test_condaenv

# Dadurch ändert sich der Prompt entsprechend - das kennen wir ja schon:
#          (test_condaenv) PS ... \testcondaenv>

# Nun installieren wir nachträglich speziell für das Environment test_condaenv
# einen Python-Interpreter:

# (test_condaenv) PS ... \testcondaenv> conda install python 

# Dann wird von Conda aufgelistet, was installiert wird. Das akzeptieren
# wir mit y(es). Nachdem die Installation abgeschlossen wurde, sehen wir uns
# nun mal den Inhalt des Environment-Verzeichnisses in Anaconda an.
# Dieses liegt hier:
#    C:\Users\thwng\anaconda3\envs\test_condaenv
# Darin ist nun u.a. eine python.exe enthalten.
# Das ist übrigens die Version 3.10.4 - also die aktuelle Python Version
# (Stand: 10.5.2022), da wir bei der Installation (s.o.) keine explizite Version
# angegeben hatten.

# Nun können wir überprüfen, ob vscode (bzw. dessen Python-Plugin) diesen
# neuen Interpreter (mitsamt seinem Environment) findet. Evtl. muss man
# vorher aber vscode neu starten (oder das Python-Projekt neu in den Explorer
# laden). Wenn wir nun in der Kommando-Palette wieder "Python:Select Interpreter"
# aufrufen, wird auch unser neues Environment test_condaenv (+ sein Interpreter)
# angezeigt.
# !!!!!!!!!!!!!!!!! 
# Evtl. müssen noch weitere Pakete (z.B. ipykernel) nachinstalliert 
# werden, wenn man mit IPython im interactive Window arbeiten will, aber das
# macht dann vscode automatisch.
# !!!!!!!!!!!!!!!!!

# Wir wollen nun für unseren Crashkurs ein eigenes Environment erstellen.
# Dazu gegen wir wieder in den Anaconda-PowerShell-Prompt und deaktivieren
# das aktuelle Environment test_condaenv:

# (test_condaenv) PS ... \testcondaenv> conda deactivate 

# Wir sind nun wieder im base-Environment und wechseln mit cd in das
# Verzeichnis, in dem sich der Crashkurs befindet. Bei mir heisst das so:

# (base) ... \pyskripte>

# Wir nennen das neue Environment "crashkurs_env" und spezifizieren
# auch gleich den Python-Interpreter und statt --name kann man auch -n
# schreiben:

# (base) PS ... \pyskripte> conda create -n crashkurs_env python=3.10.4

# In vscode wechseln wir nun via Kommando-Palette <strg+shift+p> mit
# dem Befehl "Python:Select Interpreter" das Environment zu "crashkurs_env".
# Beim ersten Ausführen von code im interactive Window wird man noch
# von vscode aufgefordert, das Paket ipykernel nachzuinstallieren.
# Das machen wir auch noch. Dann muss man das interactive-Window
# (wo der IPython-Prompt erscheint) abschiessen. Dann nochmal mit
# <shift+enter> irgendeinen dummy-Code auswerten, wodurch ein neues
# interactive Window erscheint. Jetzt läuft alles. :-)



# ======================================================================
# ======================================================================
# ======================================================================
#                        IPYTHON, JUPYTER
# ======================================================================
# ======================================================================
# ======================================================================

# http://ipython.org/
# IPython realisiert eine echte REPL-Umgebung (im Sinne von Lisp/Clojure)
# für Python. Es bildet den Kern für Jupyter-Notebooks
# https://jupyter.org/

# IPython ist die Grundlage des "interactive window" in der Python Extension
# für Visual Studio Code (vscode)
# https://code.visualstudio.com/docs/python/jupyter-support-py

# https://de.wikipedia.org/wiki/IPython
# IPython ist ein Kommandozeileninterpreter zum interaktiven Arbeiten mit 
# der Programmiersprache Python. Es handelt sich nicht um eine bloße Erweiterung 
# der in Python eingebauten Shell (siehe interaktive Benutzung von Python), 
# sondern um eine Softwaresuite zum Entwickeln und Ausführen von Python-Programmen. 
# Funktionen wie Introspektion, Befehlszeilenergänzung, Rich-Media-Einbettung und 
# verschiedenen Frontends (Terminal, Qt-basiert oder browserbasiert) ermöglichen es, 
# Python-Anwendungen mit einem Komfort zu entwickeln, wie man ihn von Software wie 
# Matlab oder Mathematica kennt. IPython kann auch als integrierte Entwicklungsumgebung 
# betrachtet werden. Tatsächlich handelt es sich bei IPython um ein Client-Server-Framework,
# welches für High-Performance-Rechnungen durch Parallelrechner verwendet werden kann. 

# Die offizielle Doku und Tutorial zu IPython:
# https://ipython.readthedocs.io/en/stable/
# https://ipython.readthedocs.io/en/stable/interactive/tutorial.html


# Folgendes Beispiel kann man in vscode mit Hilfe von IPython
# auf dreierlei Weise ausführen ... 
# a) ... markieren/selektieren, dann <shift>+<enter>
# b) ... im Eingabefeld des "interactive window" eintippen,
#        dann <shift>+<enter>
# c) ... direkt über dem Code folgenden Spezialkommentar einfügen: #%% 
#        Dadurch wird eine Code-Zelle mit einem eigenen, lokalen Menü erzeugt.
#        In diesem lokalen Menü den Befehl "Run Cell" anklicken. 

for i in range(10):
    print(i, end=' ')


# Help Commands
# -------------

help(isinstance)


# Magic Functions
# ---------------

# Diese Spezialfunktionen beginnen immer mit %
# Sie sind ausführbar mit jeder der drei obigen Optionen a), b), c)

# z.B.
# Benchmarking mit %timeit
%timeit range(1000)  #210 ns ± 2.1 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

# output all the currently defined variables
%who

# list the system environment variables
%env




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#FINIS

