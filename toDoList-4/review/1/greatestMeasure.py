# It is really to use while True
def greatestMeasure(a, b):
    if a % b == 0:
        return b
    while True:
        r = a % b
        a = b
        b = r
        if a % b == 0:
            return b

print greatestMeasure(12, 11)
print greatestMeasure(12, 4)