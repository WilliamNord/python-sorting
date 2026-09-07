random_list = [1, 2, 3, 4, 5, 60, 14, 5, 6, 2, 8, 2, 1, 5, 6, 8, 9, 98, 76, 543]


def merge_sort(liste):

    midten = len(liste) // 2
    #jeg har funnet ut at :midten går fra "ingenting før midten" til "har nådd midten"
    venstre = liste[:midten]
    hoyre = liste[midten:]