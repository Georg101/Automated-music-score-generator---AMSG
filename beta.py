import random
import winsound

generate_notes = int(input("Generate notes? "))
if generate_notes == 1:

    # 1 1
    def two_one(a):
        x = a + "1" + a + "1"
        return x

    # 0 0 0 0
    def four_zero(a):
        x = a + "0" + a + "0" + a + "0" + a + "0"
        return x

    # 3
    def one_whole(a):
        x = a
        return x + "3"

    # a0 b0 c0 d0
    def four_zero_up(a):
        q = str(ord(a) - 86)
        if q == "26":
            u = "p"
            v = "q"
            w = "r"
            x = "s"
        elif q == "27":
            u = "q"
            v = "r"
            w = "s"
            x = "t"
        elif q == "28":
            u = "r"
            v = "s"
            w = "t"
            x = "u"
        elif q == "29":
            u = "s"
            v = "t"
            w = "u"
            x = "v"
        elif q == "30":
            u = "t"
            v = "u"
            w = "v"
            x = "v"
        elif q == "31":
            u = "u"
            v = "v"
            w = "v"
            x = "v"
        else:
            u = "v"
            v = "v"
            w = "v"
            x = "v"

        return u + "0" + v + "0" + w + "0" + x + "0"

    # d0 c0 b0 a0
    def four_zero_down(a):
        q = str(ord(a) - 86)
        if q == "26":
            u = "p"
            v = "p"
            w = "p"
            x = "p"
        elif q == "27":
            u = "q"
            v = "p"
            w = "p"
            x = "p"
        elif q == "28":
            u = "r"
            v = "q"
            w = "p"
            x = "p"
        elif q == "29":
            u = "s"
            v = "r"
            w = "q"
            x = "p"
        elif q == "30":
            u = "t"
            v = "s"
            w = "r"
            x = "q"
        elif q == "31":
            u = "u"
            v = "t"
            w = "s"
            x = "r"
        else:
            u = "v"
            v = "u"
            w = "t"
            x = "s"

        return u + "0" + v + "0" + w + "0" + x + "0"

    # b1 a1
    def two_one_down(a) :
        q = str(ord(a) - 86)
        if q == "26":
            u = "p"
            v = "p"
        elif q == "27":
            u = "q"
            v = "p"
        elif q == "28":
            u = "r"
            v = "q"
        elif q == "29":
            u = "s"
            v = "r"
        elif q == "30":
            u = "t"
            v = "s"
        elif q == "31":
            u = "u"
            v = "t"
        else:
            u = "v"
            v = "u"

        x = u + "1" + v + "1"
        return x

    # a1 b1
    def two_one_up(a):
        q = str(ord(a) - 86)
        if q == "26":
            u = "p"
            v = "q"
        elif q == "27":
            u = "q"
            v = "r"
        elif q == "28":
            u = "r"
            v = "s"
        elif q == "29":
            u = "s"
            v = "t"
        elif q == "30":
            u = "t"
            v = "u"
        elif q == "31":
            u = "u"
            v = "v"
        else:
            u = "v"
            v = "v"

        x = u + "1" + v + "1"
        return x

    # a0 a0 a1
    def two_zero_one_one(a):
        x = a + "0" + a + "0" + a + "1"
        return x

    # a1 a0 a0
    def one_one_two_zero(a):
        x = a + "1" + a + "0" + a + "0"
        return x

    # a0 a1 a0
    def one_zero_one_one_one_zero(a):
        x = a + "0" + a + "1" + a + "0"
        return x



    o = open("notes.score", "w")


    how_many = int(input("Enter num of repeating: "))
    qq = 0
    while qq < how_many:

        c = "p"
        d = "q"
        e = "r"
        f = "s"
        g = "t"
        a = "u"
        h = "v"

        l = random.randint(0,6)
        if l == 0:
            x = c
        elif l == 1:
            x = d
        elif l == 2:
            x = e
        elif l == 3:
            x = f
        elif l == 4:
            x = g
        elif l == 5:
            x = a
        else:
            x = h

        dq = two_one(x)
        dw = four_zero(x)
        de = one_whole(x)
        dr = four_zero_up(x)
        dt = four_zero_down(x)
        dz = two_one_down(x)
        du = two_one_up(x)
        di = two_zero_one_one(x)
        do = one_one_two_zero(x)
        dp = one_zero_one_one_one_zero(x)
        da = four_zero_up(x)
        ds = four_zero_down(x)

        qw = random.randint(0, 11)
        if qw == 0:
            print(dq)
            o.write(dq)
        elif qw == 1:
            print(dw)
            o.write(dw)
        elif qw == 2:
            print(de)
            o.write(de)
        elif qw == 3:
            print(dr)
            o.write(dr)
        elif qw == 4:
            print(dt)
            o.write(dt)
        elif qw == 5:
            print(dz)
            o.write(dz)
        elif qw == 6:
            print(du)
            o.write(du)
        elif qw == 7:
            print(di)
            o.write(di)
        elif qw == 8:
            print(do)
            o.write(do)
        elif qw == 9:
            print(dp)
            o.write(dp)
        elif qw == 10:
            print(da)
            o.write(da)
        else:
            print(ds)
            o.write(ds)


        qq =qq + 1

    o.close()

else:
    pass


play_yes = int(input("Play? "))

if play_yes == 1:
    play = open("notes.score", "r", encoding="utf8")
    read = play.read()
    count = 0
    a = 250
    b = 500
    c = 750
    d = 1000
    number_of_chars_in_file = len(read)
    # reader not yet finished
    while count < number_of_chars_in_file:

        if read[count] == "p" and read[count + 1] == "0":
            winsound.Beep(262, a)
        elif read[count] == "p" and read[count + 1] == "1":
            winsound.Beep(262, b)
        elif read[count] == "p" and read[count + 1] == "2":
            winsound.Beep(262, c)
        elif read[count] == "p" and read[count + 1] == "3":
            winsound.Beep(262, d)


        elif read[count] == "q" and read[count + 1] == "0":
            winsound.Beep(294, a)
        elif read[count] == "q" and read[count + 1] == "1":
            winsound.Beep(294, b)
        elif read[count] == "q" and read[count + 1] == "2":
            winsound.Beep(294, c)
        elif read[count] == "q" and read[count + 1] == "3":
            winsound.Beep(294, d)


        elif read[count] == "r" and read[count + 1] == "0":
            winsound.Beep(330, a)
        elif read[count] == "r" and read[count + 1] == "1":
            winsound.Beep(330, b)
        elif read[count] == "r" and read[count + 1] == "2":
            winsound.Beep(330, c)
        elif read[count] == "r" and read[count + 1] == "3":
            winsound.Beep(330, d)

        elif read[count] == "s" and read[count + 1] == "0":
            winsound.Beep(349, a)
        elif read[count] == "s" and read[count + 1] == "1":
            winsound.Beep(349, b)
        elif read[count] == "s" and read[count + 1] == "2":
            winsound.Beep(349, c)
        elif read[count] == "s" and read[count + 1] == "3":
            winsound.Beep(349, d)

        elif read[count] == "t" and read[count + 1] == "0":
            winsound.Beep(392, a)
        elif read[count] == "t" and read[count + 1] == "1":
            winsound.Beep(392, b)
        elif read[count] == "t" and read[count + 1] == "2":
            winsound.Beep(392, c)
        elif read[count] == "t" and read[count + 1] == "3":
            winsound.Beep(392, d)


        elif read[count] == "u" and read[count + 1] == "0":
            winsound.Beep(440, a)
        elif read[count] == "u" and read[count + 1] == "1":
            winsound.Beep(440, b)
        elif read[count] == "u" and read[count + 1] == "2":
            winsound.Beep(440, c)
        elif read[count] == "u" and read[count + 1] == "3":
            winsound.Beep(440, d)


        elif read[count] == "v" and read[count + 1] == "0":
            winsound.Beep(494, a)
        elif read[count] == "v" and read[count + 1] == "1":
            winsound.Beep(494, b)
        elif read[count] == "v" and read[count + 1] == "2":
            winsound.Beep(494, c)
        elif read[count] == "v" and read[count + 1] == "3":
            winsound.Beep(494, d)

        count = count + 2
    play.close()

else:
    pass

print("Thank you for using my program")
print("the Author")
print(":-)")


