def main():
    txt = "rabracadrabra"
    pat = "rabra"
    #alphabet = [chr(i) for i in range(256)]
    #occ = bM(txt,pat,alphabet)
    print (goodSuffix(txt))

def badCharList(alphabet,pat): #calcula o ultimo indice em pat de cada char do alfabeto
    lenAlphabet = len(alphabet)
    result = lenAlphabet * [-1]
    index = 0
    while index < len(pat): #percorre o pat atualizando a lista result
        indexOfCharInResultList = alphabet.index(pat[index])
        result[indexOfCharInResultList] = index
        index += 1
    return result
	
def brd(pat):
    m = len(pat)
    nxt = (m+1)*[0] 
    i = 1
    j = 0
    while i+j < m:
        while i+j<m and pat[i+j]==pat[j]:
            j += 1
            nxt[i+j] = j
        i += max(1, (j-nxt[j])) 
        j = nxt[j]
    return nxt

def goodSuffix(p): #salto do bom sufixo
	#entrada: P = p0 ... pm-1
	#saida: S = (s-1,...,sm-1)
	m = len(p) # tamanho pattern
	B = brd(p) #calcular todas as bordas de p
	R = brd(p[::-1])#calcular borda dos reversos
	bm = B[m-1] #borda da bagaça toda
	S = (m + 1) * [m-bm] #returns
	l = 1 #aux
	while l <= m:
		j = m-1-R[l]
		if (l - R[l]) < S[j]:
			S[j] = l - R[l]
		l+=1
	return S
	
def bM(txt,pat, alphabet):
    n = len(txt) #n = size of txt
    m = len(pat) #m = size of pat
    i = 0 #i = index of txt
    j = 0 #j = index of pat
    badChrList = badCharList(alphabet,pat)
    myList = []
    while (i <= n-m) : #percorrendo txt
        j = m - 1
        while (j > 0): #percorrendo patpitoca
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
