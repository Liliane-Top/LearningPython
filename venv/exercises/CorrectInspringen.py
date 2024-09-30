# dit is 1e blok van programma code
def sum(x, y):
    # een nieuw blok op niveau 2 indent verwacht
    def doit():
        # een nieuw blok op niveau 3
        return x + y

    # weer terug in blok 2
    somedata = doit()

    # nog steeds in blok 2
    return somedata


# blok 1
def minus(x, y):
    # blok 2
    antwoord = x - y

    # nog steeds in blok 2
    return antwoord


print(sum(4, 16))
print(minus(3, 6))
