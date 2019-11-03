num = int(input())

numpad = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9"
}

for i in range(num):
    phonenumber = input()
    newphonenumber = ""
    for char in phonenumber:
        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0":
            newphonenumber = newphonenumber + char
        elif char == "-":
            pass
        else:
            newphonenumber = newphonenumber + numpad[char]
    print(str(newphonenumber[0:3]) + "-" + str(newphonenumber[3:6]) + "-" + str(newphonenumber[6:10]))