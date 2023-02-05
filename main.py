import random
from colorama import Fore

# Valores
K10 = 10000
K20 = 20000
K30 = 30000
K40 = 40000
K50 = 50000
K60 = 60000
K75 = 75000
K100 = 100000
K120 = 120000
K130 = 130000
K140 = 140000
K150 = 150000
K160 = 160000
K180 = 180000
K200 = 200000
K220 = 220000
K240 = 240001
K250 = 250000
K260 = 260000
K280 = 280000
K300 = 300000
K320 = 320000
K350 = 350000
K400 = 400000
K450 = 450000
K500 = 500000

# 3
quadradosTabuleiro = {
  0: {
    "nome": "inicio",
    "cor": "verde",
    "valor": 0,
    "status": "inicio"
  },
  1: {
    "nome": "Av. Niemeyer",
    "valor": K75,
    "cor": "verde"
  },
  2: {
    "nome": "Jd. Botânico",
    "valor": K100,
    "cor": "verde"
  },
  3: {
    "nome": "Rua Oscar Freire",
    "valor": K220,
    "cor": "vermelho"
  },
  4: {
    "nome": "Av. Ibirapuera",
    "valor": K220,
    "cor": "vermelho"
  },
  5: {
    "nome": "Praça da Sé",
    "valor": K200,
    "cor": "roxo"
  },
  6: {
    "nome": "Rua da Consolação",
    "valor": K180,
    "cor": "roxo"
  },
  7: {
    "nome": "Viaduto do Chá",
    "valor": K180,
    "cor": "roxo"
  },
  8: {
    "nome": "Jardins",
    "valor": K350,
    "cor": "rosa"
  },
  9: {
    "nome": "Av. do Contorno",
    "valor": K300,
    "cor": "laranja"
  },
  10: {
    "nome": "Praça Castro Alves",
    "valor": K300,
    "cor": "laranja"
  },
  11: {
    "nome": "Higienópolis",
    "valor": K400,
    "cor": "rosa"
  },
  12: {
    "nome": "Av. São João",
    "valor": K120,
    "cor": "lilas"
  },
  13: {
    "nome": "Barra da Tijuca",
    "valor": K260,
    "cor": "dourada"
  },
  14: {
    "nome": "Praça dos três poderes",
    "valor": K320,
    "cor": "laranja"
  },
  15: {
    "nome": "Av. Iasmim",
    "valor": K160,
    "cor": "verde"
  },
  16: {
    "nome": "Av. Carlos",
    "valor": K140,
    "cor": "verde"
  },
  17: {
    "nome": "Ponte do Guaiba",
    "valor": K140,
    "cor": "verde"
  },
  18: {
    "nome": "Av. Ipiranga",
    "valor": K100,
    "cor": "lilas"
  },
  19: {
    "nome": "Central de Força e Luz",
    "valor": K200,
    "cor": "azul"
  },
  20: {
    "nome": "Receita Federal",
    "valor": -K200,
    "cor": "azul",
    "status": "receita"
  },
  21: {
    "nome": "Ponte Rio Niterói",
    "valor": K280,
    "cor": "dourada"
  },
  22: {
    "nome": "Créditos de Carbono",
    "valor": K150,
    "cor": "azul",
    "status": "carbono"
  },
  23: {
    "nome": "Prisão",
    "valor": 0,
    "status": "preso",
    "cor": "branco"
  },
  24: {
    "nome": "Sorte ou Revés",
    "valor": 0,
    "status": "sorte-reves",
    "cor": "dourada"
  }
}
for i in range(len(quadradosTabuleiro)):
  if i not in [0, 20, 22, 23, 24]:
    quadradosTabuleiro[i]["status"] = "Não comprada"
    quadradosTabuleiro[i]["construcao"] = "sem"

propriedadesCores = {
  "dourada": {
    "propriedades": [21, 13],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 2
  },
  "roxo": {
    "propriedades": [5, 6, 7],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 3
  },
  "vermelho": {
    "propriedades": [3, 4],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 2
  },
  "lilas": {
    "propriedades": [12, 18],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 2
  },
  "rosa": {
    "propriedades": [8, 11],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 2
  },
  "laranja": {
    "propriedades": [9, 10, 14],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 3
  },
  "azul": {
    "propriedades": [19, 21, 22],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 3
  },
  "verde": {
    "propriedades": [1, 2, 15, 16, 17],
    "1c": 0,
    "2c": 0,
    "3c": 0,
    "4c": 0,
    "h": 0,
    "countMax": 5
  },
  "branco": {
    "propriedades": [23]
  }
}

propriedadesConstrucoes = {"1c": {}, "2c": {}, "3c": {}, "4c": {}, "h": {}}

cores = {
  1: Fore.RED,
  2: Fore.GREEN,
  3: Fore.LIGHTYELLOW_EX,
  4: Fore.BLUE,
  "roxo": '\033[95m',
  "vermelho": Fore.RED,
  "verde": Fore.GREEN,
  "dourado": Fore.YELLOW,
  "azul": Fore.BLUE,
  "laranja": "\033[33m",
  "rosa": Fore.MAGENTA,
  "lilas": Fore.LIGHTMAGENTA_EX,
  "dourada": Fore.YELLOW,
  "branco": Fore.WHITE
}

titulosDePosse = {
  1: {
    "a": K20,
    "1c": K10,
    "2c": K30,
    "3c": 90000,
    "4c": K160,
    "h": K250,
    "cc": K50,
    "ch": K50,
    "hip": K50
  },
  2: {
    "a": 6000,
    "1c": K30,
    "2c": 90000,
    "3c": 270000,
    "4c": K400,
    "h": K500,
    "cc": K50,
    "ch": K50,
    "hip": K50
  },
  3: {
    "a": 18000,
    "1c": 90000,
    "2c": K250,
    "3c": 700000,
    "4c": 8750000,
    "h": 1050000,
    "cc": K150,
    "ch": K150,
    "hip": 11000
  },
  4: {
    "a": 18000,
    "1c": 90000,
    "2c": K250,
    "3c": 700000,
    "4c": 8750000,
    "h": 1050000,
    "cc": K150,
    "ch": K150,
    "hip": 11000
  },
  5: {
    "a": 16000,
    "1c": 80000,
    "2c": K220,
    "3c": 600000,
    "4c": 8000000,
    "h": 1000000,
    "cc": K100,
    "ch": K100,
    "hip": K100
  },
  6: {
    "a": 14000,
    "1c": 70000,
    "2c": K200,
    "3c": 550000,
    "4c": 7500000,
    "h": 9500000,
    "cc": K100,
    "ch": K100,
    "hip": K100
  },
  7: {
    "a": 14000,
    "1c": 70000,
    "2c": K200,
    "3c": 550000,
    "4c": 7500000,
    "h": 9500000,
    "cc": K100,
    "ch": K100,
    "hip": K100
  },
  8: {
    "a": K50,
    "1c": K200,
    "2c": 600000,
    "3c": 1400000,
    "4c": 1700000,
    "h": 2000000,
    "cc": K200,
    "ch": K200,
    "hip": 175000
  },
  9: {
    "a": 26000,
    "1c": 130000,
    "2c": 900000,
    "3c": 1100000,
    "h": 1275000,
    "cc": K200,
    "ch": K200,
    "hip": K150
  },
  10: {
    "a": 26000,
    "1c": 130000,
    "2c": 900000,
    "3c": 1100000,
    "h": 1275000,
    "cc": K200,
    "ch": K200,
    "hip": K150
  },
  11: {
    "a": 35000,
    "1c": 130000,
    "2c": K500,
    "3c": 1100000,
    "h": 1300000,
    "cc": K200,
    "ch": K200,
    "hip": K150
  },
  12: {
    "a": 60000,
    "1c": 300000,
    "2C": 90000,
    "3C": K400,
    "h": K500,
    "cc": K50,
    "ch": K50,
    "hip": K50
  },
  13: {
    "a": 22000,
    "1c": 110000,
    "2c": 330000,
    "3c": 800000,
    "4c": 975000,
    "h": 1150000,
    "cc": K150,
    "ch": K150,
    "hip": K130
  },
  14: {
    "a": 12000,
    "1c": 60000,
    "2c": 180000,
    "3c": K500,
    "4c": 700000,
    "h": 900000,
    "cc": K100,
    "ch": K100,
    "hip": 80000
  },
  15: {
    "a": 28000,
    "1c": K150,
    "2c": K450,
    "3c": 10 * K100,
    "4c": 1200000,
    "h": 1400000,
    "cc": K200,
    "ch": K200,
    "hip": K160
  },
  16: {
    "a": 10000,
    "1c": K50,
    "2c": K150,
    "3c": K450,
    "4c": 625000,
    "h": 750000,
    "cc": K100,
    "ch": K100,
    "hip": 70000
  },
  17: {
    "a": 10000,
    "1c": K50,
    "2c": K150,
    "3c": K450,
    "4c": 625000,
    "h": 750000,
    "cc": K100,
    "ch": K100,
    "hip": 70000
  },
  18: {
    "a": 8000,
    "1c": 40000,
    "2c": K100,
    "3c": K300,
    "4c": K450,
    "h": 600000,
    "cc": K50,
    "ch": K50,
    "hip": K60
  },
  19: {
    "sd": K50,
    "hip": K100
  },
  21: {
    "a": 26000,
    "1c": 1300000,
    "2c": 360000,
    "3c": 850000,
    "4c": 1025000,
    "h": 1200000,
    "cc": K150,
    "ch": K150,
    "hip": 140000
  }
}

emoji = {1: "🔴", 3: "🟡", 2: "🟢", 4: "🔵"}

P1_nome = input("Insira o nome do Player1: ")
while True:
  try:
    P1_cor = int(
      input(
        f"\nEscolha uma cor\n\n1 -\033[31m Vermelho\033[37m\n2 -\033[32m Verde\033[37m\n3 -\033[33m Amarelo\033[37m\n4 -\033[34m Azul\033[37m\n\n{P1_nome}: "
      ))
  except:
    print("Por favor digite um número e não uma letra")
  else:
    if P1_cor < 1 or P1_cor > 4:
      print("Por favor digite um número entre 1 e 4")
    else:
      emojiP1 = emoji[P1_cor]
      P1_cor = cores[P1_cor]
      break

P2_nome = input("\nInsira o nome do Player2: ")
while True:
  try:
    P2_cor = int(
      input(
        f"\n\nEscolha uma cor\n\n1 -\033[31m Vermelho\033[37m\n2 -\033[32m Verde\033[37m\n3 -\033[33m Amarelo\033[37m\n4 -\033[34m Azul\033[37m\n\n{P2_nome}: "
      ))
  except:
    print("Por favor digite um número e não uma letra")
  else:
    if P2_cor < 1 or P2_cor > 4:
      print("Por favor digite um número entre 1 e 4")
    else:
      emojiP2 = emoji[P2_cor]
      P2_cor = cores[P2_cor]
      if P2_cor == P1_cor:
        print("Por favor escolha uma cor diferente do jogador 1")
      else:
        break

Player1 = {
  "id": 1,
  "nome": P1_nome,
  "cor": P1_cor,
  "icone": emojiP1,
  "conta": 2558000,
  "1K": 8,
  "5K": 10,
  "10K": 10,
  "50K": 8,
  "100K": 6,
  "200K": 2,
  "500K": 2,
  "pos": 0,
  "titulos": []
}
Player2 = {
  "id": 2,
  "nome": P2_nome,
  "cor": P2_cor,
  "icone": emojiP2,
  "conta": 2558000,
  "1K": 8,
  "5K": 10,
  "10K": 10,
  "50K": 8,
  "100K": 6,
  "200K": 2,
  "500K": 2,
  "pos": 0,
  "titulos": []
}

# Sistema que gera dois números aleatórios de 1 a 6.
#irá decidir qual jogador começará
jogadorAleatorio = random.randint(1, 2)


def comprar_propriedade(Player, idPropriedade):
  #
  Player[
    "conta"] = Player['conta'] - quadradosTabuleiro[idPropriedade]["valor"]
  Player["titulos"].append(idPropriedade)
  # print("'Oi'")  ---> 'Oi'
  # print('"Oi"') ----> "Oi"
  print(
    f"\nParabéns, você realizou a compra da propriedade '{cores[quadradosTabuleiro[idPropriedade]['cor']]}{quadradosTabuleiro[idPropriedade]['nome']}\033[39m'"
  )
  #print(f"Saldo total R${Player['conta']}\n")
  if idPropriedade != 19:
    quadradosTabuleiro[idPropriedade]["status"] = "a"
  else:
    quadradosTabuleiro[idPropriedade]["status"] = "sd"
  """
    1 - Ver o saldo do player
    2 - Ver o preço da propriedade
    3 - Descontar o valor da proprieade na conta
    4 - Dar título de posse
  """


def imprimirTabuleiro(posP1, posP2):

  up = "|"
  emojiP1 = Player1["icone"]
  emojiP2 = Player2["icone"]

  if (0 < posP1 < 11 and 0 < posP2 < 11 and posP1 != posP2):
    #print(1)
    stInit = 0
    num1Bracket = 57
    num1Up = 50
    num2Bracket = 12
  elif (0 < posP1 < 11 and 0 < posP2 < 11 and posP1 == posP2):
    #print(2)
    stInit = 10
    num1Bracket = 54
    num1Up = 48
    num2Bracket = 5
  elif (posP1 > 15 and 0 < posP2 < 11) or (0 < posP1 < 11 and posP2 > 15):
    #print(3)
    stInit = 18
    num1Bracket = 58
    num1Up = 51
    num2Bracket = 9
  elif (posP1 > 15 and 0 == posP2) or (0 == posP1 and posP2 > 15):
    stInit = 20
    num1Bracket = 58
    num1Up = 51
    num2Bracket = 9
  elif (posP1 == posP2 > 15):
    #print(4)
    stInit = 23
    num1Bracket = 60
    num1Up = 53
    num2Bracket = 0
  elif (posP1 > 15 and posP2 > 15 and posP1 != posP2):
    #print(5)
    stInit = 27
    num1Bracket = 63
    num1Up = 56
    num2Bracket = 0
  elif (posP1 >= 11 and posP1 < 15) and (posP2 >= 11 and posP2 < 15):
    #print(6)
    stInit = 18
    num1Bracket = 55
    num1Up = 48
    num2Bracket = 10
  elif (11 <= posP1 < 15 and posP2 >= 15) or (11 <= posP2 < 15
                                              and posP1 >= 15):
    #print(7)
    stInit = 22
    num1Bracket = 58
    num1Up = 52
    num2Bracket = 0
  elif (0 < posP1 < 11 and (11 <= posP2 < 15)) or (0 < posP2 < 11 and
                                                   (11 <= posP1 < 15)):
    #print(8)
    stInit = 17
    num1Bracket = 57
    num1Up = 50
    num2Bracket = 12
  elif (0 < posP1 < 11 and posP2 >= 15) or (0 < posP2 < 11 and posP1 >= 15):
    stInit = 17
    num1Bracket = 57
    num1Up = 50
    num2Bracket = 12
  elif (0 == posP1 and 0 < posP2 <= 10) or (0 == posP2 and 0 < posP1 <= 10):
    print(9)
    stInit = 0
    num1Bracket = 57
    num1Up = 50
    num2Bracket = 12
  elif (0 == posP1 and 11 <= posP2 < 15) or (0 == posP2 and 11 <= posP1 < 15):
    print(10)
    stInit = 20
    num1Bracket = 57
    num1Up = 50
    num2Bracket = 12
  elif (posP1 == 15 and posP2 > 15) or (posP2 == 15 and posP1 > 15):
    stInit = 23
    num1Bracket = 60
    num1Up = 53
    num2Bracket = 0
  elif (posP1 == 0 and posP2 == 15) or (posP1 == 15 and posP2 == 0):
    stInit = 23
    num1Bracket = 60
    num1Up = 53
    num2Bracket = 15
  elif posP1 == posP2 == 15:
    stInit = 23
    num1Bracket = 60
    num1Up = 53
    num2Bracket = 10
  print('\n')
  string1 = Fore.LIGHTCYAN_EX + "TABULEIRO\n\n"
  print(f"{string1:^60}")
  if posP1 == posP2 == 0:
    string = Fore.GREEN + f'[0: {emojiP1}{emojiP2}]' + Fore.WHITE
    num2Bracket = 7
    num1Bracket = 55
    num1Up = 48
    print(f"{string:>10}", end="")
  elif posP1 == 0:
    string = Fore.GREEN + f'[0: {emojiP1}]' + Fore.WHITE
    print(f"{string:>{stInit}}", end="")
  elif posP2 == 0:
    string = Fore.GREEN + f'[0: {emojiP2}]' + Fore.WHITE
    print(f"{string:>{stInit}}", end="")
  elif posP1 != 0 and posP2 != 0:
    string = Fore.GREEN + '[0]' + Fore.WHITE
    print(f"{string:>{stInit}}", end="")
  for i in range(1, 15):
    cor = cores[quadradosTabuleiro[i]['cor']]

    if i >= 1 and i <= 10:
      if i != posP1 and i != posP2:

        print("-" + cor + f"[{i}]", end="\033[39m")
      elif i == posP1 and i != posP2:
        print("-" + cor + f"[{i}: {emojiP1}]", end="\033[39m")
      elif i == posP2 and i != posP1:
        print("-" + cor + f"[{i}: {emojiP2}]", end="\033[39m")
      else:
        print("-" + cor + f"[{i}: {emojiP1}{emojiP2}]", end="\033[39m")
    elif i == 11:

      print('')
      if i != posP1 and i != posP2:
        bracket = cor + f"[{i}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
      elif i == posP1 and i != posP2:
        bracket = cor + f"[{i}: {emojiP1}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
      elif i != posP1 and i == posP2:
        bracket = cor + f"[{i}: {emojiP2}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
      else:
        bracket = cor + f"[{i}: {emojiP1}{emojiP2}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
    elif i > 11 and i < 14:
      if i != posP1 and i != posP2:
        bracket = cor + f"[{i}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
      elif i == posP1 and i != posP2:
        bracket = cor + f"[{i}: {emojiP1}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
      elif i != posP1 and i == posP2:
        bracket = cor + f"[{i}: {emojiP2}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
      else:
        bracket = cor + f"[{i}: {emojiP1}{emojiP2}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
    else:
      if i != posP1 and i != posP2:
        bracket = cor + f"[{i}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
        print(f'{up:>{num1Up}}')
      elif i == posP1 and i != posP2:
        bracket = cor + f"[{i}: {emojiP1}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
        print(f'{up:>{num1Up}}')
      elif i != posP1 and i == posP2:
        bracket = cor + f"[{i}: {emojiP2}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
        print(f'{up:>{num1Up}}')
      else:
        bracket = cor + f"[{i}: {emojiP1}{emojiP2}]"
        print(f'{up:>{num1Up}}')
        print(f'{bracket:>{num1Bracket}}', end="\033[39m\n")
        print(f'{up:>{num1Up}}')

  for i in reversed(range(15, 25)):
    cor = cores[quadradosTabuleiro[i]['cor']]
    if i <= 23:
      if i != posP1 and i != posP2:
        print("-" + cor + f"[{i}]", end="\033[39m")
      elif i == posP1 and i != posP2:
        print("-" + cor + f"[{i}: {emojiP1}]", end="\033[39m")
      elif i == posP2 and i != posP1:
        print("-" + cor + f"[{i}: {emojiP2}]", end="\033[39m")
      else:
        print("-" + cor + f"[{i}: {emojiP1}{emojiP2}]", end="\033[39m")
    else:
      if i != posP1 and i != posP2:
        string = cor + f"[{i}]"
        print(f"{string:>{num2Bracket}}", end="\033[39m")
      elif i == posP1 and i != posP2:
        string = cor + f"[{i}: {emojiP1}]"
        print(f"{string:>{num2Bracket}}", end="\033[39m")
      elif i == posP2 and i != posP1:
        string = cor + f"[{i}: {emojiP2}]"
        print(f"{string:>{num2Bracket}}", end="\033[39m")
      else:
        string = cor + f"[{i}: {emojiP1}{emojiP2}]"
        print(f"{string:>{num2Bracket}}", end="\033[39m")
  print("\n\n")


def construir(Player, idPropriedade, objeto):
  cor = quadradosTabuleiro[idPropriedade]['cor']
  propriedadesCores[cor][objeto] += 1
  quadradosTabuleiro[idPropriedade]["status"] = objeto
  Player["conta"] -= titulosDePosse[idPropriedade][objeto]

  print(
    f"\nVocê construiu 1 casa na propriedade {cores[cor]}{quadradosTabuleiro[idPropriedade]['nome']}\033[39m por R${titulosDePosse[idPropriedade][objeto]}"
  )

  print(f"\n\nSeu saldo atual é: {Player['conta']}\n\n")


def venderPropriedade(Player, idPropriedade, valor):

  del Player["titulos"][Player["titulos"].index(idPropriedade)]
  Player["conta"] += valor
  color = quadradosTabuleiro[idPropriedade]["cor"]
  print(
    f"\nVocê vendeu a propriedade '{cores[color]}{quadradosTabuleiro[idPropriedade]['nome']}\033[39m' por R${valor}"
  )
  print(f"\n\nSeu saldo atual é: {Player['conta']}")


def venderCasas(Player, cor, valor, objeto):
  propriedadesCores[cor][objeto[1]] = 0
  for idPropriedade in propriedadesCores[cor]["propriedades"]:
    quadradosTabuleiro[idPropriedade]["status"] = objeto[2]

  Player["conta"] += valor

  print(
    f"\nVocê vendeu 1 casa de cada propriedade da cor {cor} por R${valor}\n\n")


def pagarAluguel(Player, idPropriedade, status):

  if status == "a":
    string = f"pelo aluguel de R${titulosDePosse[idPropriedade][status]}"
  elif status == "1c":
    string = f"pelo aluguel de 1 casa construída na propriedade pelo valor de R${titulosDePosse[idPropriedade][status]}"
  elif status == "2c":
    string = f"pelo aluguel de 2 casa construída na propriedade pelo valor de R${titulosDePosse[idPropriedade][status]}"
  elif status == "3c":
    string = f"pelo aluguel de 3 casas construídas na propriedade pelo valor de R${titulosDePosse[idPropriedade][status]}"
  elif status == "4c":
    string = f"pelo aluguel de 4 casas construída na propriedade pelo valor de R${titulosDePosse[idPropriedade][status]}"
  elif status == "h":
    string = f"pelo aluguel de 1 hotel construído na propriedade pelo valor de R${titulosDePosse[idPropriedade][status]}"
  elif status == "sd":
    string = f"pelo aluguel, onde o valor é a soma dos dados multiplicado por R${titulosDePosse[idPropriedade][status]}"

  Player["conta"] -= titulosDePosse[idPropriedade][status]
  if Player["id"] == 1:
    id = 2
    Player2["conta"] += titulosDePosse[idPropriedade][status]
  else:
    id = 1
    Player1["conta"] += titulosDePosse[idPropriedade][status]
  print(
    f"\n\nO Player{id} detém a propriedade {cores[quadradosTabuleiro[idPropriedade]['cor']]}{quadradosTabuleiro[idPropriedade]['nome']}\033[39m. Você tem que pagar {string}\n\n"
  )


rodada = 1
#INICIALIZAÇÃO

while True:
  # dado1 e dado2 está gerando um número de 1 a 6 aleatório
  print(f"\033[36m-----Começando a rodada {rodada}-----\033[39m")
  print(f"\n\nQUEM IRÁ COMEÇAR É O(A) PLAYER{jogadorAleatorio}\n\n")
  print(Fore.GREEN + "Gerando dados\033[39m")

  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  print(f"Dados: {dado1}, {dado2}")

  somaDosDados = dado1 + dado2

  if jogadorAleatorio == 1:

    print(f"\nDados do(a) {Player1['cor']}{Player1['nome']}\033[39m")
    print(f"Saldo total: R${Player1['conta']}")

    # define o próximo jogador
    jogadorAleatorio = 2

    posp1 = Player1["pos"]
    #print(f"Posição do jogador 1: {posp1}")

    posp1Atual = posp1 + somaDosDados

    if posp1Atual > 24 and (posp1Atual % 24 != 0):

      # usamos o -1 para voltar para o 0
      posp1Atual = (posp1Atual % 24) - 1
      Player1["conta"] += 15000

    # verifica quando o resto de posp1Atual por 24 =0, ou seja, verifica se é um múltiplo de 24
    elif posp1Atual % 24 == 0 and posp1Atual != 24:
      posp1Atual = 24
      Player1["conta"] += 15000

    Player1["pos"] = posp1Atual
    #print(f"Posição atual do jogador 1: {posp1Atual}")

    imprimirTabuleiro(posp1Atual, Player2["pos"])
    if posp1Atual == 23 and (Player1['conta'] < 50000):
      string = f"\033[39m PARABÉNS, VOCÊ\033[32m GANHOU\033[39m O JOGO {Player2['nome'].upper()}"
      print(f"{string:^50}")
      print(
        f"\n\nO JOGADOR {Player2['nome'].upper()} PERDEU POR ESTAR PRESO E TER MENOS QUE R$50000 NA CONTA"
      )
      break
    elif posp1Atual == 23 and (Player1['conta'] >= 50000):
      print("\n\nVOCÊ ESTÁ NA PRISÃO, DESCONTANDO R$50000 PARA SER LIBERTO")
      Player1['conta'] -= 50000
    else:
      nomePropriedade = quadradosTabuleiro[posp1Atual]["nome"]
      statusPropriedade = quadradosTabuleiro[posp1Atual]["status"]

      valorPropriedade = quadradosTabuleiro[posp1Atual]["valor"]

      if posp1Atual in Player1["titulos"]:
        corPropriedade = quadradosTabuleiro[posp1Atual]["cor"]
        if set(propriedadesCores[corPropriedade]["propriedades"]).issubset(
            Player1["titulos"]):

          if statusPropriedade == "a" and (titulosDePosse[posp1Atual]['1c'] <
                                           Player1['conta']):
            print(
              f'\n{Player1["nome"]} tem todas as propriedades de cor {corPropriedade}. Você tem as seguintes opções:\n\n'
            )

            while True:
              try:
                opcao = int(
                  input(
                    f"1 - Construir 1 casa por R${titulosDePosse[posp1Atual]['1c']}\n2 - Vender a propriedade por R${0.7*valorPropriedade}\n3 - Passar a vez\n\n{Player1['cor']}{Player1['nome']}:\033[39m "
                  ))
              except:
                print("\nIrmão, coloque um número")
              else:
                if opcao < 1 and opcao > 3:
                  print("\nColoque um número de 1 a 3")
                elif opcao == 1:
                  construir(Player1, posp1Atual, "1c")
                  break
                elif opcao == 2:
                  venderPropriedade(Player1, posp1Atual,
                                    0.7 * valorPropriedade)
                  break
                else:
                  break
          elif statusPropriedade == "a" and (titulosDePosse[posp1Atual]['1c'] >
                                             Player1['conta']):
            print(
              "Você não tem saldo suficiente para construir nessa propriedade."
            )

          elif propriedadesCores[corPropriedade][
              statusPropriedade] == propriedadesCores[corPropriedade][
                "countMax"]:

            if statusPropriedade == "1c":
              construcao = "1 casa"
              objetoConstruir = ["2 casas", "2c", "a"]
            elif statusPropriedade == "2c":
              construcao = "2 casas"
              objetoConstruir = ["3 casas", "3c", "1c"]
            elif statusPropriedade == "3c":
              construcao = "3 casas"
              objetoConstruir = ["4 casas", "4c", "2c"]
            elif statusPropriedade == "4c":
              construcao = "4 casas"
              objetoConstruir = ["hotel", "h", "3c"]

            print(
              f"\n\nTodas as suas propriedades da cor {cores[corPropriedade]}{corPropriedade}\033[39m já tem {construcao}. Você tem as seguintes opções:\n\n"
            )
            while True:
              try:
                opcao = int(
                  input(
                    f"1 - Construir {objetoConstruir[0]} por R${titulosDePosse[posp1Atual][objetoConstruir[1]]}\n2 - Vender 1 casa de cada propridade da mesma cor\n3 - Passar a vez\n\n{Player1['cor']}{Player1['nome']}:\033[39m "
                  ))
              except:
                print("Irmão, digite um número")
              else:
                if opcao < 1 and opcao > 3:
                  print("\nColoque um número de 1 a 3")
                elif opcao == 1:
                  construir(Player1, posp1Atual, objetoConstruir[1])
                  break
                elif opcao == 2:
                  valor = 0
                  for casa in propriedadesCores[corPropriedade][
                      "propriedades"]:
                    valor += titulosDePosse[casa][statusPropriedade] * 0.7

                  venderCasas(Player1, corPropriedade, valor, objetoConstruir)
                  break
                else:
                  break
        else:
          print(
            f"\n\nVocê  detém a propriedade {cores[corPropriedade]}{nomePropriedade}\033[39m e tem as seguintes opções:"
          )
          while True:
            try:
              opcao = int(
                input(
                  f"\n\n1 - Vender a propriedade por R${0.7*valorPropriedade}\n3 - Passar a vez\n\n{Player1['cor']}{Player1['nome']}:\033[39m "
                ))
            except:
              print("\nIrmão, coloque um número")
            else:
              if opcao < 1 and opcao > 3:
                print("\nColoque um número de 1 a 3")
              elif opcao == 1:
                venderPropriedade(Player1, posp1Atual, 0.7 * valorPropriedade)
                break
              else:
                break

      elif statusPropriedade == "Não comprada":
        corPropriedade = quadradosTabuleiro[posp1Atual]["cor"]
        """
          1 - Comprar
          2 - Passa a vez
        """
        if valorPropriedade > Player1["conta"]:
          print("Você não tem saldo suficiente para comprar essa propriedade.")

        else:

          while True:
            try:
              opcao = int(
                input(
                  f"\nA propriedade {cores[corPropriedade]}{nomePropriedade}\33[39m ainda não foi comprada.\n\nDados da propriedade:\nValor: R${valorPropriedade}\nCor: {corPropriedade}\33[39m\n\nVocê tem as seguintes opções:\n\n1 - Comprar a propriedade\n2 - Passar a vez\n\n"
                  + Player1['cor'] + f"{Player1['nome']}:\33[39m "))
            except:
              print(
                "Irmão, coloque um número. Você tem apenas duas opções, 1 ou 2."
              )
            else:
              break
          if opcao == 1:
            comprar_propriedade(Player1, posp1Atual)

      elif statusPropriedade in ["a", "1c", "2c", "3c", "4c", "h", "sd"]:
        pagarAluguel(Player1, posp1Atual, statusPropriedade)

      elif quadradosTabuleiro[posp1Atual]["status"] == "hipo":
        pass
      elif quadradosTabuleiro[posp1Atual]["status"] == "sorte-reves":
        sorte_reves = random.randint(1, 2)
        if sorte_reves == 1:
          print("\n\nVOCÊ CAIU NA SORTE E GANHOU R$50000")
          Player1['conta'] += 50000
        else:
          print("\n\nVOCÊ CAIU NO AZAR E PERDEU R$50000")
          Player1['conta'] -= 50000
      elif quadradosTabuleiro[posp1Atual]["status"] == "receita":
        Player1['conta'] -= 50000
        print("\n\nVOCÊ ESTÁ NA RECEITA FEDERAL, PAGANDO IMPOSTO DE R$50000")
      elif quadradosTabuleiro[posp1Atual]["status"] == "carbono":
        Player1['conta'] += 30000
        print("\n\nVOCÊ GANHOU CRÉDITO DE R$30000")

      if Player1["conta"] < 0:
        string = f"\033[39m PARABÉNS, VOCÊ\033[32m GANHOU\033[39m O JOGO {Player2['nome'].upper()}"
        print(f"{string:^50}")
        print(
          f"\033[39m O jogador {Player1['cor']}{Player1['nome'].upper()}\033[31m faliu."
        )
        break
  elif jogadorAleatorio == 2:
    print(f"\nDados do(a) {Player2['cor']}{Player2['nome']}\033[39m")
    print(f"Saldo total: R${Player2['conta']}")

    # define o próximo jogador
    jogadorAleatorio = 1

    posp2 = Player2["pos"]

    #print(f"Posição do jogador 1: {posp2}")

    posp2Atual = posp2 + somaDosDados

    #print(f"Posição atual do jogador 1: {posp2Atual}")

    if posp2Atual > 24 and (posp2Atual % 24 != 0):

      # usamos o -1 para voltar para o 0
      posp2Atual = (posp2Atual % 24) - 1
      Player2["conta"] += 15000

    # verifica quando o resto de posp1Atual por 24 =0, ou seja, verifica se é um múltiplo de 24
    elif posp2Atual % 24 == 0:
      posp2Atual = 24
    Player2["pos"] = posp2Atual
    imprimirTabuleiro(Player1["pos"], posp2Atual)

    if posp2Atual == 23 and (Player2['conta'] < 50000):
      string = f"\033[39m PARABÉNS, VOCÊ\033[32m GANHOU\033[39m O JOGO {Player1['nome'].upper()}\n\n"
      print(f"{string:^50}")
      print(
        f"\n\nO JOGADOR {Player2['nome'].upper()} PERDEU POR ESTAR PRESO E TER MENOS QUE R$50000 NA CONTA"
      )
      break
    elif posp2Atual == 23 and (Player2['conta'] >= 50000):
      print("\n\nVOCÊ ESTÁ NA PRISÃO, DESCONTANDO R$50000 PARA SER LIBERTO")
      Player2['conta'] -= 50000
    else:
      nomePropriedade = quadradosTabuleiro[posp2Atual]["nome"]
      statusPropriedade = quadradosTabuleiro[posp2Atual]["status"]
      corPropriedade = quadradosTabuleiro[posp2Atual]["cor"]
      valorPropriedade = quadradosTabuleiro[posp2Atual]["valor"]

      if posp2Atual in Player2["titulos"]:
        corPropriedade = quadradosTabuleiro[posp1Atual]["cor"]
        if set(propriedadesCores[corPropriedade]["propriedades"]).issubset(
            Player2["titulos"]):

          if statusPropriedade == "a" and (titulosDePosse[posp1Atual]['1c'] <
                                           Player1['conta']):
            print(
              f'\n{Player2["nome"]} tem todas as propriedades de cor {corPropriedade}. Você tem as seguintes opções:\n\n'
            )

            while True:
              try:
                opcao = int(
                  input(
                    f"1 - Construir 1 casa por R${titulosDePosse[posp2Atual]['1c']}\n2 - Vender a propriedade por R${0.7*valorPropriedade}\n3 - Passar a vez\n\n{Player2['cor']}{Player2['nome']}:\033[39m "
                  ))
              except:
                print("\nIrmão, coloque um número")
              else:
                if opcao < 1 and opcao > 3:
                  print("\nColoque um número de 1 a 3")
                elif opcao == 1:
                  construir(Player2, posp2Atual, "1c")
                  break
                elif opcao == 2:
                  venderPropriedade(Player2, posp1Atual,
                                    0.7 * valorPropriedade)
                  break
                else:
                  break
          elif statusPropriedade == "a" and (titulosDePosse[posp1Atual]['1c'] >
                                             Player1['conta']):
            print(
              "Você não tem saldo suficiente para construir nessa propriedade."
            )
          elif propriedadesCores[corPropriedade][
              statusPropriedade] == propriedadesCores[corPropriedade][
                "countMax"]:

            if statusPropriedade == "1c":
              construcao = "1 casa"
              objetoConstruir = ["2 casas", "2c", "a"]
            elif statusPropriedade == "2c":
              construcao = "2 casas"
              objetoConstruir = ["3 casas", "3c", "1c"]
            elif statusPropriedade == "3c":
              construcao = "3 casas"
              objetoConstruir = ["4 casas", "4c", "2c"]
            elif statusPropriedade == "4c":
              construcao = "4 casas"
              objetoConstruir = ["hotel", "h", "3c"]

            print(
              f"\n\nTodas as suas propriedades da cor {cores[corPropriedade]}{corPropriedade}\033[39m já tem {construcao}. Você tem as seguintes opções:\n\n"
            )
            while True:
              try:
                opcao = int(
                  input(
                    f"1 - Construir {objetoConstruir[0]} por R${titulosDePosse[posp2Atual][objetoConstruir[1]]}\n2 - Vender 1 casa de cada propridade da mesma cor\n3 - Passar a vez\n\n{Player2['cor']}{Player2['nome']}:\033[39m "
                  ))
              except:
                print("Irmão, digite um número")
              else:
                if opcao < 1 and opcao > 3:
                  print("\nColoque um número de 1 a 3")
                elif opcao == 1:
                  construir(Player2, posp2Atual, objetoConstruir[1])
                  break
                elif opcao == 2:
                  valor = 0
                  for casa in propriedadesCores[corPropriedade][
                      "propriedades"]:
                    valor += titulosDePosse[casa][statusPropriedade] * 0.7

                  venderCasas(Player2, corPropriedade, valor, objetoConstruir)
                  break
                else:
                  break
        else:
          print(
            f"\n\nVocê  detém a propriedade {cores[corPropriedade]}{nomePropriedade}\033[39m e tem as seguintes opções:"
          )
          while True:
            try:
              opcao = int(
                input(
                  f"\n\n1 - Vender a propriedade por R${0.7*valorPropriedade}\n3 - Passar a vez\n\n{Player2['cor']}{Player2['nome']}:\033[39m "
                ))
            except:
              print("\nIrmão, coloque um número")
            else:
              if opcao < 1 and opcao > 3:
                print("\nColoque um número de 1 a 3")
              elif opcao == 1:
                venderPropriedade(Player2, posp2Atual, 0.7 * valorPropriedade)
                break
              else:
                break

      elif statusPropriedade == "Não comprada":
        corPropriedade = quadradosTabuleiro[posp2Atual]["cor"]
        """
          1 - Comprar
          2 - Passa a vez
        """
        if valorPropriedade > Player2["conta"]:
          print("Você não tem saldo suficiente para comprar essa propriedade.")
        else:

          while True:
            try:
              opcao = int(
                input(
                  f"\nA propriedade {cores[corPropriedade]}{nomePropriedade}\33[39m ainda não foi comprada.\n\nDados da propriedade:\nValor: R${valorPropriedade}\nCor: {corPropriedade}\33[39m\n\nVocê tem as seguintes opções:\n\n1 - Comprar a propriedade\n2 - Passar a vez\n\n"
                  + Player2['cor'] + f"{Player2['nome']}:\33[39m "))
            except:
              print(
                "Irmão, coloque um número. Você tem apenas duas opções, 1 ou 2."
              )
            else:
              break
          if opcao == 1:
            comprar_propriedade(Player2, posp2Atual)

      elif statusPropriedade in ["a", "1c", "2c", "3c", "4c", "h"]:
        corPropriedade = quadradosTabuleiro[posp2Atual]["cor"]
        pagarAluguel(Player2, posp2Atual, statusPropriedade)
      elif quadradosTabuleiro[posp2Atual]["status"] == "hipo":
        pass
      elif quadradosTabuleiro[posp2Atual]["status"] == "sorte-reves":
        sorte_reves = random.randint(1, 2)
        if sorte_reves == 1:
          print("\n\nVOCÊ CAIU NA SORTE E GANHOU R$50000")
          Player2['conta'] += 50000
        else:
          print("\n\nVOCÊ CAIU NO AZAR E PERDEU R$50000")
          Player2['conta'] -= 50000
      elif quadradosTabuleiro[posp2Atual]["status"] == "receita":
        Player2['conta'] -= 50000
        print("\n\nVOCÊ ESTÁ NA RECEITA FEDERAL, PAGANDO IMPOSTO DE R$50000")

      elif quadradosTabuleiro[posp2Atual]["status"] == "carbono":
        Player2['conta'] += 30000
        print("\n\nVOCÊ GANHOU CRÉDITO DE R$30000")

      if Player2["conta"] < 0:
        string = f"\033[39m PARABÉNS, VOCÊ\033[32m GANHOU\033[39m O JOGO {Player1['nome'].upper()}\n\n"
        print(f"{string:^60}")
        print(
          f"\033[39m O jogador {Player2['cor']}{Player2['nome'].upper()}\033[31m faliu."
        )
        break

  rodada += 1
