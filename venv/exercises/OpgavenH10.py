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


print(opp_rechthoek(3, 4))
print(opp_4kant(7))
print(opp_driehoek(5,6))
print(opp_cirkel(4))

