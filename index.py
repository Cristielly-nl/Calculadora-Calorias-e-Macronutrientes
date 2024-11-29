#-----------------------------------------------------------------------------
# Função para calcular a TMB (Taxa Metabólica Basal)
def calcular_tmb(peso, altura, idade, sexo):
    if sexo.upper() == 'F':
        return 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    elif sexo.upper() == 'M':
        return 66 + (13.7 * peso) + (5.0 * altura) - (6.8 * idade)
    else:
        raise ValueError("Sexo inválido! Use 'F' para feminino ou 'M' para masculino.")
    

#-----------------------------------------------------------------------------
# Função para calcular o GET (Gasto Energético Total)
def calcular_get(tmb, nivel_atividade):
    niveis_atividade = {
        1: 1.2,   # Sedentário
        2: 1.37,  # Levemente ativo
        3: 1.55,  # Moderadamente ativo
        4: 1.72,  # Muito ativo
        5: 1.9    # Extremamente ativo
    }
    fator = niveis_atividade.get(nivel_atividade) 
    if fator is None:
        raise ValueError("Nível de atividade física inválido! Escolha entre 1 e 5.")
    return tmb * fator

#------------------------------------------------------------------------------
# Entrada de dados do usuário
print("Digite seu nome: ")
nome = input()

print("Digite seu peso em kg: ")
peso = float(input())

print("Digite sua altura em cm: ")
altura = float(input())

print("Digite sua idade em anos: ")
idade = float(input())

print("Digite seu sexo (F para Feminino ou M para Masculino): ")
sexo = input()

#-----------------------------------------------------------------------------
# Cálculo da Taxa Metabolica Basal - TMB
try:
    tmb = calcular_tmb(peso, altura, idade, sexo)
    print(f"\nTaxa Metabólica Basal (TMB): {tmb:.2f} kcal/dia")
except ValueError as e:
    print(e)
    exit()

#-----------------------------------------------------------------------------
# Nível de atividade física - GET
print("\nQual seu nível de atividade física? Escolha de 1 a 5:")
print("1. Sedentário: Pouco ou nenhuma atividade física")
print("2. Levemente ativo: Atividades leves (1 a 2 vezes na semana)")
print("3. Moderadamente ativo: Atividades moderadas (3 a 4 vezes na semana)")
print("4. Muito ativo: Atividades intensas (5 a 6 vezes na semana)")
print("5. Extremamente ativo: Atividades pesadas (6+ vezes na semana)")

try:
    nivel_atividade = int(input())
    get = calcular_get(tmb, nivel_atividade)
    print("-------------------------------------------------------------------")
    print(f"\nGasto Energético Total (GET): {get:.2f} kcal/dia")
    print("-------------------------------------------------------------------")
except ValueError as e:
    print(e)
    exit()

#---------------------------------------------------------------------------
# Ajuste do GET para objetivo
print("\nEscolha seu objetivo:")
print("1. Emagrecer (Déficit calórico: 10-20%)")
print("2. Ganhar peso (Superávit calórico: 10-20%)")
print("3. Manter peso")

objetivo = int(input())
if objetivo == 1:
    get_final = get * 0.9  # Déficit de 10%
    print("-------------------------------------------------------------------")
    print(f"\nPara emagrecer, seu consumo diário deve ser em média: {get_final:.2f} kcal")
    print("-------------------------------------------------------------------")
elif objetivo == 2:
    get_final = get * 1.1  # Superávit de 10%
    print("-------------------------------------------------------------------")
    print(f"\nPara ganhar peso, seu consumo diário deve ser em média: {get_final:.2f} kcal")
    print("-------------------------------------------------------------------")
elif objetivo == 3:
    get_final = get # Manter o peso
    print("-------------------------------------------------------------------")
    print(f"\nPara manter o peso, seu consumo diário deve ser: {get_final:.2f} kcal")
    print("-------------------------------------------------------------------")
else:
    print("Objetivo inválido! Escolha entre 1, 2 ou 3.")
    exit()

#------------------------------------------------------------------------------
# Dicas de distribuição dos macronutrientes
print("\nDicas para distribuição dos macronutrientes:")
print("1. Proteínas: 10% a 35% das calorias")
print("2. Carboidratos: 45% a 65% das calorias")
print("3. Gorduras: 20% a 35% das calorias")

print("\nLevando em consideração os percentuais: proteinas = 20%, carboidratos = 50%, gorduras = 30%, temos: \n")

# Porcentagens de cada macronutriente
percentual_proteinas = 0.20  # 20%
percentual_carboidratos = 0.50  # 50%
percentual_gorduras = 0.30  # 30%

# Calorias de cada macronutriente
calorias_proteinas = get_final * percentual_proteinas
calorias_carboidratos = get_final * percentual_carboidratos
calorias_gorduras = get_final * percentual_gorduras

# Conversão das calorias para gramas (4 kcal por grama de proteína e carboidrato, 9 kcal por grama de gordura)
gramas_proteinas = calorias_proteinas / 4
gramas_carboidratos = calorias_carboidratos / 4
gramas_gorduras = calorias_gorduras / 9

# Exibição dos resultados
print(f"Calorias totais: {get_final:.2f} kcal")
print(f"Proteínas: {calorias_proteinas:.2f} kcal ({gramas_proteinas:.2f} g)")
print(f"Carboidratos: {calorias_carboidratos:.2f} kcal ({gramas_carboidratos:.2f} g)")
print(f"Gorduras: {calorias_gorduras:.2f} kcal ({gramas_gorduras:.2f} g)")



