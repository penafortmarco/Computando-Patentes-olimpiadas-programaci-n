from patent import next_patent

#probar ambos casos en muchos elementos.
#validar en caso de que no existan k patentes
#validar no letras minusculas

test_1 = next_patent('ABC151', 1)

if test_1 == 'ABC152':
    print('Success')
else:
    print('Failed')

test_2 = next_patent("AYZ999", 1)

if test_2 == 'AZA000':
    print('Success')
else:
    print('Failed')



