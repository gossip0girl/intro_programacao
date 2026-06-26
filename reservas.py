nome = input("Digite sei nome") #Texto ou String (str)

idade = int(input("Digite sua ideda:")) #NUmero inteiro

dias = int(input("Quantos dias você deseja ficar no hotel? "))

responsavel = input("Está acompanhado de um responsal? (sim/não)"). lower()

vip - input("Você é cliente VIP? (sim/não)"). lower()

aceitou_regras = input("Você aceita as regras do hotel? (sim/não)"). lower()

if responsavel == "sim":
   tem_responsavel = True
else:
    tem_responsavel = False

if vip == "sim": 
    cliente_vip = True
else:
    clientes_vip = False

if aceitou_regras == "sim": 
    aceitou = True
else:
    aceitou = False

# REGRA 1: Concordar com os termos do hotel 
#NOT

if not aceitou:
    print("Reserva cancelada.")
    print("Motivo: Não concordou com as regras")

    #REGRA 2 : Menores de 18 anosprecisam do responsável

elif idade < 18 and not tem_responsavel:
    print("Reserva negada")
    print("Menores de 18 anos precisam estar acompandos do responsavel")

else:
    print("Reserva confirmada!")

#REGRA 3: 3 diárias ou mais OU (OR) VIP = café da manhã 

if dias >= 3 or cliente_vip:
    print("Café da manhã incluso")
else:
    print("Reserva confirmada sem café incluso")

    #REGRA 4: Clientes que fica 7+ e (AND) são VIPs: quarto melhor

    if dias >= 7 and clientes_vip:
        print("Parabéns! Upgrade d quarto liberao")
    else: 
        print("Quarto padrão reservado")
        