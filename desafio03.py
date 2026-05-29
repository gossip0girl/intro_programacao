def calcular_viagem(): 
print("=== CALCULADORA DE CUSTOS DE VIAGEM ===")

# Entrada de dados
pessoas = int(input("Quantas pessoas vão viajar? "))

passagem = float(input("Digite o valor total das passagens: "))
hospedagem = float(input("Digite o valor da hospedagem: "))
alimentacao = float(input("Digite o valor gasto com alimentação: "))
outros = float(input("Digite outros gastos da viagem: "))

# Processamento
valor_total = passagem + hospedagem + alimentacao + outros

valor_por_pessoa = valor_total / pessoas

# Saída
print("\n=== RESULTADO ===")
print(f"Valor total da viagem: R$ {valor_total:.2f}")
print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")


