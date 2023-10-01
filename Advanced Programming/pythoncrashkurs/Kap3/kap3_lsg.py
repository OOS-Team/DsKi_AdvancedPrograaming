#tw, 17.6.2022

#####################################################################################

                    ### Lösungen zu Kap 3: EINIGE EINFACHE NUMERISCHE PROGRAMME ###

#####################################################################################


###############
#Lösung zu
#Aufgabe 3.1.a:
############### 
#Ändern Sie den Code 3.1.2 so, dass er den größten und nicht den kleinsten Teiler liefert.
#Tipp: Wenn y*z = x ist und y der der kleinste Teiler von x ist, ist z der größte Teiler 
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
    print('Greatest divisor of', x, 'is', int(x/smallest_divisor))    #<--- NEU
else:
    print(x, 'is a prime number')

#####################################################################################


###############
#Lösung zu
#Aufgabe 3.1.b:
############### 
#Schreiben Sie ein Programm, das den Benutzer auffordert, eine ganze Zahl einzugeben
#und zwei Ganzzahlen, root und pwr, so ausgibt, dass 1 < pwr < 6
#und root**pwr gleich der vom Benutzer eingegebenen ganzen Zahl ist. Wenn kein solches
#Paar von Ganzzahlen existiert, sollte es eine entsprechende Meldung ausgeben.
###############

x = int(input('Enter an integer: '))
no_solution = True
for pwr in range(2, 6):
    for root in range(1, 100):
        if x == root**pwr:
            print(x, 'is', root, '**', pwr)
            no_solution = False
            break
if no_solution:
    print('there is no solution for ', x)
        
#####################################################################################


###############
#Lösung zu
#Aufgabe 3.1.c:
############### 
#Schreiben Sie ein Programm, das die Summe der Primzahlen ausgibt, die
#größer als 2 und kleiner als 1000 sind. Tipp: Sie wollen wahrscheinlich
#eine Schleife, die ein Primzahltest ist, in eine weitere Schleife einfügen, die
#über die ungeraden ganzen Zahlen zwischen 3 und 999 iteriert.
###############

#Was sagt Wikipedia zu Primzahlen ?  https://de.wikipedia.org/wiki/Primzahl
#Wir gehen schrittweise vor. Hier ist erstmal ein allg. Primzahltest:

x = int(input('Enter an inter: '))
prim = True
for i in range (2, x):
    if x % i == 0:
        print(x, ' is not prim')
        prim = False
        break
if prim:
    print(x, ' is prim')

#Den verwenden wir nun in der folgenden Schleife, mit der wir alle Primzahlen
#bis 1000 ausdrucken:

for n in range(3, 1000):
    prim  = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    if prim: 
        print(n, end=' ')   #Hinweis: mit end=' ' schalten wir den Zeilenwechsel aus

#Die müssen wir nun nur noch aufsummieren:

#Variante 1 (mit Generator-Funktion)
def primsumme():
    for n in range(3, 1000):
        prim  = True
        for i in range(2, n):
            if n % i == 0:
                prim = False
                break
        if prim: 
            yield n

sum(primsumme())    #76125

#Variante 2 (summieren im äußeren loop)
summe = 0 
for n in range(3, 1000):
    prim  = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    if prim: 
        summe = summe + n
print(summe)              #76125

#Variante 3 (mit Liste)
primzahlliste = []
for n in range(3, 1000):
    prim  = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    if prim: 
        primzahlliste.append(n)

sum(primzahlliste)      #76125

#####################################################################################


###############
#Lösung zu
#Aufgabe 3.2.a: 
############### 
#Was würde der Code 3.2.2 tun, wenn x = -25 wäre?
###############

x = -25                     #mit x=-25 laufen wir in eine Endlosschleife !!    
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:                       #<--- die Ursache liegt hier: wenn x negativ
    print('low =', low, 'high =', high, 'ans =', ans)   #     ist, kann die Differenz nicht kleiner
    num_guesses += 1                                    #     werden.
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)

#####################################################################################


###############
#Lösung zu
#Aufgabe 3.2.b:
###############  
#Was müsste geändert werden, damit der Code 3.2.2 eine Annäherung an die Kubikwurzel 
#von sowohl negativen als auch positiven Zahlen findet? Tipp: Denken Sie darüber nach, 
#den Wert low zu ändern, um sicherzustellen, dass die Antwort innerhalb des gesuchten 
#Bereichs liegt.
###############

#Für den positiven Fall, müssen wir fast nichts ändern:
#Auf dem Zahlenstrahl werden low und high zu Beginn so initialisiert
#  
#     low                              high
#   __0________________________________27_______________________________>
#  
x = 27           #27 = 3^3, also Kubikwurzel von 27 ist 3                      
epsilon = 0.01
num_guesses = 0 
low = 0 
high = max(1, x)
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:                      #<-- NEU: Kubikwurzel, also **3 
    print('low =', low, 'high =', high, 'ans =', ans)   
    num_guesses += 1                                    
    if ans**3 < x:                                     #<-- NEU: Kubikwurzel, also **3                                     
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)      #number of guesses = 14
print(ans, 'is close to cubic root of', x)     #3.000091552734375 is close to cubic root of 27

#Das war simpel, aber sehen wir uns nun den negativen Fall an:
#Auf dem Zahlenstrahl werden low und high werden zu Beginn so initialisiert
#
#       low                              high
#   __ -27________________________________0_______________________________>
#  
x = -27          #-27 = (-3)^3, also: Kubikwurzel von -27 ist -3         
epsilon = 0.01
num_guesses = 0 
high = 0                 #<-- NEU: wie im positiven Fall ist high > low
low = min(-1, x)         #<-- NEU: da wir nun im negativen Bereich sind, 
                         #         ist die linke Schranke das Minimum von -1 und x 
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:                       
    print('low =', low, 'high =', high, 'ans =', ans)   
    num_guesses += 1                                    
    if ans**3 < x:                                     
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)      #number of guesses = 14
print(ans, 'is close to cubic root of', x)     #-3.000091552734375 is close to cubic root of -27

#Die beiden Fälle (positives x bzw. negatives x) können wir nun leicht zusammenfassen,
#da sie sich nur in der Initialisierung von low und high unterscheiden:
x = -27  # oder x = 27   #<-- hier kann man nun ein positive oder eine negative Zahl angeben !!                      
epsilon = 0.01
num_guesses = 0 
if x > 0:                #<-- NEU: hier ist die Unterscheidung der Initialisierungen für 
    low = 0              #         den positiven
    high = max(1, x)     #         und
else:                    #         
    high = 0             #         den negativen Fall
    low = min(-1, x)     #
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:                       
    print('low =', low, 'high =', high, 'ans =', ans)   
    num_guesses += 1                                    
    if ans**3 < x:                                                                          
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)      
print(ans, 'is close to cubic root of', x)

#####################################################################################


###############
#Lösung zu
#Aufgabe 3.2.c:
###############  
#Das Empire State Building ist 102 Stockwerke hoch. Jemand möchte wissen, aus welchem 
#Stockwerk ein Ei fallen gelassen werden kann, ohne dass es zerbricht. Folgende Idee
#wird verfolgt: ein Ei wird aus dem obersten Stockwerk fallengelassen. Sollte es 
#zerbrechen, würde man eine Etage tiefer gehen und es erneut versuchen. Dies könnte
#man so lange tun, bis das Ei nicht mehr zerbricht. Im schlimmsten Fall benötigt diese 
#Methode 102 Eier. Entwickle eine Methode, die im schlimmsten Fall sieben Eier benötigt.
###############

#Wir sehen uns einen konkreten Fall ein und wir beginnen die Stockwerkzählung bei 0:
#
#               das sei das gesuchte Stockwerk - es ist mit einem * markiert
#                  |
#                  v
#       0_1_______10________________________51____________________________102
#                 *                         |
#                                           v
#                               erstes Ei (geht kaputt): links 0 bis 50, rechts 52 bis 102,
#                                                        also auf beiden Seiten jeweils 51
#                                                        Möglichkeiten. Da es kaputt ist,
#                                                        müssen wir links weitersuchen und 
#                                                        dort in der Mitte, also bei 25,
#                                                        das nächste Ei werfen                             
#
#        0_1_______10________25______________51____________________________102       
#                  *         |
#                            v
#                   zweites Ei (geht auch kaputt): links 0 bis 24, rechts 26 bis 50,
#                                                  also auf beiden Seiten jeweils 25
#                                                  Möglichkeiten. Da es kaputt ist, 
#                                                  müssen wir links weitersuchen und 
#                                                  dort in der Mitte, also bei 12,
#                                                  das nächste Ei werfen 
#            Wir zoomen etwas rein ...
#        0_1_______10__12________25_______________51____________________________ ... 
#                  *   |
#                      v
#                drittes Ei (geht auch kaputt): links 0 bis 11, rechts 13 bis 24,
#                                               also auf beiden Seiten jeweils 12
#                                               Möglichkeiten. Da es kaputt ist,
#                                               müssen wir links weitersuchen und
#                                               dort in der Mitte (da die Anzahl der Elemente
#                                               12 ist, haben wir nun zwei Mittenelemente;
#                                               wir wählen das Kleinere), also bei 5,
#                                               das nächste Ei werfen  
#             Wir zoomen weiter rein ...
#        0_1_____5_____10_11_12_13________________25__________ ...    
#                |     *
#                v
#               viertes Ei (bleibt ganz): links 0 bis 4, rechts 6 bis 11, 
#                                         also auf der linken Seite 5
#                                         Möglichkeiten und auf der rechten Seite
#                                         6 Möglichkeiten. Da es ganz geblieben ist,
#                                         müssen wir rechts weitersuchen und
#                                         dort in der Mitte (da die Anzahl der Elemente
#                                         6 ist, haben wir zwei Mittenelemente;
#                                         wir wählen das Kleinere), also bei 8,
#                                         das nächste Ei Werfen 
#
#        0_1______6_7_8_9_10_11_12_13________________25__________ ... 
#                     |   *
#                     v
#                fünftes Ei (bleibt ganz): links 6 bis 7, rechts 9 bis 11, 
#                                          also auf der rechten Seite 2 Möglichkeiten
#                                          und auf der linken Seite 3 Möglichkeiten. 
#                                          Da es ganz geblieben ist,
#                                          müssen wir rechts weitersuchen und 
#                                          dort die verbliebenen Möglichkeiten
#                                          (also 9 bis 11) überprüfen. Die Mitte ist 10.
#                                          Dort werfen wir das nächste Ei
#                          *
#        0_1________7_8_9_10_11_12_13________________25__________ ... 
#                         |
#                         v
#                sechstes Ei (bleibt ganz): da wir aber nicht wissen, ob das Ei
#                                           auch den Wurf vom 11.Stock übersteht,
#                                           müssen wir das ebenfalls ausprobieren 
#                                           (dieses siebte Ei geht aber kaputt)
# 
#Wir haben insgesamt 4 von 7 geworfenen Eiern kaputtgemacht und wir haben das richtige
#Stockwerk (Nr. 10) gefunden.
#Es ist hilfreich, auch mal die Fälle x=11 und x=12 durchzuspielen, um sich die verschiedenen
#Sonderfälle klarzumachen. Und jetzt implementieren wir das:

#Wir suchen das höchste Stockwerk, von dem aus ein heruntergeworfenes Ei nicht kaputt geht.
#Die einzige Information, die uns zur Verfügung steht, sind die "Probe-Eier".
x = 10   #angenommen, das sei das gesuchte Stockwerk: das Ei zerbricht von hier aus nicht.
         #Findet unser Verfahren dieses Stockwerk ?     
num_guesses = 0 
low = 0
high = 102
mid = int((high + low)/2)
while (high - low) >= 0:  #wiederhole, bis nur noch ein Element vorhanden ist
    print('low =', low, 'high =', high, 'mid =', mid)
    num_guesses += 1
    if mid > x:            #<-- Ei geht kaputt:
        high = mid - 1     #    die aktuelle Mitte muss nicht mehr berücksichtigt werden
    else:                  #<-- Ei bleibt heil:
        low = mid          #    die aktuelle Mitte könnte ja auch das gesuchte Stockwerk sein     
    if (high - low) <= 2:  #<-- wenn nicht mehr als zwei Elemente im ausgewählten Intervall
        num_guesses += 1   #    verfügbar sind, ist dies das letzte zu prüfende Intervall.
        if mid != x:       #    Danach springen wir aus der Schleife heraus.
            mid = x
        if mid == x:
            break
    mid = int((high + low)/2)
print('number of guesses =', num_guesses)
print(mid, 'is the highest Egg-Not-Smashing-Floor')

#Die obige Lösung dieser Aufgabe liegt auch als eigenständiges Modul
#(Datei: aufg-3-2-c_lsg.py) vor, damit man sie mit Hilfe des Debuggers
#analysieren kann.

#####################################################################################


###############
#Lösung zu
#Aufgabe 3.3.a:
###############
#Was ist das dezimale Äquivalent der Binärzahl 10011 ?
###############

#Die Dezimalzahl 100 kann man so in Binär konvertieren:
bin(100)      #'0b1100100'
#Und da wir schon mal dabei sind: hier die Umrechnungsfkt. 
#für Hexadezimal und Oktal
hex(100)      #'0x64'
oct(100)      #'0o144'

#Und so kann man eine Binärzahl '0b1100100', die aber als String dargestellt ist,
#wieder in eine Dezimalzahl konvertieren. Dabei muss man aber auch die Basis
#angeben: binär -> Basis: 2
int('0b1100100', 2)            #100

#Nun zur Lösung der eigtl. Aufgabe:
int('0b10011', 2)              #19

#####################################################################################



###############
#Lösung zu
#Aufgabe 3.4.a:
###############
#Ergänzen Sie die Implementierung von Newton-Raphson so, dass die Anzahl der 
#Iterationen gezählt wird, um die Wurzel zu finden. Verwenden Sie diesen Code
#dann als Teil eines Programms, das die Effizienz von Newton-Raphson einerseits 
#und der Bisektionssuche andererseits vergleicht. (Sie sollten dabei 
#herausfinden, dass Newton-Raphson weitaus effizienter ist.)
###############

#Bisektionssuche
x = 24      #für diese Zahl wollen wir die Quadratwurzel finden
epsilon_bisektion = 0.01
num_guesses_bisektion = 0
low = 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon_bisektion:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses_bisektion += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('Bisektion:')
print('number of guesses =', num_guesses_bisektion)
print(ans, 'is close to square root of', x)

#Newton-Raphson
k = 24      #für diese Zahl wollen wir die Quadratwurzel finden
epsilon_newton = 0.01
num_guesses_newton = 0
guess = k/2
while abs(guess**2 - k) >= epsilon_newton:
    num_guesses_newton += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print('Newton-Raphson')
print('number of guesses =', num_guesses_newton)
print('Square root of', k, 'is about', guess)



#####################################################################################
#####################################################################################
#FINIS
