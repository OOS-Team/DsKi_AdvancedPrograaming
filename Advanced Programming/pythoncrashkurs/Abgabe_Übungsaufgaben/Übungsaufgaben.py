###############
#Aufgabe 3.1.b:
############### 
#Schreiben Sie ein Programm, das den Benutzer auffordert, eine ganze Zahl einzugeben
#und zwei Ganzzahlen, root und pwr, so ausgibt, dass 1 < pwr < 6
#und root**pwr gleich der vom Benutzer eingegebenen ganzen Zahl ist. Wenn kein solches
#Paar von Ganzzahlen existiert, sollte es eine entsprechende Meldung ausgeben.
###############

###############
#Lösung 3.1.b
###############

#i = root
#j = pwr

x = int(input('Integer eingeben: '))
for i in range(1,x):
    for j in range(2,6):
        if i ** j == x:
            print(f'Root: {i} Potenz: {j}')
            break
    if i**j == x:
        break
else:
    print('Kein Paar gefunden')



def root_base():
    x=int(input('Gebe eine ganze Zahl ein'))
    for i in range(1,x):
        for j in range(2,6):
            if i**j==x:
                print(f'roote: {i} potenz: {j}')
                break
        if i**j==x:
            break
    else:
        print('Kein Paar gefunden')

root_base()   

###############
#Aufgabe 3.2.b:
###############  
#Was müsste geändert werden, damit der Code 3.2.2 eine Annäherung an die Kubikwurzel 
#von sowohl negativen als auch positiven Zahlen findet? Tipp: Denken Sie darüber nach, 
#den Wert low zu ändern, um sicherzustellen, dass die Antwort innerhalb des gesuchten 
#Bereichs liegt.
###############
x = 27  # Wir suchen die Kubikwurzel von -27
epsilon = 0.01
num_guesses, low = 0, min(-1, x)
high = max(1, x)
ans = (high + low) / 2
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print('number of guesses =', num_guesses)
print(ans, 'is close to cube root of', x)


# In diesem Beispiel wird low auf min(-1, x) gesetzt, um sicherzustellen,
#  dass der gesuchte Bereich für negative Zahlen korrekt ist.
# Der Code sucht dann nach der Kubikwurzel, indem er ans**3 statt ans**2 verwendet.

###############
#Lösung 3.2.b
###############
# Ziel: Eine Annäherung an die Kubikwurzel von sowohl positiven als auch negativen Zahlen finden

def annaehere_kubikwurzel(zahl, genauigkeit=0.01):
    """
    Diese Funktion findet eine Annäherung an die Kubikwurzel einer Zahl.

    Parameter:
    zahl (int oder float): Die Zahl, von der die Kubikwurzel berechnet werden soll.
    genauigkeit (float): Die Genauigkeit der Annäherung. Standardwert ist 0.01.

    Rückgabe:
    float: Die angenäherte Kubikwurzel von zahl.
    """

    # Initialisiere die Anzahl der Versuche
    versuchsanzahl = 0

    # Bestimme die Anfangswerte für untere_grenze und obere_grenze abhängig vom Vorzeichen der Zahl
    if zahl >= 0:
        untere_grenze = 0
        obere_grenze = max(1, zahl)
    else:
        untere_grenze = min(-1, zahl)
        obere_grenze = 0

    # Initialisiere die Annäherung (Mittelpunkt des Bereichs)
    schaetzung = (obere_grenze + untere_grenze) / 2

    # Wiederhole, bis die Annäherung genau genug ist
    while abs(schaetzung**3 - zahl) >= genauigkeit:
        # Zähle die Versuche
        versuchsanzahl += 1

        # Passe die Grenzen an, je nachdem ob die Schätzung zu klein oder zu groß ist
        if schaetzung**3 < zahl:
            untere_grenze = schaetzung
        else:
            obere_grenze = schaetzung

        # Berechne eine neue Schätzung
        schaetzung = (obere_grenze + untere_grenze) / 2

    # Ausgabe der Ergebnisse
    print(f"Anzahl der Versuche: {versuchsanzahl}")
    return schaetzung

# Teste die Funktion mit einer positiven und einer negativen Zahl
print("Die Kubikwurzel von 27 ist ungefähr:", annaehere_kubikwurzel(27))
print("Die Kubikwurzel von -27 ist ungefähr:", annaehere_kubikwurzel(-27))




###############
#Aufgabe 3.2.c:
###############  
#Das Empire State Building ist 102 Stockwerke hoch. Jemand möchte wissen, aus welchem 
#Stockwerk ein Ei fallen gelassen werden kann, ohne dass es zerbricht. Folgende Idee
#wird verfolgt: ein Ei wird aus dem obersten Stockwerk fallengelassen. Sollte es 
#zerbrechen, würde man eine Etage tiefer gehen und es erneut versuchen. Dies könnte
#man so lange tun, bis das Ei nicht mehr zerbricht. Im schlimmsten Fall benötigt diese 
#Methode 102 Eier. Entwickle eine Methode, die im schlimmsten Fall sieben Eier benötigt.
###############

def finde_sicherstes_stockwerk():
    hoehe = 102  # Höhe des Gebäudes in Stockwerken
    niedrig = 0
    hoch = hoehe
    versuche = 0
    maximale_eier = 7

    while niedrig < hoch and versuche < maximale_eier:
        versuche += 1
        mitte = (niedrig + hoch) // 2
        print(f"Versuch {versuche}: Teste Stockwerk {mitte}")

        # Hier simulieren wir den Eierwurf. In der Praxis müsste hier eine Funktion sein,
        # die überprüft, ob das Ei zerbricht oder nicht.
        eierwurf_ergebnis = simuliere_eierwurf(mitte)

        if eierwurf_ergebnis:  # Ei zerbricht
            hoch = mitte
        else:  # Ei bleibt ganz
            niedrig = mitte + 1

    # Ausgabe des Ergebnisses
    return niedrig

def simuliere_eierwurf(stockwerk):
    import random
    # Diese Funktion simuliert das Ergebnis eines Eierwurfs.
    # In der Praxis müsste hier eine reale Prüfung stattfinden.
    kritisches_stockwerk = random.randint(0, 102)  # Beispielwert
    return stockwerk >= kritisches_stockwerk

# Hauptprogramm
sicherstes_stockwerk = finde_sicherstes_stockwerk()
print(f"Das höchste Stockwerk, von dem ein Ei fallen gelassen werden kann, ohne zu zerbrechen, ist: {sicherstes_stockwerk}")



#################
#Aufgabe 4.1.1.b:
#################
#Schreiben Sie eine Funktion is_in, die zwei Zeichenketten als Argumente akzeptiert
#und True zurückgibt, wenn eine der beiden Zeichenketten irgendwo in der anderen
#vorkommt. Andernfalls soll is_in False zurückgeben. 
#Tipp: Sie können den eingebauten in-Operator in verwenden.
################

###############
#Lösung 4.1.1.b
###############

def is_in(str1, str2):
    """
    Überprüft, ob eine der beiden Zeichenketten in der anderen enthalten ist.

    Parameter:
    str1 (str): Die erste Zeichenkette.
    str2 (str): Die zweite Zeichenkette.

    Rückgabe:
    bool: True, wenn eine der Zeichenketten in der anderen enthalten ist, sonst False.
    """
    return str1 in str2 or str2 in str1


# Beispiele für die Anwendung der Funktion
print(is_in("Hallo", "Welt"))  # Gibt False zurück
print(is_in("Hallo", "Hallo Welt"))  # Gibt True zurück


#################
#Aufgabe 4.1.1.c:
#################
#Schreiben Sie eine Testfunktion für is_in.
################


###############
#Lösung 4.1.1.c
###############

def test_is_in():
    """
    Testet die Funktion is_in mit verschiedenen Szenarien.
    """

    # Testfall 1: Beide Strings sind gleich
    assert is_in("test", "test"), "Fehler: 'test' sollte in 'test' enthalten sein."

    # Testfall 2: Der erste String ist in dem zweiten enthalten
    assert is_in("Hallo", "Hallo Welt"), "Fehler: 'Hallo' sollte in 'Hallo Welt' enthalten sein."

    # Testfall 3: Der zweite String ist in dem ersten enthalten
    assert is_in("Welt Hallo", "Hallo"), "Fehler: 'Hallo' sollte in 'Welt Hallo' enthalten sein."

    # Testfall 4: Die Strings sind nicht ineinander enthalten
    assert not is_in("Hallo", "Welt"), "Fehler: 'Hallo' sollte nicht in 'Welt' enthalten sein."

    print("Alle Tests erfolgreich durchgeführt.")

# Führe die Testfunktion aus
test_is_in()


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

###############
#Lösung 4.2.a
###############

def log(x, base, epsilon):
    """
    Nimmt an, dass x und epsilon int oder float und base ein int sind,
    x > 1, epsilon > 0 und base >= 1.
    Gibt einen float y zurück, so dass base**y innerhalb von epsilon von x ist.
    """

    # Anfangs- und Endwerte für die Suche festlegen
    low = 0
    high = max(1, x)

    # Annäherung an den Logarithmus
    guess = (high + low) / 2.0

    # Wiederhole die Suche, bis die Annäherung gut genug ist
    while abs(base**guess - x) >= epsilon and low <= high:
        if base**guess < x:
            low = guess
        else:
            high = guess

        guess = (high + low) / 2.0

    return guess

# Test der Funktion
print(log(8, 2, 0.01))  # Gibt eine Annäherung an log2(10) zurück
print(log(9, 10, 0.001))  # Gibt eine Annäherung an log10(1000) zurück

###############
#Aufgabe 4.4.a:
###############
#Schreiben Sie einen Lambda-Ausdruck mit zwei numerischen Parametern. Wenn das zweite 
#Argument gleich Null ist, sollte er None returnieren. Andernfalls sollte er den Wert 
#zurückgeben, der sich aus der Division des ersten Arguments durch das zweite Argument
#ergibt. Tipp: Verwenden Sie einen (ternären) bedingten Ausdruck.
###############
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

###############
#Lösung 5.4.a
###############

def f(L1, L2):
    """
    Nimmt zwei Listen gleicher Länge mit Zahlen entgegen und
    gibt die Summe zurück, bei der jedes Element in L1 zur Potenz des Elements
    an der gleichen Position in L2 erhoben wird.
    Zum Beispiel gibt f([1, 2], [2, 3]) 9 zurück.
    """
    return sum(map(lambda x, y: x**y, L1, L2))

# Test der Funktion
print(f([1, 2], [2, 3]))  # Sollte 9 zurückgeben

###############
#Aufgabe 5.8.a:
############### 
#Beheben Sie das oben beschriebene Problem
#Tipp: Ein einfacher Weg, dies zu tun, besteht darin, ein neues Buch zu erstellen, 
#indem Sie etwas(?) an das ursprüngliche Buch anhängen.
###############

def gen_code_keys(book, plain_text):
    # Füge ein spezielles Zeichen am Ende des Buches hinzu
    special_char = "§"  # Kann jedes seltene Zeichen sein, das im normalen Text nicht vorkommt
    book += special_char

    # Erstelle das Kodierungswörterbuch
    return {c: str(book.find(c) if c in book else book.find(special_char)) for c in plain_text}

# Test der Funktion
Don_Quixote = """In a village of La Mancha, the name of which I have no desire to call to mind, 
                 there lived not long since one of those gentlemen that keep a lance in the 
                 lance-rack, an old buckler, a lean hack, and a greyhound for coursing"""

# Verwende nun die modifizierte gen_code_keys Funktion
code_keys = gen_code_keys(Don_Quixote, "xanadu")
print(code_keys)  # '-1' wird nun durch den Index des speziellen Zeichens ersetzt


###############
#Aufgabe 5.8.b:
############### 
#Implementieren Sie anhand der obigen Beispiele encoder und encrypt
#die Funktionen decoder und decrypt. Benutzen Sie diese dann, um die Nachricht
# 22*13*33*155*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*155*59*11*23*11*1*57*6*209*7*11
#zu entschlüsseln, die mit der Buch-Chiffre des Anfangs von Don Quijote (s.o.) verschlüsselt 
#wurde.
###############

#Um die Funktionen `decoder` und `decrypt` zu implementieren,
#  gehen wir ähnlich vor wie bei `encoder` und `encrypt`.
#  Die `decoder`-Funktion nimmt das Dekodierungswörterbuch und
#  den verschlüsselten Text (Cipher-Text) entgegen und gibt den
#  entschlüsselten Text zurück. Die `decrypt`-Funktion erstellt
#  zuerst das Dekodierungswörterbuch mit `gen_decode_keys` und
#  verwendet dann `decoder`, um den Text zu entschlüsseln.

#Hier sind die Implementierungen von `decoder` und `decrypt`:

def gen_decode_keys(book, cipher_text):
    return {s: book[int(s)] for s in cipher_text.split('*') if s.isdigit()}

def decoder(decode_keys, cipher_text):
    return ''.join([decode_keys.get(c, '') for c in cipher_text.split('*')])

def decrypt(book, cipher_text):
    decode_keys = gen_decode_keys(book, cipher_text)
    return decoder(decode_keys, cipher_text)

# Test der Funktionen
Don_Quixote = """In a village of La Mancha, the name of which I have no desire to call to mind, 
                 there lived not long since one of those gentlemen that keep a lance in the 
                 lance-rack, an old buckler, a lean hack, and a greyhound for coursing"""

cipher_text = "22*13*33*155*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*155*59*11*23*11*1*57*6*209*7*11"
decrypted_message = decrypt(Don_Quixote, cipher_text)
print(decrypted_message)

#In `gen_decode_keys` wird das Buch und der verschlüsselte Text verwendet,
#  um ein Dekodierungswörterbuch zu erstellen.
#  Jede Zahl im verschlüsselten Text wird durch das entsprechende Zeichen im Buch ersetzt. 
# Die `decoder`-Funktion setzt dann diese Teile wieder zusammen,
#  um den entschlüsselten Text zu erhalten. Schließlich verwendet `decrypt`
#  diese beiden Funktionen, um den verschlüsselten Text zu entschlüsseln.

#Wenn Sie diesen Code mit dem Anfang von Don Quijote und dem gegebenen 
# verschlüsselten Text ausführen, erhalten Sie die entschlüsselte Nachricht.
