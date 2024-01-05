###############
#Lösung 3.1.b
###############

# Eingabeaufforderung für den Benutzer, um eine ganze Zahl einzugeben
x = int(input('Integer eingeben: '))


# Äußere Schleife: i durchläuft Werte von 1 bis x-1
for i in range(1, x):
    # Innere Schleife: j durchläuft Werte von 2 bis 5
    for j in range(2, 6):
        # Überprüft, ob i hoch j gleich x ist
        if i ** j == x:
            # Wenn die Bedingung wahr ist, wird das Paar (i, j) ausgegeben
            print(f'Root: {i} Potenz: {j}')
            # Unterbricht die innere Schleife, wenn ein Paar gefunden wird
            break
    # Überprüft erneut, ob die Bedingung erfüllt ist und bricht die äußere Schleife ab, falls ja
    if i ** j == x:
        break
# Die else-Klausel der for-Schleife wird ausgeführt, wenn kein Paar gefunden wird
else:
    print('Kein Paar gefunden')

# Definition der Funktion root_base
def root_base():
    # Eingabeaufforderung innerhalb der Funktion
    x = int(input('Gebe eine ganze Zahl ein'))

    # Gleiche Schleifenstruktur und Logik wie oben
    for i in range(1, x):
        for j in range(2, 6):
            if i ** j == x:
                print(f'roote: {i} potenz: {j}')
                break
        if i ** j == x:
            break
    else:
        print('Kein Paar gefunden')

# Aufruf der Funktion root_base
root_base()


#################
#Erklärung 3.1.b
#################

'''
Der bereitgestellte Code ist ein Python-Skript, das darauf abzielt,
Wurzel-Potenz-Paare für eine gegebene Zahl zu finden.
Es besteht aus zwei Hauptteilen: einem Skriptblock und einer Funktion namens root_base.
Hier ist eine detaillierte Beschreibung des Codes:

Benutzereingabe:
Der Code beginnt mit einer Aufforderung an den Benutzer, eine ganze Zahl x einzugeben.
Diese Eingabe wird als Ganzzahl (int) interpretiert und in der Variablen x gespeichert.

Suche nach Wurzel-Potenz-Paaren:
Eine verschachtelte Schleife wird verwendet, um Wurzel-Potenz-Paare zu finden,
die der Bedingung i ** j == x genügen, wobei i die Wurzel und j die Potenz ist.
Die äußere Schleife lässt i Werte von 1 bis x-1 durchlaufen.
Innerhalb der äußeren Schleife gibt es eine innere Schleife,
in der j Werte von 2 bis 5 durchläuft.
In jeder Iteration der inneren Schleife wird geprüft, ob i ** j gleich x ist.
Falls ja, wird das Paar (i, j) ausgegeben und die innere Schleife wird mittels break beendet.
Nachdem die innere Schleife beendet ist, überprüft der Code erneut, ob i ** j == x ist.
Falls dies der Fall ist, wird auch die äußere Schleife beendet.
Falls kein entsprechendes Paar gefunden wird, gibt der Code nach Beendigung der äußeren Schleife
die Nachricht "Kein Paar gefunden" aus. Dies wird durch die else-Klausel der for-Schleife ermöglicht.

Funktion root_base:
Die Funktion root_base ist im Wesentlichen eine Wiederholung des oben beschriebenen Codes.
Sie fordert den Benutzer auf, eine ganze Zahl einzugeben und sucht dann nach Wurzel-Potenz-Paaren für diese Zahl.
Die gleiche Logik und Schleifenstruktur wie im Skriptblock wird innerhalb dieser Funktion angewendet.
Nachdem die Funktion definiert wurde, wird sie aufgerufen, um ihre Funktionalität auszuführen.

Zusammenfassend ist das Ziel dieses Codes, für eine eingegebene ganze Zahl x ein Paar von Zahlen (i, j) zu finden,
sodass i hoch j gleich x ist. Der Code führt diese Suche sowohl im Hauptteil
des Skripts als auch in einer separaten Funktion durch. Wenn kein solches Paar gefunden wird,
informiert er den Benutzer entsprechend.
'''

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

#################
#Erklärung 3.2.b
#################

'''
Der bereitgestellte Python-Code definiert eine Funktion annaehere_kubikwurzel, die darauf abzielt,
eine Annäherung an die Kubikwurzel einer gegebenen Zahl zu finden.
Der Code verwendet das Bisektionsverfahren, eine Methode der numerischen Analysis,
um eine Näherungslösung zu ermitteln.
Nachfolgend wird der Code detailliert beschrieben:

Funktionsdefinition und Parameter:
Die Funktion annaehere_kubikwurzel nimmt zwei Parameter entgegen: zahl, die Kubikwurzel, die berechnet werden soll,
und genauigkeit, die die Genauigkeit der berechneten Annäherung angibt.
Der Standardwert für genauigkeit ist 0.01.

Initialisierung:
Die Variable versuchsanzahl wird initialisiert, um die Anzahl der durchgeführten Iterationen zu zählen.
Es werden zwei Grenzwerte festgelegt: untere_grenze und obere_grenze.
Diese Grenzen definieren den Bereich, in dem die Kubikwurzel gesucht wird.
Für positive Zahlen wird untere_grenze auf 0 und obere_grenze auf das Maximum von 1
und der gegebenen Zahl gesetzt. Für negative Zahlen wird untere_grenze auf
das Minimum von -1 und der Zahl und obere_grenze auf 0 gesetzt.

Bisektionsverfahren:
Die Schleife wird solange ausgeführt, bis die Differenz zwischen schaetzung**3 (der dritten Potenz der Schätzung)
und der gegebenen Zahl zahl kleiner als die vorgegebene genauigkeit ist.
In jeder Iteration der Schleife wird zunächst geprüft, ob schaetzung**3 kleiner als zahl ist.
Wenn ja, wird untere_grenze auf den aktuellen Schätzwert schaetzung gesetzt.
Andernfalls wird obere_grenze auf schaetzung gesetzt.
Die neue Schätzung wird als Mittelwert der aktuellen untere_grenze und obere_grenze berechnet.
Die Anzahl der Versuche wird in jeder Iteration um eins erhöht.

Ergebnisausgabe:
Nachdem die Schleife beendet ist, wird die Anzahl der Versuche ausgegeben, um die Annäherung zu erreichen.
Die Funktion gibt den geschätzten Wert der Kubikwurzel zurück.

Testen der Funktion:
Am Ende des Codes wird die Funktion annaehere_kubikwurzel mit zwei Beispielen getestet: einmal mit der 
positiven Zahl 27 und einmal mit der negativen Zahl -27.

Zusammenfassend verwendet dieser Code das Bisektionsverfahren, um eine Annäherung an die Kubikwurzel einer gegebenen
Zahl zu finden und demonstriert dabei eine Anwendung der numerischen Methoden in Python.
'''

###############
#Aufgabe Lösung 3.2.c:
############### 

def finde_sicherstes_stockwerk():
    hoehe = 102  # Höhe des Gebäudes in Stockwerken
    niedrig = 0
    versuche = 0
    maximale_eier = 7

    while niedrig < hoehe and versuche < maximale_eier:
        versuche += 1
        mitte = (niedrig + hoehe) // 2
        print(f"Versuch {versuche}: Teste Stockwerk {mitte}")

        eierwurf_ergebnis = simuliere_eierwurf(mitte)

        if eierwurf_ergebnis:  # Ei zerbricht
            hoehe = mitte
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
#Erklärung 3.2.c
#################

'''
Hauptfunktion: finde_sicherstes_stockwerk
Zweck: Bestimmen des höchsten Stockwerks, von dem ein Ei fallen gelassen werden kann, ohne zu zerbrechen.
Parameter: Keine expliziten Parameter.
Rückgabewert: Die Nummer des sichersten Stockwerks.
Funktionsablauf

Initialisierung:
hoehe: Stellt die Höhe des Gebäudes in Stockwerken dar, initialisiert mit 102.
niedrig: Der Startpunkt der Suche, initialisiert mit 0.
versuche: Zählt die Anzahl der durchgeführten Tests, initialisiert mit 0.
maximale_eier: Begrenzt die Anzahl der Versuche, hier auf 7 festgelegt.
Hauptschleife:

Die Schleife läuft, solange niedrig < hoehe und die Anzahl der versuche kleiner als maximale_eier ist.
Bei jedem Durchlauf wird versuche um 1 erhöht.
mitte: Berechnet das mittlere Stockwerk zwischen niedrig und hoehe.
Eierwurf-Simulation:

Aufruf der Funktion simuliere_eierwurf mit dem aktuellen mitte-Wert.
Je nach Ergebnis (Ei zerbricht oder bleibt ganz) wird der Suchbereich angepasst:
Wenn das Ei zerbricht (eierwurf_ergebnis == True), wird hoehe auf mitte gesetzt.
Wenn das Ei ganz bleibt, wird niedrig auf mitte + 1 gesetzt.
Ergebnis:

Die Funktion gibt den Wert von niedrig zurück, sobald die Schleife beendet ist. 
Dies repräsentiert das sicherste Stockwerk.
Hilfsfunktion: simuliere_eierwurf
Zweck: Simuliert den Eierwurf von einem bestimmten Stockwerk.
Parameter:
stockwerk: Das Stockwerk, von dem das Ei geworfen wird.
Rückgabewert: Ein boolescher Wert, der angibt, ob das Ei beim Wurf zerbricht.
Funktionsablauf
Simulation:
Die Funktion nutzt die random-Bibliothek, um ein kritisches Stockwerk zufällig auszuwählen.
Der Vergleich stockwerk >= kritisches_stockwerk bestimmt, ob das Ei zerbricht.
Hauptprogramm
Das Hauptprogramm ruft finde_sicherstes_stockwerk auf und speichert das Ergebnis in sicherstes_stockwerk.
Anschließend wird das Ergebnis ausgegeben: "Das höchste Stockwerk, von dem ein Ei fallen gelassen werden kann,
ohne zu zerbrechen, ist: [sicherstes_stockwerk]".

Zusammenfassung
Dieser Code verwendet eine binäre Suchstrategie, um effizient das "sicherste" Stockwerk in einem hohen Gebäude
zu ermitteln, von dem ein Ei fallen gelassen werden kann, ohne zu zerbrechen. Die Simulation setzt dabei eine
begrenzte Anzahl von Versuchen (Eier) voraus und verwendet eine zufällige Auswahl,
um das kritische Stockwerk zu bestimmen.
'''

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
#Erklärung 4.1.1.b
#################

'''
Die Funktion is_in ist dazu bestimmt, zu überprüfen, ob eine der beiden übergebenen Zeichenketten (str1 oder str2)
in der anderen enthalten ist. Hier ist eine detaillierte Erläuterung der Funktionsweise
und der verwendeten Syntax:
Funktion: is_in

Parameter:
str1 (str): Die erste Zeichenkette.
str2 (str): Die zweite Zeichenkette.

Rückgabewert:
bool: Die Funktion gibt einen booleschen Wert (True oder False) zurück.
True: Wird zurückgegeben, wenn str1 in str2 enthalten ist oder umgekehrt.
False: Wird zurückgegeben, wenn keine der Zeichenketten in der anderen enthalten ist.
Funktionsweise
Logische Operation:
Die Funktion nutzt den in Operator in Python, der überprüft, ob eine Zeichenkette Teil einer anderen ist.
str1 in str2 überprüft, ob str1 in str2 enthalten ist.
str2 in str1 überprüft, ob str2 in str1 enthalten ist.
Der logische Operator or wird verwendet, um zu prüfen, ob eine der beiden Bedingungen True ergibt.
Wenn ja, gibt die Funktion True zurück, sonst False.

Beispiele
print(is_in("Hallo", "Welt")):

Überprüft, ob "Hallo" in "Welt" enthalten ist oder umgekehrt.
Da keines in dem anderen enthalten ist, gibt die Funktion False zurück.
print(is_in("Hallo", "Hallo Welt")):

Überprüft, ob "Hallo" in "Hallo Welt" enthalten ist oder umgekehrt.
Da "Hallo" ein Teil von "Hallo Welt" ist, gibt die Funktion True zurück.

Zusammenfassung
Die Funktion is_in ist eine einfache und effektive Methode, um zu bestimmen, 
ob eine Zeichenkette in einer anderen enthalten ist. Sie kann in verschiedenen Kontexten verwendet werden,
wie zum Beispiel beim Textvergleich oder der Suche in Zeichenketten.
'''

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

#################
#Erklärung 4.1.1.b
#################

'''
Die Funktion test_is_in ist eine Testfunktion, die darauf abzielt, verschiedene Szenarien für eine andere
Funktion namens is_in zu überprüfen. Die is_in-Funktion (die nicht im bereitgestellten Code enthalten,
aber implizit definiert ist) soll überprüfen, ob einer von zwei gegebenen Strings im anderen enthalten ist. 
Hier ist eine Erläuterung der Testfunktion:

Funktion: test_is_in
Zweck: Testen der Funktionalität der is_in-Funktion in verschiedenen Szenarien.
Testfälle in der Funktion:

Testfall 1 - Gleiche Strings:
assert is_in("test", "test"): Überprüft, ob der String "test" in sich selbst enthalten ist.
Die Fehlermeldung "Fehler: 'test' sollte in 'test' enthalten sein." wird ausgegeben, falls der Test fehlschlägt.

Testfall 2 - Erster String im zweiten enthalten:
assert is_in("Hallo", "Hallo Welt"): Testet, ob der String "Hallo" im String "Hallo Welt" enthalten ist.
Die Fehlermeldung für einen Fehlschlag lautet hier: "Fehler: 'Hallo' sollte in 'Hallo Welt' enthalten sein."

Testfall 3 - Zweiter String im ersten enthalten:
assert is_in("Welt Hallo", "Hallo"): Überprüft, ob "Hallo" im String "Welt Hallo" enthalten ist.
Im Falle eines Fehlschlags wird die Nachricht "Fehler: 'Hallo' sollte in 'Welt Hallo' enthalten sein." angezeigt.

Testfall 4 - Strings nicht ineinander enthalten:
assert not is_in("Hallo", "Welt"): Stellt sicher, dass "Hallo" nicht im String "Welt" enthalten ist.
Bei einem Fehlschlag erscheint die Fehlermeldung "Fehler: 'Hallo' sollte nicht in 'Welt' enthalten sein."

Testdurchführung:
Die Funktion test_is_in führt diese Tests aus und gibt "Alle Tests erfolgreich durchgeführt." aus,
wenn alle assert-Anweisungen bestehen, d.h., wenn alle Tests die erwarteten Ergebnisse liefern.
Die Verwendung von assert bedeutet, dass bei einem Fehlschlagen eines Tests eine Ausnahme ausgelöst
wird und die Ausführung der Funktion abgebrochen wird. Dies zeigt an, dass die is_in-Funktion nicht
wie erwartet funktioniert.

Zusammenfassung
Die test_is_in-Funktion dient als eine Reihe von automatisierten Tests, um sicherzustellen, 
dass die is_in-Funktion korrekt arbeitet. Solche Testfunktionen sind in der Softwareentwicklung üblich, 
um die Zuverlässigkeit und Korrektheit des Codes zu gewährleisten.
'''

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

#################
#Erklärung 4.2 a
#################

'''
Die Funktion log ist dazu gedacht, eine Annäherung an den Logarithmus einer Zahl x zur Basis base zu finden.
Hier ist eine detaillierte Erklärung des Codes:

Parameter der Funktion log

x: Die Zahl, deren Logarithmus berechnet werden soll. Es wird angenommen, dass x ein Integer oder Float ist
und größer als 1.
base: Die Basis des Logarithmus. Es wird angenommen, dass base ein Integer ist und mindestens 1.
epsilon: Die Genauigkeit der Annäherung. Es wird angenommen, dass epsilon ein Integer oder Float
ist und größer als 0.
Funktionsablauf

Initialisierung der Grenzwerte:
low wird auf 0 gesetzt.
high wird auf das Maximum von 1 und x gesetzt, um sicherzustellen, dass der Bereich, in dem gesucht wird, sinnvoll ist.

Anfängliche Schätzung:
guess (die geschätzte Potenz) wird als der Mittelwert zwischen low und high initialisiert.

Suchschleife:
Die Schleife wird so lange ausgeführt, bis der Unterschied zwischen base**guess und x kleiner als epsilon ist, was bedeutet, dass eine ausreichende Annäherung erreicht wurde.

Innerhalb der Schleife:
Wenn base**guess kleiner als x ist, wird low auf den aktuellen Schätzwert guess gesetzt.
Andernfalls, wenn base**guess größer oder gleich x ist, wird high auf guess gesetzt.
Nach jeder Anpassung der Grenzen wird guess neu berechnet als der Mittelwert von low und high.
Rückgabe:

Die Funktion gibt den geschätzten Wert guess zurück, sobald die Annäherung innerhalb der vorgegebenen 
Genauigkeit epsilon liegt.
Testbeispiele
log(8, 2, 0.01): Berechnet eine Annäherung an den Logarithmus von 8 zur Basis 2 (log2(8)) 
mit einer Genauigkeit von 0.01.
log(9, 10, 0.001): Berechnet eine Annäherung an den Logarithmus von 9 zur Basis 10 (log10(9))
mit einer Genauigkeit von 0.001.

Zusammenfassung
Diese Funktion ist ein gutes Beispiel für die Anwendung des Bisektionsverfahrens, 
einer effizienten Methode zur Lösung von Problemen, bei denen eine kontinuierliche 
Funktion (in diesem Fall base**y - x) innerhalb eines bestimmten Bereichs (zwischen low und high)
einen bestimmten Wert (nahe 0) erreichen soll. Durch wiederholtes Halbieren des Suchbereichs nähert
sich die Funktion einer Lösung an, die der realen Lösung des Logarithmus von x zur Basis base sehr nahekommt.
'''

###############
#Lösung Aufgabe 4.4.a:
###############

teile = lambda x, y: None if y == 0 else x / y

#Testen:
teile(5,2)   # 2.5
teile(6,0)   # None

#################
#Erklärung 4.4.a
#################

'''
Der bereitgestellte Code definiert einen Lambda-Ausdruck namens teile, der zwei Parameter x und y annimmt
 und eine bedingte Operation ausführt:

Lambda-Ausdruck: teile
Zweck: Berechnet die Division von x durch y und behandelt dabei den Fall, dass y gleich Null ist.

Struktur:
lambda x, y: Definiert einen anonymen (lambda) Funktion, die zwei Argumente x (Dividend) und y (Divisor) akzeptiert.
None if y == 0 else x / y: Ein bedingter Ausdruck (auch als ternärer Operator bekannt).
Bedingung: y == 0
Wenn y gleich Null ist, könnte eine Division zu einem Division-durch-Null-Fehler führen. Um dies zu vermeiden,
gibt der Ausdruck in diesem Fall None zurück.
Andernfalls: x / y
Wenn y nicht Null ist, führt der Ausdruck die Division von x durch y aus und gibt das Ergebnis zurück.

Testfälle
teile(5, 2):
x = 5 und y = 2.
Da y nicht Null ist, wird die Division durchgeführt: 5 / 2, was 2.5 ergibt.
Das Ergebnis ist 2.5.
teile(6, 0):

x = 6 und y = 0.
Da y gleich Null ist, könnte eine Division durch Null stattfinden, was nicht erlaubt ist.
Der Lambda-Ausdruck gibt daher None zurück, um einen Fehler zu vermeiden.
Das Ergebnis ist None.

Zusammenfassung
Der Lambda-Ausdruck teile ist eine kurze und effiziente Methode, um eine sichere Division durchzuführen.
Er vermeidet Division-durch-Null-Fehler, indem er None zurückgibt, wenn der Divisor 0 ist,
und führt andernfalls die reguläre Division aus.
'''

###############
#Lösung Aufgabe 5.3.a:
############### 
L = [1, 2, 3]
L.append(L)
print(L)
'''Die Aufgabe zeigt, dass eine Liste sich selbst als Element enthalten kann.
 Dies führt zu einer Art von "unendlicher" Verschachtelung,
   wenn man versucht, die Liste auszudrucken oder zu inspizieren.
'''
print(L is L[-1])

#################
#Erklärung 5.3.a
#################

'''
Code-Teil 1: Erstellen und Modifizieren der Liste
L = [1, 2, 3]
L.append(L)
print(L)

Erstellen der Liste L: Zunächst wird eine Liste L mit den Elementen [1, 2, 3] erstellt.
Selbstreferenzierung: Anschließend wird die Liste L selbst als ein weiteres Element an L angehängt.
Nach dieser Operation enthält L vier Elemente: die drei ursprünglichen Zahlen und die Liste selbst.
Ausgabe der Liste: Der print-Befehl gibt L aus. Das Ergebnis ist [1, 2, 3, [...]]. Hierbei steht [...] 
für die Selbstreferenz der Liste L. Python verhindert eine unendliche Rekursion bei der Ausgabe,
indem es die Selbstreferenz mit [...] kennzeichnet.

Code-Teil 2: Überprüfen der Objektidentität
print(L is L[-1])

Vergleich mit 'is': Der is-Operator überprüft, ob zwei Referenzen dasselbe Objekt im Speicher zeigen.
L ist eine Referenz auf die Liste.
L[-1] ist eine Referenz auf das letzte Element in L, welches, aufgrund der vorherigen Operation, L selbst ist.
Ergebnis des Vergleichs: Da L[-1] direkt auf L verweist (sie sind dasselbe Objekt), 
ist der Ausdruck L is L[-1] True.

Zusätzliche Erläuterungen
Unendliche Verschachtelung: In Python können Listen selbstreferenziell sein, d.h., sie können 
sich selbst als Element enthalten. Dies führt jedoch nicht zu einer tatsächlich unendlichen Liste. 
Vielmehr entsteht eine Art von Verschachtelung, bei der ein Element der Liste auf die Liste selbst verweist.

Vermeidung von unendlicher Rekursion: Python handhabt die Ausgabe von selbstreferenziellen Listen intelligent, 
um eine unendliche Rekursion zu vermeiden. Statt die Liste unendlich oft auszugeben, 
wird die Selbstreferenz durch [...] symbolisiert.

Objektidentität vs. Gleichheit: Der is-Operator überprüft die Identität, nicht die Gleichheit. 
Zwei Variablen sind identisch, wenn sie auf dasselbe Objekt im Speicher verweisen. 
In diesem Fall sind L und L[-1] identisch, da sie auf dasselbe Listenobjekt verweisen.
Zusammengefasst zeigt dieser Code ein besonderes Verhalten von Listen in Python, 
das Selbstreferenz und die Verwendung des is-Operators zur Überprüfung der Objektidentität umfasst.
'''


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

#################
#Erklärung 5.4.a
#################
'''
Die Funktion f, wie sie im bereitgestellten Code definiert ist, berechnet die Summe der Potenzen
von korrespondierenden Elementen zweier Listen gleicher Länge. 
Hier ist eine detaillierte Erklärung des Codes:

Funktion f
Parameter
L1, L2: Zwei Listen mit numerischen Werten. Es wird erwartet, dass beide Listen die gleiche Länge haben.
Rückgabewert
Die Funktion gibt eine einzelne Zahl zurück, die die Summe der Potenzen der korrespondierenden Elemente aus
L1 und L2 darstellt.

Funktionsweise

Map-Funktion:
map(lambda x, y: x**y, L1, L2): Die map-Funktion wendet eine angegebene Funktion (hier ein Lambda-Ausdruck) 
auf jedes Element-Paar der beiden Listen L1 und L2 an.
Der Lambda-Ausdruck lambda x, y: x**y nimmt ein Element x aus L1 und ein Element y 
aus L2 und berechnet x hoch y.

Summierung:
sum(...): Die sum-Funktion berechnet die Gesamtsumme aller Werte, die von der map-Funktion zurückgegeben werden.
Das bedeutet, dass für jedes Paar (x, y) aus L1 und L2 die Potenz x**y berechnet und zur Gesamtsumme addiert wird.

Beispiel
f([1, 2], [2, 3]):
Für das erste Element-Paar (1, 2) wird 1^2 = 1 berechnet.
Für das zweite Element-Paar (2, 3) wird 2^3 = 8 berechnet.
Die Summe dieser Werte ist 1 + 8 = 9.

Zusammenfassung
Die Funktion f ist eine elegante und effiziente Art, die Summe der Potenzen von Paaren 
korrespondierender Elemente aus zwei Listen zu berechnen. Sie ist besonders nützlich, 
wenn man Operationen auf Paaren von Datenpunkten ausführen möchte, die in zwei separaten Listen gespeichert sind.
'''

###############
#Lösung 5.8.a:
############### 

# Erweiterte gen_code_keys Funktion
def gen_code_keys_erweitert(book, plain_text):
    erweitertes_buch = book + '#'  # Füge ein spezielles Zeichen am Ende des Buchs hinzu
    return {c: str(erweitertes_buch.find(c)) if c in book else str(len(book)) for c in plain_text}

# Beispiel
Don_Quixote = '''In a village of La Mancha, the name of which I have no desire to call to mind,
                there lived not long since one of those gentlemen that keep a lance in the lance-rack,
                  an old buckler, a lean hack, and a greyhound for coursing'''

plain_text = "Hello Cypher Punk"

# Generiere Kodierungswörterbuch
kodierungswörterbuch = gen_code_keys_erweitert(Don_Quixote, plain_text)
print(kodierungswörterbuch)

#################
#Erklärung 5.8.a
#################
'''
Der Codeausschnitt definiert eine Funktion gen_code_keys_erweitert, die zur Kodierung eines Textes dient, 
basierend auf einem vorgegebenen "Buch" (Textgrundlage). Diese Funktion wird verwendet, 
um eine einfache Form der Verschlüsselung durchzuführen. 

Hier ist eine detaillierte Erklärung des Codes:

Funktion: gen_code_keys_erweitert
Zweck: Erstellt ein Wörterbuch zur Verschlüsselung eines Textes (plain_text) basierend auf den Positionen 
der Zeichen im gegebenen book.

Parameter:
book: Ein String, der als Grundlage für die Verschlüsselung dient.
plain_text: Der zu verschlüsselende Text.
Funktionsablauf
Erweiterung des Buches:

Das Buch (book) wird um ein spezielles Zeichen '#' am Ende erweitert. 
Dies dient dazu, ein eindeutiges Ende des Buches zu markieren.

Erstellung des Kodierungswörterbuchs:

Für jedes Zeichen c im plain_text wird ein Eintrag im Wörterbuch erstellt.
Wenn das Zeichen c im book vorhanden ist, wird der Index dieses Zeichens (seine Position im book) 
als String gespeichert.
Falls das Zeichen c nicht im book vorkommt, wird die Länge des book (ohne das zusätzliche '#') als 
Ersatzwert verwendet.
Das resultierende Wörterbuch bildet jeden Buchstaben des plain_text auf seine Position im book 
oder auf die Länge des book ab.
Beispiel
Buch (Don_Quixote): Ein langer Textausschnitt, der als Grundlage für die Verschlüsselung dient.
Zu verschlüsselnder Text (plain_text): "Hello Cypher Punk".

Ausgabe (kodierungswörterbuch): Ein Wörterbuch, das jeden Buchstaben von "Hello Cypher Punk" 
auf seine Position im Text von Don Quixote oder auf die Länge des Textes abbildet.

Anwendung
Dieser Code kann in Kontexten verwendet werden, wo eine einfache Verschlüsselungsmethode benötigt wird, 
etwa in einem Bildungs- oder Unterhaltungsszenario. Es ist jedoch wichtig zu beachten, dass diese Art 
der Verschlüsselung nicht sicher für ernsthafte Anwendungen wie die Übertragung sensibler Daten ist.
'''

###############
# Lösung Aufgabe 5.8.b:
############### 

def decoder(book, cipher_text):
    # Erstelle ein Dekodierungswörterbuch
    decode_keys = {str(book.find(c)): c for c in set(book)}
    return ''.join(decode_keys[code] for code in cipher_text.split('*') if code in decode_keys)

def decrypt(book, cipher_text):
    # Verwende den Decoder, um den Text zu entschlüsseln
    return decoder(book, cipher_text)

# Don Quijote Text
Don_Quixote = """In a village of La Mancha, the name of which I have no desire to call to mind, 
                 there lived not long since one of those gentlemen that keep a lance in the 
                 lance-rack, an old buckler, a lean hack, and a greyhound for coursing"""

# Verschlüsselter Text
cipher_text = "22*13*33*155*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*155*59*11*23*11*1*57*6*209*7*11"

# Entschlüsseln des Textes
decrypted_text = decrypt(Don_Quixote, cipher_text)
print(decrypted_text)

#################
#Erklärung 5.8.b
#################
'''
Funktion: decoder
Zweck: Entschlüsselt einen gegebenen verschlüsselten Text (cipher_text) mithilfe eines Buches (book).

Parameter:
book: Der Text, der als Grundlage für die Erstellung des Dekodierungswörterbuchs dient.
cipher_text: Der zu entschlüsselnde Text.
Rückgabewert: Der entschlüsselte Text als Zeichenkette.
Funktionsablauf
Erstellung des Dekodierungswörterbuchs (decode_keys):

Für jeden einzigartigen Buchstaben im Buch book wird ein Schlüssel-Wert-Paar im Wörterbuch erstellt.
Der Schlüssel ist die Position des Buchstabens im Text book, konvertiert in einen String.
Der Wert ist der Buchstabe selbst.
Entschlüsselungsprozess:

Der cipher_text wird anhand des Sternzeichens * in einzelne Codes zerlegt.
Für jeden Code wird im Dekodierungswörterbuch nach dem entsprechenden Buchstaben gesucht.
Die Buchstaben werden zusammengesetzt, um den entschlüsselten Text zu bilden.

Funktion: decrypt
Zweck: Einfache Wrapper-Funktion, die decoder aufruft, um den cipher_text zu entschlüsseln.
Parameter:
book: Der Text, der für die Dekodierung verwendet wird.
cipher_text: Der zu entschlüsselnde Text.
Rückgabewert: Der von decoder zurückgegebene entschlüsselte Text.
Anwendungsbeispiel

Vorbereitung: Der Text von „Don Quijote“ wird als book verwendet.
Verschlüsselter Text (cipher_text): Eine Zeichenkette von durch Sternchen getrennten Zahlen, 
die Positionen von Buchstaben im book repräsentieren.
Durchführung: Der cipher_text wird durch die Funktion decrypt entschlüsselt.
Ergebnis: Der entschlüsselte Text wird ausgegeben.

Zusammenfassung
Dieser Code demonstriert ein einfaches Verfahren zur Textentschlüsselung. 
Es wird ein Buch (oder ein beliebiger Text) verwendet, um ein Dekodierungswörterbuch zu erstellen, 
wobei jeder Buchstabe des Textes durch seine Position repräsentiert wird.
Der verschlüsselte Text besteht aus einer Reihe von Zahlen, die den Positionen der Buchstaben 
im Originaltext entsprechen. Durch das Umwandeln dieser Zahlen zurück in Buchstaben wird der 
Originaltext rekonstruiert.
'''