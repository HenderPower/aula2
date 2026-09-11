nome = input("Qual o nome do estudante: """)
estudante = input("É um estudante: " "sim" + "/" + "nao: " or "nao")
dia_semana = input("Qual dia da semana: " "terca" + "/" + "outro: " or "outro")
tipo_sala = input("Tipo de sala: " " VIP" + "/" + "Comum: " or "Comum")

if estudante == "sim" and dia_semana == "terca" and tipo_sala == "Comum":
    situacao = "Desconto Aplicado!"

else:
    situacao = "Valor Integral!"

print (f"Nome: {nome}")
print (f"Dia da Semana: {dia_semana}")
print (f"Sala: {tipo_sala}")
print (f"Situacao: {situacao}") 