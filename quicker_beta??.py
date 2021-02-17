import random
import winsound

y = (random.randint(1, 2))
f = open("notes.score", "w", encoding="utf8")
# Entering the number of notes

while True:
    try:
        how_many_notes = int(input("How many notes? "))
    except:
        continue
    break

count = 0
while count < how_many_notes:
    y = (random.randint(40, 52))
    z = (random.randint(0, 3))
    # C
    if y == 40 and z == 0:
        f.write("d0")
    elif y == 40 and z == 1:
        f.write("d1")
    elif y == 40 and z == 2:
        f.write("d2")
    elif y == 40 and z == 3:
        f.write("d3")
    # Cis
    elif y == 41 and z == 0:
        f.write("e0")
    elif y == 41 and z == 1:
        f.write("e1")
    elif y == 41 and z == 2:
        f.write("e2")
    elif y == 41 and z == 3:
        f.write("e3")
    # D
    elif y == 42 and z == 0:
        f.write("f0")
    elif y == 42 and z == 1:
        f.write("f1")
    elif y == 42 and z == 2:
        f.write("f2")
    elif y == 42 and z == 3:
        f.write("f3")
    # Dis
    elif y == 43 and z == 0:
        f.write("g0")
    elif y == 43 and z == 1:
        f.write("g1")
    elif y == 43 and z == 2:
        f.write("g2")
    elif y == 43 and z == 3:
        f.write("g3")
    # E
    elif y == 44 and z == 0:
        f.write("h0")
    elif y == 44 and z == 1:
        f.write("h1")
    elif y == 44 and z == 2:
        f.write("h2")
    elif y == 44 and z == 3:
        f.write("h3")
    # F
    elif y == 45 and z == 0:
        f.write("i0")
    elif y == 45 and z == 1:
        f.write("i1")
    elif y == 45 and z == 2:
        f.write("i2")
    elif y == 45 and z == 3:
        f.write("i3")
    # Fis
    elif y == 46 and z == 0:
        f.write("j0")
    elif y == 46 and z == 1:
        f.write("j1")
    elif y == 46 and z == 2:
        f.write("j2")
    elif y == 46 and z == 3:
        f.write("j3")
    # G
    elif y == 47 and z == 0:
        f.write("k0")
    elif y == 47 and z == 1:
        f.write("k1")
    elif y == 47 and z == 2:
        f.write("k2")
    elif y == 47 and z == 3:
        f.write("k3")
    # Gis
    elif y == 48 and z == 0:
        f.write("l0")
    elif y == 48 and z == 1:
        f.write("l1")
    elif y == 48 and z == 2:
        f.write("l2")
    elif y == 48 and z == 3:
        f.write("l3")
    # A
    elif y == 49 and z == 0:
        f.write("m0")
    elif y == 49 and z == 1:
        f.write("m1")
    elif y == 49 and z == 2:
        f.write("m2")
    elif y == 49 and z == 3:
        f.write("m3")
    # Ais
    elif y == 50 and z == 0:
        f.write("n0")
    elif y == 50 and z == 1:
        f.write("n1")
    elif y == 50 and z == 2:
        f.write("n2")
    elif y == 50 and z == 3:
        f.write("n3")
    # H
    elif y == 51 and z == 0:
        f.write("o0")
    elif y == 51 and z == 1:
        f.write("o1")
    elif y == 51 and z == 2:
        f.write("o2")
    elif y == 51 and z == 3:
        f.write("o3")
    # C2 is 52 or p
    elif y == 52 and z == 0:
        f.write("p0")
    elif y == 52 and z == 1:
        f.write("p1")
    elif y == 52 and z == 2:
        f.write("p2")
    elif y == 52 and z == 3:
        f.write("p3")

    count = count + 1

f.close()

play = open("notes.score", "r", encoding="utf8")
read = play.read()
count = 0
a = 50
b = 75
c = 100
d = 125
number_of_chars_in_file = len(read)

#11 segments by 8
#todo add more notes to player
while count < number_of_chars_in_file:
    #1
    if read[count] == "0" or read[count] == "1" or read[count] == "2" or read[count] == "3" or read[count] == "4" or read[count] == "5" or read[count] == "6" or read[count] == "7":
        pass
    #2
    elif read[count] == "8" or read[count] == "9" or read[count] == "A" or read[count] == "B" or read[count] == "C" or read[count] == "D" or read[count] == "E" or read[count] == "F":
        pass
    #3
    elif read[count] == "G" or read[count] == "H" or read[count] == "I" or read[count] == "J" or read[
            count] == "K" or read[count] == "L" or read[count] == "M" or read[count] == "N":
        pass
    #4
    elif read[count] == "O" or read[count] == "P" or read[count] == "Q" or read[count] == "R" or read[
            count] == "S" or read[count] == "T" or read[count] == "U" or read[count] == "V":
        pass
    #5
    elif read[count] == "W" or read[count] == "X" or read[count] == "Y" or read[count] == "Z" or read[
            count] == "a" or read[count] == "b" or read[count] == "c" or read[count] == "d":
        if read[count] == "d" and read[count + 1] == "0":
            winsound.Beep(262, a)
        elif read[count] == "d" and read[count + 1] == "1":
            winsound.Beep(262, b)
        elif read[count] == "d" and read[count + 1] == "2":
            winsound.Beep(262, c)
        elif read[count] == "d" and read[count + 1] == "3":
            winsound.Beep(262, d)
        else :
            print("ERROR IN SEGMENT 5")
    #6
    elif read[count] == "e" or read[count] == "f" or read[count] == "g" or read[count] == "h" or read[
            count] == "i" or read[count] == "j" or read[count] == "k" or read[count] == "l":
        if read[count] == "e" and read[count + 1] == "0":
            winsound.Beep(277, a)
        elif read[count] == "e" and read[count + 1] == "1":
            winsound.Beep(277, b)
        elif read[count] == "e" and read[count + 1] == "2":
            winsound.Beep(277, c)
        elif read[count] == "e" and read[count + 1] == "3":
            winsound.Beep(277, d)

        elif read[count] == "f" and read[count + 1] == "0":
            winsound.Beep(294, a)
        elif read[count] == "f" and read[count + 1] == "1":
            winsound.Beep(294, b)
        elif read[count] == "f" and read[count + 1] == "2":
            winsound.Beep(294, c)
        elif read[count] == "f" and read[count + 1] == "3":
            winsound.Beep(294, d)

        elif read[count] == "g" and read[count + 1] == "0":
            winsound.Beep(311, a)
        elif read[count] == "g" and read[count + 1] == "1":
            winsound.Beep(311, b)
        elif read[count] == "g" and read[count + 1] == "2":
            winsound.Beep(311, c)
        elif read[count] == "g" and read[count + 1] == "3":
            winsound.Beep(311, d)

        elif read[count] == "h" and read[count + 1] == "0":
            winsound.Beep(330, a)
        elif read[count] == "h" and read[count + 1] == "1":
            winsound.Beep(330, b)
        elif read[count] == "h" and read[count + 1] == "2":
            winsound.Beep(330, c)
        elif read[count] == "h" and read[count + 1] == "3":
            winsound.Beep(330, d)

        elif read[count] == "i" and read[count + 1] == "0":
            winsound.Beep(349, a)
        elif read[count] == "i" and read[count + 1] == "1":
            winsound.Beep(349, b)
        elif read[count] == "i" and read[count + 1] == "2":
            winsound.Beep(349, c)
        elif read[count] == "i" and read[count + 1] == "3":
            winsound.Beep(349, d)

        elif read[count] == "j" and read[count + 1] == "0":
            winsound.Beep(368, a)
        elif read[count] == "j" and read[count + 1] == "1":
            winsound.Beep(368, b)
        elif read[count] == "j" and read[count + 1] == "2":
            winsound.Beep(368, c)
        elif read[count] == "j" and read[count + 1] == "3":
            winsound.Beep(368, d)

        elif read[count] == "k" and read[count + 1] == "0":
            winsound.Beep(392, a)
        elif read[count] == "k" and read[count + 1] == "1":
            winsound.Beep(392, b)
        elif read[count] == "k" and read[count + 1] == "2":
            winsound.Beep(392, c)
        elif read[count] == "k" and read[count + 1] == "3":
            winsound.Beep(392, d)

        elif read[count] == "l" and read[count + 1] == "0":
            winsound.Beep(415, a)
        elif read[count] == "l" and read[count + 1] == "1":
            winsound.Beep(415, b)
        elif read[count] == "l" and read[count + 1] == "2":
            winsound.Beep(415, c)
        elif read[count] == "l" and read[count + 1] == "3":
            winsound.Beep(415, d)

        else:
            print("ERROR IN SEGMENT SIX")
    #7
    elif read[count] == "m" or read[count] == "n" or read[count] == "o" or read[count] == "p" or read[count] == "q" or read[count] == "r" or read[count] == "s" or read[count] == "t":
        if read[count] == "m" and read[count + 1] == "0":
            winsound.Beep(440, a)
        elif read[count] == "m" and read[count + 1] == "1":
            winsound.Beep(440, b)
        elif read[count] == "m" and read[count + 1] == "2":
            winsound.Beep(440, c)
        elif read[count] == "m" and read[count + 1] == "3":
            winsound.Beep(440, d)

        elif read[count] == "n" and read[count + 1] == "0":
            winsound.Beep(466, a)
        elif read[count] == "n" and read[count + 1] == "1":
            winsound.Beep(466, b)
        elif read[count] == "n" and read[count + 1] == "2":
            winsound.Beep(466, c)
        elif read[count] == "n" and read[count + 1] == "3":
            winsound.Beep(466, d)

        elif read[count] == "o" and read[count + 1] == "0":
            winsound.Beep(494, a)
        elif read[count] == "o" and read[count + 1] == "1":
            winsound.Beep(494, b)
        elif read[count] == "o" and read[count + 1] == "2":
            winsound.Beep(494, c)
        elif read[count] == "o" and read[count + 1] == "3":
            winsound.Beep(494, d)

        elif read[count] == "p" and read[count + 1] == "0":
            winsound.Beep(523, a)
        elif read[count] == "p" and read[count + 1] == "1":
            winsound.Beep(523, b)
        elif read[count] == "p" and read[count + 1] == "2":
            winsound.Beep(523, c)
        elif read[count] == "p" and read[count + 1] == "3":
            winsound.Beep(523, d)
        else :
            print("ERROR IN SEGMENT 7")

    #8
    elif read[count] == "u" or read[count] == "v" or read[count] == "w" or read[count] == "x" or read[
            count] == "y" or read[count] == "z" or read[count] == "Ě" or read[count] == "Š":
        pass
    #9
    elif read[count] == "Č" or read[count] == "Ř" or read[count] == "Ž" or read[count] == "Ý" or read[
            count] == "Á" or read[count] == "Í" or read[count] == "É" or read[count] == "Ů":
        pass
    #10
    elif read[count] == "Ú" or read[count] == "ě" or read[count] == "š" or read[count] == "č" or read[
            count] == "ř" or read[count] == "ž" or read[count] == "ý" or read[count] == "á":
        pass
    else:
       pass
    count = count + 2

print("Thank you for using my program")
print("Any feedback welcome")
print("the Author")
print(":-)")
