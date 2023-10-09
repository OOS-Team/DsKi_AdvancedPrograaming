#tw, 5.1.23  



#                         FUNKTIONEN, SCOPING UND ABSTRAKTION





#Bisher haben wir Zahlen, Zuweisungen, Eingabe/Ausgabe, Vergleiche und Schleifen eingeführt. 
#Wie leistungsfähig ist diese Teilmenge von Python-Sprachkonstrukten ? Theoretisch ist sie 
#so mächtig, wie Sie sie jemals brauchen werden, d.h. sie ist Turing-vollständig. Das heißt, 
#wenn ein Problem überhaupt mit Hilfe von Berechnungen gelöst werden kann, kann es bereits 
#mit nur diesen linguistischen Mechanismen gelöst werden.
#Aber nur weil etwas getan werden kann, heißt das nicht, dass es auf diese Weise getan werden
#sollte ! Zwar kann jede Berechnung im Prinzip nur mit diesen Mechanismen durchgeführt werden, 
#aber das ist äußerst unpraktisch. Im letzten Kapitel haben wir uns einen Algorithmus 
#angesehen, der eine Annäherung (Approximation) an die Quadratwurzel einer positiven Zahl 
#durchführt, siehe folgenden Code 4.0.1.



#Code 4.0.1
#--- Annäherung an die Quadratwurzel von x durch Bisektionssuche ---
x = 25
epsilon = 0.01
if x < 0:
    print('Does not exist')
else:
    low = 0
    high = max(1, x)
    ans = (high + low)/2
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    print(ans, 'is close to square root of', x)
#---



#Wenn man den obigen Code 4.0.1 ausführt (auswertet), erhält man dieses
#Ergebnis:   5.00030517578125 is close to square root of 25

#Dies ist ein vernünftiges Stück Code, aber es fehlt ihm an allgemeinem Nutzen. 
#Er funktioniert nur für die Werte, die den Variablen x und epsilon zugewiesen sind.
#Das heißt, wenn wir ihn wiederverwenden wollen, müssen wir den Code kopieren,
#möglicherweise die Variablennamen bearbeiten und ihn an der gewünschten Stelle einfügen. 
#Wir können diese Berechnung nicht einfach innerhalb einer anderen, komplexeren 
#Berechnung verwenden. 
#Wenn wir außerdem Kubikwurzeln statt Quadratwurzeln berechnen wollen, müssen wir den 
#Code bearbeiten. Wenn wir ein Programm haben wollen, das sowohl Quadrat- als auch Kubik-
#wurzeln berechnet (oder Quadratwurzeln an zwei verschiedenen Stellen berechnet), 
#würde dieses Programm mehrere fast identische Codeabschnitte enthalten.

#Code 4.0.2 passt den Code 4.0.1 an, um die Summe aus der Quadratwurzel von x1 und der 
#Kubikwurzel von x2 auszugeben. Der Code 4.0.2 funktioniert, aber er ist nicht schön.



#Code 4.0.2
#--- Summieren einer Quadratwurzel und einer Kubikwurzel ---
epsilon = 0.01
#Bestimme die Quadratwurzel von x1 durch Bisektion:
x1 = 25
if x1 < 0:
    print('Does not exist')
else:
    low = 0
    high = max(1, x1)
    ans = (high + low)/2
    while abs(ans**2 - x1) >= epsilon:
        if ans**2 < x1:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
x1_root = ans
#Bestimme die Kubikwurzel von x2 durch Bisektion:
x2 = -8
if x2 < 0:
    is_pos = False
    x2 = -x2
else:
    is_pos = True
low = 0
high = max(1, x2)
ans = (high + low)/2
while abs(ans**3 - x2) >= epsilon:
    if ans**3 < x2:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
if is_pos:
    x2_root = ans
else:
    x2_root = -ans
    x2 = -x2
print('Square root of', x1, 'is close to', x1_root, 
      'and cube root of', x2, 'is close to', x2_root)
print('Sum of square root of', x1, 'and cube root of', x2,
      'is close to', x1_root + x2_root)
#---



#Wenn man den obigen Code 4.0.2 ausführt (auswertet), erhält man dieses
#Ergebnis: 
# Square root of 25 is close to 5.00030517578125 and cube root of -8 is close to -2.0
# Sum of square root of 25 and cube root of -8 is close to 3.00030517578125

#Je mehr Code ein Programm enthält, desto größer ist die Wahrscheinlichkeit, dass etwas
#schief gehen kann, und der Code ist umso schwieriger zu warten. Stellen Sie sich zum 
#Beispiel vor, es gäbe einen Fehler in der ursprünglichen Implementierung der Bisektionssuche, 
#und der Fehler würde beim Testen des Programms zutage treten. Es wäre nur allzu leicht, 
#die Implementierung an einer Stelle zu korrigieren und nicht zu bemerken, dass an anderer 
#Stelle ähnlicher Code repariert werden muss.
#Glücklicherweise bietet Python mehrere linguistische Techniken, die es relativ einfach 
#machen, Code zu verallgemeinern und wiederzuverwenden. Die wichtigste derartige Technik
#ist die Funktion.



#------------------------------------------------------------------------------------
#                             4.1 Funktionen und Scoping
#------------------------------------------------------------------------------------

#Wir haben bereits eine Reihe von eingebauten Funktionen verwendet, z. B. max und abs
#im obigen Code 4.0.1. Die Möglichkeit für Programmierer, eigene Funktionen zu definieren und 
#dann zu verwenden, als ob sie eingebaut wären, ist ein qualitativer Sprung in Sachen Komfort.



#                             4.1.1 Definitionen von Funktionen
#------------------------------------------------------------------------------------

#In Python hat jede Funktionsdefinition die Form
#                   -------------------

#          def funktionsname (Liste der formalen Parameter):
#              Funktionskörper

#Wir könnten zum Beispiel die Funktion max_val mit dem folgenden Code definieren:

def max_val(x, y):
    if x > y:
        return x
    else:
        return y

#def ist ein reserviertes Wort, das Python mitteilt, dass eine Funktion definiert werden 
#soll. Der Funktionsname (max_val in diesem Beispiel) ist einfach ein Name, der verwendet 
#wird, um auf die Funktion zu verweisen. Die PEP 8-Konvention lautet dass Funktionsnamen in 
#Kleinbuchstaben geschrieben werden sollten, wobei die Wörter durch Unterstriche getrennt 
#werden, um die Lesbarkeit zu verbessern.

#PEP 8 ist der "Style Guide for Python Code"  https://peps.python.org/pep-0008/

#Die Reihenfolge der Namen innerhalb der Klammern nach dem Funktionsnamen (x,y in diesem 
#Beispiel) sind die formalen Parameter der Funktion. Wenn die Funktion verwendet wird, 
#                   ------------------
# werden die formalen Parameter (wie in einer Zuweisungsanweisung) an die aktuellen Parameter
#                                                                         -------------------
#(oft als Argumente bezeichnet) des Funktionsaufrufs (auch als function call bezeichnet)  
#         ---------                 ----------------           -------------
#gebunden. Zum Beispiel bindet der Aufruf

max_val(3, 4)          #ergibt: 4

#den formalen Parameter x an 3 und den formalen Parameter y an 4.

#Der Funktionskörper ist ein beliebiges Stück Python-Code. Es gibt eine spezielle Anweisung, 
#return, die nur innerhalb des Funktionskörpers verwendet werden kann.
#------
#Ein Funktionsaufruf ist ein Ausdruck, und wie alle Ausdrücke hat er einen Wert. Dieser 
#Wert wird von der aufgerufenen Funktion zurückgegeben, z.B.: der Wert des Ausdrucks 

max_val(3,4) * max_val(3,2)    #ergibt12, 

#weil der erste Aufruf von max_val den int-Wert 4 zurückgibt und der zweite gibt den int-Wert 
#3 zurück. Beachten Sie, dass die Ausführung einer return-Anweisung einen Aufruf der Funktion 
#beendet. Zusammenfassend lässt sich sagen, dass beim Aufruf einer Funktion 
#folgendes gilt ...

#     1. Die Ausdrücke, aus denen die Aktualparameter bestehen, werden augewertet
#        und die Formalparameter der Funktion werden an diese resultierenden Werte 
#        gebunden. Zum Beispiel bindet der Aufruf max_val(3+4, z) den formalen 
#        Parameter x an den Wert 7 und den Formalparameter y an den Wert, 
#        den die Variable z hat, wenn der Aufruf ausgeführt wird.
#
#     2. Der Ausführungspunkt (point of execution), d.h. die nächste auszuführende 
#            ------------------------------------
#        Anweisung) verschiebt sich vom Punkt des Aufrufs der Funktion (function call) 
#        zur ersten Anweisung im Körper der Funktion.
#
#     3. Der Code im Körper der Funktion wird ausgeführt, bis entweder eine
#        Return-Anweisung auftritt; in diesem Fall wird der Wert des Ausdrucks 
#        nach dem Return zum Wert des Funktionsaufrufs insgesamt, oder es werden
#        keine weiteren Anweisungen ausgeführt; in diesem Fall gibt die Funktion 
#        den Wert None zurück, d.h. wenn kein Ausdruck auf die Rückgabe folgt, 
#        ist der Wert des Aufrufs None.
#
#     4. Der Wert des Aufrufs der Funktion ist der Rückgabewert.
#
#     5. Der Ausführungspunkt (point of execution) wird an den Code zurückgegeben, 
#        der unmittelbar auf den Aufruf (function call) folgt.

#Parameter ermöglichen es Programmierern, Code zu schreiben, der nicht auf
#spezifische Objekte zugreift, sondern auf die Objekte, die der Aufrufer der Funktion 
#als aktuelle Parameter verwenden will. Dies wird als Lambda Abstraktion bezeichnet.
#                                                     ------------------
#Siehe dazu: https://de.wikipedia.org/wiki/Lambda-Kalk%C3%BCl

#Der folgende Code 4.1.1.1 enthält eine Funktion, die drei formale Parameter hat
#und einen Wert zurückgibt, nennen wir ihn ans, so dass gilt: 
#       abs(ans**power - x) >= epsilon.



#Code 4.1.1.1
#--- Eine Funktion zur Ermittlung von Wurzeln ---
def find_root(x, power, epsilon):
    #find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no real-valued roots
    low = min(-1, x)
    high = max(1, x)
    #use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:           #<-------
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
#---



#Der folgende Code 4.1.1.2 enthält Code, der verwendet werden kann, um zu testen, 
#ob find_root wie vorgesehen funktioniert. Die Testfunktion test_find_root ist etwa 
#genauso lang wie find_root selbst. Für unerfahrene Programmierer scheint das Schreiben 
# von Testfunktionen oft eine Verschwendung von Aufwand zu sein. Erfahrene Programmierer 
#     -------------- 
#wissen jedoch, dass eine Investition in das Schreiben von Testcode oft einen großen Nutzen 
#bringt. Es ist sicherlich besser als während der Fehlersuche (dem Debugging) immer wieder 
#                                                 ---------------------------
# Testfälle in die Shell einzugeben, um herauszufinden, warum ein Programm nicht 
#funktioniert, und es dann zu beheben. Beachten Sie, dass wir test_find_root mit 
#drei Tupeln (d.h. Sequenzen von Werten) der Länge drei aufrufen. Ein Aufruf der Testfunktion
#prüft damit 27 Kombinationen von Parametern. Da test_find_root schließlich prüft, 
#ob find_root eine passende Antwort liefert und das Ergebnis meldet, erspart es dem 
#Programmierer die mühsame und fehleranfällige Aufgabe, jede Ausgabe visuell zu inspizieren
#und auf Korrektheit zu prüfen. Wir kehren zum Thema Testen in Kapitel 8 zurück.


#Code 4.1.1.2
#--- Zum Testen von find_root ---
def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result**p - x) > e:
                        val = 'Bad'
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')
#---



#Jetzt wenden wir die Testfunktion test_find_root mal an:
                     
x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)   #ergibt:x = 0.25, power = 1, epsilon = 0.1: Okay
                                           #       x = 0.25, power = 1, epsilon = 0.001: Okay
                                           #       x = 0.25, power = 1, epsilon = 1: Okay
                                           #       x = 0.25, power = 2, epsilon = 0.1: Okay
                                           #       x = 0.25, power = 2, epsilon = 0.001: Okay
                                           #       x = 0.25, power = 2, epsilon = 1: Okay
                                           #       x = 0.25, power = 3, epsilon = 0.1: Okay
                                           #       x = 0.25, power = 3, epsilon = 0.001: Okay
                                           #       x = 0.25, power = 3, epsilon = 1: Okay
                                           #       x = 8, power = 1, epsilon = 0.1: Okay
                                           #       x = 8, power = 1, epsilon = 0.001: Okay
                                           #       x = 8, power = 1, epsilon = 1: Okay
                                           #       x = 8, power = 2, epsilon = 0.1: Okay
                                           #       x = 8, power = 2, epsilon = 0.001: Okay
                                           #       x = 8, power = 2, epsilon = 1: Okay
                                           #       x = 8, power = 3, epsilon = 0.1: Okay
                                           #       x = 8, power = 3, epsilon = 0.001: Okay
                                           #       x = 8, power = 3, epsilon = 1: Okay
                                           #       x = -8, power = 1, epsilon = 0.1: Okay
                                           #       x = -8, power = 1, epsilon = 0.001: Okay
                                           #       x = -8, power = 1, epsilon = 1: Okay
                                           #       x = -8, power = 2, epsilon = 0.1: No root exists
                                           #       x = -8, power = 2, epsilon = 0.001: No root exists
                                           #       x = -8, power = 2, epsilon = 1: No root exists
                                           #       x = -8, power = 3, epsilon = 0.1: Okay
                                           #       x = -8, power = 3, epsilon = 0.001: Okay
                                           #       x = -8, power = 3, epsilon = 1: Okay



#################
#Aufgabe 4.1.1.a:
#################
#Verwenden Sie die Funktion find_root (Code 4.1.1.1), um Folgendes zu drucken:
#die Summe der sukzessiven Approximation an die Quadratwurzel von 25, 
#die Kubikwurzel von -8 und 
#die vierte Wurzel von 16. 
#Verwenden Sie 0.001 als Epsilon.
################
x = (-8, 16)
powers=(3,4)
epsilon = 0.001
test_find_root(x, powers, epsilon)

#################
#Aufgabe 4.1.1.b:
#################
#Schreiben Sie eine Funktion is_in, die zwei Zeichenketten als Argumente akzeptiert
#und True zurückgibt, wenn eine der beiden Zeichenketten irgendwo in der anderen
#vorkommt. Andernfalls soll is_in False zurückgeben. 
#Tipp: Sie können den eingebauten in-Operator in verwenden.
################



#################
#Aufgabe 4.1.1.c:
#################
#Schreiben Sie eine Testfunktion für is_in.
################



#                             4.1.2 Keyword Argumente und Default-Werte
#------------------------------------------------------------------------------------

#In Python gibt es zwei Möglichkeiten, wie formale Parameter an aktuelle Parameter gebunden 
#werden. Die häufigste Methode wird als Positionsargument (positional argument) bezeichnet.
#                                       --------------------------------------
#Diese Methode haben wir bislang immer eingesetzt: der erste formale Parameter wird dabei 
#an den ersten aktuellen Parameter gebunden, der zweite formale an den zweiten aktuellen 
#Parameter usw. Python unterstützt aber auch sog. Schlüsselwortargumente (keyword arguments),   
#                                                 -----------------------------------------
#bei denen formale an aktuelle Parameter gebunden werden, indem der Name des formalen 
#Parameters beim Funktionsaufruf explizit verwendet wird. Betrachten Sie z.B. diese 
#Funktionsdefinition ...

def print_name(first_name, last_name, reverse): 
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

#Die Funktion print_name geht davon aus, dass first_name und last_name Zeichenketten sind 
#und dass reverse ein Boolescher Wert ist. Wenn reverse == True ist, druckt sie
#last_name, first_name; andernfalls wird first_name last_name ausgegeben.
#Jeder der folgenden Aufrufe ist ein gleichwertiger Aufruf von print_name:

print_name('Olga', 'Puchmajerova', False)
print_name('Olga', 'Puchmajerova', reverse = False)
print_name('Olga', last_name = 'Puchmajerova', reverse = False)
print_name(last_name = 'Puchmajerova', first_name = 'Olga', reverse = False)

#Obwohl die Schlüsselwortargumente in beliebiger Reihenfolge in der Liste der aktuellen 
#Parameter erscheinen können, ist es nicht zulässig, nach einem Schlüsselwortargument mit 
#einem positional Argument, also einem Nicht-Schlüsselwort-Argument, zu folgen. Daher 
#würde eine Fehlermeldung erzeugt werden durch ...

print_name('Olga', last_name = 'Puchmajerova', False)   #SyntaxError: positional argument 
                                                        #follows keyword argument

#Schlüsselwortargumente werden i.d.R. in Verbindung mit Standard(default)-Parameterwerten 
#                                                       ---------------------------------
#in der Funktionsdefinition(!!) verwendet. Wir können zum Beispiel schreiben ...

#           der Defaultwert des Parameters reverse ist hier False
#                                           |
#                                     ______v_________
def print_name(first_name, last_name, reverse = False):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

#Standardwerte erlauben es dem Programmierer, eine Funktion mit weniger
#als der angegebenen Anzahl von Argumenten aufzurufen. Zum Beispiel,

print_name('Olga', 'Puchmajerova')                    #Olga Puchmajerova
print_name('Olga', 'Puchmajerova', True)              #Puchmajerova, Olga
print_name('Olga', 'Puchmajerova', reverse = True)    #Puchmajerova, Olga

#Die beiden letzten Aufrufe von print_name sind semantisch gleichwertig.
#Der letzte Aufruf hat den Vorteil, dass er eine Dokumentation für das vielleicht mysteriöse 
#Argument True darstellt. Allgemeiner ausgedrückt: Die Verwendung von Schlüsselwortargumenten
#verringert die Gefahr, dass ein aktueller Parameter versehentlich an den falschen formalen 
#Parameter gebunden wird. Die Codezeile

print_name(nachname = 'Puchmajerova', vorname = 'Olga')

#lässt keine Zweifel an der Absicht des Programmierers, der sie geschrieben hat. Dies ist 
#nützlich, weil der Aufruf einer Funktion mit den richtigen Argumenten in der falschen 
#Reihenfolge ein häufiger Fehler ist.
#Der mit einem Standardparameter verbundene Wert wird zum Zeitpunkt der Funktionsdefinition 
#berechnet. Dies kann zu überraschendem Programmverhalten führen, wie wir in Abschnitt 5.3 
#erörtern werden.



#################
#Aufgabe 4.1.2.a:
#################
#Schreibe eine Funktion mult, die entweder ein oder zwei integer-Werte als Argumente 
#akzeptiert. Wenn sie mit zwei Argumenten aufgerufen wird, gibt die Funktion das Produkt 
#der beiden Argumente aus. Wenn sie mit einem Argument aufgerufen wird, gibt sie dieses 
#Argument selbst aus.
################



#                             4.1.3 Variable Anzahl von Argumenten
#------------------------------------------------------------------------------------

#Python verfügt über eine Reihe von eingebauten Funktionen, die mit einer variablen
#Anzahl von Argumenten arbeiten. Zum Beispiel die Ausdrücke

min(6,4)           #4
min(3,4,1,6)       #1

#sind beide legal (und werten das aus, was Sie glauben, dass sie tun). Python macht es 
#Programmierern leicht, ihre eigenen Funktionen zu definieren, die eine variable Anzahl 
#von Argumenten akzeptieren. Der Entpackungsoperator (unpacking operator) * erlaubt es 
#                                ------------------------------------------
#einer Funktion, eine variable Anzahl von Positionsargumenten zu akzeptieren, zum Beispiel:

def mean(*args):
    '''Assumes at least one argument and all arguments are numbers
       Returns the mean of the arguments'''
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

#berechnet den Mittelwert der als Argumente gegebenen Zahlen und kann so verwendet werden

mean(1.5, -1.0)                    #0.25
mean(1, 2, 3, 4, 5, 6, 7, 8, 9)    #5.0

#Beachten Sie, dass der Name nach dem * in der Argumentliste nicht args sein muss. 
#Er kann ein beliebiger Name sein. Für mean wäre es vielleicht anschaulicher gewesen, 
#                 def mean(*numbers) 
#zu schreiben.



#################
#Aufgabe 4.1.3.a:
#################
#Weisen Sie nach, dass args im Funktionskörper der obigen Funktion mean
#ein Tupel ist, dessen Länge der Anzahl der übergebenen Argumente entspricht.
################

def mean(*args):
    '''Assumes at least one argument and all arguments are numbers
       Returns the mean of the arguments'''
    tot = 0
    print(type(args))
    for a in args:
        tot += a
    return tot/len(args)

#                             4.1.4 Scoping (Geltungsbereich)
#------------------------------------------------------------------------------------

#Schauen wir uns ein weiteres kleines Beispiel an:

def f(x): #name x used as formal parameter
    y = 1
    x = x + y
    print('x =', x)                                  #<----
    return x
x = 3
y = 2
z = f(x) #value of x used as actual parameter
print('z =', z)                                      #<----
print('x =', x)                                      #<----
print('y =', y)                                      #<----

#Wenn wir obigen Code ausführen, erhalten wir:
#          x = 4    
#          z = 4
#          x = 3
#          y = 2

#Was ist hier los? Beim Aufruf von f wird der Formalparameter x lokal an den Wert des 
#Aktualparameters x im Kontext des Funktionskörpers von f gebunden. Obwohl der aktuelle 
#und der formale Parameter denselben Namen haben, sind sie nicht dieselbe Variable. 
#Jede Funktion definiert einen neuen Namensraum (name space), auch Scope genannt. 
#                                    ----------------------        -----
#Der formale Parameter x und die lokale Variable y, die in f verwendet werden, existieren
#                                --------------- 
#nur innerhalb des Geltungsbereichs (scope) der Definition von f. Die Zuweisungsanweisung 
#x = x + y innerhalb des Funktionskörpers bindet den lokalen Namen x an den Wert 4.
#Die Zuweisungen in f haben keinen Einfluss auf die Bindungen der Namen x und y, die 
#außerhalb des Geltungsbereichs der Definition von f existieren.

#Wir könnten beim Aufruf von f sogar Keyword-Parameter in folgender Weise verwenden ...
def f(x): 
    print('x =', x)      #.   das wurde hier zusätzlich eingefügt, um die Zusammenhänge zu verdeutlichen
    y = 1
    x = x + y
    print('x =', x)      #..                            
    return x
x = 3
y = 2
z = f(x=x)                          #<----- !!!! Das sieht SEHR seltsam aus. Wenn man es sich 
print('z =', z)          #...       #            allerdings genau überlegt, macht es Sinn:
print('x =', x)          #....      #            Der formale Parameter x wird an den Wert der
print('y =', y)          #.....     #            globalen Variablen x (also 3) gebunden.

#und damit erhalten wir nun:  
#.          x = 3          
#..         x = 4    
#...        z = 4
#....       x = 3
#.....      y = 2

#Hier ist eine Möglichkeit, sich diese ganzen Zusammenhänge vorzustellen:
#         1. Auf der obersten Ebene, d.h. der Ebene der Shell, werden in einer 
#            Symboltabelle (symbol table) alle auf dieser Ebene definierten Namen 
#            ---------------------------
#            und ihre aktuellen Bindungen registriert.
#         2. Wenn eine Funktion aufgerufen wird, wird eine neue Symboltabelle 
#            (oft als stack frame bezeichnet) erstellt. Diese Tabelle speichert 
#                     -----------
#            alle Namen, die innerhalb der Funktion definiert sind (einschließlich 
#            der formalen Parameter) und ihre aktuellen Bindungen (scope, name space). 
#            Wird eine Funktion von innerhalb des Funktionskörpers aufgerufen, 
#            wird ein weiterer Stackframe erstellt.
#         3. Wenn die Funktion beendet ist, verschwindet ihr Stack-Frame.

#In Python können Sie den Gültigkeitsbereich eines Namens immer dadurch bestimmen, indem 
#man sich den Programmtext ansieht. Dies wird statisches oder lexikalisches Scoping genannt.
#                                             -------------------------------------
#Code 4.1.4.1 enthält ein Beispiel, das die Scoping-Regeln von Python veranschaulicht. 
#Die zu diesem Code gehörende History der entsprechenden Stack-Frames ist in
#Abb. 4.1.4.1 gezeigt.



#Code 4.1.4.1
#--- Verschachtelte Geltungsbereiche (nested scopes) ---
def f(x):
    def g():
        x = 'abc'
        print('x =', x)           #<----  ...        .......
    def h():
        z = x
        print('z =', z)           #<----  ..
    x = x + 1
    print('x =', x)               #<----  .
    h()
    g()
    print('x =', x)               #<----  ....
    return g

x = 3
z = f(x)
print('x =', x)                   #<----  .....
print('z =', z)                   #<----  ......
z()
#---



#Wenn man den Code 4.1.4.1 ausführt, wird folgenes ausgedruckt, wobei die entsprechenden
#print-Anweisungen in der Reihenfolge ihrer Ausführung durch Punkte im Kommentar (s.o.) markiert 
#sind: 
#                  x = 4                                               . 
#                  z = 4                                               ..
#                  x = abc                                             ...
#                  x = 4                                               ....
#                  x = 3                                               .....
#                  z = <function f.<locals>.g at 0x0000021FE72A6040>   ......
#                  x = abc                                             .......

#Die erste Spalte in Abb. 4.1.4.1 enthält die Menge der Namen, die außerhalb des 
#Körpers der Funktion f bekannt sind, d.h. die Variablen x und z und den Funktionsnamen f.
#Die erste Zuweisungsanweisung bindet x an 3.


#Abb.4.1.4.1 (Stack Frames zu Code 4.1.4.1)
#
#                                   ┌─────┐               ┌─────┐
#                                   │  z  │               │  x  │
#                                   └─────┘               └─────┘           
#             
#             
#                        ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
#                        │  h  │    │  h  │    │  h  │    │  h  │    │  h  │
#                        └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
#             
#                        ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
#                        │  g  │    │  g  │    │  g  │    │  g  │    │  g  │
#                        └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
#             
#                        ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐               ┌─────┐
#                        │  x  │    │  x  │    │  x  │    │  x  │    │  x  │               │  x  │
#                        └─────┘    └─────┘    └─────┘    └─────┘    └─────┘               └─────┘
#             
#             
#             ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐ 
#             │  z  │    │  z  │    │  z  │    │  z  │    │  z  │    │  z  │    │  z  │    │  z  │
#             └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
#             
#             ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
#             │  x  │    │  x  │    │  x  │    │  x  │    │  x  │    │  x  │    │  x  │    │  x  │
#             └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
#             
#             ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
#             │  f  │    │  f  │    │  f  │    │  f  │    │  f  │    │  f  │    │  f  │    │  f  │
#             └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
#             
#             
#    Spalte      1          2          3          4          5          6          7          8
#
#                         in f       in  h      in f       in g       in f                 in z (die von f 
#                                                                                          returnierte 
#                                                                                          Funktion g)


#Die Zuweisungsanweisung z = f(x) wertet zunächst den Ausdruck f(x) aus, indem sie die 
#Funktion f mit dem Wert aufruft, an den x gebunden ist. Beim Aufruf von f wird ein 
#stack frame erstellt wie in Spalte 2 von Abb.4.1.4.1 dargestellt.
#Die Namen im stack-frame sind x (der formale Parameter x, nicht das x im Aufrufkontext), 
#g und h. Die Variablen g und h sind an Objekte vom Typ function gebunden. Die Eigenschaften 
#dieser Funktionen sind gegeben durch die Funktionsdefinitionen innerhalb von f.

#Wenn h von f aus aufgerufen wird, wird ein weiterer stack-frame erstellt, wie in Spalte 3 
#gezeigt. Dieser stack-frame enthält nur die lokale Variable z. Warum enthält er nicht 
#auch x? Ein Name wird demjenigen Bereich (scope) hinzugefügt, der mit einer Funktion 
#verbunden ist, wenn dieser Name ein formaler Parameter der Funktion oder eine an ein 
#Objekt gebundene Variable innerhalb des Körpers der Funktion gebunden ist. Im Körper 
#von h kommt x nur auf der rechten Seite einer Zuweisungsanweisung vor. Das Auftreten 
#eines Namens (in diesem Fall x), der nicht an ein Objekt gebunden ist, irgendwo im 
#Funktionskörper (in diesem Fall der Körper von h), veranlasst den Interpreter, denjenigen 
#stack-frame zu durchsuchen, der zu dem Bereich (scope) gehört, in dem die Funktion definiert 
#ist (also dem stack-frame, der mit f verbunden ist). Wenn der Name gefunden wird (was hier 
#der Fall ist), wird der Wert, an den er gebunden ist (siehe Spalte 4), verwendet. Wird er 
#nicht gefunden, wird eine Fehlermeldung ausgegeben.

#Wenn h zurückkehrt, verschwindet der stack-frame, der mit dem Aufruf von h assoziiert ist 
#(er wird von der Spitze des Stapels (stack) entfernt (popped)), wie in Spalte 4 dargestellt. 
#                                                      ------
#Beachten Sie, dass wir nie Frames aus der Mitte des Stapels entfernen, sondern nur den 
#jeweils zuletzt hinzugefügten Frame. Dieses "last in first out"-Verhalten (LIFO) 
#                                                                          ------
#motiviert den Begriff "Stapel" (stack). (Stellen Sie sich vor, einen Stapel Pfannkuchen 
#                               -------
#zu backen. Wenn der erste aus der Pfanne kommt kommt, legt der Koch ihn auf eine Servier-
#platte. Jeder weitere Pfannkuchen wird auf die bereits auf der Platte liegenden Pfannkuchen 
#gestapelt. Wenn es an der Zeit ist, die Pfannkuchen zu essen, wird der erste Pfannkuchen, 
#der serviert wird, der auf dem Stapel ganz oben liegende sein. Der vorletzte Pfannkuchen, 
#der dem Stapel hinzugefügt wurde, ist dann der neue oberste Pfannkuchen und somit der 
#nächste Pfannkuchen, der serviert wird, etc.).


#Abb: Pfannkuchen-Stapel
#                                   
#                      __....----`````-----------`````----....__
#                 _-'''                                         ```-_
#               .'                                                   `.
#               |`-_                                               _-'|
#               |   ```--....____                     ____....--'''   |
#               |                `````-----------'''''                |
#               |-__                                               __-|
#               |   ~~~--________                     ________--~~~   |
#               |                ~~~~~-----------~~~~~                |
#               |-__                                               __-|
#               |   ~~~--________                     ________--~~~   |
#               |                ~~~~~-----------~~~~~                |
#               | `-_                                               _-|
#               |    ```--....____                     ____....--'''  |
#               |                 ~~~~~-----------~~~~~               |
#               |-__                                               __-|
#               |   ~~~--________                     ________--~~~   |
#               |                ~~~~~-----------~~~~~                |
#               |-__                                               __-|
#               |   ~~~--________                     ________--~~~   |
#               |                ~~~~~-----------~~~~~                |
#                `-_                                               _-'
#                   ```--....____                     ____....--'''
#                                `````-----------'''''                    


#Kehren wir zu unserem Python-Beispiel zurück: g wird nun aufgerufen und ein stack-frame, 
#der die lokale Variable x von g enthält, wird hinzugefügt (Spalte 5). Wenn g zurückkehrt, 
#wird dieser frame entfernt (Spalte 6). Wenn f zurückkehrt, wird der stack-frame, der die 
#mit f verknüpften Namen enthält, gelöscht (popped), wodurch wir zurück zum ursprünglichen 
#stack-frame gelangen (Spalte 7). Die von f returnierte Funktion g wird an z gebunden und
#dann als z() aufgerufen (Spalte 8)

#Beachten Sie, dass nach der Rückkehr von f, obwohl die Variable g nicht mehr existiert, 
#das Objekt vom Typ function, an das dieser Name einst gebunden war, noch existiert. 
#Das liegt daran, dass Funktionen Objekte sind, die zurückgegeben werden können, wie jede 
#andere Art von Objekt auch. So kann z an den Wert Wert gebunden werden, der von f zurück-
#gegeben wird, und der Funktionsaufruf z() kann verwendet werden, um die Funktion aufzurufen, 
#die in f an den Namen g gebunden wurde - auch wenn der Name g außerhalb des Kontexts von f 
#nicht bekannt ist.


#Die Reihenfolge, in der ein Name genannt wird, ist nicht entscheidend. Wenn ein Objekt 
#irgendwo im Funktionskörper an einen Namen gebunden ist (auch wenn es in einem Ausdruck 
#vorkommt, bevor es als linke Seite einer Zuweisung erscheint), wird es als lokal für 
#diese Funktion behandelt. Dieses Design von Python wird oft kritisiert, und hier folgt
#ein Beispiel warum. Betrachten Sie z.B. diesen Code:

def f():
    print(x)
def g():
    print(x)          #<--- hier wird versucht den Wert der lokalen Variablen x auszudrucken; sie hat hier aber noch keinen Wert !
    x = 1             #<--- dadurch ist x nun lokal in g definiert
x = 3
f()
x = 3
g()

#Beim Ausführen des obigen Codes wird beim Aufruf von f zuerst 3 ausgegeben, 
#aber dann folgt gleich die Fehlermeldung:

#       UnboundLocalError: local variable 'x' referenced before assignment

#Dies geschieht, weil die Zuweisungsanweisung nach der print-Anweisung bewirkt, dass x 
#lokal zu g ist. Und weil x lokal zu g ist, hat es keinen definierten Wert, wenn die 
#print-Anweisung ausgeführt wird.
#Schon verwirrt? Die meisten Menschen brauchen ein wenig Zeit, um die Scoping-Regeln zu 
#verstehen. Lassen Sie sich davon nicht beirren. Machen Sie erst einmal weiter und fangen 
#Sie an, Funktionen zu verwenden. Die meiste Zeit werden Sie nur Variablen verwenden wollen, 
#die lokal zu einer Funktion sind, und die Feinheiten des Scopings werden irrelevant sein. 
#Wenn Ihr Programm von einer subtilen Scoping-Regel abhängt, sollten Sie in Erwägung ziehen, 
#es umzuschreiben, um dies zu vermeiden.



#------------------------------------------------------------------------------------
#                             4.2 Spezifikationen
#------------------------------------------------------------------------------------

#Eine Spezifikation einer Funktion definiert einen Vertrag zwischen dem Implementierer
#     ------------- 
#einer Funktion und denjenigen, die Programme schreiben werden, die diese Funktion verwenden. 
#Wir bezeichnen die Benutzer einer Funktion als ihre Klienten (clients). Dieser Vertrag kann 
#                                                    -----------------
#aus zwei Teilen bestehen:
#
#      *   Annahmen (assumptions): Diese beschreiben die Bedingungen, die von den Klienten 
#          ---------------------
#          der Funktion erfüllt werden müssen. Typischerweise beschreiben sie Beschränkungen 
#          für die aktuellen Parameter. Fast immer spezifizieren sie den akzeptablen Satz
#          von Typen für jeden Parameter und nicht selten auch einige
#          Beschränkungen (constraints) für den Wert eines oder mehrerer Parameter. 
#          Z.B. könnte die Spezifikation von find_root erfordern, dass power eine
#          positive ganze Zahl sein soll.
#
#      *   Garantien (guarantees): Diese beschreiben Bedingungen, die von der Funktion
#          ---------------------
#          erfüllt werden müssen, vorausgesetzt, sie wurde in einer Weise aufgerufen, die 
#          die Annahmen erfüllt. Z.B. könnte die Spezifikation von find_root garantieren, 
#          dass sie None zurückgibt, wenn sie eine Wurzel finden soll, die nicht existiert 
#          (z.B. die Quadratwurzel einer negativen Zahl, wenn wir nur im Reellen bleiben).

#Funktionen sind eine Möglichkeit, Berechnungselemente zu erstellen, die wir als Primitive 
#betrachten können. Sie bieten Dekomposition und Abstraktion.

#Decomposition schafft Struktur. Sie ermöglicht es uns, ein Programm in Teile zu zerlegen, 
#-------------
#die einigermaßen in sich geschlossen sind und die in verschiedenen Umgebungen wiederverwendet 
#werden können.

#Abstraktion verbirgt Details. Sie ermöglicht es uns, ein Stück Code so zu verwenden, als
#-----------
#als wäre er eine Blackbox - also etwas, dessen innere Details wir nicht sehen können, 
#nicht sehen müssen und auch nicht sehen wollen sollten. Essenz der Abstraktion ist es, 
#Informationen zu bewahren, die in einem bestimmten Kontext relevant sind, und das 
#Vergessen von Informationen, die in diesem Kontext irrelevant sind. Der Schlüssel zum 
#effektiven Einsatz von Abstraktion in der Programmierung besteht darin, einen Begriff von 
#Relevanz zu finden, der sowohl für den Ersteller einer Abstraktion als auch für die 
#potenziellen Klienten der Abstraktion geeignet ist. Das ist die wahre Kunst des 
#Programmierens.

#Dies ist die Art und Weise, wie Unternehmen Teams von Programmierern einsetzen, um
#Dinge zu erledigen. Mit einer Spezifikation für ein Modul kann ein Programmierer
#an der Implementierung dieses Moduls arbeiten, ohne sich darum zu kümmern, was die
#anderen Programmierer im Team gerade tun. Außerdem können die anderen Programmierer die 
#Spezifikation nutzen, um mit dem Schreiben von Code zu beginnen, der das Modul verwendet, 
#ohne sich Gedanken darüber zu machen, wie das Modul implementiert wird.

#Code 4.2.1 fügt eine Spezifikation zu der Implementierung von find_root von Code 4.1.1.1
#hinzu:



#Code 4.2.1
#--- Eine Funktionsdefinition mit Spezifikation ---     
def find_root(x, power, epsilon): 
    """Assumes x and epsilon int or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None"""
    #find interval containing answer
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    #use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

#Zum Testen:
e = 0.001
print(find_root(25, 2, e), find_root(-8, 3, e), find_root(14, 4, e))
#ergibt: 4.9999237060546875 -1.9999542236328125 1.9343223571777344
#---



#Der Text zwischen den dreifachen Anführungszeichen in der Funktionsdefinition wird in 
#Python als docstring bezeichnet. Üblicherweise verwenden Python-Programmierer docstrings
#           ---------
#zur Spezifikation von Funktionen. Diese docstrings können über die eingebaute Funktionshilfe 
#aufgerufen werden. Eines der schönen Dinge an Python-IDEs ist, dass sie ein interaktives 
#Werkzeug zur Verfügung stellen, um Fragen zu den eingebauten Objekten zu stellen. Wenn Sie 
#wissen wollen, was eine bestimmte Funktion tut, müssen Sie nur help(<object>) in das 
#                                                               ------------ 
#Konsolenfenster eingeben. Zum Beispiel erzeugt... 

help(abs) 

#den Text
#            Help on built-in function abs in module builtins:
#            abs(x, /)
#                Return the absolute value of the argument.

#Dies sagt uns, dass abs eine Funktion ist, die ein einzelnes Argument auf seinen absoluten 
#Wert abbildet. (Das / in der Argumentliste bedeutet, dass das Argument positional sein muss.
#nach dem slash / durfen nämlich nur noch keyword-Argumente folgen.) 
#Wenn Sie help() eingeben, wird eine interaktive Hilfesitzung gestartet, und der Interpreter 
#zeigt die Eingabeaufforderung help> im Konsolenfenster. Ein Vorteil des interaktiven Modus 
#ist, dass Sie Hilfe zu Python-Konstrukten erhalten können, die keine Objekte sind. 
#Z.B.,

#                  help> if
#                  The "if" statement
#                  ******************
#
#                  The "if" statement is used for conditional execution:
#                   if_stmt ::= "if" expression ":" suite
#                   ("elif" expression ":" suite)*
#                   ["else" ":" suite]
#
#                  It selects exactly one of the suites by evaluating the expressions one
#                  by one until one is found to be true (see section Boolean operations
#                  for the definition of true and false); then that suite is executed
#                  (and no other part of the "if" statement is executed or evaluated).
#                  If all expressions are false, the suite of the "else" clause, if
#                  present, is executed.
#
#                  Related help topics: TRUTHVALUE

#Die interaktive Hilfe kann durch Eingabe von quit beendet werden.
#Wenn der Code 4.2.1 (siehe oben) in eine IDE geladen worden wäre, würde die Eingabe von

help(find_root) 

#in der Shell folgendes (also den docstring) anzeigen:

#         find_root(x, power, epsilon)
#             Assumes x and epsilon int or float, power an int, 
#                 epsilon > 0 & power >= 1
#             Returns float y such that y**power is within epsilon of x.
#                 If such a float does not exist, it returns None

#Die Spezifikation von find_root ist eine Abstraktion von allen möglichen Implementierungen, 
#die diese Spezifikation erfüllen. Klienten von find_root können annehmen, dass die 
#Implementierung die Spezifikation erfüllt, aber sie sollten nichts weiter annehmen. 
#Zum Beispiel können Klienten annehmen, dass der Aufruf 

find_root(4, 2, 0.01) 

#einen Wert liefert, dessen Quadrat zwischen 3,99 und 4,01 liegt. Der zurückgegebene Wert 
#kann positiv oder negativ sein, und auch wenn 4 ein perfektes Quadrat ist, ist der 
#zurückgegebene Wert nicht unbedingt 2 oder -2. Entscheidend ist, dass, wenn die Annahmen 
#der Spezifikation nicht erfüllt sind, man nichts über die Wirkung des Aufrufs der Funktion
#sagen kann. Zum Beispiel könnte der Aufruf find_root(8, 3, 0) könnte 2 zurückgeben. 
#Er könnte aber auch abstürzen, ewig laufen oder eine Zahl zurückgeben, die nicht 
#annähernd die Kubikwurzel aus 8 ist.



###############
#Aufgabe 4.2.a:
###############
#Schreiben Sie unter Verwendung des Algorithmus aus Code 3.2.3 (in Kap3) eine Funktion, 
#die die folgende Spezifikation erfüllt:
def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x."""
###############



#------------------------------------------------------------------------------------
#                             4.3 Verwendung von Funktionen zur Modularisierung von Code
#------------------------------------------------------------------------------------

#Bisher waren alle Funktionen, die wir implementiert haben, klein. Sie passen gut auf eine 
#einzelne Seite. Wenn wir kompliziertere Funktionen implementieren, ist es sinnvoll, 
#die Funktionen in mehrere Funktionen aufzuteilen, von denen jede eine einfache Aufgabe 
#erfüllt. Zur Veranschaulichung dieser Idee, haben ich find_root etwas überflüssigerweise 
#in drei separate Funktionen auf, wie in Code 4.3.1 gezeigt. Jede dieser Funktionen hat 
#ihre eigene Spezifikation und jede macht als eigenständige Einheit Sinn. Die Funktion 
#find_root_bounds findet ein Intervall, in dem die Wurzel liegen muss, 
#bisection_solve sucht in diesem Intervall mittels Bisektionssuche nach einer Approximation 
#an die Wurzel, und find_root ruft einfach die beiden anderen auf und gibt die Wurzel zurück.

#Ist diese Version von find_root einfacher zu verstehen als die ursprüngliche, monolithische 
#Implementierung von Code 4.2.1 ? Wahrscheinlich nicht. Eine gute Faustregel ist, wenn eine 
#Funktion bequem auf eine einzige Seite passt, muss sie wahrscheinlich nicht unterteilt 
#werden, um leicht verständlich zu sein.



#Code 4.3.1
#--- Aufteilung von find_root in mehrere Funktionen ---
def find_root_bounds(x, power):
    """x a float, power a positive int
       return low, high such that low**power <=x and high**power >= x"""
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """x, epsilon, low, high are floats
        epsilon > 0
        low <= high and there is an ans between low and high s.t.
            ans**power is within epsilon of x
        returns ans s.t. ans**power within epsilon of x"""
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

def find_root(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None"""
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high)
#---



#Zum Testen von Code 4.3.1:

x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons) #test_find_root ist definiert in Code 4.1.1.2 (s.o.)

#Das funktioniert offensichtlich genauso, wie die monolithische Fassung von find_root,
#siehe Abschnitt 4.1.1 .



#------------------------------------------------------------------------------------
#                             4.4 Funktionen als Objekte
#------------------------------------------------------------------------------------

#In Python sind Funktionen Objekte erster Klasse. Das heißt, sie können wie Objekte 
#jedes anderen Typs, z.B. int oder list, behandelt werden. Sie haben Typen, z.B. hat 
#der Ausdruck 

type(abs)     #builtin_function_or_method

#den Wert builtin_function_or_method; sie können in Ausdrücken erscheinen, 
#z.B. als rechte Seite einer Zuweisungsanweisung oder als Argument für eine Funktion; 
#sie können von Funktionen zurückgegeben werden; usw.

#Die Verwendung von Funktionen als Argumente ermöglicht eine Art der Programmierung, die als
#Programmierung höherer Ordnung (higher-order programming) bezeichnet wird, siehe:
#--------------------------------------------------------
#  
# https://en.wikipedia.org/wiki/Higher-order_programming
#
#Diese ermöglicht es uns, Funktionen zu schreiben, die allgemeiner nützlich sind. 
#Z.B. kann die Funktion bisection_solve im Code 4.3.1 (s.o) so umgeschrieben werden, 
#dass sie auch für andere Aufgaben als die Wurzelbestimmung verwendet werden kann, 
#wie dies im folgenden Code 4.4.1 gezeigt wird.



#Code 4.4.1
#--- Verallgemeinerte (higher-order) Bisektionssuche ---
def bisection_solve(x, eval_ans, epsilon, low, high):
    """x, epsilon, low, high are floats
       epsilon > 0
       eval_ans a function mapping a float to a float
       low <= high and there is an ans between low and high s.t.
           eval(ans) is within epsilon of x
       returns ans s.t. eval(ans) within epsilon of x"""
    ans = (high + low)/2
    while abs(eval_ans(ans) - x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
#---



#Wir beginnen damit, den ganzzahligen Parameter power durch eine Funktion eval_ans zu 
#ersetzen, die Gleitkommazahlen auf Gleitkommazahlen abbildet. Dann ersetzen wir jede 
#Instanz des Ausdrucks ans**power durch den Funktionsaufruf eval_ans(ans).

#Wenn wir die neue Funktion bisection_solve verwenden wollten, um z.B. eine Annäherung 
#an die Quadratwurzel von 99 zu bestimmen, könnten wir den folgenden Code ausführen
#(die Codes 4.3.1 und 4.4.1 werden ebenfalls benötigt) ... 

def square(ans):
    return ans ** 2

low, high = find_root_bounds(99, 2)
print(bisection_solve(99, square, 0.01, low, high))    #9.94970703125

#Sich die Mühe zu machen, eine Funktion zu definieren, um etwas so Einfaches wie das 
#Quadrieren einer Zahl auszuführen, scheint ein wenig albern. Zufälligerweise unterstützt Python
#die Erstellung von anonymen Funktionen (d.h. Funktionen, die nicht an einen Namen gebunden 
#sind), unter Verwendung des reservierten Wortes lambda. 
#Die allgemeine Form eines lambda-Ausdrucks (lambda expression) ist:
#                          -----------------------------------

#          lambda sequence of variable names : expression

#Zum Beispiel gibt der Lambda-Ausdruck 
#                 lambda x, y: x*y 
#eine Funktion zurück, die das Produkt ihrer beiden Argumente zurückgibt. Lambda-Ausdrücke 
#werden häufig als Argumente für Funktionen höherer Ordnung verwendet. 
#Siehe dazu auch:
#  
# https://en.wikipedia.org/wiki/Lambda_expression
# https://en.wikipedia.org/wiki/Anonymous_function
#
#Wir könnten zum  Beispiel den obigen Aufruf von bisection_solve durch Folgendes esetzen:

print(bisection_solve(99, lambda ans: ans**2, 0.01, low, high))    #9.94970703125



###############
#Aufgabe 4.4.a:
###############
#Schreiben Sie einen Lambda-Ausdruck mit zwei numerischen Parametern. Wenn das zweite 
#Argument gleich Null ist, sollte er None returnieren. Andernfalls sollte er den Wert 
#zurückgeben, der sich aus der Division des ersten Arguments durch das zweite Argument
#ergibt. Tipp: Verwenden Sie einen (ternären) bedingten Ausdruck.
###############
#3 ist ein Rückgabewert
3 if 4<2 else 5

if 3 < 2:
    print('Kein Rückgabewert')
else:
    print('Kein Rückg.wert')

#Da Funktionen Objekte erster Klasse sind, können sie innerhalb von Funktionen erstellt 
#und innerhalb von Funktionen zurückgegeben werden. Zum Beispiel, wenn die Funktions-
#definition lautet


#Nennt sich let over lambda

def create_eval_ans():
    power = input('Enter a positive integer: ')
    return lambda ans: ans**int(power)

#dann wird die Ausführung des folgenden Codes (die Codes 4.3.1 und 4.4.1 werden ebenfalls
#benötigt) ... 

eval_ans = create_eval_ans()
print(bisection_solve(99, eval_ans, 0.01, low, high))

#eine Annäherung an die n-te Wurzel aus 99 ergeben, wobei n eine vom Benutzer eingegebene 
#Zahl ist. Wenn z.B. 10 eingegeben wird (power ist dann 10), dann wird die 10-te Wurzel
#von 99 berechnet. Das wäre dann 1.58331298828125

#Die Art und Weise, wie wir bisection_solve verallgemeinert haben, bedeutet, dass es
#nicht nur für Approximationen von Wurzeln verwendet werden kann, sondern auch für
#Approximationen an eine beliebige monotone (also nicht-schwankende, sondern eben monoton
#steigende oder fallende) Funktion, die Floats auf Floats abbildet. Der folgende Code 4.4.2 
#verwendet zum Beispiel bisection_solve, um Approximationen von Logarithmen zu finden.



#Code 4.4.2
#--- Verwendung von bisection_solve zur Approximation von Logs ---
def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
           x > 1, epsilon > 0 & power >= 1
       Returns float y such that base**y is within epsilon of x."""
    def find_log_bounds(x, base):
        upper_bound = 0
        while base**upper_bound < x:
            upper_bound += 1
        return upper_bound - 1, upper_bound
    low, high = find_log_bounds(x, base)
    return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)
#---



#Beachten Sie, dass die Implementierung von log die Definition einer lokalen Funktion, 
#find_log_bounds beinhaltet. Diese Funktion hätte man auch außerhalb von log definieren 
#können, aber da wir nicht erwarten, sie in einem anderen Kontext zu verwenden, schien es 
#besser, dies nicht zu tun.

#Und zum Testen von Code 4.4.2 haben wir folgendes:
import math

def test_log():
    epsilon = 0.001
    for b in range(2, 6):
        for x in range(1, 100):
            if abs(math.log(x, b) - log(x, b, epsilon)) > epsilon:
                print('Failed on', x, b)
    print('Finished test_log')

test_log()      #ergibt: Finished test_log
#D.h. die in diesen Schleifen definierten Logarithmen konnten alle durch die
#Funktion log approximiert werden.



#------------------------------------------------------------------------------------
#                             4.5 Methoden (stark vereinfacht/verkürzt erläutert)
#------------------------------------------------------------------------------------

#Methoden sind funktionsähnliche Objekte. Sie können aufgerufen werden mit Parametern, 
#sie können Werte zurückgeben und sie können Seiteneffekte haben. Sie unterscheiden sich 
#von Funktionen in einigen wichtigen Punkten, die wir im Kontext der OOP mit Klassen 
#kennengelernt haben und die wir im Kapitel 10 nochmals vertiefen wollen.

#Betrachten Sie Methoden vorerst als eine besondere Syntax für einen Funktionsaufruf. 
#Anstatt das erste Argument in Klammern nach dem Funktionsnamen zu setzen, verwenden wir 
#die Punktnotation (dot notation), um dieses Argument vor den Funktionsnamen zu setzen. 
#Wir führen Methoden ein, weil viele nützliche Operationen mit eingebauten Typen Methoden 
#sind und daher in Punktschreibweise aufgerufen werden. Wenn zum Beispiel s eine 
#Zeichenkette ist, kann die find-Methode verwendet werden, um den Index des ersten
#Vorkommens einer Teilzeichenkette in s zu bestimmen. Wenn s also 'abcbc' wäre, 

s = 'abc'

#würde der Aufruf

s.find('bc')

#1 zurückgeben. Der Versuch, find wie eine Funktion zu behandeln, z.B. der Aufruf von 
 
find(s,'bc')

#erzeugt die Fehlermeldung NameError: name 'find' is not defined



###############
#Aufgabe 4.5.a:
###############
#Was gibt s.find(sub) zurück, wenn sub nicht in s vorkommt?
###############

print(s.find('sub'))

###############
#Aufgabe 4.5.b:
###############
#Verwenden Sie find, um eine Funktion zu implementieren, die der folgenden
#Spezifikation genügt:
def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
###############



#------------------------------------------------------------------------------------
#                             4.6 In diesem Kapitel eingeführte Begriffe
#------------------------------------------------------------------------------------

#       function definition
#       formal parameter
#       actual parameter
#       argument
#       function invocation (function call)
#       return statement
#       point of execution
#       lambda abstraction
#       test function
#       debugging
#       positional argument
#       keyword argument
#       default parameter value
#       unpacking operator (*)
#       name space
#       scope
#       local variable
#       symbol table
#       stack frame
#       static (lexical) scoping
#       stack (LIFO)
#       specification
#       client
#       assumption
#       guarantee
#       decomposition
#       abstraction
#       docstring
#       help function
#       first-class object
#       higher-order programming
#       lambda expression
#       method
#       dot notation


#####################################################################################
#####################################################################################
#FINIS