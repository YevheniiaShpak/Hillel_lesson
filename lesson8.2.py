inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

def palindrome(word):
    return word.lower() == word.lower()[::-1]

filtered_palindromes = filter(palindrome, inputdata)
result = tuple(filtered_palindromes)

print(result)


