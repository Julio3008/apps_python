import random
chars="abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
password=""
length=int(input("Longitud de la contraseña: "))
for c in range(length):
    password+=random.choice(chars)
print(password)
