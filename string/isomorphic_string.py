from collections import defaultdict

def isomorphic(s, t):
    freq1, freq2 = defaultdict(list), defaultdict(list)

    for i in range(len(s)):
        if freq1.get(s[i], ''):
            if freq1.get(s[i], '') != t[i] : return True
        else:
            if freq2.get(t[i], '') : return False
            freq1[s[i]].append(t[i])
            freq2[t[i]].append(s[i])
    
    return True

print(isomorphic("egg", "dff"))
