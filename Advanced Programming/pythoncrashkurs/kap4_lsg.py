#tw, 22.12.2022

###############################################################################################

                      ###   Lösungen zu Kap. 4 FUNKTIONEN, SCOPING UND ABSTRAKTION          ###

###############################################################################################



#################
#Lösung zu
#Aufgabe 4.1.1.a:
#################
#Verwenden Sie die Funktion find_root (Code 4.1.1.1), um Folgendes zu drucken:
#die Summe der sukzessiven Approximation an die Quadratwurzel von 25, 
#die Kubikwurzel von -8 und 
#die vierte Wurzel von 16. 
#Verwenden Sie 0.001 als Epsilon.
################

#Kopie von Code 4.1.1.1
#--- Eine Funktion zur Ermittlung von Wurzeln ---
def find_root(x, power, epsilon):
    #find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no real-valued roots
    low = min(-1, x)
    high = max(1, x)
    #use bisection search
    ans = (high + low)/2
    sum_ans = ans 
    while abs(ans**power - x) >= epsilon:           
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
#---

print(str(find_root(25, 2, 0.001) + find_root(-8, 3, 0.001) + find_root(16, 4, 0.001)))   
#ergibt: 4.999988555908203


#####################################################################################


#################
#Lösung zu
#Aufgabe 4.1.1.b:
#################
#Schreiben Sie eine Funktion is_in, die zwei Zeichenketten als Argumente akzeptiert
#und True zurückgibt, wenn eine der beiden Zeichenketten irgendwo in der anderen
#vorkommt. Andernfalls soll is_in False zurückgeben. 
#Tipp: Sie können den eingebauten in-Operator in verwenden.
################

def is_in(s1, s2):
    if s1 in s2:
        return True
    elif s2 in s1:
        return True
    else:
        return False

s_lang='abcde'
s_kurz='cd'
is_in(s_lang, s_kurz)             #True

is_in('ldhrkjehrkktuuri','xyz')   #False


#####################################################################################


#################
#Lösung zu
#Aufgabe 4.1.1.c:
#################
#Schreiben Sie eine Testfunktion für is_in.
################

teststring = '1123345678900ß+üpoiuzztreewqasdfghjklöä-.,mnbvcxxyyy<-löhluurraopcuoinzroip#o'

def test_is_in(s_test, n):
    from random import randint
    counter = 0
    while counter < n:
        i = randint(0,len(s_test)-1)                     #zufällige Indizes
        j = randint(0,len(s_test)-1)
        if i > j:
            i, j = j, i
        part = s_test[i : j]                             #Teilstring, der zu diesen zufälligen Indizes gehört
        print(part, '-', is_in(s_test, part))
        part_rev = part[::-1]                            #umgekehrter zufälliger Teilstring
        print(part_rev, '-', is_in(s_test, part_rev))
        counter += 1

test_is_in(teststring, 10)


#####################################################################################


#################
#Lösung zu
#Aufgabe 4.1.2.a:
#################
#Schreibe eine Funktion mult, die entweder ein oder zwei integer-Werte als Argumente 
#akzeptiert. Wenn sie mit zwei Argumenten aufgerufen wird, gibt die Funktion das Produkt 
#der beiden Argumente aus. Wenn sie mit einem Argument aufgerufen wird, gibt sie dieses 
#Argument selbst aus.
################

def mult(faktor1, faktor2 = 0):
    if faktor2 == 0:
        return faktor1
    else:
        return faktor1 * faktor2

mult(10, 5)      #50
mult(66)         #66


#####################################################################################


#################
#Lösung zu
#Aufgabe 4.1.3.a:
#################
#Weisen Sie nach, dass args im Funktionskörper der obigen Funktion mean
#ein Tupel ist, dessen Länge der Anzahl der übergebenen Argumente entspricht.
################

#Kopie von mean:
def mean(*args):
    '''Assumes at least one argument and all arguments are numbers
       Returns the mean of the arguments'''
    tot = 0
    print(args, 'ist ein', type(args), 'und hat die Länge', str(len(args)))    #<--------
    for a in args:
        tot += a
    return tot/len(args)

mean(1,2,3,4,5)


#####################################################################################


###############
#Lösung zu
#Aufgabe 4.2.a:
###############
#Schreiben Sie unter Verwendung des Algorithmus aus Code 3.2.3 (in Kap3) eine Funktion, 
#die die folgende Spezifikation erfüllt:
def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x."""
###############

#Hier ist erstmal eine Kopie von Code 3.2.3 (aus Kap3):
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
#---
#Ausgabe: 6.0224609375 is close to the log base 2 of 65

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x."""
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    #perform bisection search
    ans = (high + low)/2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

#Zum Testen:
print(str(log(65, 2, 0.01)), 'is close to the log base 2 of', 65)


#####################################################################################


###############
#Lösung zu
#Aufgabe 4.4.a:
###############
#Schreiben Sie einen Lambda-Ausdruck mit zwei numerischen Parametern. Wenn das zweite 
#Argument gleich Null ist, sollte er None returnieren. Andernfalls sollte er den Wert 
#zurückgeben, der sich aus der Division des ersten Arguments durch das zweite Argument
#ergibt. Tipp: Verwenden Sie einen (ternären) bedingten Ausdruck.
###############

lambda x,y: None if y==0 else x/y

#Testen:
loesgaufg4_4_a = lambda x,y: None if y==0 else x/y
loesgaufg4_4_a(5,2)   # 2.5
loesgaufg4_4_a(6,0)   # None


#####################################################################################


###############
#Lösung zu
#Aufgabe 4.5.a:
###############
#Was gibt s.find(sub) zurück, wenn sub nicht in s vorkommt?
###############

s = 'abc'
s.find('bc')    #1
s.find('x')     #-1

#Antw: -1


#####################################################################################


###############
#Lösung zu
#Aufgabe 4.5.b:
###############
#Verwenden Sie find, um eine Funktion zu implementieren, die der folgenden
#Spezifikation genügt:
def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
###############

#----------------
#---Variante 1---

#Erstmal ausprobieren und überlegen...
s_test = 'xabcxabcxabcxabc'
#                     |
#          das letzte x liegt bei Index: 12
#Diesen Index wollen wir nun bestimmen, indem wir alles umdrehen und von hinten suchen...
s_test_rev = s_test[::-1]
sub_test = 'x'
sub_test_rev = sub_test[::-1]
s_test_rev.find(sub_test_rev)   #3
len(s_test_rev) - (s_test_rev.find(sub_test_rev) + len(sub_test_rev))   #12 - hier ist der gesuchte Index !!

#Dann verpacken wir unsere obigen Berechnungen in die Funktion find_last_v1...
def find_last_v1(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    s_rev = s[::-1]
    sub_rev = sub[::-1]
    if s_rev.find(sub_rev) == -1:
        return None
    else:
        return len(s_rev) - (s_rev.find(sub_rev) + len(sub_rev)) 
    
#Und schliesslich die Funktion testen...
find_last_v1('xabcxabcxabcxabc', 'x')          #12
find_last_v1('xabcxabcxabcxabc', 'abc')        #13
find_last_v1('xabcxabcxabcxabc', 'y')          #None  

#----------------
#---Variante 2--- 

s_test = 'xabcxabcxabcxabc'
sub_test = 'x' 
s = s_test
idx = 0
print(s)
#Wir durchsuchen den gesamten String s_test nach Allen treffern von sub_test...
while s.find(sub_test) != -1:
    idx += len(s) - len(s[s.find(sub_test)+len(sub_test)::]) #... und merken uns an welcher Stelle (welchem Index)
                                                             #der Treffer auftrat und zwar relativ zum jeweils 
                                                             #aktuellen s. Diese relativen Indizes werden aufsummiert
                                                             #und...    
    s = s[s.find(sub_test)+len(sub_test)::]        #...dann entfernen wir den Treffer und alles, was links von 
                                                   #ihm liegt; d.h. s wird sukzessive kürzer, und irgendwann das
                                                   #verbleibende s die Abbruchbedingung der While-Schleife,...
    print(s, str(idx - len(sub_test)))  #...wobei dann der letzte Ausdruck der Form str(idx - len(sub_test)) 
                                        #die Lösung ist.
                                     
#Dann verpacken wir unsere obigen Berechnungen in die Funktion find_last_v2...
def find_last_v2(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    idx = 0
    while s.find(sub) != -1:
        idx += len(s) - len(s[s.find(sub)+len(sub)::])     
        s = s[s.find(sub)+len(sub)::]        
    return None if idx == 0 else str(idx - len(sub)) 
   
#Und schliesslich die Funktion testen...
find_last_v2('xabcxabcxabcxabc', 'x')          #12
find_last_v2('xabcxabcxabcxabc', 'abc')        #13
find_last_v2('xabcxabcxabcxabc', 'y')          #None  

#----------------
#Wir haben jetzt zwei völlig unterschiedliche Implementierungen der Funktion find_last.
#Aber beide erfüllen die Spezifikation voll und ganz:

find_last = find_last_v1
find_last('xabcxabcxabcxabc', 'x')          #12
find_last = find_last_v2
find_last('xabcxabcxabcxabc', 'x')          #12


#####################################################################################
#####################################################################################
#FINIS