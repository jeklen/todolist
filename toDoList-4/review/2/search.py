def main():
    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    m = input('Enter month number (1-12): ')
    pos = (m-1) * 3
    monthAbbr = month[pos:pos+3]
    print 'The month abbreviation is', monthAbbr+'.'

main()