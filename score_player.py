import winsound
f = open("notes.score", "r")

read = f.read()

if read[3] == 'e':
    print('c')
else:
    print('nic')

count = 0

while count <30 :
    
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
