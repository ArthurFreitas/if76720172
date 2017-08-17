
def badchar(pat, ab):
    l = len(ab)
    m = len(pat)
    bc = l*[-1]
    for i in range(m):
        bc[ab.index(pat[i])] = i 
    return bc


def boyermoore(txt, pat, ab):
    m, n, l = len(pat), len(txt), len(ab)
    occ = []
    bc = badchar(pat,ab)
    i = 0
    while i+m <= n:
        j = m-1
        while j>=0 and txt[i+j] == pat[j]:
            j -= 1
        print txt
        print "%s%s%s"%((i+j)*" " if j>=0 else i*" " , "!" if j>=0 else "",(m-j-1)*"=")
        print "%s%s"%(i*" ",pat)
        print
        if j<0:
            occ.append(i)
            i += 1
        else:
            i += max(1, j-bc[ab.index(txt[i+j])]) 
    return occ

def main():
    ab = [chr(i) for i in range(256)]
    pat = "rabra"
    txt = "rabracadrabra"
    occ = boyermoore(txt, pat, ab)
    print occ

    

if __name__ == "__main__":
    main()
