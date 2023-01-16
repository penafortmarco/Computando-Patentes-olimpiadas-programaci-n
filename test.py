from patent import next_patent

#probar ambos casos en muchos elementos.
#validar en caso de que no existan k patentes
#validar no letras minusculas

test_1 = next_patent('ABC151', 1)

if test_1 == 'ABC152':
    print('Success')
else:
    print('Failed')

test_2 = next_patent('AYZ999', 1)

if test_2 == 'AZA000':
    print('Success')
else:
    print('Failed')

test_3 = next_patent('AAA000', 17575999) 

if test_3 == 'ZZZ999':
    print('Success')
else:
    print('Failed')

test_4 = next_patent('ZZZ999', 1)
    #It should throw "Patent does not exist" and return none.

test_5 = next_patent('AA100AZ', 1)

if test_5 == 'AA100BA':
    print('Success')
else:
    print('Failed')

test_6 = next_patent('ZZ999ZY', 1)

if test_6 == 'ZZ999ZZ':
    print('Success')
else:
    print('Failed')

test_7 = next_patent('AA000AA', 456975999)

if test_7 == 'ZZ999ZZ':
    print('Success')
else:
    print('Failed')

test_8 = next_patent('AA000AA', 456976000)
    #It should throw "Patent does not exist" and return none.




