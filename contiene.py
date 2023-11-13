#! /usr/bin/python3
# contiene.py

def contiene(S, s):
    """_summary_

    Args:
        S (str): container
        s (str): contained

    Returns:
        bool: 
    """

    return s in S  # eso es todo.

    # un continente vacio -len 0- no puede contener nada,,
    if 0 == len(S):  # not S
        return False

    # un contenido vacio no puede aparecer en ningun continente,,
    if 0 == len(s): # not s
        return False

    # un contenido no puede ser mayor que su continente
    if len(S) < len(s):
        return False

    # hay continente y contenido adecuados -en tam.-
    
    # 1: avanzar en S hasta encontrar -o no- la 1ª letra de s (s[0])
    i = 0
    while ((i < len(S)) and (S[i] != s[0])):
        i += 1

    # S agotada?
    if i == len(S):
        return False

    j = 0
    while ((j < len(s)) and (S[i] == s[j])):
        i += 1
        j += 1        

    if j == len(s):
        return True
    else:
        return False

if __name__ == "__main__":

    print(contiene("", "algo"))       # no container: False
    print(contiene("algunsitio", "")) # no content: False
    print(contiene("bc", "abcd")) # container first! ,, False
    print(contiene("abcd", "cd"))   # contained:True
    print(contiene("abcd", "ab"))   # contained:True
    print(contiene("rwx", "r"))     # contained:True
    print(contiene("rwx", "w"))     # contained:True
    print(contiene("rwx", "x"))     # contained:True
    print(contiene("rw", "x"))      # contained:False
