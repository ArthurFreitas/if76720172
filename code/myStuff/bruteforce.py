def main():
    txt = "rabracadrabra"
    pat = "rabra"
    occ = bruteforce(txt, pat)
    print (occ)

def bruteforce(txt,pat):
    n = len(txt) #n = size of txt
    m = len(pat) #m = size of pat
    i = 0 #i = index of txt
    j = 0 #j = index of pat
    myList = []
    while (i <= n-m) :
        while (j < m):
            if (pat[j] == txt[i+j]):
                j += 1 #se der match, anda no index do padrão
            else:
                break #se der mismatch quebra e testa a prox pos
        if (j == m):
            myList.append(i); #se o indice do padrão andou a string inteira sem mismatches, adiciona na lista de ocorrências
        j = 0   #reseta o indice do padrão
        i += 1  #incrementa o indice do texto
    return myList
        
if __name__ == "__main__":
    main()
