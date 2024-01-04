class String(str):
    def __add__(self, other):
        if isinstance(other, str):
            return String(str.__add__(self, other))
        elif isinstance(other, (int, float)):
            return String(str.__add__(self, str(other)))
        elif isinstance(other, list):
            return String(str.__add__(self, str(other)))

    def __sub__(self, other):
        if isinstance(other, (str, int, float)):
            other_str = str(other)
            if other_str in self:
                result_str = self.replace(other_str, '', 1)
                return String(result_str)
            else:
                return String(self)

s1 = String("New")
s2 = String(890)
s3 = s1 + s2
s33 = s2 + 567
s333 = s2 + ['s', ' ', 23]
print(s3)
print(s33)
print(s333)

print("___"*10)

s4 = s1 - "e"
s44 = s33 - 5

print(s4)
print(s44)