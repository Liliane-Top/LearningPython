# famous first line
print("Hello world.")
# berekeningen = expressies
print(12345 + 678)  # 13023
print(987 + 654 - 123)  # 1518
print("Hello" + " " + "world. (again)")
print("hello" * 5)  # hellohellohellohellohello

# using variables
naam = "Liliane Top"
print("Goedemorgen " + naam)

# gebruik van verschillende type variabele
naam = 42
print(naam)
naam = 13 / 37
print(naam)

# TypeError: can only concatenate str (not "int") to str
naam = 45
naam = '45'  # it works with string concatenation
print("Goedemorgen " + naam)

# int omzetten naar string str()
naam = 145
print("Goedemorgen " + str(naam))


# bereken oppervlakte van vierkant met zijde n => def subroutine() :
def opp_vierkant(n):
    return n * n


# aanroepen subroutine = functie = methode
print("de oppervlakte van een vierkant met zijde van 5 = " + str(opp_vierkant(5)))
print("de oppervlakte van een vierkant met zijde van 2.0 = " + str(opp_vierkant(2.0)))

# geeft een foutmelding met het volgende
print(opp_vierkant("de jong")) # TypeError: can't multiply sequence by non-int of type 'str'
# print(opp_vierkant(2.0))) # SyntaxError: invalid syntax en nu breekt het programma af
# print(opp_vierkant(3.0) # SyntaxError: invalid syntax

