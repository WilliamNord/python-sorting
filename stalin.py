# Stalin sort algorytme O(n)
# hvis tallet ikke er i riktig rekkefølge, så blir det sendt til gulag

import random
antall = int(input("Hvor mange tall vil du sortere? "))

liste = list(range(1, antall+1))
random.shuffle(liste)

print(liste)

i = 0
while i < len(liste) - 1:
    if (liste[i] > liste[i+1]):
        print("to the gulag")
        liste.pop(i+1)
    else:
        i += 1

print(liste)