# Aqui a ideia é fazer com que a máquina gere um número aleatório dentro de um range e o usuário tem que acertar que número é esse.

from random import randint 

def chute(x):
  numero_aleatorio = randint(1, x)
  chute = 0 # Definindo um número inicial mas que será alterado. Definindo como 0 e o random iniciando com 1, significa que o número aleatório nunca será 0
  palpites = 0

  while chute != numero_aleatorio:
    chute = int(input(f"Adivinhe o número entre 1 e {x}: "))
    palpites += 1
    if chute < numero_aleatorio:
      print("Tente novamente. Muito abaixo")
    elif chute > numero_aleatorio:
      print("Tente novamente. Muito alto")
  
  print(f"Parabéns!! Você adivinhou o número {numero_aleatorio} corretamente depois de {palpites} tentativas")

# chute(20)

# Fazendo o inverso da função, podemos definir um número para que o computador adivinhe o número que pensamos.
def computer_guess(x):
  # Como sabemos o número, definiremos o limite em que a máquina irá advinhar. Que será entre 1 e o valor definido.
  low = 1
  high = x
  feedback = "" # Será através do feedback que daremos as pistas para a maquina advinhar o número.
  attempts = 0

  while feedback != "c":
    guess = randint(low, high)
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
    attempts += 1

    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1
    
  print(f"Yay! The computer guessed your number, {guess}, correctly, after {attempts} attempts!")

computer_guess(100)