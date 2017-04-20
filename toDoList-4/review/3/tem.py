f = input('Temperature in degrees Fahrenheit: ')
c = (f - 32) * 5.0 / 9
print('Temperture in degreesCelsius:', c)
if c > 35:
    print 'Warning, hot wave!'
else:
    print 'ok'