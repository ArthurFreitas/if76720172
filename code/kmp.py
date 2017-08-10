def str_brd(X):
    n = len(X)
    mk = 0
    for k in range(1,n-1):
        if X[:k]==X[n-k:]:
            mk = k
    return mk
        
def brd_bf(pat):
    m = len(pat)
    brd = (m+1)*[0]
    for j in range(2,m+1):
        brd[j] = str_brd(pat[:j])
    return brd

def bruteforce(txt, pat):
    n = len(txt)
    m = len(pat)
    occ = []
    i = 0
    while i <= n-m:
        j = 0
        while j<m and txt[i+j]==pat[j]:
            j += 1
        if j==m:
            occ.append(i)
        i += 1
    return occ


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


def kmp(txt, pat):
    n = len(txt)
    m = len(pat)
    nxt = brd(pat)
    print "nxt=", nxt
    occ = []
    i = 0
    j = 0
    while i <= n-m:
        while j<m and txt[i+j]==pat[j]:
            j += 1
        print txt
        print "%s%s%s"%(i*" ",j*"=","!" if j<m else "")
        print "%s%s"%(i*" ",pat)
        print "%s%s"%(i*" ",nxt[j]*"-")
        print
        if j==m:
            occ.append(i)
        print "skipping ", max(1, (j-nxt[j]))
        i += max(1, (j-nxt[j])) 
        j = nxt[j]
    return occ

def main():
    txt = "rabracadrabra"
    pat = "rabra"
    occ = kmp(txt, pat)
    print occ

if __name__ == "__main__":
    main()
