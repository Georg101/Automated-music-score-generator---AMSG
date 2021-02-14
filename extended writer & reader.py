"""
import random

y = (random.randint(1,2))
f = open("notes.score", "w")
how_many_notes = int(input("How many notes?"))
count = 0

while count <how_many_notes-2 :
    y = (random.randint(1,88))
    
    if y == 1:
        print("0")
        f.write("0")       
    elif y == 2:
        print("1")
        f.write("1")
    elif y == 3:
         f.write("2")
    elif y == 4:
         f.write("3")
    elif y == 5:
        f.write("4")
    elif y == 6:
        f.write("5")        
    elif y == 7:
        f.write("6")
    elif y == 8:
        f.write("7") 
    elif y == 9:
        f.write("8")     
    elif y == 10:
        f.write("9")
    elif y == 11:
        f.write("A")
    elif y == 12:
        f.write("B")
    elif y == 13:
        f.write("C")
    elif y == 14:
        f.write("D")
    elif y == 15:
        f.write("E")
    elif y == 16:
        f.write("F")
    elif y == 17:
        f.write("G")
    elif y == 18:
        f.write("H")
    elif y == 19:
        f.write("I")
    elif y == 20:
        f.write("J")
    elif y == 21:
        f.write("K")
    elif y == 22:
        f.write("L")
    elif y == 23:
        f.write("M")
    elif y == 24:
        f.write("N")
    elif y == 25:
        f.write("O")
    elif y == 26:
        f.write("P")
    elif y == 27:
        f.write("Q")
    elif y == 28:
        f.write("R")
    elif y == 29:
        f.write("S")
    elif y == 30:
        f.write("T")
    elif y == 31:
        f.write("U")
    elif y == 32:
        f.write("V")
    elif y == 33:
        f.write("W")
    elif y == 34:
        f.write("X")
    elif y == 35:
        f.write("Y")
    elif y == 36:
        f.write("Z")
    elif y == 37:
        f.write("a")
    elif y == 38:
        f.write("b")
    elif y == 39:
        f.write("c")
    elif y == 40:
        f.write("d")
    if y == 41:
        f.write("e")
    elif y == 42:
        f.write("f")
    elif y == 43:
        f.write("g")
    elif y == 44:
        f.write("h")
    elif y == 45:
        f.write("i")
    elif y == 46:
        f.write("j")
    elif y == 47:
        f.write("k")
    elif y == 48:
        f.write("l")
    elif y == 49:
        f.write("m")
    elif y == 50:
        f.write("n")
    elif y == 51:
        f.write("o")
    elif y == 52:
        f.write("p")
    elif y == 53:
        f.write("q")
    elif y == 54:
        f.write("r")
    elif y == 55:
        f.write("s")
    elif y == 56:
        f.write("t")
    elif y == 57:
        f.write("u")
    elif y == 58:
        f.write("v")
    elif y == 59:
        f.write("w")
    elif y == 60:
        f.write("x")
    elif y == 61:
        f.write("y")
    elif y == 62:
        f.write("z")
    elif y == 63:
        f.write("Ě")
    elif y == 64:
        f.write("Š")
    elif y == 65:
        f.write("Č")
    elif y == 66:
        f.write("Ř")
    elif y == 67:
        f.write("Ž")
    elif y == 68:
        f.write("Ý")
    elif y == 69:
        f.write("Á")
    elif y == 70:
        f.write("Í")
    elif y == 71:
        f.write("É")
    elif y == 72:
        f.write("Ů")
    elif y == 73:
        f.write("Ú")
    elif y == 74:
        f.write("ě")
    elif y == 75:
        f.write("š")
    elif y == 76:
        f.write("č")
    elif y == 77:
        f.write("ř")
    elif y == 78:
        f.write("ž")
    elif y == 79:
        f.write("ý")
    elif y == 80:
        f.write("á")
    elif y == 81:
        f.write("í")
    elif y == 82:
        f.write("é")
    elif y == 83:
        f.write("ů")
    elif y == 84:
        f.write("ú")
    elif y == 85:
        f.write("Ó")
    elif y == 86:
        f.write("Ň")
    elif y == 87:
        f.write("ó")
    elif y == 88:
        f.write("ň")
    else:
        f.write("&")
    count = count + 1   

f.close()
"""
import winsound
play = open("notes - kopie.score", "r")
read = play.read()
count = 0

while count <100 :
   
    if read[count] == "6":
        winsound.Beep(39, 1000)
    elif read[count] == "7":
        winsound.Beep(41, 1000)
    elif read[count] == "8":
        winsound.Beep(44, 1000)
    elif read[count] == "9":
        winsound.Beep(46, 1000)
    elif read[count] == "A":
        winsound.Beep(49, 1000)
    elif read[count] == "B":
        winsound.Beep(52, 1000)
    elif read[count] == "C":
        winsound.Beep(55, 1000)
    elif read[count] == "D":
        winsound.Beep(58, 1000)
    elif read[count] == "E":
        winsound.Beep(62, 1000)
    elif read[count] == "F":
        winsound.Beep(65, 1000)
    elif read[count] == "G":
        winsound.Beep(69, 1000)
    elif read[count] == "H":
        winsound.Beep(73, 1000)
    elif read[count] == "I":
        winsound.Beep(78, 1000)
    elif read[count] == "J":
        winsound.Beep(82, 1000)
    elif read[count] == "K":
        winsound.Beep(87, 1000)
    elif read[count] == "L":
        winsound.Beep(92, 1000)
    elif read[count] == "M":
        winsound.Beep(98, 1000)
    elif read[count] == "N":
        winsound.Beep(104, 1000)
    elif read[count] == "O":
        winsound.Beep(110, 1000)
    elif read[count] == "P":
        winsound.Beep(116, 1000)
    elif read[count] == "Q":
        winsound.Beep(123, 1000)
    elif read[count] == "R":
        winsound.Beep(131, 1000)
    elif read[count] == "S":
        winsound.Beep(139, 1000)
    elif read[count] == "T":
        winsound.Beep(147, 1000)
    elif read[count] == "U":
        winsound.Beep(155, 1000)
    elif read[count] == "V":
        winsound.Beep(165, 1000)
    elif read[count] == "W":
        winsound.Beep(175, 1000)
    elif read[count] == "X":
        winsound.Beep(185, 1000)
    elif read[count] == "Y":
        winsound.Beep(196, 1000)
    elif read[count] == "Z":
        winsound.Beep(208, 1000)
    elif read[count] == "a":
        winsound.Beep(220, 1000)
    elif read[count] == "b":
        winsound.Beep(233, 1000)
    elif read[count] == "c":
        winsound.Beep(1000, 1000)
    elif read[count] == "d":
        winsound.Beep(262, 1000)
    elif read[count] == "e":
        winsound.Beep(277, 1000)
    elif read[count] == "f":
        winsound.Beep(294, 1000)
    elif read[count] == "g":
        winsound.Beep(311, 1000)
    elif read[count] == "h":
        winsound.Beep(330, 1000)
    elif read[count] == "i":
        winsound.Beep(349, 1000)
    elif read[count] == "j":
        winsound.Beep(368, 1000)
    elif read[count] == "k":
        winsound.Beep(392, 1000)
    elif read[count] == "l":
        winsound.Beep(415, 1000)
    elif read[count] == "m":
        winsound.Beep(440, 1000)
    elif read[count] == "n":
        winsound.Beep(466, 1000)
    elif read[count] == "o":
        winsound.Beep(494, 1000)
    elif read[count] == "p":
        winsound.Beep(523, 1000)
    elif read[count] == "q":
        winsound.Beep(554, 1000)
    elif read[count] == "r":
        winsound.Beep(587, 1000)
    elif read[count] == "s":
        winsound.Beep(622, 1000)
    elif read[count] == "t":
        winsound.Beep(659, 1000)
    elif read[count] == "u":
        winsound.Beep(698, 1000)
    elif read[count] == "v":
        winsound.Beep(740, 1000)
    elif read[count] == "w":
        winsound.Beep(787, 1000)
    elif read[count] == "x":
        winsound.Beep(831, 1000)
    elif read[count] == "y":
        winsound.Beep(880, 1000)
    elif read[count] == "z":
        winsound.Beep(932, 1000)
   
    else:
        winsound.Beep(700, 1000)
    count = count + 1

