# Inicializa os valores globais
jogo = True
matriz = [["_","_","_","_"],["_","_","_","_"]]

def inicio():
  # Modulo inicial
  print("   HOTEL DOS ANIMAIS   ")
  print("\n")
  print("Especificando as posições")

def posicoes():
  # Mostra os valores de cada opção, que devem ser escolhidos 
  matriz_posicoes = [[1,2,3,4],[5,6,7,8]]
  #Imprime as Posições
  print(matriz_posicoes[0])
  print(matriz_posicoes[1])

  print("\n")

def compara(linha,coluna, letra):
  #Compara as posições adjacentes
  global jogo
  
  #Se for Rato
  if (letra == "R"):
    #Verefica se a posição adjacente é Gato
    if (matriz[linha][coluna] == "G"):
      jogo = False
  #Se for Cachorro    
  if (letra == "C"):
    #Verefica se a posição adjacente é Osso
    if (matriz[linha][coluna] == "O"):
      jogo = False
  #Se for Gato    
  if (letra == "G"):
    #Verefica se a posição adjacente é Cão
    if (matriz[linha][coluna] == "C"):
      jogo = False
  #Se for Queijo    
  if (letra == "Q"):
    #Verefica se a posição adjacente é Rato
    if (matriz[linha][coluna] == "R"):
      jogo = False  

def verificar(linha,coluna, letra):
  #Verificando se a posição do jogo da game over
  global matriz
    
  if (linha == 0):   
    #Compara com o valor da mesma coluna e linha de baixo  
    compara(1,coluna, letra)
    if ((coluna >= 0) and (coluna < 3)):
      #Compara com o valor da mesma linha e coluna a direita
      compara(0,coluna + 1, letra) 
    elif (coluna == 3):
      #Compara com o valor da mesma linha e coluna a esquerda
      compara(0,coluna - 1, letra)    
  elif (linha == 1): 
    #Compara com o valor da mesma coluna e linha de cima 
    compara(0,coluna, letra)
    if ((coluna >= 0) and (coluna < 3)):
      #Compara com o valor da mesma linha e coluna a direita
      compara(1,coluna + 1, letra)
    elif (coluna == 3):
      #Compara com o valor da mesma linha e coluna a esquerda
      compara(1,coluna - 1, letra)      
     
def alocar(opcao, letra):
  #Alocar valores na posição escolhida
  global matriz

  repetir = True  
  while(repetir):
    #Repetir laço até escolher uma posição vazia    
    #Posição recebe o valor da opção digitada 
    posicao = int(input("em qual posicao quer alocar o "+ opcao +"? "))
    #Se posição entre o intervalo entra na condição, senão repete pergunta 
    if (posicao >= 1 and posicao <= 8 ):      
      #Converte opção para as coordenadas linha e coluna
      if (posicao <= 4):
        linha = 0
        coluna = posicao - 1        
      else:
        linha = 1
        coluna = posicao - 5     

      #Verefica se posição vazia
      if (matriz[linha][coluna] == "_"):
        #Atribui valor a posição da matriz
        matriz[linha][coluna] = letra
        #Sai do laço de repetição
        repetir = False    

  #Imprime matriz atualizada
  print(matriz[0])
  print(matriz[1])
  #Verifica se posição é valida conforme o Animal mencionado
  verificar(linha,coluna, letra)

def primeira_fase():
  global matriz

  print("\n")
  print("Bem vindos a fase 1")
  print("Na Fase 1, o jogador deve alocar o RATO e o GATO segunte matriz que representa os quartos.")
  
  #Incializa matriz da fase do jogo, apenas as posções _ são vazias
  matriz = [["*","*","_","G"],["R","_","*","*"]]  
  #Imprime matriz atualizada
  print(matriz[0])
  print(matriz[1])
  #Chama os modulos para solicitar as informações, passando os parametros conforme o enunciado da fase
  alocar("RATO", "R") 
  alocar("GATO", "G") 

def segunda_fase():
  global matriz

  print("\n")
  print("Bem vindos a fase 2")
  print("Na segunda fase o jogador deve alocar :  CÃO, CÃO E OSSO.")

  #Incializa matriz da fase do jogo, apenas as posções _ são vazias
  matriz = [["_","*","*","*"],["*","C","_","_"]]  
  #Imprime matriz atualizada
  print(matriz[0])
  print(matriz[1])
  #Chama os modulos para solicitar as informações, passando os parametros conforme o enunciado da fase
  alocar("CÃO", "C") 
  alocar("CÃO", "C") 
  alocar("OSSO", "O") 

def terceira_fase():
  global matriz

  print("\n")
  print("Bem vindos a fase 3")
  print("Na fase 3 o jogador deverá alocar : GATO, RATO E OSSO.")

  #Incializa matriz da fase do jogo, apenas as posções _ são vazias
  matriz = [["_","*","*","*"],["_","G","_","*"]]  
  #Imprime matriz atualizada
  print(matriz[0])
  print(matriz[1])
  #Chama os modulos para solicitar as informações, passando os parametros conforme o enunciado da fase
  alocar("GATO", "G") 
  alocar("RATO", "R") 
  alocar("OSSO", "O") 

def quarta_fase():
  global matriz

  print("\n")  
  print("Bem vindos a fase 4")
  print("Na fase 4, o jogador deverá alocar: QUEIJO, QUEIJO, OSSO.")

  #Incializa matriz da fase do jogo, apenas as posções _ são vazias
  matriz = [["_","_","_","*"],["*","R","*","*"]]
  #Imprime matriz atualizada
  print(matriz[0])
  print(matriz[1])
  #Chama os modulos para solicitar as informações, passando os parametros conforme o enunciado da fase
  alocar("QUEIJO", "Q") 
  alocar("QUEIJO", "Q") 
  alocar("OSSO", "O") 

def vencedor():
  #Mensagem impressa para o Vencedor
  print("Parabéns, você ganhou!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")  


if(__name__ == "__main__"):
  
  #Modulo incial 
  inicio()
  #Imprime posições
  posicoes()
  
  #Verifica se o jogo ja deu Game Over 
  if (jogo):
     #Chama cada Fase do Jogo
    primeira_fase()
  #Verifica se o jogo ja deu Game Over
  if (jogo):
     #Chama cada Fase do Jogo
    segunda_fase()
  #Verifica se o jogo ja deu Game Over    
  if (jogo):
     #Chama cada Fase do Jogo
    terceira_fase()
  #Verifica se o jogo ja deu Game Over    
  if (jogo):
     #Chama cada Fase do Jogo
    quarta_fase()
  #Verifica se o jogo Teve Vencedor
  if (jogo):  
    vencedor()
  else:
    print("Game Over!!!")  