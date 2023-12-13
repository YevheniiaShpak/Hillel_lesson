x = 'Росла в гаю конвалія'
y = 'Під дубом високим,'
z = 'Захищалась від негоди'
c = 'Під віттям широким.'

file = open('poem.txt', 'w')
file.write(x + '\n')
file.write(y + '\n')
file.close()

file1 = open('poem.txt', 'a')
file1.write(z + '\n')
file1.write(c + '\n')
file1.close()

