phrase = input('Введить два слова: ')
first_word = phrase.split( ) [0]
second_word = phrase.split( ) [1]

new_phrase1 = '!%(second_word)s %(first_word)s?' % ({'first_word':first_word.title(), 'second_word':second_word.upper()})

new_phrase2 = '!{1} {0}?'.format(first_word.title(), second_word.upper())

new_phrase3 = f'!{second_word.upper()} {first_word.title()}?'

print(phrase, new_phrase1, new_phrase2, new_phrase3, sep='<<<>>>')

additional_file = open('Additional.txt', 'w')
print(phrase, new_phrase1, new_phrase2, new_phrase3, sep='<<<>>>', file=additional_file, end='')
additional_file.close()
