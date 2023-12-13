a = b'r\xc3\xa9sum\xc3\xa9'

b = a.decode()

d = b.encode('Latin-1')

e = d.decode('Latin-1')

print(b, d, e, sep='\n')
