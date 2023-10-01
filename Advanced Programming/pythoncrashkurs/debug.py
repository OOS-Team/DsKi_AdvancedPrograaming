# Dieses Datei enthält detaillierte Infos zum Debugging im Python-Plugin
# von VSCODE. Die offizielle Doku dazu findet man hier: 
# https://code.visualstudio.com/docs/python/debugging

# Beachte: der Haltepunkt im Code ist die Funktion breakpoint(), s.u. !!!!

# Es gibt nun 3 Möglichkeiten, mit dem Debugging zu arbeiten.

# 1.) Pdb
# ------- 
# Die ganze Datei kann mit dem Run-Button (oben rechts) bzw. im Hauptmenü
# mit Run-> Run without debugging gestartet werden. 
# Aufgrund des Haltepunkts wird nun automatisch der Standard-Debugger pdb des 
# Python-Interpreters im Terminal aktiviert. Letzlich wird dadurch        
# "python.exe debug.py" ausgeführt. Das Terminal ist dann im interaktiven 
# debug-Modus (Pdb) und das Programmzeiger wartet am Haltepunkt.
# Im pdb kann man mit help eine Befehlsübersicht bekommen. Mit step kann man
# im Programm einen Schritt weitergehen. Mit list kann man sich den Quellcode
# anzeigen lassen, in dem der Programmzeiger aktuell steht. Und mit quit
# kann man den interaktiven debug-Modus wieder verlassen.

# 2.) Zellbasiertes Debuggen im interaktiven Fenster
# --------------------------------------------------
# Zuerst muss man die erste Zelle starten (Run cell). Eine Zelle ist erkennbar 
# am Spezial-Kommentar # %%, durch den die Zelle erzeugt wird.
# Im Code der darunter stehenden Zelle befindet sich der Haltepunkt (breakpoint()).
# In dem kleinen Menü direkt darüber gibt es die Option "Debug Cell". 
# Wenn man das anklickt, wird der debugger des Python-Plugins
# aktiviert. Im linken sidebar ist nun der Debug-and-Run Bereich geöffnet.
# Sowohl im kleinen, lokalen Zell-Menü, als auch in der Mitte oben erscheinen 
# Steuer-Befehle für den Programmzeiger (z.B. Step over, etc.).

# 3.) Ganze Datei debuggen
# ------------------------
# Die ganze Datei kann mit dem Debug-Button (im Pull-Down-Menü des Run-Button:
# Debug Python File) in den Debugger gefüllt werden - oder im Hauptmenü mit 
# Run->Start Debugging. Dann erscheinen wieder die Steuerbefehle des
# Programmzeigers in der Mitte oben und wenn man den Sidebar "Run and Debug"
# aufklappt werden die Programmzustände angezeigt.
# Mit dem Stop-Button (Rotes Quadrat im Debugger-Kontrollmenü, Mitte oben)
# kann man den Debug-Modus wieder verlassen. 


# Für alle Debug-Varianten Nicht vergessen, zuerst diese erste Code-Zelle auszuwerten, 
# bevor der Debugger aktiviert wird !!!
# %%
def func(x):
    c = 3
    print(c+x)

a = 2
b = 3

# %%
if(a+b == 5):
    breakpoint()         #<----- hier ist der Haltepunkt, den wir
    print('sum is 5')    #       in unseren Code eingefügt haben.
    func(a+b)            #       Bei Bedarf kann man natürlich weitere
                         #       Haltepunkte einfügen.
func(100)

#@@@@@@@@@@@@@@
#FINIS