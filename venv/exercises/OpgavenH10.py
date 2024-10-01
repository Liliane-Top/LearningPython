import math


def opp_rechthoek(m, n):
    return m * n


# bereken de oppervlakte van een veirkant met de zijden van lengte n
def opp_4kant(n):
    return opp_rechthoek(n, n)


# maak een subroutine om de oppervlakte te berekenen van een driehoek
def opp_driehoek(basis, hoogte):
    return basis * (.5 * hoogte)


# maar een subroutine om de oppervlakte van een circel te berekenen
def opp_cirkel(r):
    return 3.14159265358979 * r * r


# bereken inhoud van een bol
def inhoud_bol(r):
    print(math.pow(2, 3))
    return 4 / 3 * math.pi * math.pow(r, 3)


def opp_bol(r):
    return str(4 * r ** 2) + " pi"


def print_tafel(n):
    for x in range(1, 11):
        print(str(x) + " keer " + str(n) + " is " + str(x * n))


def print_tafel2(n):
    for x in range(1, 21):
        print(str(x) + " keer " + str(n) + " is " + str(x * n))


def oneven_getallen_tot(n):
    print("oneven getallen tot " + str(n))
    for i in range(1, n + 1, 2):
        print(i)


def print_letter4letter(string):
    print("elke letter")
    for i in range(len(string)):
        print(string[i])


cijfers = "1234567890"
i = 3
print(cijfers[i - 1:i + 1])  # 34
print(cijfers[i - 1:i + 2])  # 345


def print_per3(string):
    for i in range(0, len(string), 3):
        print(string[i:i + 3])


print_per3("nou ben ik reuze benieuws hoe dit nou werkt")
print("Probeer dit in de interactive mode!".index("P"))  # 0 index
print("Probeer dit in de interactive mode!".index("int"))  # 18
# print("Probeer dit in de interactive mode!".index("Helaas"))  # geeft foutmelding


alfabet = "abcdefghijklmnopqrstuvwxyz"


def rot13(text):
    retstring = ""
    for letter in text:
        index = alfabet.index(letter)
        retstring += alfabet[(index + 13) % 26]
    print("ik print hier i: " + letter)
    return retstring


# result = rot13("kwaliteitseisen")  # xjnyvgrvgfrvfra
# result = rot13("presidentskandidaat")   # cerfvqragfxnaqvqnng
result = rot13("viaduct")   # IVNQHPG
print(result.upper())
result = rot13(result)
print(result)


def rot5(text):
    retstring = ""
    for i in text:
        index = alfabet.index(i)
        retstring += alfabet[(index + 5) % 26]
    return retstring


def rot5_inverse(text):
    retstring = ""
    for i in text:
        index = alfabet.index(i)
        retstring += alfabet[(index - 5) % 26]
    #     in boek staat retstring += alfabet[(index + 21) % 26]
    return retstring


print(rot5("liliane"))
print(rot5_inverse("liliane"))
print(rot5_inverse(rot5("abcdefghijklmnopqrstuvwxyz")))
print(rot5(rot5_inverse("liliane")))


def caesar(n, text):
    resultText = ""
    for symbol in text:
        if symbol in alfabet:
            index = alfabet.index(symbol)
            resultText += alfabet[(index + n) % 26]
        else:
            resultText += symbol
    return resultText


print(caesar(13, alfabet))
print(caesar(3, "alle 3 zijn er bij @feest"))


# rot13() met leestekens
def rot13_met_leestekens(text):
    result = ""
    for symbol in text:
        if symbol in alfabet:
            index = alfabet.index(symbol)
            result += alfabet[(index + 13) % 26]
        else:
            result += symbol
    return result


print(rot13_met_leestekens("liliane gaat lekker!"))


# print(opp_rechthoek(3, 4))
# print(opp_4kant(7))
# print(opp_driehoek(5,6))
# print(opp_cirkel(4))
# print(inhoud_bol(5))
# print(opp_bol(3))
# print_tafel(13)
# oneven_getallen_tot(15)
# print_letter4letter("liliane")
