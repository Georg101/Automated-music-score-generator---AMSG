import random
import time
import re
import winsound

f = open("notes.score", "w")
y = (random.randint(0,6))

how_many_notes = int(input("How many notes?"))
#this part makes the first and last note be same
if y == 0:
    print("c")
    f.write("c")
    
elif y == 1:
    print("d")
    f.write("d")

elif y == 2:
     print("e")
     f.write("e")

elif y == 3:
     print("f")
     f.write("f")

elif y == 4:
    print("g")
    f.write("g")

elif y == 5:
    print("a")
    f.write("a")
else:
    print("h")
    f.write("h")

#this part writes x notes to the file notes.score
count = 0

while count <how_many_notes-2 :
    x = (random.randint(0,6))
    if x == 0:
        print("c")
        f.write("c")
    
    elif x == 1:
        print("d")
        f.write("d")

    elif x == 2:
        print("e")
        f.write("e")

    elif x == 3:
        print("f")
        f.write("f")

    elif x == 4:
        print("g")
        f.write("g")

    elif x == 5:
        print("a")
        f.write("a")
    else:
        print("h")
        f.write("h")
    count = count + 1


#this part makes the first and last note be same
if y == 0:
    print("c")
    f.write("c")
    
elif y == 1:
    print("d")
    f.write("d")

elif y == 2:
     print("e")
     f.write("e")

elif y == 3:
     print("f")
     f.write("f")

elif y == 4:
    print("g")
    f.write("g")

elif y == 5:
    print("a")
    f.write("a")
else:
    print("h")
    f.write("h")


f.write("c")

    
f.close()


#this part checks for "cd", "dc", "hc", "ch"
f = open("notes.score", "r")
read = f.read()
text = read
if re.search(r"ch", text):
    print("ch Match found")
else:
    print("ch Match not found")

if re.search(r"dc", text):
    print("dc Match found")
else:
    print("dc Match not found")

if re.search(r"cd", text):
    print("cd Match found")
else:
    print("cd Match not found")

if re.search(r"hc", text):
    print("hc Match found")
else:
    print("hc Match not found")

# this part deletes the "cd", "dc", "hc", "ch" patterns


f = open('notes.score', "r+")
a = open('notes.v1', "w")

data = f.read().replace('cd', '')
a.write(data)
print(data)
f.close()
a.close()

f = open('notes.v1', "r+")
b = open('notes.v2', "w")

data = f.read().replace('dc', '')
b.write(data)
print(data)
f.close()
b.close()

f = open('notes.v2', "r+")
c = open('notes.v3', "w")

data = f.read().replace('hc', '')
c.write(data)
print(data)
f.close()
c.close()

f = open('notes.v3', "r+")
d = open('notes.v4', "w")

data = f.read().replace('ch', '')
d.write(data)
print(data)
f.close()
d.close()


# this part plays the "notes.v4"
play = open("notes.v4", "r")
read = play.read()
count = 0

while count <1000 :
    
    if read[count] == "c":
        print("c")
        winsound.Beep(261, 500)
    
    elif read[count] == "d":
        print("d")
        winsound.Beep(293, 500)

    elif read[count] == "e":
        print("e")
        winsound.Beep(330, 500)
    elif read[count] == "f":
        print("f")
        winsound.Beep(349, 500)

    elif read[count] == "g":
        print("g")
        winsound.Beep(392, 500)
        

    elif read[count] == "a":
        print("a")
        winsound.Beep(440, 500)
    else:
        print("h")
        winsound.Beep(494, 500)
    count = count + 1


