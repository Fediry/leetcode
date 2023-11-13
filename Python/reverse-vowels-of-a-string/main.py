def reverseVowels(s: str) -> str:
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    index_of_vowels = []
    vowels = []
    result = []

    for i, v in enumerate(s):
        result.append(v)
        if v.lower() in VOWELS:
            index_of_vowels.append(i)
            vowels.append(v)

    for v in index_of_vowels:
        result[v] = vowels.pop()
        
    return ''.join(result)

test = "hello there."
print(reverseVowels(test))