import random
print("Bem-vindo ao gerador de password!")
tamanho_total = int(input("Quantas letras você quer na sua senha? "))
quantidade_de_simbolos = int(input("Qual é o total de símbolos que você quer? "))
quantidade_de_numeros = int(input("Qual é a quantidade de números vai ter? "))

letras = ['q','w', 'e', 'r', 't','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
simbolos = ['!','@','#','$','%','*','^','&','*','(',')','-','+','=','_','<','>','?','/','"','[', ']','{','}',',''|','~','`']
numeros = ['1','2','3','4','5','6','7','8','9','0']

password_list = []

for char in range(1,tamanho_total+1):
    password_list += random.choice(letras)

for char in range(1,quantidade_de_simbolos):
    password_list+= random.choice(simbolos)

for char in range(1,quantidade_de_numeros):
    password_list in range(1,quantidade_de_numeros)

random.shuffle(password_list)

mypassword = ''
for char in password_list:
    mypassword += char

print("Aqui Esta sua senha, não va esquecer\n\n" + mypassword)