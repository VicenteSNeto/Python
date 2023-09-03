
print("Olá mundo!") 
nome = "Vicente" 
print(nome) 
type(nome) 

# Variável numérica do tipo inteiro 

idade = 28 

print(idade) 

type(idade) 

altura = 1.74 

print(altura) 

type(altura) 

#ENTRADA 

nome = input("Digite o seu nome: ")  

print(f"Olá {nome}! Seja bem vindo(a) ao programa Match!")  

print(f"Oi, meu nome e {nome}, eu tenho {idade} anos e {altura} de altura.")                    

#ENTRADAS 

#Pedir dois números para o usuário. 

numero1 = int(input("Digite o primeiro número: ")) 
numero2 = int(input("Digite o segundo número: "))  

#PROCESSAMENTO 

#Somar os dois números 

# soma = numero1 + numero2 
# print(soma) 

resultado = numero1 + numero2  

#SAÍDA 
# Mostrar o resultado na tela   

print(f"A soma do número {numero1} + o número {numero2} é: {resultado}")  

print(f"A soma é: {numero1 + numero2}")
             
#ENTRADA 

nota1 = float(input(f"Digite a primeira nota: ")) 
nota2 = float(input(f"Digite a segunda nota: ")) 
nota3 = float(input(f"Digite a terceira nota: "))

    
#PROCESSAMENTO 

media = (nota1 + nota2 + nota3) / 3 
# print(media) 

if media >= 6: 
    print(f"Parabéns! Você tirou media {media}. Você passou de ano.") 

else: 
    print("Infelizmente você reprovou:(")   

 #SAIDA  