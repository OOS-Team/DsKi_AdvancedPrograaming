#tw, 28.8.2022

#####################################################################################

                    ### Lösungen zu Kap 5: STRUKTURIERTE TYPEN UND MUTABILITÄT    ###

#####################################################################################



###############
#Lösung zu
#Aufgabe 5.2.a:
############### 
#Schreiben Sie einen Ausdruck, der den Mittelwert von Tupeln von Zahlen ergibt. 
#Verwenden Sie die Funktion sum.
###############

#Version 1

(2,2).__len__()   #2
"dkhddkfjdkf".__len__()   #11
#diese in Iterables eingebaute __len__ Methode können wir verwenden

def mittelwert_v1(t):
    """t ist ein Tupel, das Zahlen enthaelt"""
    summe = 0
    for e in t:
        summe += e
    return summe / t.__len__()

mittelwert_v1((1,2,3,4,5,6,7,8,9))     #5.0

#Version 2

len((1,2,3))         #3

def mittelwert_v2(t):
    """t ist ein Tupel, das Zahlen enthaelt"""
    summe = 0
    for e in t:
        summe += e
    return summe / len(t)

mittelwert_v2((1,2,3,4,5,6,7,8,9))     #5.0

#Version 3

#und jetzt ohne len() oder __len__() zu verwenden
def mittelwert_v3(t):
    """t ist ein Tupel, das Zahlen enthaelt"""
    summe = 0
    anzahl = 0
    for e in t:
        anzahl += 1
        summe += e
    return summe / anzahl

mittelwert_v3((1,2,3,4,5,6,7,8,9))     #5.0

#####################################################################################


###############
#Lösung zu
#Aufgabe 5.3.a:
############### 
#Was gibt der folgende Code aus?
#Nicht einfach ausprobieren, sondern erst austüfteln und vorhersagen:
L = [1, 2, 3]
L.append(L)
print(L is L[-1])
#Hinweis: der Index -1 bzeichnet das letzte Listenelement, siehe z.B.:
[1,2,3][-1]    #3
###############

#siehe dazu auch: https://stackoverflow.com/questions/28227397/why-does-appending-a-list-by-itself-create-an-infinite-list
#Naiv könnten man meinen, folgendes wird durch L.append[L] mit L passieren: 
#  [1,2,3, [1,2,3]]  - das ist aber falsch gedacht !
#Was dabei wirklich geschieht, ist die Konstruktion einer rekursiv-unendlichen Liste am Ende:
#  [  1,2,3, [1,2,3, [1,2,3, [1,2,3,[...]]]]  ]
#            -------------------------------
#                        |
#                   Das wird von Python durch [...] abgekürzt.
#                   Deswegen ergibt print(L): [1,2,3,[...]]
print(L)         
#Warum ist das so ?
#Antw: Wir fügen ja die Referenz(!!!) L auf die Liste L wieder in die Liste L ein.
#Sprachlich können wir das so ausdrücken:
#"Etwas, das sich selbst enthält, ist etwas, das sich selbst enthält, das sich selbst enthält."
#Und diese sprachliche Beschreibung endet hiermit ja nicht. Die obige Aussage können
#wir nun weiterspinnen:
#"Etwas, das sich selbst enthält, ist etwas, das sich selbst enthält, das sich selbst enthält,
#und das ist etwas, das sich selbst enthält."
#Und dieses Spiel geht endlos weiter ...

#Und was ist mit 
print(L is L[-1])     #True
print(L[-1])          #[1, 2, 3, [...]]
#Wie kann das sein ?
#Da L nun eine unendlich-rekursive Liste ist, ist sie identisch mit ihrem hinteren
#Teil. Salopp gesagt: [1,2,3,[1,2,3,[1,2,3,[...]]]] = [1,2,3,[1,2,3,[...]]]
#                     ------
#Auch wenn man die ersten drei Elemente wegläßt, bleibt aufgrund der Unendlichkeit
#die Struktur unverändert (das Weglassen wird durch die ... wieder wettgemacht).
#Unendlichkeiten sind immer kontra-intuitiv ! Sie wiedersprechen unserem normalen
#Alltagsverstand.

#####################################################################################


#################
#Lösung zu
#Aufgabe 5.3.2.a:
################# 
#Schreiben Sie eine List-Comprehension, die alle Nicht-Primzahlen 
#zwischen 2 und 100 erzeugt.
###############

print([x for x in range(2, 100) if any(x % y == 0 for y in range(2, x))])   #[4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21,..., 98, 99]
#                                  ---       ----      <-- das sind die Modifikationen
#                                                          im Vergleich zur Primzahl-List-Comprehension                  

#####################################################################################


###############
#Lösung zu
#Aufgabe 5.4.a:
############### 
#Implementieren Sie eine Funktion, die die folgende Spezifikation erfüllt. 
#Hinweis: Es ist zweckmäßig, lambda im Körper der der Implementierung zu verwenden.
def f(L1, L2):
    """L1, L2 lists of same length of numbers
       returns the sum of raising each element in L1
       to the power of the element at the same index in L2
       For example, f([1,2], [2,3]) returns 9"""
###############

sum(list(map(lambda x,y: pow(x,y), [1,2], [2,3])))
#oder noch einfacher:
sum(list(map(pow, [1,2], [2,3])))

def f(L1, L2):
    return sum(list(map(lambda x,y: pow(x,y), L1, L2)))

f([1,2],[2,3])      #9

#####################################################################################


###############
#Lösung zu
#Aufgabe 5.7.a:
############### 
#Implementieren Sie eine Funktion, die folgender Spezifikation entspricht
def get_min(d):
 """d a dict mapping letters to ints returns the value in d 
    with the key that occurs first in the alphabet. 
    E.g., if d = {x = 11, b = 12}, get_min returns 12."""
###############

type('a')                #str
d = {'x': 11, 'b': 12}
'a' < 'b'                #True
min('c','a','b')         #'a'
min(d.keys())            #'b
d[min(d.keys())]         #12

def get_min(d):
    return d[min(d.keys())]

print(get_min(d))        #12

#####################################################################################


###############
#Lösung zu
#Aufgabe 5.8.a:
############### 
#Beheben Sie das im letzten Absatz von Kap.5.8 beschriebene Problem.
#Tipp: Ein einfacher Weg, dies zu tun, besteht darin, ein neues Buch zu erstellen, 
#indem Sie etwas(?!) an das ursprüngliche Buch anhängen.
###############

#zuerst sammeln wir mal alles, was wir brauchen...
gen_code_keys = lambda book, plain_text:{c: str(book.find(c)) for c in plain_text}
encoder = lambda code_keys, plain_text:''.join(['*' + code_keys[c] for c in plain_text])[1:]
gen_decode_keys = lambda book, cipher_text: {s: book[int(s)] for s in cipher_text.split('*')}
encrypt = lambda book, plain_text:encoder(gen_code_keys(book, plain_text), plain_text)

#Wir fügen im Buch als letztes Zeichen etwas ein, das wir als Platzhalter-Symbol für unbekannte 
#Zeichen verwenden wollen, z.B. ein '*':
Don_Quixote = """In a village of La Mancha, the name of which I have no desire to call to mind, 
                 there lived not long since one of those gentlemen that keep a lance in the 
                 lance-rack, an old buckler, a lean hack, and a greyhound for coursing *"""
#                                                                                      ^
#                                                                                     ||
#Der cipher_text enthält jetzt einen Eintrag -1, der besagt, das an dieser Stelle ein
#unbekanntes Zeichen steht:
encrypt(Don_Quixote, 'xanadu')                    #'-1*3*1*3*55*210'
#                     -                             --
#Und mit diesem cipher_text erhalten wir dann folgenden Dekodierschlüssel:
gen_decode_keys(Don_Quixote, '-1*3*1*3*55*210')   #{'-1': '*', '3': 'a', '1': 'n', '55': 'd', '210': 'u'}
#Und das ist konsistent: -1 verweist auch hier auf unseren Platzhalter für unbekannte Zeichen.

#####################################################################################


###############
#Lösung zu
#Aufgabe 5.8.b:
############### 
#Implementieren Sie anhand der obigen Beispiele encoder und encrypt
#die Funktionen decoder und decrypt. Benutzen Sie diese dann, um die Nachricht
# 22*13*33*155*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*155*59*11*23*11*1*57*6*209*7*11
#zu entschlüsseln, die mit der Buch-Chiffre des Anfangs von Don Quijote (s.o.) verschlüsselt 
#wurde.
###############

#Wir können die obigen Definitionen in 5.8.a von gen_code_keys, encoder, gen_decode_keys, encrypt
#und Don_Quixote auch hier verwenden.
#Zum Erproben könnte Folgendes noch nützlich sein:
cipher_text = encrypt(Don_Quixote, 'no is no')
print(cipher_text)        #'1*13*2*6*57*2*1*13'
decode_keys = gen_decode_keys(Don_Quixote, cipher_text)
print(decode_keys)        #'{'1': 'n', '13': 'o', '2': ' ', '6': 'i', '57': 's'}'

#decoder ist eine Funktion, die als Parameter den Dekodierschlüssel und den verschlüsselten
#Text bekommt und daraus den Klartext bestimmt
decoder = lambda decode_keys, cipher_text:''.join([decode_keys[s] for s in cipher_text.split('*')])
decoder(decode_keys, cipher_text)   #'no is no'

#decrypt ist eine Funktion, die als Parameter das Buch und den verschlüsselten Text erhält,
#und daraus den Klartext bestimmt
decrypt = lambda book, cipher_text:decoder(gen_decode_keys(book, cipher_text), cipher_text)
decrypt(Don_Quixote, cipher_text)   #'no is no'  

#Und damit entschlüsseln wir nun den cipher der Aufgabe:
decrypt(Don_Quixote, '22*13*33*155*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*155*59*11*23*11*1*57*6*209*7*11')
#Die Lösung lautet: 'comprehension is incomprehensible'

#####################################################################################


#####################################################################################
#####################################################################################
#FINIS