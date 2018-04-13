verb = str(input('verb: ').lower())
if verb[-1] == 'r':
    if verb[-2] == 'a':
        print('First conjugation.')
    elif verb[-2] == 'e' or verbo[-2] == 'o':
        print('Second conjugation.')
    elif verb[-2] == 'i':
        print('Third conjugation.')

else:
    print('Is not the infinitive.')
