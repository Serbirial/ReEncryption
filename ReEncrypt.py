def encrypt(sentence):
    encrypted = str("")
    letter = bool(False)
    for i in range(len(sentence)):
        count = 0
        currentChar = sentence[i]
        letter = True
        if currentChar == "A":
            count = int(1)
        elif currentChar == "B":
            count = int(2)
        elif currentChar == "C":
            count = int(3)
        elif currentChar == "D":
            count = int(4)
        elif currentChar == "E":
            count = int(5)
        elif currentChar == "F":
            count = int(6)
        elif currentChar == "G":
            count = int(7)
        elif currentChar == "H":
            count = int(8)
        elif currentChar == "I":
            count = int(9)
        elif currentChar == "J":
            count = int(10)
        elif currentChar == "K":
            count = int(11)
        elif currentChar == "L":
            count = int(12)
        elif currentChar == "M":
            count = int(13)
        elif currentChar == "N":
            count = int(14)
        elif currentChar == "O":
            count = int(15)
        elif currentChar == "P":
            count = int(16)
        elif currentChar == "Q":
            count = int(17)
        elif currentChar == "R":
            count = int(18)
        elif currentChar == "S":
            count = int(19)
        elif currentChar == "T":
            count = int(20)
        elif currentChar == "U":
            count = int(21)
        elif currentChar == "V":
            count = int(22)
        elif currentChar == "W":
            count = int(23)
        elif currentChar == "X":
            count = int(24)
        elif currentChar == "Y":
            count = int(25)
        elif currentChar == "Z":
            count = int(26)
        elif currentChar == "a":
            count = int(27)
        elif currentChar == "b":
            count = int(28)
        elif currentChar == "c":
            count = int(29)
        elif currentChar == "d":
            count = int(30)
        elif currentChar == "e":
            count = int(31)
        elif currentChar == "f":
            count = int(32)
        elif currentChar == "g":
            count = int(33)
        elif currentChar == "h":
            count = int(34)
        elif currentChar == "i":
            count = int(35)
        elif currentChar == "j":
            count = int(36)
        elif currentChar == "k":
            count = int(37)
        elif currentChar == "l":
            count = int(38)
        elif currentChar == "m":
            count = int(39)
        elif currentChar == "n":
            count = int(40)
        elif currentChar == "o":
            count = int(41)
        elif currentChar == "p":
            count = int(42)
        elif currentChar == "q":
            count = int(43)
        elif currentChar == "r":
            count = int(44)
        elif currentChar == "s":
            count = int(45)
        elif currentChar == "t":
            count = int(46)
        elif currentChar == "u":
            count = int(47)
        elif currentChar == "v":
            count = int(48)
        elif currentChar == "w":
            count = int(49)
        elif currentChar == "x":
            count = int(50)
        elif currentChar == "y":
            count = int(51)
        elif currentChar == "z":
            count = int(52)
        else:
            letter = False
        if count > 0 and letter == True:
            encrypted = encrypted + "r" + ("e"*count)
    return encrypted
def Decrypt(sentence):
    record = bool(False)
    count = int(0)
    recordedString = ""
    count = int(0)
    resetCount = bool(False)
    for i in range(len(sentence)):
        currentChar = sentence[i]
        if currentChar == "r" and record == bool(True):
            record = bool(False)
            if count == 1:
                recordedString = recordedString + "A"
            elif count == 2:
                recordedString = recordedString + "B"
            elif count == 3:
                recordedString = recordedString + "C"
            elif count == 4:
                recordedString = recordedString + "D"
            elif count == 5:
                recordedString = recordedString + "E"
            elif count == 6:
                recordedString = recordedString + "F"
            elif count == 7:
                recordedString = recordedString + "G"
            elif count == 8:
                recordedString = recordedString + "H"
            elif count == 9:
                recordedString = recordedString + "I"
            elif count == 10:
                recordedString = recordedString + "J"
            elif count == 11:
                recordedString = recordedString + "K"
            elif count == 12:
                recordedString = recordedString + "L"
            elif count == 13:
                recordedString = recordedString + "M"
            elif count == 14:
                recordedString = recordedString + "N"
            elif count == 15:
                recordedString = recordedString + "O"
            elif count == 16:
                recordedString = recordedString + "P"
            elif count == 17:
                recordedString = recordedString + "Q"
            elif count == 18:
                recordedString = recordedString + "R"
            elif count == 19:
                recordedString = recordedString + "S"
            elif count == 20:
                recordedString = recordedString + "T"
            elif count == 21:
                recordedString = recordedString + "U"
            elif count == 22:
                recordedString = recordedString + "V"
            elif count == 23:
                recordedString = recordedString + "W"
            elif count == 24:
                recordedString = recordedString + "X"
            elif count == 25:
                recordedString = recordedString + "Y"
            elif count == 26:
                recordedString = recordedString + "Z"
            elif count == 27:
                recordedString = recordedString + "a"
            elif count == 28:
                recordedString = recordedString + "b"
            elif count == 29:
                recordedString = recordedString + "c"
            elif count == 30:
                recordedString = recordedString + "d"
            elif count == 31:
                recordedString = recordedString + "e"
            elif count == 32:
                recordedString = recordedString + "f"
            elif count == 33:
                recordedString = recordedString + "g"
            elif count == 34:
                recordedString = recordedString + "h"
            elif count == 35:
                recordedString = recordedString + "i"
            elif count == 36:
                recordedString = recordedString + "j"
            elif count == 37:
                recordedString = recordedString + "k"
            elif count == 38:
                recordedString = recordedString + "l"
            elif count == 39:
                recordedString = recordedString + "m"
            elif count == 40:
                recordedString = recordedString + "n"
            elif count == 41:
                recordedString = recordedString + "o"
            elif count == 42:
                recordedString = recordedString + "p"
            elif count == 43:
                recordedString = recordedString + "q"
            elif count == 44:
                recordedString = recordedString + "r"
            elif count == 45:
                recordedString = recordedString + "s"
            elif count == 46:
                recordedString = recordedString + "t"
            elif count == 47:
                recordedString = recordedString + "u"
            elif count == 48:
                recordedString = recordedString + "v"
            elif count == 49:
                recordedString = recordedString + "w"
            elif count == 50:
                recordedString = recordedString + "x"
            elif count == 51:
                recordedString = recordedString + "y"
            elif count == 52:
                recordedString = recordedString + "z"
            resetCount = True
        elif currentChar == "e" and record == bool(False):
            count = count + 1
            record = bool(True)
            resetCount = False
        elif record == True:
            if currentChar.lower() == currentChar.upper():
                #recordedString = recordedString + currentChar
                #print("recorded unencrypted data")
                gay = 0
            else:
                count = count + 1
        if i == len(sentence) -1:
            if count == 1:
                recordedString = recordedString + "A"
            elif count == 2:
                recordedString = recordedString + "B"
            elif count == 3:
                recordedString = recordedString + "C"
            elif count == 4:
                recordedString = recordedString + "D"
            elif count == 5:
                recordedString = recordedString + "E"
            elif count == 6:
                recordedString = recordedString + "F"
            elif count == 7:
                recordedString = recordedString + "G"
            elif count == 8:
                recordedString = recordedString + "H"
            elif count == 9:
                recordedString = recordedString + "I"
            elif count == 10:
                recordedString = recordedString + "J"
            elif count == 11:
                recordedString = recordedString + "K"
            elif count == 12:
                recordedString = recordedString + "L"
            elif count == 13:
                recordedString = recordedString + "M"
            elif count == 14:
                recordedString = recordedString + "N"
            elif count == 15:
                recordedString = recordedString + "O"
            elif count == 16:
                recordedString = recordedString + "P"
            elif count == 17:
                recordedString = recordedString + "Q"
            elif count == 18:
                recordedString = recordedString + "R"
            elif count == 19:
                recordedString = recordedString + "S"
            elif count == 20:
                recordedString = recordedString + "T"
            elif count == 21:
                recordedString = recordedString + "U"
            elif count == 22:
                recordedString = recordedString + "V"
            elif count == 23:
                recordedString = recordedString + "W"
            elif count == 24:
                recordedString = recordedString + "X"
            elif count == 25:
                recordedString = recordedString + "Y"
            elif count == 26:
                recordedString = recordedString + "Z"
            elif count == 27:
                recordedString = recordedString + "a"
            elif count == 28:
                recordedString = recordedString + "b"
            elif count == 29:
                recordedString = recordedString + "c"
            elif count == 30:
                recordedString = recordedString + "d"
            elif count == 31:
                recordedString = recordedString + "e"
            elif count == 32:
                recordedString = recordedString + "f"
            elif count == 33:
                recordedString = recordedString + "g"
            elif count == 34:
                recordedString = recordedString + "h"
            elif count == 35:
                recordedString = recordedString + "i"
            elif count == 36:
                recordedString = recordedString + "j"
            elif count == 37:
                recordedString = recordedString + "k"
            elif count == 38:
                recordedString = recordedString + "l"
            elif count == 39:
                recordedString = recordedString + "m"
            elif count == 40:
                recordedString = recordedString + "n"
            elif count == 41:
                recordedString = recordedString + "o"
            elif count == 42:
                recordedString = recordedString + "p"
            elif count == 43:
                recordedString = recordedString + "q"
            elif count == 44:
                recordedString = recordedString + "r"
            elif count == 45:
                recordedString = recordedString + "s"
            elif count == 46:
                recordedString = recordedString + "t"
            elif count == 47:
                recordedString = recordedString + "u"
            elif count == 48:
                recordedString = recordedString + "v"
            elif count == 49:
                recordedString = recordedString + "w"
            elif count == 50:
                recordedString = recordedString + "x"
            elif count == 51:
                recordedString = recordedString + "y"
            elif count == 52:
                recordedString = recordedString + "z"
        if resetCount == True:
            count = 0
            if currentChar == " ":
                recordedString += " "
    return recordedString
