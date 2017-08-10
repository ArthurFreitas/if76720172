
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

def main():
    txt = "abracadabra"
    pat = "abra"
    occ = bruteforce(txt, pat)
    print occ

if __name__ == "__main__":
    main()
