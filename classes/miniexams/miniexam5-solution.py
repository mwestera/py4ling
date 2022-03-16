s = ['ahjgasd', 'qweeqw', 'dsaasdads']          # not requested

def analyze_strings(strings):
    print(len(strings))

    total_length = 0
    total_n_vowels = 0

    for string in strings:
        print(len(string))
        n_vowels = len([char for char in string.lower() if char in 'aeiou'])
        # n_vowels = 0
        # for char in string.lower():
        #     if char in 'aeiou':
        #         n_vowels += 1
        print(n_vowels)
        total_n_vowels += n_vowels
        total_length += len(string)

    print(total_n_vowels)
    print(total_length)


analyze_strings(s)