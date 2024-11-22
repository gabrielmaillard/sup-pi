## Exercice 3 Fin de Chapitre

def increment(d):
    """increment(d: list[int]) -> NoneType"""
    i = 0
    while i < len(d) and d[i] == 1:
        d[i] = 0
        i += 1
    if i >= len(d):
        d.append(1)
    else:
        d[i] = 1

## Exercice 4 Fin de Chapitre

def espace_binaire(n: int) -> int:
    """espace_binaire(n: int) -> int"""
    max_espace = compteur = 0
    a_trouve_un = False

    while n > 0:
        bit = n % 2
        n //= 2
        if bit == 1:
            if a_trouve_un:
                max_espace = max(max_espace, compteur)
            compteur = 0
            a_trouve_un = True
        elif a_trouve_un:
            compteur += 1

    return max_espace

## Exercice 6 Fin de Chapitre

def decomposition(d, n):
    """binaire(d: int, n: int) -> list[bool]"""
    reste = n
    decomposition_ = []
    for i in range(n):
        if (2**(n-1-i)) <= reste:
            decomposition_.append(True)
            reste -= 2**(n-1-i)
        else:
            decomposition_.append(False)
    return decomposition_

def prix_decoupe(d, p):
    """prix_decoupe(d: list[bool], p: list[int]) -> int"""
    prix_total = 0
    deb_barre = 0
    for i in range(len(d)):
        if d[i]:
            prix_total += p[i+1-deb_barre]
            deb_barre = i
    prix_total += p[i+2-len(d)]
    return prix_total


def meilleur_prix(p):
    """meilleur_prix(p: list[int]) -> tuple[list[bool], int]"""
    n = len(p) - 1
    meilleur_prix = prix_decoupe([False]*n, p)
    meilleure_decomposition = [False]*n
    for i in range(1 << n):
        d = decomposition(i, n)
        prix = prix_decoupe(d, p)

        if prix > meilleur_prix:
            meilleur_prix = prix
            meilleure_decomposition = d

    return meilleure_decomposition, meilleur_prix


print(meilleur_prix(
    [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
))