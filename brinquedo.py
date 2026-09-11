crianca = input("Digite o nome da criança: ")
idade = int(input("Digite a idade: "))
altura = int(input("Digite a altura em centímetro: "))
autorizacao = input("tem autorização dos pais?")

if altura <= 140 and idade <= 12 and autorizacao == "Nao":
    situacao = "A criança não pode andar no brinquedo"

else: 
    situacao = "A criança pode usar o brinquedo!"



print (f"Nome: {crianca}")
print (f"Idade: {idade}")
print (f"Altura: {altura}")
print (f"Situação: {situacao}")