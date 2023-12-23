
def zpracuj_prihlasku(jmeno, gender=""):
    return f"{jmeno}, {gender}"


jmeno = input("Zadej jmeno: ")
gender = input("Zadej gender: ")

if gender == "":
    print(zpracuj_prihlasku(jmeno))
else:
    print(zpracuj_prihlasku(jmeno, gender))