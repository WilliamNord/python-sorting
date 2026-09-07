import random
antall = int(input("Hvor mange tall vil du sortere? "))

liste = list(range(1, antall+1))  # Lager en liste med tall fra 1 til antall valgt
random.shuffle(liste)  # tilfeldig rekkefølge

antall_operasjoner = 0


def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    
    pivot = liste[-1]
    venstre = []
    høyre = []

    for i in range(len(liste)-1):
        if liste[i] < pivot:
            venstre.append(liste[i])
        else:
            høyre.append(liste[i])

    print(f"liste under sortering: \n {liste}")
    global antall_operasjoner
    antall_operasjoner += 1
    
    return quick_sort(venstre) + [pivot] + quick_sort(høyre)

print(f"liste før: \n {liste}")
sortert = quick_sort(liste)
print(f"liste etter: \n {sortert}")
print(f"dette tok {antall_operasjoner} ganger")