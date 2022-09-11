# General solution seems to be intelligently recreating string from a frequency
# dict either by taking two elements at a time or tracking last element taken.

def reorganizeString(s):
    mod = sorted(sorted(s), key=s.count, reverse=True)
    half = len(mod) // 2 + (len(mod) % 2)
    if mod.count(mod[0]) > half:
        return ""
    mod[::2], mod[1::2] = mod[:half], mod[half:]
    return "".join(mod)

s = "a"
print(reorganizeString(s))