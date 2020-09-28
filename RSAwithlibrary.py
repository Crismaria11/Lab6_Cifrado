from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

print("Primero se indica el largo que tendran nuestras llaves. seleccionamos 4096 bit para que sea seguro")
llaves = RSA.generate(4096)

print ("indicamos que pk sera nuestra llave publica y procedemos a mostarla tanto en hex como formato pem")
pk = llaves.publickey()
print(f"Llave publica:  (n={hex(pk.n)}, e={hex(pk.e)})")
pkPEM = pk.exportKey()
print(pkPEM.decode('ascii'))

print ("Procedemos a crear el PEM de la llave privada para poder mostrarlo")
print(f"Llave privada: (n={hex(pk.n)}, d={hex(llaves.d)})")
skPEM = llaves.exportKey()
print(skPEM.decode('ascii'))

print ("Declaramos el mensaje a encriptar, en este cadso el siguiente sera")
mensaje = b'Este es el mensaje a encriptar'
print (mensaje)
print("declaramos el encriptor, usando RSA con PKCS#1 OAEP padding usando la llave publica")
encryptor = PKCS1_OAEP.new(pk)
print ("procedemos a, encriptar el mensaje")
encrypted = encryptor.encrypt(mensaje)
print("Mensaje encriptado:", binascii.hexlify(encrypted))

print ("decalramos el desencriptador, utilizando el pkcs RSA OAEP utilizando ambas llaves")
decryptor = PKCS1_OAEP.new(llaves)
print ("procedemos a desencriptar el mensaje")
decrypted = decryptor.decrypt(encrypted)
print('Mensaje desencriptado :', decrypted)
