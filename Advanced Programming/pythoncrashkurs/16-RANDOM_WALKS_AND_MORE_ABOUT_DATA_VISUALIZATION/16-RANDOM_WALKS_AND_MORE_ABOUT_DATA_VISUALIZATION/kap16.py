#tw, 30.5.23  



#                         RANDOM WALKS UND MEHR ÜBER DATENVISUALISIERUNG





#Unser Fokus ist der Einsatz von "Computation" zur Lösung von Problemen. Bislang haben
#wir uns auf Probleme konzentriert, die mit einem deterministischen Programm gelöst werden 
#können. Ein Programm ist deterministisch, wenn es mit der gleichen Eingabe immer die
#                         --------------- 
#gleiche Ausgabe erzeugt, siehe auch https://de.wikipedia.org/wiki/Determinismus_(Algorithmus) 
#Ein nicht-deterministisches Programm hingegen enthält Zustandsübergänge, die mehrwertig im
#    -----------------------     
#Sinne einer Auswahl aus einer Menge von Alternativen sein können, siehe
#https://de.wikipedia.org/wiki/Nichtdeterminismus
#Es gibt aber noch eine weitere Kategorie von Berechnungsarten. Viele Aspekte der Welt, 
#in der wir leben, können nur als stochastische Prozesse genau modelliert werden.
#                                 ----------------------
#Das Wort stammt vom griechischen Wort stokhastikos ab, das bedeutet so viel wie "fähig zu 
#erahnen". Ein stochastisches Programm, zielt, wie wir sehen werden, darauf ab, ein gutes 
#Ergebnis zu erzielen, aber die genauen Ergebnisse sind nicht garantiert. Ein Prozess ist 
#stochastisch, wenn sein nächster Zustand von einem Zufallselement abhängen kann. Der Ausgang 
#eines stochastischen Prozesses ist in der Regel ungewiss. Daher können wir selten endgültige 
#Aussagen darüber machen, was ein stochastischer Prozess tun wird. Stattdessen machen wir 
#probabilistische Aussagen darüber, was sie tun könnten. Das ganze dient also dazu, Programme
#zu entwerfen, die dabei helfen, unsichere bzw. verrauschte bzw. unvollständig bekannte 
#Situationen zu verstehen, siehe https://de.wikipedia.org/wiki/Stochastischer_Prozess
#Viele dieser Programme werden Simulationsmodelle sein. Eine Simulation ahmt die Aktivität 
#                              ------------------
#eines realen Systems nach. Man betrachtet ein derartiges Programm als ein Experimentiergerät,
#Simulationsmodell genannt, das nützliche Informationen über die möglichen Verhaltensweisen 
#des modellierten Systems liefert. Simulationen werden unter anderem häufig verwendet, um den 
#zukünftigen Zustand eines physikalischen Systems (z.B. die Temperatur des Planeten in 50 
#Jahren) abzuschätzen und als Ersatz für Experimente in der realen Welt, die zu teuer, zu 
#zeitaufwändig oder zu gefährlich wären, siehe z.B.
#https://www.llnl.gov/science-technology/hpc-simulation-data-science
#https://www.ifw-kiel.de/de/institut/forschungszentren/global-commons-und-klimapolitik/klima/
#https://bio7.org/
#u.v.a.
#und natürlich die Welt der Simulationsspiele, wie z.B.
#https://de.wikipedia.org/wiki/Dwarf_Fortress
#u.v.a.
#Es ist wichtig, immer daran zu denken, dass Simulationsmodelle, wie alle Modelle, nur eine 
#Annäherung an die Realität sind. Wir können nie sicher sein, dass sich das tatsächliche 
#System so verhält, wie es das Modell vorhersagt. Tatsächlich können wir in der Regel ziemlich 
#sicher sein, dass das tatsächliche System sich nicht genau so verhält, wie das Modell es 
#vorhersagt. Die Realität ist zwangsläufig immer komplexer als das Modell. Eine häufig 
#zitierte Binsenweisheit dazu lautet "alle Modelle falsch sind, aber einige sind nützlich." 



#------------------------------------------------------------------------------------
#                             16.1 Random Walks (Zufallsbewegungen)
#------------------------------------------------------------------------------------

#Im Jahr 1827 beobachtete der schottische Botaniker Robert Brown, dass im Wasser schwebende
#Pollen zufällig umherzuschweben schienen. Er hatte keine plausible Erklärung für dieses 
#Phänomen, das später als Brownsche Bewegung bekannt wurde, und unternahm keinen Versuch, 
#sie mathematisch zu modellieren. Er war auch nicht der erste, der dies beobachtete. 
#Bereits 60 v.Chr. beschrieb der Römer Titus Lucretius (Lukrez) in seinem Gedicht "Über die 
#Natur der Dinge" (De rerum natura) ein ähnliches Phänomen und hat sogar angedeutet, dass es 
#durch die zufällige Bewegung von Atomen verursacht wird, 
#siehe https://de.wikipedia.org/wiki/Lukrez 
#Ein klares mathematisches Modell des Phänomens wurde erstmals im Jahr 1900 in Louis Bacheliers 
#Doktorarbeit "The Theory of Speculation". Da sich diese Arbeit jedoch mit dem damals 
#anrüchigen Problem des Verständnisses der Finanzmärkte befasste, wurde sie von angesehenen 
#Wissenschaftlern weitgehend ignoriert. Fünf Jahre später brachte der junge Albert Einstein
#diese Art des stochastischen Denkens und Modellierens in die Welt der Physik ein, das fast 
#dem von Bachelier entsprach und einer Beschreibung, wie es verwendet werden könnte, um die 
#Existenz von Atomen nachzuweisen, an deren Existenz damals niemand glaubte.
#Offensichtlich schienen die Menschen damals der Meinung gewesen zu sein, dass das Verständnis 
#der Physik wichtiger sei als das Geldverdienen - die Welt hörte zu, was Einstein zu sagen 
#hatte. Das waren wohl andere Zeiten damals. Einsteins Arbeit hieß "Über die von der molekular-
#kinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten 
#Teilchen" (Mai 1905). Einstein hat das Jahr 1905 später als sein "annus mirabilis" bezeichnet. 
#In diesem Jahr veröffentlichte er zusätzlich zu seiner Arbeit über die Brownschen Bewegung 
#noch die Abhandlungen über die Erzeugung und Umwandlung des Lichts (eine Erklärung des 
#photoelektrischen Effekts, die entscheidend war für die Entwicklung der Quantentheorie), 
#über die "Elektrodynamik bewegter Körper" (spezielle Relativitätstheorie) und über die 
#Äquivalenz von Materie und Energie (E = m*c^2). Kein schlechtes Jahr für einen frisch-
#gebackenen Doktor, siehe https://de.wikipedia.org/wiki/Albert_Einstein
#
#Die Brownsche Bewegung (https://de.wikipedia.org/wiki/Brownsche_Bewegung) ist ein Beispiel 
#für eine zufällige Bewegung. Solche "Random Walks" werden häufig verwendet, um physikalische 
#Prozesse zu modellieren (z.B. Diffusion), biologische Prozesse (z.B. die Kinetik der 
#Verdrängung von RNA aus Heteroduplexen durch DNA) und soziale Prozesse (z.B. die Bewegungen 
#des des Aktienmarktes).
#
#In diesem Kapitel befassen wir uns aus drei Gründen mit Random Walks: 
#
#         *    Random Walks sind an sich schon interessant und weit verbreitet. 
#         *    Sie liefern uns ein gutes Beispiel dafür, wie man abstrakte Datentypen und 
#              Vererbung zur Strukturierung von Programmen im Allgemeinen und Simulations-
#              modelle im Besonderen einsetzen kann. 
#         *    Sie bieten die Möglichkeit, ein paar weitere Funktionen von Python vorzustellen 
#              und einige zusätzliche Techniken zur Erstellung von Diagrammen.



#------------------------------------------------------------------------------------
#                             16.2 Der Drunkard's Walk (Die Wanderung des Betrunkenen)
#------------------------------------------------------------------------------------

#Siehe https://de.wikipedia.org/wiki/Drunkard%E2%80%99s_Walk
#Schauen wir uns einen zufälligen Spaziergang an, bei dem tatsächlich gelaufen wird. 
#Ein Betrunkener steht in der Mitte eines Feldes, und jede Sekunde macht er einen Schritt 
#in eine zufällige Richtung. Wie groß ist seine mittlere Entfernung vom Ausgangspunkt in 
#1000 Sekunden (also nach 1000 Schritten)? Wenn er viele Schritte macht, wird er sich 
#wahrscheinlich immer weiter vom Ursprung entfernen, oder ist es wahrscheinlicher, dass er 
#immer wieder zum Ursprung zurückwandert und am Ende nicht weit von seinem Ausgangspunkt 
#landet? Lassen Sie uns eine Simulation schreiben, um das herauszufinden.
#Ein damit entfernt verwandtes Problem ist "Gambler's Ruin", siehe
#https://de.wikipedia.org/wiki/Ruin_des_Spielers
#

#Bevor man mit dem Entwurf eines Programms beginnt, ist es immer eine gute Idee, zu versuchen,
#eine gewisse Intuition für die Situation zu entwickeln, die das Programm modellieren soll. 
#Beginnen wir mit der Skizzierung eines einfachen Modells der Situation unter Verwendung 
#kartesischer Koordinaten. Angenommen, der Betrunkene steht auf einem Feld steht, auf dem 
#das Gras auf mysteriöse Weise so geschnitten wurde, dass es einem Stück Millimeterpapier 
#ähnelt. Nehmen wir weiter an, dass jeder Schritt des Betrunkenen die Länge eins hat und 
#parallel zur x-Achse oder zur y-Achse verläuft.

#         g ┌────┬────┬────┬────┬────┬─────┬────┐              g ┌────┬────┬────┬────┬────┬─────┬────┐
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#         f ├────┼────┼────┼────┼────┼─────┼────┤              f ├────┼────┼────┼────┼────┼─────┼────┤
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#         e ├────┼────┼────┼────o────┼─────┼────┤              e ├────┼────┼────┼────│────o─────┼────┤
#           │    │    │    │    ▲    │     │    │                │    │    │    │    │    ▲     │    │
#           │    │    │    │    │    │     │    │   1.Schritt    │    │    │    │    │    │     │    │   2.Schritt
#         d ├────┼────┼────o─◄──x──►─o─────┼────┤    =====>    d ├────┼────┼─────────o─◄──x───►─o────┤   =====>  ...
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#           │    │    │    │    ▼    │     │    │                │    │    │    │    │    ▼     │    │
#         c ├────┼────┼────┼────o────┼─────┼────┤              c ├────┼────┼────┼────│────o─────┼────┤
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#         b ├────┼────┼────┼────┼────┼─────┼────┤              b ├────┼────┼────┼────┼────┼─────┼────┤
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#           │    │    │    │    │    │     │    │                │    │    │    │    │    │     │    │
#         a └────┴────┴────┴────┴────┴─────┴────┘              a └────┴────┴────┴────┴────┴─────┴────┘
#           1    2    3    4    5    6     7    8                1    2    3    4    5    6     7    8

#Das obige Bild zeigt einen Betrunkenen x, der mitten auf dem Feld steht.
#Mit o sind alle Orte markiert, an denen er nach einem Schritt sein könnte. 
#Beachten Sie, dass er nach einem Schritt immer genau eine Einheit von seinem Ausgangspunkt 
#entfernt ist. Nehmen wir an, dass er bei seinem ersten Schritt von Ausgangsort (d,5) nach 
#Osten wandert, also nach (d,6).

#Zweiter Schritt:
#----------------
#Wie weit könnte er nach seinem zweiten Schritt vom Ausgangspunkt (d,5) dann entfernt sein?
#Betrachtet man die mit o markierten Orte in der obigen Abbildung rechts, so sieht man, 
#dass er mit einer Wahrscheinlichkeit von 0.25 mit dem Abstand 0 vom Ausgangsort (d,5) 
#entfernt sein wird (weil es nur eine Möglichkeit gibt von (d,6) nach (d,5) zurückzukehren), 
#und mit einer Wahrscheinlichkeit von 0.25 wird er 2 Einheiten von (d,5) entfernt sein (weil 
#es nur eine Möglichkeit gibt, weiter nach Osten zu laufen, also nach (d,7)), und mit einer 
#Wahrscheinlichkeit von 0.5 wird er sqrt(2) Einheiten von (d,5) entfernt sein (weil es zwei 
#Möglichkeiten gibt, sich vertikal zu bewegen, entweder nach (e,6) oder nach (c,6) - und nach
#Pythagoras ist der Abstand dieser beiden Punkte von (d,5) eben gerade 1.414=sqrt(2)).
#Im Durchschnitt wird er also nach zwei Schritten weiter entfernt sein als nach einem Schritt,
#denn 0.25 * 0 + 0.25 * 2 + 0.5 * 1.414 > 1.2
 
#Dritter Schritt:
#----------------
#Was ist mit dem dritten Schritt? Wenn der zweite Schritt nach Norden oder Süden erfolgt ist, 
#bringt der dritte Schritt den Betrunkenen in der Hälfte der Fälle näher an den Ursprung 
#heran und in der anderen Hälfte der Fälle führt er sie weiter weg. 
#Z.B. --2.Schritt(nach Norden)--> (e,6) --3.Schritt--> (d,6) oder (e,5)  => Entfernung zu (d,5): 1
#                                                      (f,6) oder (e,7)  => Entfernung zu (d,5): sqrt(5)
#bzw. --2.Schritt(nach Süden)--> (c,6) --3.Schritt--> (d,6) oder (c,5)  => Entfernung zu (d,5): 1
#                                                     (b,6) oder (c,7)  => Entfernung zu (d,5): sqrt(5)
#Also: 0.25 * (1 + sqrt(5) + 1 + (sqrt(5)))
#Wenn der zweite Schritt nach Westen gerichtet war (also wieder auf den Ursprung (d,5)), 
#führt der dritte Schritt notwendigerweise wieder weg vom Ursprung, d.h. Entfernung: 1 
#Wenn der zweite Schritt nach Osten gerichtet war (also in (d,7) gelandet ist), ist der 
#dritte Schritt im Viertel der Fälle näher am Ursprung (da er wieder in (d,6) gelandet ist) 
#und in drei Viertel der Fälle ((e,7), (d,8), (c,7)) noch weiter weg vom Ursprung (d,5).
#
#Also insgesamt nach dem dritten Schritt die mittlere Entfernung vom Ursprung (d,5): 
#0.25 * (1 + sqrt(5) + 1 + (sqrt(5))) + 0.25 * 1 + 0.25 * (0.25 * 1 + 0.75 * (sqrt(5) + 3 + sqrt(5))) = 3.3315

from math import sqrt
0.25 * (1 + sqrt(5) + 1 + (sqrt(5))) + 0.25 * 1 + 0.25 * (0.25 * 1 + 0.75 * (sqrt(5) + 3 + sqrt(5)))

#Es scheint, je mehr Schritte der Betrunkene macht, desto größer ist die erwartete Entfernung 
#vom Ursprung. Wir könnten diese erschöpfende Aufzählung von Möglichkeiten fortsetzen
#und vielleicht eine ziemlich gute Intuition darüber entwickeln, wie diese Entfernung mit der 
#Anzahl der Schritte wächst. Da dies jedoch sehr mühsam ist, scheint es eine bessere Idee zu 
#sein, ein Programm zu schreiben, das diese Aufgabe für uns übernimmt.

#Beginnen wir den Entwurfsprozess, indem wir über einige Datenabstraktionen nachdenken, 
#die für die Erstellung dieser Simulation und vielleicht auch anderer Arten von 
#Random Walks nützlich sein könnten. Wie üblich, sollten wir versuchen, Datentypen zu 
#erfinden, die den Arten von Dingen entsprechen die in der Situation vorkommen, die wir zu 
#modellieren versuchen. 
#Drei naheliegende Typen (also Klassen) sind Location, Field und Drunk. Wenn wir uns die
#Klassen, die diese Typen bereitstellen ansehen, sagen sie etwas über die Art der
#Simulationsmodelle aus, die mit ihnen erstellt werden können.

#Beginnen wir mit der Klasse Location, siehe Code 16.2.1. Dies ist eine einfache Klasse,
#aber sie verkörpert zwei wichtige Entscheidungen. Sie sagt uns, dass die Simulation
#höchstens zwei Dimensionen umfassen wird. Dies steht im Einklang mit den obigen Bildern. 
#Da die Werte, die für delta_x und delta_y eher Fließkommazahlen als ganze Zahlen sein 
#können, gibt es keine eingebaute Annahmen über die Menge der Richtungen, in die sich 
#ein Betrunkener bewegen könnte. Dies ist eine Verallgemeinerung des obigen, eher 
#informellen Modells, in dem jeder Schritt die Länge eins hatte und parallel zur x-Achse 
#oder y-Achse verlief.
#
#Die Klasse Field, siehe Code 16.2.1, ist ebenfalls recht einfach, aber auch sie enthält
#bemerkenswerte Entscheidungen. Sie verwaltet einfach eine Zuordnung von Betrunkenen zu
#Orten. Es gibt keine Beschränkungen für Orte, so dass ein Feld von unbegrenzter Größe ist. 
#Es erlaubt das Hinzufügen mehrerer Betrunkener in ein Feld an zufälligen Orten. Sie sagt 
#nichts über die Art und Weise aus, in denen sich Betrunkene bewegen, noch verbietet es, 
#dass mehrere Betrunkene denselben Ort besetzen oder sich durch Ort zu bewegen, an denen
#sich bereits anderen Betrunkene aufhalten.
#
#Die Klassen Drunk und Usual_drunk in Code 16.2.1 definieren, wie ein Betrunkener durch 
#das Feld wandern kann. Insbesondere der Wert von step_choices in Usual_drunk führt die 
#Einschränkung ein, dass jeder Schritt die Länge eins hat und entweder parallel zur x-Achse 
#oder zur y-Achse verläuft. Da die Funktion random.choice ein zufällig ausgewähltes Element
#der ihr übergebenen Sequenz zurückgibt, ist jede Art von Schritt gleich wahrscheinlich
#und wird von den vorherigen Schritten nicht beeinflusst. Später werden wir weitere Unter-
#klassen von Drunk mit verschiedenen Arten von Verhalten betrachten.



#Code 16.2.1
#--- Die Klassen Location, Field und Drunk ---
import random

class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self._x, self._y = x, y

    def move(self, delta_x, delta_y):
        """delta_x and delta_y are numbers"""
        return Location(self._x + delta_x, self._y + delta_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def dist_from(self, other):
        ox, oy = other._x, other._y
        x_dist, y_dist = self._x - ox, self._y - oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return f'<{self._x}, {self._y}>'

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self._name = name

    def __str__(self):
        if self != None:
            return self._name
        return 'Anonymous'

class Usual_drunk(Drunk):
    def take_step(self):
        step_choices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

class Field(object):
    def __init__(self):
        self._drunks = {}
        
    def add_drunk(self, drunk, loc):
        if drunk in self._drunks:
            raise ValueError('Duplicate drunk')
        else:
            self._drunks[drunk] = loc
            
    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self._drunks[drunk]
        #use move method of Location to get new location
        self._drunks[drunk] = current_location.move(x_dist, y_dist)
        
    def get_loc(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        return self._drunks[drunk]
#---



#Probieren wir die beiden Klassen mal aus - bißchen rumspielen damit...
loc1 = Location(1,1)
loc2 = Location(1,2)
print(loc1, loc2)                 #<1, 1> <1, 2>
loc1.dist_from(loc2)              #1.0
loc2_1 = loc2.move(0,1)
print(loc2_1)                     #<1, 3>
otto = Usual_drunk('Otto')
print(otto)                       #Otto
hamlet = Usual_drunk('Hamlet')
print(hamlet)                     #Hamlet
#Jeder Usual_drunk kann sich in jedem Schritt in einer der vier Himmelsrichtungen bewegen:
#
#                         (0,1) Nord
#                           ▲
#                           │
#                           │
#        West (-1,0) ◄──────┼──────► (1,0) Ost
#                           │
#                           │
#                           ▼
#                        (0,-1) Süd
#
#hamlet z.B. bewegt sich in 10 aufeinander folgenden Schritten zufällig so:
for _ in range(10):           
    print(hamlet.take_step())     #(0, -1)
                                  #(1, 0)
                                  #(-1, 0)
                                  #(1, 0)
                                  #(-1, 0)
                                  #(0, 1)
                                  #(1, 0)
                                  #(1, 0)
                                  #(0, 1)
                                  #(0, -1)
#Jetzt erzeugen wir ein Feld und setzen hamlet und otto an Locations loc1 und loc2 drauf
feld = Field()
feld.add_drunk(hamlet, loc1)
feld.get_loc(hamlet).__str__()        #'<1, 1>'
print(feld.get_loc(hamlet))           #<1, 1>
feld.add_drunk(otto, loc2)
print(feld.get_loc(otto))             #<1, 2>
#Das Feld verwaltet seine Betrunkenen mit Hilfe des dicts _drunks:
feld._drunks       #{<__main__.Usual_drunk at 0x18a3b53fe50>: <__main__.Location at 0x18a3b44dbb0>,
                   # <__main__.Usual_drunk at 0x18a3b0529d0>: <__main__.Location at 0x18a3b44d910>}
#Jetzt soll otto sich mal bewegen:
feld.move_drunk(otto)
#Er wird sich zufällig in eine der vier Himmelsrichtungen bewegt haben. Mal sehen,
#wohin es ihn verschlagen hat:
print(feld.get_loc(otto))       #<2, 2> (das kann bei ihnen natürlich ein anderer Ort sein!)
#Damit haben wir die wesentlichen Funktionalitäten der Klassen von Code 16.2.1 kennengelernt.

#Der nächste Schritt ist die Verwendung dieser Klassen, um eine Simulation zu erstellen, 
#die die ursprüngliche Frage (siehe oben, erster Absatz in 16.2) beantwortet. Der folgende
#Code 16.2.2 enthält drei Funktionen, die zusammenspielen, um diese Simulation realisieren.
#--- walk --- läßt einen Betrunkenen auf einem Feld rumlaufen. Nach einer vorgegebenen Anzahl von
#Schritten wird seine Distanz zum Startpunkt returniert.
#--- sim_walks --- führt walk mehrmals (num_trials) aus und returniert eine Liste der jeweils
#erreichten Distanzen zurück.
#--- drunk_test --- ist die Hauptfunktion der Simulation. Sie führt sim_walks mehrmals aus
#und zwar nach Vorgabe der Elemente in walk_lengths.


#Code 16.2.2
#--- Die Drunkard's Walk Simulation ---
def walk(f, d, num_steps):
    """Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
       Moves d num_steps times; returns the distance between the
       final location and the location at the start of the  walk."""
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))

def sim_walks(num_steps, num_trials, d_class):
    """Assumes num_steps an int >= 0, num_trials an int > 0,
         d_class a subclass of Drunk
       Simulates num_trials walks of num_steps steps each.
       Returns a list of the final distances for each trial"""
    Homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, num_steps), 1))
    return distances

def drunk_test(walk_lengths, num_trials, d_class):
    """Assumes walk_lengths a sequence of ints >= 0
         num_trials an int > 0, d_class a subclass of Drunk
       For each number of steps in walk_lengths, runs sim_walks with
         num_trials walks and prints results"""
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'walk of', num_steps, 'steps: Mean =',
              f'{sum(distances)/len(distances):.3f}, Max =',
              f'{max(distances)}, Min = {min(distances)}')
#---



#Die Funktion drunk_test hat auch einen Parameter, d_class, vom Typ class. Er wird zweimal 
#verwendet, einmal im Aufruf von sim_walks und einmal in der ersten print-Anweisung. 
#In der print-Anweisung wird das eingebaute Klassen-Attribut __name__ verwendet, um eine 
#Zeichenkette mit dem Namen der Klasse zu erhalten.
#Wenn wir drunk_test ausführen

drunk_test((10, 100, 1000, 10000), 100, Usual_drunk) 

#wird Folgendes gedruckt:
#          Usual_drunk walk of 10 steps: Mean = 2.774, Max = 7.1, Min = 0.0
#          Usual_drunk walk of 100 steps: Mean = 10.040, Max = 28.3, Min = 0.0
#          Usual_drunk walk of 1000 steps: Mean = 26.892, Max = 64.9, Min = 2.0
#          Usual_drunk walk of 10000 steps: Mean = 88.387, Max = 213.1, Min = 9.1
#
#Wie zu erwarten, wächst der mittlere Abstand vom Ursprung mit der Anzahl der Schritte.
#Schauen wir uns nun eine Darstellung der mittleren Abstände vom Ursprung an, 
#siehe Abb-16-2-a.PNG. 
#Um ein Gefühl dafür zu vermitteln, wie schnell der Abstand wächst, haben wir in diese Abb.
#eine zusätzliche Linie eingezeichnet, die die Quadratwurzel der Anzahl der Schritte
#der Schritte anzeigt (und wir haben zusätzlich die Anzahl der Schritte auf 100.000 
#(= 10^5) erhöht).



################
#Aufgabe 16.2.a:
################
#Schreiben Sie geeigneten Code, um das Diagramm von Abb-16-2-a.PNG zu erzeugen.
#Hinweis: Beachten Sie, dass der gezeigte Plot sowohl in der Ordinate als auch in der
#Abszisse eine logarithmische Skala besitzt.
################



#Gibt diese Darstellung Aufschluss über den voraussichtlichen endgültigen Aufenthaltsort des 
#Betrunkenen? Sie sagt uns, dass sich der Betrunkene im Durchschnitt irgendwo auf einem Kreis 
#befindet, dessen Mittelpunkt im Ursprung liegt und dessen Radius gleich der erwarteten 
#Entfernung vom Ursprung ist. Allerdings sagt sie uns wenig darüber aus, wo wir den 
#Betrunkenen am Ende eines bestimmten Walks finden. Wir kommen auf dieses Thema im nächsten 
#Abschnitt zurück.



#------------------------------------------------------------------------------------
#                             16.3 Biased Random Walks (Verzerrte Random Walks)
#------------------------------------------------------------------------------------

#Siehe...
#https://de.wikipedia.org/wiki/Random_Walk
#https://en.wikipedia.org/wiki/Random_walk
#https://en.wikipedia.org/wiki/Biased_random_walk_on_a_graph
#
#Nun, da wir eine funktionierende Simulation haben, können wir damit beginnen, sie zu 
#modifizieren, um andere Arten von Random Walks zu untersuchen. Nehmen wir zum Beispiel an, 
#dass das Verhalten eines Betrunkenen auf der nördlichen Hemisphäre beschreiben wollen, 
#der die Kälte hasst und selbst in der Lage ist, sich doppelt so schnell zu bewegen, wenn 
#seine Zufallsbewegung in südliche Richtung führt. Oder vielleicht ein phototroper 
#Betrunkener, der sich immer in Richtung der Sonne bewegt (morgens nach Osten und nachmittags
#nach Westen). Dies sind Beispiele für verzerrte Zufallsbewegungen. Der Walk ist immer noch 
#stochastisch, aber es gibt eine Verzerrung (bias) im Ergebnis.

#Der untenstehende Code 16.3.1 definiert zwei weitere Unterklassen von Drunk: Cold_drunk hat 
#eine Vorliebe für den Süden (0.0, -2.0) und EW_drunk läuft nur nach Osten (1.0, 0.0) und 
#Westen (-1.0, 0.0). In jedem Fall beinhaltet die Spezialisierung also die Wahl eines 
#geeigneten Wertes für step_choices. Die Funktion sim_all iteriert dann über eine Folge von
#Unterklassen von Drunk, um Informationen darüber zu erhalten, wie sich jede Art verhält.



#Code 16.3.1
#--- verschiedene Unterklassen der Basisklasse Drunk ---
class Cold_drunk(Drunk):
    def take_step(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class EW_drunk(Drunk):
    def take_step(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices) 

def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)
#---



#Rufen wir nun sim_all mal auf...
sim_all((Usual_drunk, Cold_drunk, EW_drunk), (100, 1000), 10)
#das ergibt:
#          Usual_drunk walk of 100 steps: Mean = 8.730, Max = 21.3, Min = 3.2
#          Usual_drunk walk of 1000 steps: Mean = 25.350, Max = 51.0, Min = 9.9
#          Cold_drunk walk of 100 steps: Mean = 25.830, Max = 40.8, Min = 18.7
#          Cold_drunk walk of 1000 steps: Mean = 245.310, Max = 292.3, Min = 210.0
#          EW_drunk walk of 100 steps: Mean = 8.200, Max = 18.0, Min = 0.0
#          EW_drunk walk of 1000 steps: Mean = 23.800, Max = 48.0, Min = 0.0

#Es scheint, dass sich unser wärmesuchender Betrunkener (Cold_drunk) schneller vom Ursprung 
#entfernt als die beiden anderen Arten von Betrunkenen. Es ist jedoch nicht einfach, alle
#alle Infos des obigen Outputs zu verdauen. Es ist wieder einmal an der Zeit von der 
#textuellen Ausgabe wegzukommen und mit Diagrammen zu arbeiten.
#Da wir verschiedene Arten von Betrunkenen im selben Diagramm darstellen wollen, werden wir 
#jeder Art von Betrunkenen einen eigenen Stil zuordnen, damit man sie leichter unterscheiden 
#kann. Der Stil wird drei Aspekte haben:
#
#      *    Die Farbe der Linie und der Markierung
#      *    Die Form der Markierung
#      *    Die Art der Linie, z.B. durchgezogen oder gepunktet

#Die Klasse style_iterator, siehe Code 16.3.2, durchläuft eine Folge von Stilen, die durch 
#das Argument von style_iterator.__init__ definiert sind. "Durchläuft" ist nicht ganz
#korrekt - besser: "Rotiert fortlaufend" durch eine Sequenz von Stilen.



#Code 16.3.2
#--- Iteration über Stile ---
class style_iterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
#---



#Analog zur Simulation von Code 16.3.1 wird im folgenden Code 16.3.3 Simulationen
#verschiedener Drunk-Varianten mit unterschiedlichen Schritt-Anzahlen (walk_lengths)
#erprobt und deren Ergebnisse geplottet...   



#Code 16.3.2
#--- Aufzeichnung der Spaziergänge verschiedener Betrunkener ---
import matplotlib.pyplot as plt

def sim_drunk(num_trials, d_class, walk_lengths):
    meanDistances = []
    for num_steps in walk_lengths:
        print('Starting simulation of', num_steps, 'steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    style_choice = style_iterator(('m-', 'r:', 'k-.'))
    for d_class in drunk_kinds:
        cur_style = style_choice.next_style()
        print('Starting simulation of', d_class.__name__)
        means = sim_drunk(num_trials, d_class, walk_lengths)
        plt.plot(walk_lengths, means, cur_style, label = d_class.__name__)
    plt.title(f'Mean Distance from Origin ({num_trials} trials)')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc = 'best')
    plt.semilogx()
    plt.semilogy()
#---



#Probieren wir es aus mit unseren drei Drunk-Varianten, die unterschiedliche Längen von
#Spaziergängen absolvieren sollen. :
sim_all_plot((Usual_drunk, Cold_drunk, EW_drunk), (10, 100, 1000, 10000, 100000), 100)
#(siehe Abb-16-3-2-a.PNG)

#Der normale Betrunkene (Usual_drunk) und der phototrope Betrunkene (EW_drunk) scheinen sich
#in etwa gleichem Tempo vom Ursprung zu entfernen, aber der wärmesuchende Betrunkene 
#(Cold_drunk) scheint sich um Größenordnungen schneller zu bewegen. Dies ist interessant, 
#da er sich im Durchschnitt nur 25 % schneller bewegt (er macht im Durchschnitt fünf Schritte 
#für vier Schritte der der anderen).

#Konstruieren wir ein anderes Diagramm, um einen besseren Einblick in das Verhalten dieser 
#drei Klassen zu erhalten. Anstatt die Veränderung der Entfernung über die Zeit für eine 
#zunehmende Anzahl von Schritten darzustellen, zeigt der folgende Code 16.3.3 die Verteilung 
#der endgültigen Positionen für eine einzige Anzahl von Schritten...



#Code 16.3.3
#--- Plotten der finalen Standorte ---
def get_final_locs(num_steps, num_trials, d_class):
    locs = []
    d = d_class()
    for t in range(num_trials):
        f = Field()
        f.add_drunk(d, Location(0, 0))
        for s in range(num_steps):
            f.move_drunk(d)
        locs.append(f.get_loc(d))
    return locs

def plot_locs(drunk_kinds, num_steps, num_trials):
    style_choice = style_iterator(('k+', 'r^', 'mo'))
    for d_class in drunk_kinds:
        locs = get_final_locs(num_steps, num_trials, d_class)
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        meanX = sum(x_vals)/len(x_vals)
        meanY = sum(y_vals)/len(y_vals)
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style,
                 label = (f'{d_class.__name__} mean loc. = <' + f'{meanX}, {meanY}>'))
    plt.title(f'Location at End of Walks ({num_steps} steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc = 'best')
#---



#Als erstes erstellt plot_locs eine Instanz von style_iterator mit drei Arten von 
#Markierungen für die Plots. Anschließend verwendet plt.plot diese Instanz, um eine 
#Markierung an derjenigen Stelle zu platzieren, die dem Ende eines jeden Versuchs entspricht.
#Der Aufruf von plt.plot legt alsodie Farbe und Form der zu zeichnenden Markierung unter 
#Verwendung der vom Iterator style_iterator zurückgegebenen Werte fest.
#Probieren wir es aus...

plot_locs((Usual_drunk, Cold_drunk, EW_drunk), 100, 200)
#(siehe Abb-16-3-3-a.PNG)

#Als Erstes ist zu sagen, dass sich unsere Betrunkenen anscheinend so verhalten wie 
#angekündigt. Der EW_drunk landet auf der x-Achse, der Cold_drunk scheint nach Süden 
#vorgedrungen zu sein, und der Usual_drunk scheint ziellos umhergeirrt zu sein.
#Aber warum scheint es viel weniger Kreismarkierungen zu geben als Dreieck- oder 
#+-Markierungen? Weil viele der Wanderungen des EW_drunk an der gleichen Stelle endeten. 
#Das ist nicht überraschend, wenn man die geringe Anzahl von möglichen Endpunkten (200) 
#für den EW_drunk berücksichtigt. Auch die Kreismarkierungen scheinen ziemlich gleichmäßig 
#über die x-Achse verteilt zu sein.
#Es ist, zumindest für uns, nicht sofort ersichtlich, warum der Cold_drunk es schafft, 
#sich im Durchschnitt so viel weiter vom Ursprung zu entfernen als die anderen Betrunkenen. 
#Vielleicht ist es an der Zeit, nicht nur die die Endpunkte vieler Spaziergänge zu betrachten, 
#sondern einzelne Wege insgesamt. Dazu dient der folgende Code 16.3.4... 



#Code 16.3.4
#--- Spaziergänge aufzeichnen ---
def trace_walk(drunk_kinds, num_steps):
    style_choice = style_iterator(('k+', 'r^', 'mo'))
    f = Field()
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style, label = d_class.__name__)
    plt.title('Spots Visited on Walk ('
                + str(num_steps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc = 'best')
#---



#Probieren wir es aus...

trace_walk((Usual_drunk, Cold_drunk, EW_drunk), 200)
#(siehe Abb-16-3-4-a.PNG)

#Da der Spaziergang 200 Schritte lang ist und der EW_drunk weniger als 30 verschiedene Orte 
#besucht, ist es klar, dass er viel Zeit damit verbringt, dieselben Orte immer wieder zu
#besuchen. Die gleiche Art von Beobachtung gilt für den Usual_drunk. Im Gegensatz dazu macht 
#der Cold_drunk zwar nicht gerade einen Florida-Besuch, aber er verbringt relativ wenig Zeit 
#damit, Orte zu besuchen, an denen er schon einmal war.
#Keine dieser Simulationen ist für sich genommen interessant. (In Kapitel 18 werden wir uns 
#mit intrinsisch interessanteren Simulationen beschäftigen.) Aber es gibt einige Punkte, 
#die es wert sind, mitgenommen zu werden:
#
#       *    Zu Beginn haben wir unseren Simulationscode in vier separate Brocken aufgeteilt. 
#            Drei davon waren Klassen (Location, Field, und Drunk), die den abstrakten 
#            Datentypen entsprechen, die in der informellen Beschreibung des Problems 
#            auftauchten. Der vierte Brocken war eine Gruppe von Funktionen, die diese 
#            Klassen zur konkreten Implementierung einer einfachen Simulation verwendeten.
#
#       *    Anschließend haben wir Drunk zu einer Hierarchie von Klassen ausgebaut, 
#            so dass wir verschiedene Arten von verzerrten Random Walks beobachten konnten. 
#            Der Code für Location und Field blieb unangetastet, aber der Simulationscode
#            wurde geändert durch verschiedenen Unterklassen von Drunk. 
#            Dabei haben wir uns die Tatsache zunutze gemacht, dass eine Klasse selbst ein 
#            Objekt ist und daher als Argument übergeben werden kann.
#
#       *    Schließlich nahmen wir eine Reihe von inkrementellen Änderungen an der
#            Simulation vor, die keine Änderungen an den Klassen beinhalteten, die die 
#            abstrakten Typen repräsentieren. Diese Änderungen umfassten hauptsächlich
#            die Einführung von Diagrammen, die einen Einblick in die verschiedenen Walks
#            erlaubten. Dies ist typisch für die Art und Weise, in der Simulationen
#            entwickelt werden. Zuerst wird die Basissimulation zum Laufen gebracht, und 
#            dann werden Funktionen hinzugefügt.



#------------------------------------------------------------------------------------
#                             16.4 Trügerische Felder (treacherous fields)
#------------------------------------------------------------------------------------

#Wir können leicht eine neue Art Eigenschaft in die Felder (fields) unseres Random Walks 
#einbauen, indem wir Locations mit "Wurmlöchern" erstellen, die es erlauben instantan von
#einem Ort zu einem weit entfernten Ort zu springen. Der folgende Code 16.4.1 zeigt wie man
#das umsetzen könnte. Die zweite Codezeile in der Funktion trace_walk (siehe Code 16.3.4) 
#wird dabei z.B. durch die folgende Zeile ersetzt
#
#      f = Odd_field(1000, 100, 200)
#
#In einem Odd_field wird ein Drunk, der ein Wurmloch betritt, zu dem Ort am anderen Ende 
#des Wurmlochs transportiert...



#Code 16.4.1
#--- Felder mit seltsamen Eigenschaften und Modifikation von trace_walk ---
class Odd_field(Field):
    def __init__(self, numHoles, x_range, y_range):
        Field.__init__(self)
        self._wormholes = {}
        for _ in range(numHoles):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            newX = random.randint(-x_range, x_range)
            newY = random.randint(-y_range, y_range)
            newLoc = Location(newX, newY)
            self._wormholes[(x, y)] = newLoc

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        x = self._drunks[drunk].get_x()
        y = self._drunks[drunk].get_y()
        if (x, y) in self._wormholes:
            self._drunks[drunk] = self._wormholes[(x, y)]

def trace_walk(drunk_kinds, num_steps):
    style_choice = style_iterator(('k+', 'r^', 'mo'))
    f = Odd_field(1000, 100, 200) # <--------------------- Änderung !!
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style, label = d_class.__name__)
    plt.title('Spots Visited on Walk ('
                + str(num_steps) + ' steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc = 'best')
#---



#Probieren wir es aus...

trace_walk((Usual_drunk, Cold_drunk, EW_drunk), 500)
#(siehe Abb-16-4-1-a.PNG)

#Das sieht ziemlich seltsam aus!
#Die Veränderung der Eigenschaften des Feldes hatte eindeutig eine dramatische Wirkung. 
#Das ist jedoch nicht der Sinn dieses Beispiels. Die wichtigsten Punkte sind:
#
#    *   Aufgrund der Art und Weise, wie wir unseren Code strukturiert haben, 
#        war es einfach, eine wesentliche Änderung der modellierten Situation 
#        zu berücksichtigen. So wie wir verschiedene Arten von Betrunkenen hinzufügen 
#        konnten, ohne die Klasse Field anzufassen, können wir auch eine neue Art 
#        von Field hinzufügen, ohne dass wir Drunk oder eine seiner Unterklassen
#        modifizieren müssen. (Wären wir vorausschauend genug gewesen, das Feld 
#        zu einem Parameter von trace_walk zu machen, hätten wir auch trace_walk 
#        nicht ändern müssen.)
#
#    *   Es wäre zwar möglich gewesen, analytisch verschiedene Informationen über das 
#        erwartete Verhalten des einfachen Random Walk und sogar des Biased Random Walk 
#        abzuleiten. Aber es wäre eine Herausforderung gewesen, sobald die Wurmlöcher 
#        eingeführt worden wären. Es war jedoch äußerst einfach, die Simulation zu ändern, 
#        um die neue Situation zu modellieren. Simulationsmodelle genießen diesen Vorteil 
#        oft im Vergleich zu analytischen Modellen.



#------------------------------------------------------------------------------------
#                             16.5 In diesem Kapitel eingeführte Begriffe
#------------------------------------------------------------------------------------

#           stochastic process
#           simulation model
#           random walk
#           biased random walks
#           logarithmic scale
  

#####################################################################################
#####################################################################################
#FINIS