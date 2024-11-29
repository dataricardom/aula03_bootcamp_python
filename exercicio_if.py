# x = int(input("Digite um numero inteiro:"))

# if x < 0:
#     x=0
#     print("Alterado para zero")
# elif x == 0:
#     print("Zero")
# elif x ==  1:
#     print(" Single ")
# else:
#     print("more")

# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# quantidade = int(input("Insira a quantidade: "))
# preco = float(input("Diga o preço: "))

# if quantidade > 0 and preco > 0:
#     print("Dados validos")
# else:
#     print ("Dados invalidos.")
#Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. 
# Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# temperatura = float(input("Por favor insira a temperatura: "))

# if temperatura < 18:
#     print("Temperatura: BAIXA")
# elif temperatura <= 26:
#     print("Temperatura: NORMAL")
# else:
#     print("Temperatura: MUITO ALTA")


#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log_aplic = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log_aplic['level'] == 'ERROR':
#     print (log_aplic['message'])


idade = int(input("Por favor insira a sua idade: "))
email_usu = input("Por favor digite o seu email.")

if  18 >= idade <=65:
    print("Idade fora do intervalo permitido")
elif "@" not in email_usu or "." not in email_usu:
    print("Email invalido")
else:
    print("Dados de usuarios validos")