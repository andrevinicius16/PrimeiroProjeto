#Informações dos Viajantes
valor_bruto_pacote = float(input("Informe o valor do pacote: "))
categoria_assentos = input("Por favor informe a categoria de assentos: ")
quantidades_viajantes = int(input("Informe a quantidade de viajantes: "))

# 1. Definir o desconto padrão como 0 antes de testar as condições
desconto = 0

# 2. Verificação Categoria Econômica
if categoria_assentos.upper() == "ECONOMICA":
    if quantidades_viajantes == 2:
        desconto = valor_bruto_pacote * 0.03
    elif quantidades_viajantes == 3:
        desconto = valor_bruto_pacote * 0.04
    elif quantidades_viajantes >= 4:
        desconto = valor_bruto_pacote * 0.05
#Verificação Categoria Executiva
if categoria_assentos.upper()  == "EXECUTIVO":
    if quantidades_viajantes == 2:
        desconto = valor_bruto_pacote * 0.05
    elif quantidades_viajantes == 3:
        desconto = valor_bruto_pacote * 0.07
    elif quantidades_viajantes >= 4:
        desconto = valor_bruto_pacote * 0.08
#Verificação Categoria Primeira Classe
if categoria_assentos.upper() == "PRIMEIRA CLASSE":
    if quantidades_viajantes == 2:
        desconto = valor_bruto_pacote * 0.10
    elif quantidades_viajantes == 3:
        desconto = valor_bruto_pacote * 0.15
    elif quantidades_viajantes >= 4:
        desconto = valor_bruto_pacote * 0.20
#Verificação Calculos Finais
valor_liquido = valor_bruto_pacote - desconto
media_viajante = valor_liquido / quantidades_viajantes

# Exibir Resultados
print("O valor da viagem é de R${}. Após os descontos de R${}, a viagem custará R${}. Cada passageiro tem um custo médio de R${}.".format(valor_bruto_pacote, desconto, valor_liquido, media_viajante))











