## Exercice 2 Fin de Chapitre

# Question 1

def delta(t, k):
    """delta(t: list[int], k: int) -> int"""
    delta_k = 0
    for i in range(k):
        delta_k += t[i]
    for i in range(k, n):
        delta_k -= t[i]
    return delta_k

def equilibre(t):
    """equilibre(t: list[int]) -> int"""
    n = len(t)
    delta_eq = delta(t, 0)
    for k in range(1, n+1):
        delta_k = delta(t, k)
        if delta_k < delta_eq:
            delta_eq = delta_k
    return delta_eq

# La complexité de cette fonction equilibre est GrandTeta(n^2) où n est la longueur de la liste t

# Question 2

def somme_liste(t):
    """somme_liste(t: list[int]) -> int"""
    somme = 0
    for i in range(len(t)):
        somme += t[i]
    return somme

def equilibre_lineaire(t):
    """equilibre_lineaire(t: list[int]) -> int"""
    partie_g = 0
    partie_d = somme_liste(t)
    delta_eq = -partie_d
    for i in range(len(t)):
        partie_g += t[i]
        partie_droite -= t[i]
        delta_k = partie_gauche - partie_droite
        if delta_k < delta_eq:
            delta_eq = delta_k
    return delta_eq

# Cet algorithme a bien une complexité en GrandTeta(n). La complexité est linéaire par rapport à la taille de la liste t.

## Exercice 4 Fin de Chapitre

# Question 1

def cherche_somme(t, s):
    """cherche_somme(t: list[int], s: int) -> tuple[int, int]"""
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] + t[j] == s:
                return (i, j)
    return None

# La complexité de cet algorithme est GrandTeta(n^2) où n est la taille de la liste t.

# Question 2

def cherche_somme_croissant(t, s):
    """cherche_somme_croissant(t: list[int], s: int) -> tuple[int, int]"""
    i = 0
    j = len(t) - 1
    while i < j:
        somme = t[i] + t[j]
        if somme == s:
            return (i, j)
        elif somme < s:
            i += 1
        elif somme > s:
            j -= 1
    return None

# Question 3

# Idée : trier la liste puis appliquer l'algorithme de la question 2

def fusion(t1, t2):
    """fusion(t1: list[int], t2: list[int]) -> list[int]"""
    t = []
    i1 = 0
    i2 = 0
    while i1 < len(t1) and i2 < len(t2):
        if t1[i1] <= t2[i2]:
            t.append(t1[i1])
            i1 += 1
        else:
            t.append(t2[i2])
            i2 += 1
    t.extend(t1[i1:])
    t.extend(t2[i2:])
    return t

def tri_fusion(t):
    """tri_fusion(t: list[int]) -> list[int]"""
    n = len(t)
    if n <= 1:
        return t[:]
    n1 = n // 2
    t1 = tri_fusion(t[0:n1])
    t2 = tri_fusion(t[n1:n])
    t = fusion(t1, t2)
    return t

def cherche_somme_opti(t):
    t = tri_fusion(t)
    return cherche_somme_croissant(t)

# La complexité l'algorithme du tri fusion vaut nlog(n) et celle de cherche_somme_croissant vaut n. La complexite de cherche_somme_opti vaut donc log(n)(n+1), c'est-à-dire GrandTeta(nlog(n))