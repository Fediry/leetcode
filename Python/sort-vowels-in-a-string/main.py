
def sortVowels(s: str) -> str:
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    index_of_vowels = []
    vowels = []
    result = list(s)

    for i, v in enumerate(s):
        if v.lower() in VOWELS:
            index_of_vowels.append(i)
            vowels.append(v)

    vowels.sort()

    for i, v in enumerate(vowels):
        result[index_of_vowels[i]] = v
        
    return ''.join(result)


test = "This Is a TEsT Of Sorting vOwels."
print(sortVowels(test))