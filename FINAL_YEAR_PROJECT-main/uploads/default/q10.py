def count_vowels_consonants(word):
    vowels = 'aeiou'
    v_count = 0
    c_count = 0
    for char in word:
        if char.lower() in vowels:
            v_count += 1
        elif char.isalpha():
            c_count += 1
    return v_count, c_count


input_word1 = "pythonlobby"
vowels1, consonants1 = count_vowels_consonants(input_word1)
print("Input:", input_word1)
print("Output: Vowels:", vowels1, "Consonants:", consonants1)


input_word2 = "sabudhfoundation"
vowels2, consonants2 = count_vowels_consonants(input_word2)
print("Input:", input_word2)
print("Output: Vowels:", vowels2, "Consonants:", consonants2)
