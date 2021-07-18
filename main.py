
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys
import numpy as np
import sounddevice
import time
import threading



def quit(self):
    sys.exit()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(103, 10, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.cycles = QtWidgets.QSpinBox(self.centralwidget)
        self.cycles.setGeometry(QtCore.QRect(300, 100, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.cycles.setFont(font)
        self.cycles.setMinimum(1)
        self.cycles.setProperty("value", 1)
        self.cycles.setObjectName("cycles")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")


        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(150, 230, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.generate.setFont(font)
        self.generate.setObjectName("generate")
        self.generate.clicked.connect(self.pushed)


        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(310, 230, 116, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.play.setFont(font)
        self.play.setObjectName("play")
        self.play.clicked.connect(self.player)


        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(14, 32, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.about.setFont(font)
        self.about.setObjectName("about")
        self.about.clicked.connect(self.Popup)


        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(14, 82, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.help.setFont(font)
        self.help.setObjectName("help")
        self.help.clicked.connect(self.Helpful)


        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(380, 340, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.quit.setFont(font)
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(quit)


        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(190, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(29)
        self.welcome.setFont(font)
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")


        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(140, 340, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.notworking)

        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(160, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.status.setFont(font)
        self.status.setObjectName("status")


        self.statusshow = QtWidgets.QLabel(self.centralwidget)
        self.statusshow.setGeometry(QtCore.QRect(230, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setItalic(True)
        self.statusshow.setFont(font)
        self.statusshow.setObjectName("statusshow")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def pushed(self):
        value = self.cycles.value()
        self.statusshow.setText("generuji")

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
        def two_one_down(a):
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

        how_many = int(value)
        qq = 0
        while qq < how_many:

            c = "p"
            d = "q"
            e = "r"
            f = "s"
            g = "t"
            a = "u"
            h = "v"

            l = random.randint(0, 6)
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

            qq = qq + 1

        o.close()

        self.statusshow.setText("hotovo")


    def player(self):
        x = threading.Thread(target=self.playerxy)
        x.daemon = True
        x.start()

    def playerxy(self):
        def func(frequency, duration):
            frequency = frequency
            fs = 48000  # Hz
            T = duration  # second, arbitrary length of tone

            # 1 kHz sine wave, 1 second long, sampled at 8 kHz
            t = np.arange(0, T, 1 / fs)

            # Generate a x Hz sine wave
            note = 0.8 * np.sin(1 * frequency * t * np.pi) * np.exp(-2 * t)
            note += 0.6 * np.sin(2 * frequency * t * np.pi) * np.exp(-2 * t)
            note += 0.4 * np.sin(3 * frequency * t * np.pi) * np.exp(-2 * t)
            note += 0.2 * np.sin(4 * frequency * t * np.pi) * np.exp(-2 * t)
            note = note * note * note

            x = (note * 4096).astype(np.int16)  # scale to int16 for sound card

            # note = np.sin(frequency * t * 2 * np.pi)

            sounddevice.play(x, fs)  # releases GIL
            time.sleep(T+0.1)

        def playit():
            play = open("notes.score", "r", encoding="utf8")
            read = play.read()
            count = 0
            a = 0.25
            b = 0.5
            c = 0.75
            d = 1
            number_of_chars_in_file = len(read)
            # reader not yet finished
            while count < number_of_chars_in_file:

                if read[count] == "p" and read[count + 1] == "0":
                    func(261.6, a)
                elif read[count] == "p" and read[count + 1] == "1":
                    func(261.6, b)
                elif read[count] == "p" and read[count + 1] == "2":
                    func(261.6, c)
                elif read[count] == "p" and read[count + 1] == "3":
                    func(261.6, d)



                elif read[count] == "q" and read[count + 1] == "0":
                    func(293.6, a)
                elif read[count] == "q" and read[count + 1] == "1":
                    func(293.6, b)
                elif read[count] == "q" and read[count + 1] == "2":
                    func(293.6, c)
                elif read[count] == "q" and read[count + 1] == "3":
                    func(293.6, d)



                elif read[count] == "r" and read[count + 1] == "0":
                    func(329.6, a)
                elif read[count] == "r" and read[count + 1] == "1":
                    func(329.6, b)
                elif read[count] == "r" and read[count + 1] == "2":
                    func(329.6, c)
                elif read[count] == "r" and read[count + 1] == "3":
                    func(329.6, d)


                elif read[count] == "s" and read[count + 1] == "0":
                    func(349.2, a)

                elif read[count] == "s" and read[count + 1] == "1":
                    func(349.2, b)

                elif read[count] == "s" and read[count + 1] == "2":
                    func(349.2, c)

                elif read[count] == "s" and read[count + 1] == "3":
                    func(349.2, d)


                elif read[count] == "t" and read[count + 1] == "0":
                    func(392, a)
                elif read[count] == "t" and read[count + 1] == "1":
                    func(392, b)
                elif read[count] == "t" and read[count + 1] == "2":
                    func(392, c)
                elif read[count] == "t" and read[count + 1] == "3":
                    func(392, d)


                elif read[count] == "u" and read[count + 1] == "0":
                    func(440, a)
                elif read[count] == "u" and read[count + 1] == "1":
                    func(440, b)
                elif read[count] == "u" and read[count + 1] == "2":
                    func(440, c)
                elif read[count] == "u" and read[count + 1] == "3":
                    func(440, d)


                elif read[count] == "v" and read[count + 1] == "0":
                    func(493.8, a)
                elif read[count] == "v" and read[count + 1] == "1":
                    func(493.8, b)
                elif read[count] == "v" and read[count + 1] == "2":
                    func(493.8, c)
                elif read[count] == "v" and read[count + 1] == "3":
                    func(493.8, d)

                count = count + 2
            play.close()

        playit()

    def Helpful(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Nápověda")
        msgbox.setText("Však ty to pochopíš, já ti věřím")
        msgbox.setStandardButtons(QMessageBox.Ok)
        font = QtGui.QFont()
        font.setFamily("Arial")
        x = msgbox.exec_()

    def Popup(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("O programu")
        msgbox.setText("Tento program jsem vytvořil já. " + "Nevydávejte ho prosím za svůj" + " Tvorba trvala kolem šesti měsíců.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        font = QtGui.QFont()
        font.setFamily("Arial")

        x = msgbox.exec_()

    def notworking(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Uložit")
        msgbox.setText("Zatím to nefachčí")
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setStandardButtons(QMessageBox.Ok)
        font = QtGui.QFont()
        font.setFamily("Arial")

        x = msgbox.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMSG - Automated Music Score Generator"))
        self.label.setText(_translate("MainWindow", "Počet cyklů:"))
        self.generate.setText(_translate("MainWindow", "Generovat"))
        self.play.setText(_translate("MainWindow", "Přehrát"))
        self.about.setText(_translate("MainWindow", "O programu"))
        self.help.setText(_translate("MainWindow", "Nápověda"))
        self.quit.setText(_translate("MainWindow", "Konec"))
        self.welcome.setText(_translate("MainWindow", "Vítej!"))
        self.save.setText(_translate("MainWindow", "Uložit"))
        self.status.setText(_translate("MainWindow", "Stav:"))
        self.statusshow.setText(_translate("MainWindow", "připraven"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
