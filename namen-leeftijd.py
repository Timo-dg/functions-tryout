

def program():
    naam = 'naam: '
    leeftijd = 'leeftijd: '
    while naam != 'stop' and leeftijd != 'stop':
        naam = input('naam: ')
        if naam == 'stop':
            break
        leeftijd = input('leeftijd: ')
        if leeftijd == 'stop':
            break
        
        print('Hallo', naam, 'je leeftijd is', leeftijd, 'jaar' )
program()