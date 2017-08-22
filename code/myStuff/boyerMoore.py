def main():
    txt = "rabracadrabra"
    pat = "rabra"
    alphabet = [chr(i) for i in range(256)]
    occ = bM(txt,pat,alphabet)
    print (occ)

def badCharList(alphabet,pat): #calcula o ultimo indice em pat de cada char do alfabeto
    lenAlphabet = len(alphabet)
    result = lenAlphabet * [-1]
    index = 0
    while index < len(pat): #percorre o pat atualizando a lista result
        indexOfCharInResultList = alphabet.index(pat[index])
        result[indexOfCharInResultList] = index
        index += 1
    return result

def bM(txt,pat, alphabet):
    n = len(txt) #n = size of txt
    m = len(pat) #m = size of pat
    i = 0 #i = index of txt
    j = 0 #j = index of pat
    badChrList = badCharList(alphabet,pat)
    myList = []
    while (i <= n-m) : #percorrendo txt
        j = m - 1
        while (j > 0): #percorrendo pat
            if (pat[j] == txt[i+j]):
                j -= 1 #se der match, anda no index do padrão
            else:#Sad Path
                badCharPos = badChrList[alphabet.index(txt[j+i])]
                if badCharPos < j: #evita pulo para trás
                    i = (i+j) - badCharPos
                else:
                    i+=1
                break
            #print (txt)
            #print ("%s%s%s"%((i+j)*" " if j>=0 else i*" " , "!" if j>=0 else "",(m-j-1)*"="))
            #print ("%s%s"%(i*" ",pat))
            #print()
        if (j == 0): #Happy Path
            myList.append(i); #se o indice do padrão andou a string inteira sem mismatches, adiciona na lista de ocorrências
            i+=1
        print("Iterating")
    return myList
        
if __name__ == "__main__":
    main()
