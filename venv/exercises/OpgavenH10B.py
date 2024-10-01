def div3(n):
    if n % 3 == 0:
        # True is type boolean "True" is type string
        return True
    else:
        return False


print(div3(9))
print(div3(10))

alfabet = "abcdefghijklmnopqrstuvwxyz"


def ceasar(n, text):
    result = ""
    for symbol in text:
        index = text.index(symbol)
        if symbol in alfabet:
            result += alfabet[(index + n) % 26]
        elif symbol.lower() in alfabet:
            result += alfabet[(index + n) % 26].upper()
        else:
            result += symbol
    return result


print(ceasar(2, "Liliane Top is 58 jaar oud"))


def numstars(text):
    count = 0
    for symbol in text:
        if symbol == "*":
            count += 1
    return count


def nextstring(text):
    result_text = ""
    add_stars = numstars(text) + 1
    for symbol in text:
        if symbol == "*":
            result_text += "*" * add_stars
        else:
            result_text += symbol
    return result_text


print(nextstring("a*bc**efg"))  # a****bc********efg
print(nextstring("*a*bc**efg"))


def next_string(text):
    # voeg spatie toe aan begin en einde zodat deze ook een buur hebben
    widestr = " " + text + " "
    retstr = ""
    # loop over de text met toegevoegde spaties maar start op 2 plek en eindig voorlaatste
    # want dat is een spatie die niet aan beide zijde een buur heeft
    for i in range(1, len(widestr) - 1):
        # voeg het symbool toe aan het resultaat
        retstr += widestr[i]
        # als het symbool een *
        if widestr[i] == "*":
            # vind de buren van dit symbool
            i_en_buren = widestr[i - 1: i + 2]
            # check of buren ook * zijn en tel deze op
            add_stars = numstars(i_en_buren)
            # voeg het aantal extra sterren toe aan het resultaat
            retstr += widestr[i] * add_stars + " "
    # geeft het resultaat terug
    return retstr


print(next_string("*"))
print(next_string("a*bc*efg"))
print(next_string("a*bc**efg"))
print(next_string("*a*bc**"))
print(next_string("***b*c**"))


def next_string_2(text):
    wide_string = " " + text + " "
    resultaat = ""
    for i in range(1, len(wide_string) - 1):
        i_en_buren = wide_string[i - 1:i + 2]
        num_stars = numstars(i_en_buren)
        if num_stars == 1:
            resultaat += "*"
        else:
            resultaat += "1"
    return resultaat


print(next_string_2(" * "))  # ***
print(next_string_2("* *"))  # * *
print(next_string_2(" ** * **"))  # '*   *  '
