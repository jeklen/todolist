class Cheese(float):
    def __str__(self):
        return 'Muenster'

    def __repr__(self):
        return 'Stilton'

chunk = Cheese(-123.4)

print(str(chunk))
# Muenster
print(repr(chunk))
# Stilton
print(int(chunk))
# -123
print('%s\t%r\t%d'%(chunk, chunk, chunk))