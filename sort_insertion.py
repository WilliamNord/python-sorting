import random
antall = int(input("Hvor mange tall vil du sortere? "))

liste = list(range(1, antall+1))
random.shuffle(liste)

antall_operasjoner = 0

# Insertion Sort
for i in range(1, len(liste)):
    nokkel = liste[i]
    j = i - 1

    # Flytt elementer som er større enn nøkkelen én plass til høyre
    while j >= 0 and liste[j] > nokkel:
        liste[j + 1] = liste[j]
        j -= 1
        antall_operasjoner += 1
    
    # Sett inn nøkkelen på riktig plass
    liste[j + 1] = nokkel

print(f"liste etter: \n {liste}, dette tok {antall_operasjoner} operasjoner")