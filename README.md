# Computando patentes

> Computando patentes es un problema de 
> índole lógica - matemática el cual se basa
> en la entrada dos argumentos.
> Una patente (de formato viejo o nuevo)
> y "k" que representa a las siguientes
> posiciones  a la respectiva patente.
> Se pueden leer más detalles del problema
> en la "Descripción del problema".


A continuación el detalle de los módulos y una descripción de sus funciones. 
## patent.py

- next_patent(patent, k)
        Recibe como argumento patent(string) y k(int). 
		El argumento patent debe ser de 6 o 7 carácteres y el argumentok debe ser mayor a 0. Caso contrario el formato no sería correcto y devolvería un mensaje de error dando aviso del mismo. Una vez que se corrobora que el formato sea correcto. 
		Se elige un formato dependiendo de si es una nueva o vieja patente. Se llaman a las funciones que correspondan según el caso. Retorna la nueva patente.
## common.py

- get_patent_numbers(increment)
        Recibe como argumento increment(int) el cual es el resultado de sumar k y el número de la patente.
		Retorna el número que quedará finalmente en la patente y el número de incrementos que hay que hacerle a la letra. Para hacer esto, recurre a la función int_division.
- int_division(number, divider)
        Recibe como argumento number(int) y divider(int). 
		Calcula el resto, que será la cantidad de números a incrementar, y con la división de enteros calcula la cantidad de letras a incrementar. 
		Retorna ambos valores.
- get_letter_and_increment(number, divider)
        Recibe como argumento number(int) y divider(int). 
		Llama a la función int_division con la diferencia que retornará la letra que corresponda al orden y un incremento de la siguiente posición.
- number_to_str(number)
        Recibe como argumento number(int). 
		Agrega los ceros a la izquierda necesarios para ajustarse al formato de la patente.
		Retorna un string con el número transformado.

Además el módulo common.py contiene dos variables globales: alphabet el cual es una lista con el alfabeto inglés (A-Z) y alphabet_size que es el tamaño alphabet.

## old_patent.py

- get_old_patent_format(patent, k)
        Recibe como argumento patent(string) y k (int).
		Convierte a las letras y números en dos listas distintas.
		Calcula el incremento y llama a la función get_patent_numbers(increment)
		Si el incremento de letras resulta ser 0, retorna el nuevo número con las letras originales concantedos. Si el incremento de letras es 1 o más, llama a la función get_old_patent_letters(letter, increment_letter) y finalmente retorna el valor de las nuevas letras concatenadas con el nuevo número.
- get_old_patent_letters(letters, increment)
        Recibe como argumento letters(list) e increment (int).
		Busca el índice de las letras que le corresponden al alfabeto.
		Llama a la función get_letter_and_increment por cada letra, pasando como argumento su índice en el alfabeto sumado a increment.
		En el caso de que la última letra tenga incremento, significa que no existe la patente que estamos buscando.
		Retorna en una lista las nuevas letras.
## new_patent.py

- get_new_patent_format(patent, k)
		Recibe como argumento patent(string) y k (int).
		Convierte a las letras y números en tres listas distintas (dos de letras y una de números).
		Llama a la función get_new_patent_letters con las últimas letras, obtiene las nuevas letras y el incremento que le corresponde al número.
		Llama a la función get_patent_numbers para obtener el nuevo número de patente.
		Llama nuevamente a la función get_new_patent_letters pero esta vez con las primeras letras.
		Retorna un string concatenando las primeras letras,  el número y las últimas letras.
- get_new_patent_letters(patent, k)
		Recibe como argumento letters(list), increment (int) e is_first(boolean).
		Busca el índice de las letras que le corresponden al alfabeto.
		Llama a la función get_letter_and_increment por cada letra, pasando como argumento su índice en el alfabeto sumado a increment.
		 En el caso de is_first sea verdadero (es decir, que enviamos las primeras letras) y aún quede incremento, significa que no existe la patente que estamos buscando.
		 Retorna un string con las letras y un incremento.
## test.py
Es un módulo que contiene algunas pruebas básicas del funcionamiento del algoritmo. Hay 4 pruebas generales por cada uno de los formatos.
## main.py
Es el archivo principal del proyecto, donde hay un input que definirá el usuario para calcular las patentes que busca.
____________________________________________________________________________________________________________________________
        Descripción del problema
En Argentina conviven actualmente dos
sistemas principales para la numeración
de las matrículas automovilísticas, también denominadas patentes:
1. Un formato utilizando desde 1995
hasta 2016, en el cual la patente de un vehículo es una cadena
de exactamente seis caracteres.
Los primeros 3 de estos caracteres
son letras mayúsculas y los últimos 3 son dígitos. Algunos ejemplos:
BET123, PAT180, BAD666, AAA000
y ZZZ381
2. Un formato utilizado desde 2016
hasta hoy, en el cual la patente
de un vehículo es una cadena de
exactamente siete caracteres. Los
primeros 2 y los últimos 2 son letras mayúsculas y los 3 del medio son dígitos. Algunos ejemplos:
AB123CD, AG759LH, ZZ100XX
En ambos formatos, se entiende por
letra a cualquiera de los 26 caracteres
del alfabeto inglés (es decir, el alfabeto
castellano sin la Ñ, desde A hasta Z) y por
dígito a uno de los 10 posibles caracteres
numéricos desde 0 hasta 9 inclusive.
En los dos casos, la patente siguiente de una dada es la que se obtiene
avanzando el último caracter, es decir, reemplazándolo por el caracter siguiente
correspondiente. Por ejemplo la patente
siguiente de ABC151 es ABC152, y la patente siguiente de TE200AW es TE200AX.
Cuando el último caracter es 9 o Z, que
no tienen un caracter siguiente, se vuelve
a comenzar por 0 o por A, y además se
pasa a avanzar el anteúltimo caracter
de la patente. Si este también era 9 o
Z, este proceso continúa hasta conseguir
la siguiente patente. Por ejemplo, la patente siguiente de AB999ZZ es AC000AA,
y la patente siguiente de DOW199 es
DOW200.
Para ayudar a la Dirección Nacional de
los Registros Nacionales de la Propiedad
del Automotor y de Créditos Prendarios,
debes escribir un programa que dada una
patente, la cual puede estar en cualquiera
de los dos formatos, calcule la K-ésima
patente siguiente en el mismo formato. Es
decir, si K = 1 se debe calcular la patente
siguiente, como en los ejemplos ya vistos.
Si K = 2 se debe tomar la siguiente de la
siguiente, y así.
Detalles de implementación
Debes implementar la función
siguiente(patente, K), que recibe una
cadena de caracteres patente, que
contiene la patente en alguno de los dos
formatos, y el entero K.
La función debe retornar una cadena
de caracteres que contenga la K-ésima
siguiente patente.
Se garantiza que la patente recibida es
válida en alguno de los dos formatos, y
que existe una K-ésima siguiente patente.
Por ejemplo, si K = 1, se garantiza que
no se recibirá la patente ZZZ999 ni la
ZZ999ZZ.
