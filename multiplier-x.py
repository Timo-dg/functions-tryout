gevraagdGetal = int(input('Van welk getal wilt u de tafel zien? 1/10 '))
def tafel(noemer: int):
    for teller in range(1, 11):
        print(teller, 'x', noemer, '=', teller * noemer )
tafel(gevraagdGetal)


    