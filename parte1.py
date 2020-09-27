# Cristina Bautista 161260


import sympy as sp

from Crypto.Util import number
from Crypto.Random import get_random_bytes


# funciones vistas en clase
def get_coprime(N):
	coprimes = []
	for number in range(1, N+1):
		list_commons = []
		for i in range(1, min(number, N)+1):
			if number % i == N % i == 0:
				list_commons.append(i)
		if (len(list_commons) <= 1):
			coprimes.append(number)
	return coprimes

def get_e(list_1, list_2):
	list_e = []
	for element in list_1:
		if (element in list_2 and element > 1):
			list_e.append(element)
	return list_e

def get_possible_d(e, phi):
	possibles_d = []
	for i in range(1, e * e):
		ed = e * i
		ed_mod = ed % phi
		if (ed_mod == 1):
			possibles_d.append(i)
	return possibles_d



# Desde aqui se obtiene las llaves pk y sk 
p = number.getPrime(N=3, randfunc=get_random_bytes)
q = number.getPrime(N=3, randfunc=get_random_bytes)

N = p * q

phi_n = (p - 1) * (q - 1)

coprimeN = get_coprime(N)
coprimePhiN = get_coprime(phi_n)

e = get_e(coprimeN, coprimePhiN)

d = get_possible_d(e[0], len(coprimeN))


print("p: ",p)
print("q: ", q)
print("N: ", N)
print("phi(N): ", phi_n)
print("Lista de N")
print(coprimeN)
print("Lista de coprimos de phi(N)")
print(coprimePhiN)
print("Lista de e: ", e)
print("Se escoge el ultimo", e[0])
print("Lista de d: ", d)
print("Se escoge el primero", d[0])

e = e[-1]
d = d[0]

pk = [e, N]

sk = [d, N]

abecedario = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 
							11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
							21: 't', 22: 'u', 23: 'v', 24: 'w', 25: 'x', 26: 'y', 27: 'z'}

# el mensaje es lero lero en numeros
text_number = [12, 5, 18, 15, 12, 5, 18, 15]

cipher_numbers = []

for number in text_number:
	list_cipher_numbers = number ** pk[0] % pk[1]
	cipher_numbers.append(list_cipher_numbers)

print("Lista de numeros cifrados")
print(cipher_numbers)

decipher_numbers = []

for number in cipher_numbers:
	list_decipher_numbers = number ** sk[0] % sk[1]
	decipher_numbers.append(list_decipher_numbers)

print("Lista de numeros decifrados")
print(decipher_numbers)

texto = []

# en este for busca cada numero la letra que le corresponde
# para mostrar el texto
for number in decipher_numbers:
	letter = abecedario[number]
	texto.append(letter)

print(texto)