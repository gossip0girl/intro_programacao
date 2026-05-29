#calcular custos

def calcular_custos(diaria, dias):
    custo = diaria * dias 
    return custo


def analisar_viagem(orcamento):
    print("analisando viagem")
    if orcamento >= 800:
     print("sua viagem sera confortavel")
    else:
     print("sua viagem sera economica")

def exibir_resultado(nome, dias, diaria, lugares):
    print("resumo da viagem")

    print(f"nome do viajante: {nome}")
    print(f"dias de viagem: {dias}")
    print(f"valor da diaria: {diaria}")
    print(f"locais de viagem: {lugares}")

    custo = calcular_custos(diaria, dias)

    print(f"gasto total: {custo}")

#principal

print("bem vindo a agencia de viagens")

nome = input("digite seu nome para começar: ")

dias_viagem = int(input("quantos dias de viagem? "))

diaria = float(input("qual o valor da diaria que deseja? "))

lugares = input("digite os lugares que deseja visitar separado por vírgula")

lugares = lugares.split(",")

exibir_resultado(nome, dias_viagem, diaria, lugares)

analisar_viagem(orcamento)