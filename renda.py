renda_mensal = float(input("Qual ë sua renda mensal: "))
score_mensal = int(input("Qual é seu Score de Crédito: (Valor entre 0 a 1000): "))
garantia = input("Possui bens como garantia: " "Sim" + "/" + "Nao: " or "Nao")
inadimplencia = input("Tem Histórico de Inadimplência: " "Sim" + "/"  + "Nao: " or "Nao")

if renda_mensal >= 3000 and score_mensal >= 600 and inadimplencia == "Nao":
    situacao = "O empréstimo será aprovado!"

elif inadimplencia == "Nao" and garantia == "Sim":
        situacao = "O empréstimo foi aprovado!"

else:
        situacao = "O empréstimo será reprovado!"

print (f"Renda: {renda_mensal}")
print (f"Crédito: {score_mensal}")
print (f"Garantia: {garantia}")
print (f"Inadimplencia: {inadimplencia}")  
print (f"Situacao: {situacao}")  
