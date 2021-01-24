import random

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

#this part writes 20 notes to the file notes.txt
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
