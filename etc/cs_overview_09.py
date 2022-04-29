def permute1(s, l, r):
    if l == r:
        print(s)
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute1(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


text = ["A", "B", "C"]
permute1(text, 0, len(text) - 1)
print("")


def permute2(s, l, r):
    if l == r:
        print(s)
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute2(s, l + 1, r)
            # s[l], s[i] = s[i], s[l]


text = ["A", "B", "C"]
permute2(text, 0, len(text) - 1)
print("")


def permute3(s, l, r):
    if l == r:
        print(s)
    else:
        for i in range(l, r + 1):
            s2 = s[:]
            s2[l], s2[i] = s2[i], s2[l]
            permute3(s2, l + 1, r)


text = ["A", "B", "C"]
permute3(text, 0, len(text) - 1)
print("")
