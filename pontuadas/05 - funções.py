import os
#Limpa tela
def logo():
    os.system("clear")

#Calculando valor do INSS
def calcular_inss(salario_base):
    if salario_base <= 1100:
        valor_inss = salario_base * 0.075
    elif salario_base <= 2203.48:
        valor_inss = salario_base * 0.09
    elif salario_base <=3305.22:
        valor_inss = salario_base * 0.12
    elif salario_base <= 6433.57:
        valor_inss = salario_base * 0.14
    else:
        valor_inss = 854.36
        
    return valor_inss

#Calculando valor do IRRF
def calcular_irrf(salario_base, qtd_dependentes):
    deducao = qtd_dependentes * 189.59
    
    if salario_base <= 2259.20:
        valor_irrf = 0.0
    elif salario_base <= 2826.65:
        valor_irrf= salario_base * 0.075
    elif salario_base <= 3751.06:
        valor_irrf= salario_base * 0.15 
    elif salario_base <= 4664.68:
        valor_irrf= salario_base * 0.225 
    else:
        valor_irrf = salario_base * 0.275
        
    valor_irrf = valor_irrf - deducao
    return valor_irrf
    
#Calculando valor do VT
def calcular_vale_transporte(salario_base):
    return salario_base * 0.06
    
#Calculando valor do VR
def calcular_vale_refeicao(beneficio_empresa):
    beneficio = beneficio_empresa * 0.20
    return beneficio
    
#Calculando plano de saude
def plano_saude(qtd_dependentes):
    valor = 150.0
    valor_dependente = 150.0
    return valor +  (qtd_dependentes * valor_dependente)

#variaveis para armazenar desconts iniciais
inss = 0
irrf = 0

#solicitando dados(OK)
login = input("informe seu login: ")
senha = input("informe sua senha: ")
logo()
salario = float(input("Informe o valor do seu salario: "))
qtddepen = int(input("Informe quantos dependentes vc possui: "))
vale_transporte = input("Informe se deseja receber vale tranporte(S/N): ").lower()
vale_comida = float(input("Informe o valor do vale refeicao fornecido pela empresa: "))
    
#calculando inss(OK)
inss = calcular_inss(salario)

#calculando irrf(OK)
irrf = calcular_irrf(salario, qtddepen)


#calculando vale transporte (OK)
if vale_transporte == 's':
    vale_trans = calcular_vale_transporte(salario)
else:
    vale_trans = 0.0

#calculando vale refeição (OK)
vale_refeicao = calcular_vale_refeicao(vale_comida)

#Plano de saude (OK)
plano = plano_saude(qtddepen)

#descontando do salario
desconto_total = vale_trans + vale_refeicao + inss + irrf + plano

    
#CALCULANDO SALARIO LIQUIDO (OK)
salario_liquido = salario - desconto_total

#Mostrando pro usuario
logo()
print("======== DADOS DO USUARIO ========")
print("Matricula: {}".format(login))
print("Senha: {}".format(senha))
print("Salario bruto:R$ {:.2f}".format(salario))
print("Desconto INSS:R$ {:.2f}".format(inss))
print("Desconto IRRF:R$ {:.2f}".format(irrf))
print("Vale transporte:R$ {:.2f}".format(vale_trans))
print("Vale refeição:R$ {:.2f}".format(vale_refeicao))
print("Plano de saúde:R$ {:.2f}".format(plano))
print("desconto total:R$ {:.2f}".format(desconto_total))
print("Salario liquido:R$ {:.2f}".format(salario_liquido))
print("=" * 34)