# script.py

def calcula_imc(altura, peso):
    altura_x_altura = altura * altura
    imc = peso / altura_x_altura
    return imc 

def gasto_calorico_basal_feminino(altura, peso, idade):
    gasto_basal = 655 + (9.5 * peso) + (1.8 * altura) - (4.7 * idade)
    return gasto_basal

def gasto_calorico_basal_masculino(altura, peso, idade):
    gasto_basal = 66 + (13.7 * peso) + (5 * altura) - (16.8 * idade)
    return gasto_basal


def gasto_calorico_basal_geral (altura, peso, idade, genero):
    if genero == "f":
        gasto_basal = 655 + (9.5 * peso) + (1.8 * altura) - (4.7 * idade)
        return gasto_basal
    else:
        gasto_basal = 66 + (13.7 * peso) + (5 * altura) - (16.8 * idade)
        return gasto_basal