import script as sc

altura = float(input('Escreva aqui qual é a sua altura: '))
peso = float(input('Escreva aqui qual é o seu peso: '))
idade = float(input('Escreva aqui qual é a sua idade: '))
genero = input('Qual o seu gênero? Escreva "F" para feminino e "M" para masculino.').lower()


'''
Calcula o IMC da pessoa. Por ora, o input é hard code.
'''
retorno = sc.calcula_imc(altura, peso)
print(f'O seu IMC é de {retorno:.2f}')


'''
Cálculo do gasto energético basal de acordo com altura, peso, idade e gênero.
'''
gasto_calorico_basal =  sc.gasto_calorico_basal_geral(altura, peso, idade, genero)
print(f'O seu gasto energético basal é de {gasto_calorico_basal:.2f} calorias.')