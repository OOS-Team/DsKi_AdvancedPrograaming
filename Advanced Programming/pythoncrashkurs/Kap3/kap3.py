#tw, 16.6.22  



#                         EINIGE EINFACHE NUMERISCHE PROGRAMME





#------------------------------------------------------------------------------------
#                             3.1 Erschöpfende Aufzählung
#------------------------------------------------------------------------------------

#Der folgende Code gibt die ganzzahlige Kubikwurzel, sofern sie existiert, 
#einer ganzen Zahl aus. Wenn die Eingabe kein perfekter Würfel (also eine Kubikzahl) ist, 
#wird eine entsprechende Meldung ausgegeben.
#Der Operator != bedeutet "nicht gleich".


#Code 3.1.1 
#---Suche nach der Kubikwurzel durch erschöpfende Aufzählung---

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,'is', ans)


#Hinweis: probiere z.B. 8, 27, 125 und dann 28

#Der Code versucht zunächst, die Variable ans auf die Kubikwurzel des absoluten Werts 
#von x zu setzen. Gelingt dies, wird ans auf -ans gesetzt, wenn x negativ ist.
#Die eigentliche Arbeit in diesem Code wird in der while-Schleife ausgeführt. 
#Wann immer ein Programm eine Schleife enthält, ist es wichtig zu verstehen,
#was das Programm veranlasst, die Schleife zu verlassen. 
#Für welche Werte von x wird diese while-Schleife enden? Die Antwort lautet "für alle
#Ganzzahlen". Dies lässt sich ganz einfach begründen.

#    - Der Wert des Ausdrucks ans**3 beginnt bei 0 und wird bei jedem Durchlauf 
#      der Schleife größer. 
#    - Wenn er abs(x) erreicht oder überschreitet, wird die Schleife beendet.
#    - Da abs(x) immer positiv ist, gibt es nur eine endliche Anzahl von Iterationen, 
#      bevor die Schleife abgebrochen werden muss. 

#Dieses Argument basiert auf dem Begriff der dekrementierenden Funktion. 
#Dies ist eine Funktion, die die folgenden Eigenschaften hat:

#   - Sie bildet eine Menge von Programmvariablen auf eine Ganzzahl ab.
#   - Beim Eintritt in die Schleife ist ihr Wert nichtnegativ.
#   - Wenn ihr Wert ≤ 0 ist, wird die Schleife beendet.
#   - Ihr Wert wird bei jedem Durchlauf der Schleife verringert.

#Wie lautet die Dekrementierungsfunktion für die while-Schleife im obigen Code ?
#Antw: 
#          abs(x) - ans**3

#Fügen wir nun einige Fehler ein und sehen, was passiert. Versuchen Sie zunächst
#die Anweisung ans = 0 auszukommentieren. Der Python-Interpreter gibt dann die 
#Fehlermeldung aus

#        NameError: name 'ans' is not defined

#weil der Interpreter versucht, den Wert zu finden, an den ans gebunden ist, 
#bevor er an irgendetwas gebunden wurde. Restaurieren Sie die Initialisierung 
#von ans nun wieder und ersetzen Sie die Anweisung 
# ans = ans + 1 durch ans = ans, und versuchen Sie, die Kubikwurzel aus 8 zu finden. 
#Wenn Sie des Wartens müde sind warten, geben Sie <strg>+<c> ein oder drücken Sie 
#den Interrupt-Button ein. Damit kehren Sie zur Eingabeaufforderung in der Shell zurück.
#Fügen Sie nun die Anweisung

#        print('Wert der dekrementierenden Funktion abs(x) - ans**3 ist', abs(x) - ans**3)

#am Anfang der Schleife ein und versuchen Sie, sie erneut auszuführen. Diesmal wird 
#der Wert der dekrementierenden Funktion "abs(x) - ans**3 ist 8" immer wieder ausgegeben.
#Das Programm würde ewig gelaufen, weil der Schleifenkörper nicht mehr den Abstand zwischen 
# ans**3 und abs(x) verringert. Wenn man mit einem Programm konfrontiert wird, 
#das nicht beendet zu werden scheint, fügen erfahrene Programmierer oft Print-Anweisungen 
#ein, wie die, die wir hier eingefügt haben, um zu testen, ob die dekrementierende 
#Funktion tatsächlich dekrementiert.

#Die in diesem Programm verwendete algorithmische Technik der erschöpfenden Aufzählung
#(exhaustive enumaration) ist eine Variante des Prinzips "Erraten und Prüfen" 
#(Guess-and-Check).
#Wir zählen dabei alle Möglichkeiten auf, bis wir die richtige Antwort gefunden haben 
#oder den den Raum der Möglichkeiten erschöpfen. 
#Auf den ersten Blick mag dies eine unglaublich dumme Art zu sein, ein Problem zu lösen. 
#Überraschenderweise sind jedoch Algorithmen mit erschöpfender Aufzählung oft der 
#praktischste Weg ein Problem zu lösen. Sie sind in der Regel einfach zu implementieren 
#und leicht zu verstehen. Und in vielen Fällen laufen sie schnell genug für alle
#praktischen Zwecke. Entfernen oder kommentieren Sie die Druckanweisung aus, die
#die Sie zur Fehlersuche eingefügt haben, und fügen Sie die ursprüngliche (und korrekte)
#Anweisung  ans = ans + 1  wieder ein. 
#Versuchen Sie nun, die Kubikwurzel von 
#           1957816251 
#zu finden. Das Programm wird fast augenblicklich beendet. 
#Versuchen Sie nun 
#           7406961012236344616.
#Wie Sie sehen, ist die Laufzeit des Programms kein Problem, auch wenn Millionen von 
#Schätzungen erforderlich sind. Moderne Computer sind erstaunlich schnell. 
#Es braucht weniger als eine Nanosekunde - ein Milliardstel einer Sekunde - um
#einen Befehl auszuführen. Es ist kaum zu glauben, wie schnell das ist. 
#Zum Vergleich: Licht braucht etwas mehr als eine Nanosekunde, um einen
#einen einzigen Fuß (0,3 Meter) zurückzulegen. Eine andere Möglichkeit, sich das 
#vorzustellen, ist, dass ein moderner Computer in der Zeit, die der Klang Ihrer 
#Stimme für eine Strecke von 100 Fuß braucht, Millionen von Anweisungen ausführen kann.
#Versuchen Sie doch einfach mal, den folgenden Code auszuführen
 

max_val = int(input('Geben Sie eine positive ganze Zahl ein: '))
i = 0
while i < max_val:
    i = i + 1
print(i)


#Hinweis: z.B. 1000, 10000, 100000, 1000000

#Sehen Sie sich an, wie viele ganze Zahlen Sie eingeben müssen, bevor es eine
#eine spürbare Pause gibt, bis das Ergebnis gedruckt wird.
#Schauen wir uns ein weiteres Beispiel für eine erschöpfende Aufzählung an: 
#Testen, ob eine ganze Zahl eine Primzahl ist und den kleinsten Teiler zurückgeben,
#wenn sie es nicht ist. Eine Primzahl ist eine ganze Zahl größer als 1, die
#die nur durch sich selbst und 1 teilbar ist. 2, 3, 5 und 111, 119
#sind Primzahlen, und 4, 6, 8 und 62.710.561 sind keine Primzahlen.
#Der einfachste Weg, um herauszufinden, ob eine ganze Zahl x größer als 3 eine
#Primzahl ist, besteht darin, x durch jede ganze Zahl zwischen 2 und x-1 zu teilen. 
#Wenn der Rest einer dieser Divisionen 0 ist, ist x nicht prim, andernfalls ist x
#Primzahl. Der folgende Code implementiert diesen Ansatz. Er fordert zunächst
#den Benutzer auf, eine ganze Zahl einzugeben, konvertiert die zurückgegebene 
#Zeichenkette in eine ganze Zahl und weist diese der Variablen x zu.
#Anschließend werden die Anfangsbedingungen für eine "erschöpfende Aufzählung" 
#durch Initialisierung von guess auf 2 und die Variable smallest_divisor auf None 
#vorgenommen. Was bedeutet, dass bis zum bis zum Beweis des Gegenteils davon 
#ausgegangen wird, dass x eine Primzahl ist.
#Die erschöpfende Aufzählung erfolgt in einer for-Schleife. Die Schleife
#endet, wenn entweder alle möglichen ganzzahligen Teiler von x durchprobiert wurden
#oder eine ganze Zahl gefunden wurde, die ein Teiler von x ist.
#Nach Verlassen der Schleife prüft der Code den Wert von smallest_divisor und gibt 
#den entsprechenden Text aus.
#Eine Variable vor dem Eintritt in eine Schleife zu initialisieren und anschließend
#zu prüfen, ob dieser Wert beim Verlassen der Schleife geändert wurde, 
#ist ein gängiger Trick.


#Code 3.1.2
#---Verwendung der erschöpfenden Aufzählung zur Prüfung der Primzahleigenschaft---

x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')


#Hinweis: 17, 23, 107 sind prim

#Der zentrale Punkt ist die Bedingung  if x % guess == 0. Was macht sie ?
# % ist der Modulo-Operator. Er bestimmt den Rest nach ganzzahliger Division.
#z.B.: 
6 % 3     #0
6 % 4     #2 
10 % 3    #1



###############
#Aufgabe 3.1.a:
############### 
#Ändern Sie den Code 3.1.2 so, dass er den größten und nicht den kleinsten Teiler liefert.
#Tipp: Wenn y*z = x ist und y der kleinste Teiler von x ist, ist z der größte Teiler 
#von x.
###############

x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')

#Der Code 3.1.2 funktioniert zwar, ist aber unnötig ineffizient. Es ist zum 
#Beispiel nicht nötig, gerade Zahlen jenseits von 2 zu prüfen, denn wenn eine ganze Zahl 
#durch eine gerade Zahl teilbar ist, ist sie auch durch 2 teilbar. Der Code 3.1.3 macht 
#sich diese Tatsache zunutze, indem er zunächst prüft ob x eine gerade Zahl ist. 
#Wenn nicht, wird in einer Schleife geprüft, ob x durch eine ungerade Zahl teilbar ist.
#Der Code 3.1.3 ist zwar etwas komplexer als der Code 3.1.2, aber er ist 
#wesentlich schneller, da nur halb so viele Zahlen innerhalb der Schleife geprüft werden. 
#Die Möglichkeit, die Komplexität des Codes gegen Laufzeiteffizienz einzutauschen, 
#ist ein weit verbreitetes Phänomen. Aber schneller bedeutet nicht immer besser. 
#Es spricht viel für einfachen Code, der offensichtlich korrekt und dennoch 
#schnell genug ist.


#Code 3.1.3
#---Ein effizienterer Primzahltest---

x = int(input('Enter an integer greater than 2: '))    
smallest_divisor = None
if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x%guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')
    


###############
#Aufgabe 3.1.b:
############### 
#Schreiben Sie ein Programm, das den Benutzer auffordert, eine ganze Zahl einzugeben
#und zwei Ganzzahlen, root und pwr, so ausgibt, dass 1 < pwr < 6
#und root**pwr gleich der vom Benutzer eingegebenen ganzen Zahl ist. Wenn kein solches
#Paar von Ganzzahlen existiert, sollte es eine entsprechende Meldung ausgeben.
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
#Aufgabe 3.1.c:
############### 
#Schreiben Sie ein Programm, das die Summe der Primzahlen ausgibt, die
#größer als 2 und kleiner als 1000 sind. Tipp: Sie wollen wahrscheinlich
#eine Schleife, die ein Primzahltest ist, in eine weitere Schleife einfügen, die
#über die ungeraden ganzen Zahlen zwischen 3 und 999 iteriert.
###############
primzahl_flag = False

x = int(input('Gebe eine ganze Zahl ein'))
for i in range (3,x):
    if x%i==0:
        primzahl_flag = False
        (f'{x} is keine Primzah')
        break
else:
    (f'{x} is eine Primzah')

#Claude:

x = int(input('Gebe eine ganze Zahl ein: '))

is_prime = True

for i in range(2, x):
  if x % i == 0:
    is_prime = False
    break

if is_prime:
  print(f"{x} ist eine Primzahl")
else:
  print(f"{x} ist keine Primzahl")


#############



# Initialize sum to 0 
sum = 0

# Loop through numbers 3 to 999
for num in range(3, 1000, 2):

  # Assume number is prime  
  is_prime = True
  
  # Test if num is divisible by any odd number
  for i in range(3, int(num**0.5) + 1, 2):
    if num % i == 0:
      is_prime = False
      break

  # If prime, add to sum
  if is_prime:
    sum += num

print(sum)   


#------------------------------------------------------------------------------------
#           3.2 Näherungslösungen und Bisektionssuche (Intervallhalbierung)
#------------------------------------------------------------------------------------

#Stellen Sie sich vor, jemand bittet Sie, ein Programm zu schreiben, das die
#Quadratwurzel einer beliebigen nichtnegativen Zahl ausgibt. Was sollten Sie tun?
#Wahrscheinlich sollten Sie zunächst sagen, dass Sie eine bessere
#Problemstellung brauchen. Was sollte das Programm zum Beispiel tun, wenn
#gebeten wird, die Quadratwurzel aus 2 zu finden? Die Quadratwurzel von 2 ist keine
#rationale Zahl. Das bedeutet, dass es keine Möglichkeit gibt, ihren Wert genau
#als endliche Ziffernfolge (oder als Gleitkommazahl) darzustellen, so dass das
#Problem in seiner ursprünglichen Form nicht gelöst werden kann.

#Was ein Programm tun kann, ist eine Annäherung an die Quadratwurzel zu finden - 
#d.h. eine Antwort, die nahe genug an der tatsächlichen Wurzel liegt. 
#Wir werden auf dieses Thema später noch einmal ausführlich eingehen. Aber für 
#den Moment betrachten wir "nahe genug" als eine pragmatische Antwort. 
#Damit ist gemeint: die gefundene Antwort liegt nicht weiter als eine bestimmte 
#Konstante, nennen wir sie Epsilon, von der der tatsächlichen Antwort entfernt.

#Der folgende Code 3.2.1 implementiert einen Algorithmus, der eine Annäherung an die 
#Quadratwurzel von x ausgibt.


#Code 3.2.1: 
#---Annäherung an die Quadratwurzel durch erschöpfende Aufzählung---

x = 25 #Wir suchen z.B. die Wurzel von 25
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1
print('number of guesses =', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)


#Ausgabe:
#           number of guesses = 49990
#           4.999000000001688 is close to square root of 25

#Auch hier handelt es sich um eine erschöpfende Aufzählung. Beachten Sie, dass
#diese Methode zur Ermittlung der Quadratwurzel nichts mit der der Art und Weise 
#zu tun hat, wie man Quadratwurzeln mit Papier und Bleistift findet, die Sie 
#vielleicht in der Schule gelernt haben. Es ist oft der Fall, dass die beste 
#Methode zur Lösung eines Problems per Computer, ganz anders ist, als wenn man
#das Problem mit der Hand angehen würde.

#Wenn x gleich 25 ist, gibt der Code Folgendes aus:
#           number of guesses = 49990
#           4.999000000001688 is close to square root of 25
#Sollten wir enttäuscht sein, dass das Programm nicht herausgefunden hat,
#dass 25 ein perfektes Quadrat ist und 5 ausgibt? Nein. Das Programm hat getan, was es
#eigentlich tun sollte. Es wäre zwar in Ordnung gewesen, 5 zu drucken, aber das
#ist nicht besser, als irgendeinen Wert zu drucken, der nahe genug an 5 liegt.

#Was glauben Sie, wird passieren, wenn wir x = 0.25 setzen? Wird es eine
#Wurzel in der Nähe von 0,5? Nein. Leider wird es Folgendes melden
#           number of guesses = 2501
#           Failed on square root of 0.25

#Die erschöpfende Aufzählung ist eine Suchtechnik, die nur funktioniert, wenn
#die Menge der gesuchten Werte die Antwort enthält. In diesem Fall werden die Werte 
#zwischen 0 und dem Wert von x aufgezählt. Wenn x zwischen zwischen 0 und 1 liegt, 
#liegt die Quadratwurzel von x nicht in diesem Intervall. Klar: für eine Zahl y kleiner
#1, muss für ihre Wurzel w gelten: w > y. Z.B. Wurzel(0.81) = 0.9   

import math
math.sqrt(0.81)      #0.9

#d.h. die Wurzel einer Zahl < 1 ist immer größer als diese Zahl.

#Eine Möglichkeit, dies zu beheben, ist die Änderung des zweiten Operanden 
#in der ersten Zeile der while-Schleife wie folgt

#           while abs(ans**2 - x) >= epsilon and ans*ans <= x:

#Wenn wir den Code 3.2.1 nach dieser Änderung ausführen, meldet er, dass
#0.48989999999996237 nahe an der Quadratwurzel von 0.25 liegt

#Überlegen wir nun, wie lange die Ausführung des Programms dauern wird. Die
#Anzahl der Iterationen hängt davon ab, wie nahe die Antwort an unserem
#Startpunkt 0 liegt, und von der Größe der Schritte. Grob gesagt, wird die 
#while-Schleife höchstens x/step lang ausführen.

#Probieren wir den Code für eine größere Zahl aus, z. B. x = 123456. Er wird
#eine ganze Weile laufen und dann ausgeben
#          number of guesses = 3513631
#          Failed on square root of 123456
#Was denken Sie, was passiert ist? Sicherlich gibt es eine Fließkommazahl
#Zahl, die die Quadratwurzel aus 123456 mit einer Genauigkeit von 0,01 annähert.
#Warum hat unser Programm sie nicht gefunden? Das Problem ist, dass unsere Schrittweite
#(also step) zu groß war und das Programm alle passenden Antworten übersprungen hat.
#Wieder einmal haben wir einen Raum erschöpfend durchsucht, der keine Lösung enthält. 
#Versuchen Sie, die Schrittweite auf epsilon**3 zu setzen und starten Sie das Programm. 
#Es wird schließlich eine passende Antwort finden, aber vielleicht haben Sie
#nicht die Geduld, darauf zu warten.

#Wie viele Tate-Versuche muss es ungefähr anstellen? Die Schrittweite beträgt 0.000001 
#(das ist 0.01**3 = 1e-6) und die Quadratwurzel aus 123456 ist etwa 351,36. 
#Das bedeutet, dass das Programm ca. 351.000.000 Schätzungen vornehmen muss, um 
#eine zufriedenstellende Antwort zu finden. Wir könnten versuchen, zu beschleunigen, 
#indem wir näher an der Antwort beginnen, aber das setzt voraus, dass wir die 
#Umgebung der Antwort kennen.

#Es ist an der Zeit, nach einem anderen Weg zu suchen, das Problem anzugehen. 
#Wir müssen einen besseren Algorithmus wählen, statt Code 3.2.1. 
#Doch bevor wir das tun, wollen wir uns ein Problem ansehen, das auf den ersten Blick
#völlig anders aussieht als das obige Finden von Wurzeln:

#Und zwar betrachten wir das Problem, herauszufinden, ob ein Wort, das
#mit einer bestimmten Buchstabenfolge beginnt, in einem gedruckten Wörterbuch
#der englischen Sprache steht. Eine vollständige Aufzählung würde im Prinzip,
#funktionieren. Man könnte mit dem ersten Wort beginnen und jedes Wort untersuchen, 
#bis man entweder ein Wort gefunden hat, das mit der Buchstabenfolge beginnt oder 
#bis man keine Wörter mehr zu untersuchen sind. Wenn das Wörterbuch n Wörter enthielte, 
#würde man im Durchschnitt n/2 Versuche brauchen, um das Wort zu finden. Wäre das Wort
#nicht im Wörterbuch, würde man n Versuche brauchen, um das zu verifizieren. 
#Natürlich können diejenigen, die schon einmal das Vergnügen hatten, ein Wort in 
#einem physischen (und nicht in einem Online-Wörterbuch) nachzuschlagen, niemals 
#auf diese Weise vorgehen.

#Glücklicherweise machen sich die Herausgeber von Wörterbüchern in Papierform die
#die Mühe, die Wörter in lexikografische Reihenfolge zu bringen. Dadurch können wir
#das Buch auf einer Seite aufschlagen, auf der wir das Wort vermuten (z.B., in der 
#Nähe der Mitte bei Wörtern, die mit dem Buchstaben m beginnen). Wenn die gesuchte
#Buchstabenfolge lexikografisch vor dem ersten Wort dieser Seite steht, wissen wir, 
#dass wir rückwärts gehen müssen. Wenn die gesuchte Buchstabenfolge auf das letzte 
#Wort der Seite folgt, wissen wir, dass wir vorwärts gehen müssen. Andernfalls prüfen 
#wir, ob die Buchstabenfolge mit einem Wort auf der Seite übereinstimmt.

#Wir wollen nun diese prinzipielle Idee auf das Problem übertragen, die Quadratwurzel 
#von x zu finden. Angenommen, wir wissen, dass eine gute Annäherung an die Quadratwurzel 
#von x irgendwo zwischen 0 und max liegt. Wir können uns jetzt die Tatsache zunutze 
#machen, dass Zahlen völlig geordnet sind. Das heißt, für jedes Paar verschiedener 
# Zahlen, n1 und n2, ist entweder n1 < n2 oder n1 > n2. Wir können uns die Quadratwurzel 
#von x also so vorstellen, dass sie irgendwo auf der Linie

#       0_________________________________________________________max

#liegt und beginnen mit der Suche in diesem Intervall. Da wir nicht unbedingt wissen
#wo wir mit der Suche beginnen sollen, fangen wir in der Mitte an. Das ist unser guess.

#       0__________________________guess__________________________max

#Wenn dieser guess nicht die richtige Antwort ist (und das wird er meistens nicht sein),
#müssen wir fragen, ob er zu groß oder zu klein ist. Wenn er zu groß ist, wissen wir, 
#dass die Antwort links liegen muss. Wenn er zu klein ist, wissen wir, dass die Antwort
#auf der rechten Seite liegen muss. Wir wiederholen den Vorgang dann in analoger Weise
#für das Intervall, in dem wir die Antwort vermuten, also entweder für das Intervall
#[0 bis guess] oder für das Intervall [guess bis max]. Der folgende Code 3.2.2 enthält 
#eine Implementierung und einen Test dieses Algorithmus.


#Code 3.2.2:
#---Annäherung an die Quadratwurzel durch Bisektionssuche---

x = 25     #wir suchen die Wurzel von 25
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)


#Ausgabe:
#low = 0 high = 25 ans = 12.5
#low = 0 high = 12.5 ans = 6.25
#low = 0 high = 6.25 ans = 3.125
#low = 3.125 high = 6.25 ans = 4.6875
#low = 4.6875 high = 6.25 ans = 5.46875
#low = 4.6875 high = 5.46875 ans = 5.078125
#low = 4.6875 high = 5.078125 ans = 4.8828125
#low = 4.8828125 high = 5.078125 ans = 4.98046875
#low = 4.98046875 high = 5.078125 ans = 5.029296875
#low = 4.98046875 high = 5.029296875 ans = 5.0048828125
#low = 4.98046875 high = 5.0048828125 ans = 4.99267578125
#low = 4.99267578125 high = 5.0048828125 ans = 4.998779296875
#low = 4.998779296875 high = 5.0048828125 ans = 5.0018310546875
#number of guesses = 13
#5.00030517578125 is close to square root of 25

#Beachten Sie, dass er eine andere Antwort findet als unser früherer Algorithmus.
#Das ist völlig in Ordnung, da er immer noch die Spezifikation des Problems erfüllt.
#Noch wichtiger ist, dass bei jeder Iteration der Schleife die Größe des zu 
#durchsuchenden Raums um die Hälfte reduziert wird. Aus diesem Grund wird der
#Algorithmus als Bisektionssuche (Intervallhalbierung) bezeichnet. Siehe auch:
#            https://de.wikipedia.org/wiki/Bisektion
#Die Bisektionssuche ist eine enorme Verbesserung gegenüber unserem früheren 
#Algorithmus, der den Suchraum bei jeder Iteration nur um einen kleinen Betrag 
#reduzierte.
#Probieren wir noch einmal x = 123456. Diesmal braucht das Programm nur 30
#Versuche, um eine akzeptable Antwort zu finden. Wie wäre es mit x = 123456789? 
#Es braucht nur 45 Versuche.

#Es ist nichts Besonderes, diesen Algorithmus zum Finden von Quadratwurzeln
#Wurzeln zu benutzen. Wenn wir zum Beispiel ein paar "Zweien" in "Dreien" umwandeln, 
#können wir ihn verwenden, um eine Kubikwurzel aus einer nichtnegativen Zahl annähern. 
#In einem späteren Kapitel werden wir einen Mechanismus einsetzen, der es uns erlaubt, 
#diesen Code zu verallgemeinern, um jede Wurzel zu finden.

#Die Bisektionssuche ist auch für viele andere Aufgabestellungen eine sehr nützliche 
#Technik. Der Code 3.2.3 verwendet zum Beispiel Bisektionssuche, um eine Annäherung 
#an die logarithmische Basis 2 von x zu finden (d. h. eine Zahl, ans, so dass 2**ans 
#nahe an x liegt). Er ist genau so aufgebaut wie der Code, mit dem eine Annäherung 
#an eine Quadratwurzel gefunden wird. Er sucht zunächst ein Intervall, das eine 
#geeignete Antwort enthält, und verwendet dann Bisektionssuche, um dieses Intervall 
#effizient zu erkunden.


#Code 3.2.3:
#---Schätzung der logarithmischen Basis 2 mittels Bisektionssuche---

x = 65             #wir suchen den Logarithmus von 65 zur Basis 2
epsilon = 0.01
# Find lower bound on ans
lower_bound = 0
while 2**lower_bound < x:
    lower_bound += 1
low = lower_bound - 1
high = lower_bound + 1
#perform bisection search
ans = (high + low)/2
while abs(2**ans - x) >= epsilon:
    if 2**ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print(ans, 'is close to the log base 2 of', x)


#Ausgabe: 6.0224609375 is close to the log base 2 of 65

#Probe:
2**6.0224609375      #65.00419581813443

#Die Bisektionssuche ist ein Beispiel für ein Verfahren der sukzessiven Annäherung.
#Bei solchen Methoden wird eine Folge von Vermutungen angestellt, die die Eigenschaft
#haben, dass jede Vermutung näher an der richtigen Antwort liegt als die vorherige 
#Schätzung. Wir werden uns einen wichtigen sukzessiven Näherungsalgorithmus, 
# die Newton-Methode, später in diesem Kapitel ansehen.



###############
#Aufgabe 3.2.a: 
############### 
#Was würde der Code 3.2.2 tun, wenn x = -25 wäre?
###############

# Der Code 3.2.2 ist darauf ausgelegt, die Quadratwurzel einer 
# positiven Zahl zu finden. Wenn x = -25 gesetzt wird, würde der Code 
# in eine Endlosschleife geraten. Das liegt daran, dass ans**2 immer positiv sein wird,
#  und daher niemals gleich -25 sein kann. Die Bedingung abs(ans**2 - x) >= epsilon würde
#  immer wahr sein, und die Schleife würde nie enden.


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
#Aufgabe 3.2.c:
###############  
#Das Empire State Building ist 102 Stockwerke hoch. Jemand möchte wissen, aus welchem 
#Stockwerk ein Ei fallen gelassen werden kann, ohne dass es zerbricht. Folgende Idee
#wird verfolgt: ein Ei wird aus dem obersten Stockwerk fallengelassen. Sollte es 
#zerbrechen, würde man eine Etage tiefer gehen und es erneut versuchen. Dies könnte
#man so lange tun, bis das Ei nicht mehr zerbricht. Im schlimmsten Fall benötigt diese 
#Methode 102 Eier. Entwickle eine Methode, die im schlimmsten Fall sieben Eier benötigt.
###############



#------------------------------------------------------------------------------------
#        3.3 Ein paar Anmerkungen zur Verwendung von Gleitkommazahlen (floats)
#------------------------------------------------------------------------------------

#In den meisten Fällen bieten Zahlen vom Typ Float eine recht gute Näherung für reelle 
#Zahlen. Aber "die meiste Zeit" bedeutet eben auch "nicht immer", und wenn dies nicht 
#der Fall ist, kann dies zu überraschenden Konsequenzen führen. 
#Versuchen Sie zum Beispiel, den folgenden Code auszuführen


x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')


#Vielleicht finden Sie, wie die meisten Menschen, es überraschend, dass dieses
#Ergebnis angezeigt wird 
#              0.9999999999999999 is not 1.0

#Wie kommt es überhaupt zu der else-Klausel?
#Um zu verstehen, warum dies geschieht, müssen wir verstehen, wie Gleitkommazahlen 
#(floating point numbers) im Computer während einer Berechnung dargestellt werden. 
#Und um das zu verstehen, müssen wir die binären Zahlen verstehen.

#Als Sie das erste Mal etwas über Dezimalzahlen gelernt haben - d. h. Zahlen
#zur Basis 10 - haben Sie gelernt, dass jede Dezimalzahl dargestellt werden kann durch
#eine Folge der Ziffern 0123456789. Die Ziffer ganz rechts ist die 10^0 Stelle, 
#die nächste Ziffer auf der linken Seite ist die 10^1 Stelle, usw. - zum Beispiel,
#die Folge der Dezimalziffern 302 entspricht 3*100 + 0*10 + 2*1 = 3*10^2 + 0*10^1 + 2*10^0.
#Wie viele verschiedene Zahlen lassen sich durch eine Folge der Länge n dargestellen ? 
#Eine Folge der Länge 1 kann eine beliebige von 10 Zahlen (0-9) darstellen; 
#eine Folge der Länge 2 kann 100 verschiedene Zahlen darstellen (0-99). 
#Allgemeiner ausgedrückt, kann eine Folge der Länge n also 10^n verschiedene Zahlen 
#darstellen.

#Binäre Zahlen - Zahlen zur Basis 2 - funktionieren auf ähnliche Weise. Eine binäre
#Zahl wird durch eine Folge von Ziffern dargestellt, von denen jede entweder
#0 oder 1 ist. Diese Ziffern werden oft als Bits bezeichnet. Die Ziffer ganz rechts ist 
#die 2^0 Stelle, die nächste Ziffer auf der linken Seite ist die 2^1 Stelle, usw. 
#Wieder ein Beispiel: die Folge der Binärziffern 101 entspricht 
#1*4 + 0*2 + 1*1 = 1*2^2 + 0*2^1 + 1*2^0 = 5.
#Wie viele verschiedene Zahlen lassen sich durch eine Folge der Länge n darstellen ? 
#Antwort: 2^n



###############
#Aufgabe 3.3.a:
###############
#Was ist das dezimale Äquivalent der Binärzahl 10011 ?
###############



#Vielleicht weil die meisten Menschen zehn Finger haben, verwenden wir gerne
#Dezimalstellen zur Darstellung von Zahlen. Auf der anderen Seite stellen alle 
#modernen Computersysteme Zahlen im Binärformat dar. Das liegt nicht daran, 
#dass Computer mit zwei Fingern geboren werden. Es liegt daran, dass es einfach ist, 
#Hardware-Schalter zu bauen, d.h. Geräte, die nur einen von zwei Zuständen annehmen 
#können. Dass Computer eine binäre Darstellung verwenden und Menschen eine 
#Dezimaldarstellung, kann zu gelegentlichen kognitiven Dissonanzen führen.

#In modernen Programmiersprachen werden nicht-ganzzahlige Zahlen in einer Darstellung 
#verwendet, die Gleitkomma genannt wird. Für den Moment nehmen wir an, dass die 
#interne Darstellung in Dezimalzahlen erfolgt. Wir würden eine Zahl dann als ein Paar 
#von ganzen Zahlen darstellen - die signifikanten Ziffern der Zahl und einen Exponenten. 
#Zum Beispiel würde die Zahl 1949 als Paar (1949, -3) dargestellt werden, was für
#das Produkt 1949*10^3 steht.

#Die Anzahl der signifikanten Ziffern bestimmt die Genauigkeit, mit der
#die Zahlen dargestellt werden können. Gäbe es zum Beispiel nur zwei signifikante 
#Ziffern, könnte die Zahl 1949 nicht exakt dargestellt werden. Sie müsste in einen 
#Näherungswert von 1949, in diesem Fall 19, umgewandelt werden. Dieser Näherungswert 
#wird als gerundeter Wert bezeichnet.

#Moderne Computer verwenden binäre, nicht dezimale Darstellungen.
#Sie stellen die signifikanten Ziffern und Exponenten binär und nicht dezimal dar, und 
#erhöhen den Exponenten um 2 statt um 10. 
#Beispiel: Die Zahl, die durch die Dezimalziffern 0.625 (= 5/8) dargestellt wird, wird 
#als Paar (101, -11) dargestellt; denn 101 ist die die binäre Darstellung der Zahl 5 
#und -11 die binäre Darstellung von -3; somit steht das Paar (101, -11) für 
# 5*2^-3 = 5/8 = 0.625.

#Was ist mit dem Dezimalbruch 1/10, den wir in Python als 0.1 schreiben? Das Beste, 
#was wir mit vier signifikanten Binärziffern machen können, ist (0011, -101). 
#Dies entspricht 3/32, d.h. 0.09375. Hätten wir fünf, würden wir 0,1 als (11001, -1000) 
#darstellen, was 25/256, also 0.09765625, entspricht. Wie viele signifikante
#Stellen bräuchten wir, um eine exakte Gleitkommadarstellung von 0.1 zu bekommen? 
#Eine unendliche Anzahl von Ziffern! Es gibt keine ganzen Zahlen sig und exp, 
#so dass sig * 2^-exp gleich 0.1 ist. Es spielt also keine Rolle, wie viele Bits
#Python (oder jede andere Sprache) verwendet, um Fließkommazahlen darzustellen, 
#sie kann nur eine Annäherung an 0.1 darstellen. In den meisten Python-Implementierungen 
#stehen 53 Bits für die Genauigkeit von Fließkommazahlen zur Verfügung, so dass die 
#signifikanten Ziffern, die für die Dezimalzahl 0.1 gespeichert sind, folgende sind
#          11001100110011001100110011001100110011001100110011001
#Dies entspricht der Dezimalzahl 
#          0.1000000000000000055511151231257827021181583404541015625
#Ziemlich nahe an 1/10, aber nicht genau 1/10.

#Um auf das ursprüngliche Rätsel zurückzukommen, warum 


x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'ist nicht 1.0')


#folgendes Ergebnis ausdruckt: 0.99999999999999 ist nicht 1.0

#Wir sehen nun, dass der Test x == 1.0 das Ergebnis False liefert, weil der Wert, 
#an den x gebunden ist, nicht genau 1.0 ist. Dies erklärt warum die else-Klausel 
#ausgeführt wurde. Aber warum hat sie entschieden, dass x kleiner als 1.0 ist, 
#wenn wir doch weiter oben gesehen hatten, dass die Fließkommadarstellung von 0.1 
#etwas größer als 0.1 ist?
#Antw: weil Python während der Iteration der Schleife keine signifikanten Ziffern 
#mehr hatte und eine Rundung vornahm, die zufällig nach unten ausfiel. 
#Was wird gedruckt, wenn wir am Ende der else-Klausel den Code print x == 10.0*0.1 
#hinzufügen? Es wird False gedruckt. Das ist nun nicht das, was uns unsere 
#Grundschullehrer beigebracht haben. Hier haben wir nämlich den Fall,dass zehnmal 
#0.1 zu addieren, nicht denselben Wert ergibt wie die Multiplikation von 0.1 mit 10.

#Übrigens, wenn Sie eine Fließkommazahl explizit runden wollen, verwenden Sie die
#Rundungsfunktion round. Der Ausdruck round(x,num_digits) gibt die Fließkommazahl 
#zurück, die der Rundung des Wertes von x auf num_digits Nachkommastellen entspricht. 
#Zum Beispiel gibt round(2**0.5, 3) den Wert 1.414 als Annäherung an die an die 
#Quadratwurzel von 2.

#Spielt der Unterschied zwischen reellen Zahlen und Fließkommazahlen wirklich eine 
#Rolle? In den meisten Fällen ist das zum Glück nicht der Fall. Es gibt nur wenige 
#Situationen, in denen der Unterschied zwischen 0,99999999999999, 1,0 und 
#1,00000000000000001 wichtig ist. Eine Sache, die jedoch fast immer eine Überlegung 
#wert ist, sind Tests auf Gleichheit. Wie wir gesehen haben, kann die Verwendung 
#von == zum Vergleich zweier Fließkommazahlen ein überraschendes Ergebnis liefern. 
#Es ist fast immer angemessener zu fragen, ob zwei Fließkommawerte nahe genug 
#beieinander liegen, nicht ob sie identisch sind. So ist es zum Beispiel besser, 
# abs(x-y) < 0,0001  zu schreiben, anstatt x == y.

#Ein weiteres Problem ist die Häufung von Rundungsfehlern. Meistens klappt das 
#ganz gut, denn manchmal ist die im Computer gespeicherte Zahl ein wenig größer 
#als beabsichtigt, und manchmal ist sie ein wenig kleiner als beabsichtigt. 
#In einigen Programmen gehen die Rundungsfehler jedoch alle in dieselbe Richtung 
#und häufen sich so mit der Zeit an.



#------------------------------------------------------------------------------------
#                       3.4 Das Newton-Raphson Verfahren
#------------------------------------------------------------------------------------

#Der am häufigsten verwendete Näherungsalgorithmus wird gewöhnlich Isaac Newton 
#zugeschrieben. Er wird üblicherweise als Newton-Verfahren bezeichnet, wird aber 
#manchmal auch als Newton-Raphson-Verfahren bezeichnet. Siehe auch:
#
#      https://de.wikipedia.org/wiki/Newtonverfahren

#Es kann verwendet werden, um die reellen Wurzeln vieler Funktionen zu finden, aber wir
#betrachten es nur im Zusammenhang mit der Bestimmung der reellen Wurzeln eines 
#Polynoms mit einer Variablen. Die Verallgemeinerung auf Polynome mit mehreren Variablen
#ist sowohl in mathematischer als auch in algorithmischer Hinsicht sehr einfach.
#Ein Polynom mit einer Variablen (aus Konvention schreiben wir die Variable als x) 
#ist entweder 0 oder die Summe einer endlichen Anzahl von Nicht-Null Termen, z. B. 
# 
#         3x^2 + 2x + 3 
# 
#Jeder Term, z. B. 3x^2, besteht aus einer Konstante (dem Koeffizienten des Terms, 
#in diesem Fall 3), multipliziert mit der Variable (in diesem Fall x) multipliziert 
#mit einem nichtnegativen ganzzahligen Exponenten (in diesem Fall 2). Der Exponent in 
#einem Term wird als Grad des Terms bezeichnet. Der Grad eines Polynoms ist der größte 
#Grad eines einzelnen Terms. Einige Beispiele sind 3 (Grad 0), 2,5x + 12 (Grad 1) und 
#3x^2 (Grad 2).

#Wenn p ein Polynom und r eine reelle Zahl ist, schreiben wir p(r), um damit den Wert 
#des Polynoms auszudrücken, wenn x = r ist. Eine Wurzel des Polynoms p ist eine Lösung 
#der Gleichung p(r) = 0, d. h. wir suchen ein solches r, dass p(r) = 0. 
#So kann zum Beispiel das Problem, eine Näherung der Quadratwurzel aus 24 zu finden, 
#so formuliert werden, dass ein x gefunden werden soll, das x^2 - 24 nahe bei 0 liegt.

#Newton bewies ein Theorem, das besagt, dass, wenn ein Wert, nennen wir ihn guess, 
#eine Annäherung an eine Wurzel eines Polynoms ist, dann ist der folgende Wert 
# 
#             guess  -  p(guess)/p'(guess)
#
#eine bessere Annäherung an die Wurzel des Polynoms p als guess, wobei p' die erste 
#Ableitung von p ist.

#Die erste Ableitung einer Funktion f(x) drückt aus, wie sich der Wert von f(x) 
#in Bezug auf Änderungen von x verhält. Die erste Ableitung einer Konstanten 
#ist zum Beispiel 0, weil der Wert einer Konstanten sich nicht ändert. 
#Für jeden Term   c * x^p   ist die erste Ableitung dieses Terms   c * p * x^(p-1)  . 
#Somit ist die erste Ableitung eines Polynoms der Form
#
#            c1 * x^p  +  c2 * x^(p-1)  +  ...  +  c * x  +  k
#also
#            c1 * p * x^(p-1)  +  c2 * (p-1) * x^(p-2)  +  ...  +  c

#Um nun die Quadratwurzel einer Zahl, z. B. k, zu finden, müssen wir einen Wert x 
#finden, so dass  x^2 - k = 0  . Die erste Ableitung dieses Polynoms ist einfach 2x. 
#Wir wissen aufgrund des Newton-Raphson-Verfahrens, dass wir die aktuelle 
#Schätzung verbessern können, indem wir als nächste Schätzung den Ausdruck  
# 
#      guess - (guess^2 - 𝑘) / (2 * guess)
# 
#verwenden. 
#Der folgende Code 3.4.1 veranschaulicht, wie man diese Methode verwendet, um
#schnell eine Annäherung an die Quadratwurzel zu finden.


#Code 3.4.1:
#---Anwendung der Newton-Raphson-Methode, um die Wurzel einer Zahl zu finden---

k = 24        #für diese Zahl wollen wir die Quadratwurzel finden
epsilon = 0.01
guess = k/2
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)


#Ausgabe: Square root of 24 is about 4.8989887432139305



###############
#Aufgabe 3.4.a:
###############
#Ergänzen Sie die Implementierung von Newton-Raphson so, dass die Anzahl der 
#Iterationen gezählt wird, um die Wurzel zu finden. Verwenden Sie diesen Code
#dann als Teil eines Programms, das die Effizienz von Newton-Raphson einerseits 
#und der Bisektionssuche andererseits vergleicht. (Sie sollten dabei 
#herausfinden, dass Newton-Raphson weitaus effizienter ist.)
###############



#------------------------------------------------------------------------------------
#                    3.5 In diesem Kapitel eingeführte Begriffe
#------------------------------------------------------------------------------------

#dekrementierende Funktion      decrementing function
#Raten und Prüfen               guess-and-check
#erschöpfende Aufzählung        exhaustive enumeration
#Annäherung                     approximation
#totale Ordnung                 total ordering
#Halbierungssuche               bisection search
#sukzessive Annäherung          successive approximation
#Binärzahlen                    binary numbers
#Bit                            bit
#Schalter                       switch
#Gleitkomma                     floating point
#signifikante Ziffern           significant digits
#Exponent                       exponent
#Genauigkeit                    precision
#Rundung                        rounding
#Newton-Raphson                 Newton–Raphson
#Polynom                        polynomial      
#Koeffizient                    coefficient
#Grad                           degree
#Wurzel                         root


#####################################################################################
#####################################################################################
#FINIS